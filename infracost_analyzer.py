#!/usr/bin/env python3
"""
Enhanced Infracost Analyzer - 3-Band Cost Comparison (Half/Baseline/Double)
Provides apples-to-apples cost comparisons for both incumbent cloud and Railway
"""

import json
import os
import subprocess
from pathlib import Path
import yaml
import tempfile


class InfracostAnalyzer:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.api_key = os.getenv("INFRACOST_API_KEY")
        
    def analyze_with_bands(self, tf_directory, tf_data, railway_config):
        """
        Generate 3-band cost comparison (50%, 100%, 200% usage)
        Returns dict with low/baseline/high costs for both incumbent and Railway
        """
        if not self.api_key:
            return None
        
        tf_path = Path(tf_directory).resolve()
        
        # Determine baseline usage based on service context
        baseline_usage = self._determine_baseline_usage(tf_data, railway_config)
        
        # Generate 3 usage scenarios: half, baseline, double
        scenarios = {
            "low": self._scale_usage(baseline_usage, 0.5),      # 50%
            "baseline": baseline_usage,                         # 100%
            "high": self._scale_usage(baseline_usage, 2.0)      # 200%
        }
        
        results = {}
        
        for scenario_name, usage_data in scenarios.items():
            # Run infracost for incumbent cloud
            incumbent_cost = self._run_infracost_with_usage(tf_path, usage_data)
            
            # Calculate Railway cost with same usage
            railway_cost = self._calculate_railway_cost_with_usage(
                railway_config, 
                usage_data,
                scenario_name
            )
            
            results[scenario_name] = {
                "usage": usage_data,
                "incumbent": incumbent_cost,
                "railway": railway_cost
            }
        
        return results
    
    def _determine_baseline_usage(self, tf_data, railway_config):
        """
        Determine sensible baseline usage based on service context
        Considers: resource count, service types, architecture pattern
        """
        resources = tf_data.get("resources", {})
        services = railway_config.get("services", [])
        
        # Calculate total resource count
        total_resources = sum(len(v) for v in resources.values() if isinstance(v, list))
        
        # Determine scale category
        if total_resources < 10:
            scale = "startup"
        elif total_resources < 30:
            scale = "small"
        elif total_resources < 100:
            scale = "medium"
        else:
            scale = "large"
        
        # Analyze service types
        has_api = any(s.get("type") == "web" and "api" in s.get("name", "").lower() 
                     for s in services)
        has_db = len(railway_config.get("databases", [])) > 0
        has_multiple_services = len(services) > 2
        
        # Baseline profiles by scale and pattern
        profiles = {
            "startup": {
                "default": {"requests_per_month": 50000, "avg_duration_ms": 200},
                "api": {"requests_per_month": 100000, "avg_duration_ms": 150},
                "with_db": {"requests_per_month": 30000, "avg_duration_ms": 300}
            },
            "small": {
                "default": {"requests_per_month": 500000, "avg_duration_ms": 200},
                "api": {"requests_per_month": 1000000, "avg_duration_ms": 150},
                "with_db": {"requests_per_month": 300000, "avg_duration_ms": 300}
            },
            "medium": {
                "default": {"requests_per_month": 5000000, "avg_duration_ms": 200},
                "api": {"requests_per_month": 10000000, "avg_duration_ms": 150},
                "with_db": {"requests_per_month": 3000000, "avg_duration_ms": 300}
            },
            "large": {
                "default": {"requests_per_month": 50000000, "avg_duration_ms": 200},
                "api": {"requests_per_month": 100000000, "avg_duration_ms": 150},
                "with_db": {"requests_per_month": 30000000, "avg_duration_ms": 300}
            }
        }
        
        # Select appropriate profile
        scale_profiles = profiles.get(scale, profiles["small"])
        
        if has_api:
            base_profile = scale_profiles["api"]
        elif has_db:
            base_profile = scale_profiles["with_db"]
        else:
            base_profile = scale_profiles["default"]
        
        # Build usage data structure
        usage = {
            "version": "0.1",
            "resource_usage": {},
            "metadata": {
                "scale": scale,
                "requests_per_month": base_profile["requests_per_month"],
                "avg_duration_ms": base_profile["avg_duration_ms"],
                "profile": "api" if has_api else ("with_db" if has_db else "default")
            }
        }
        
        # Add Lambda/Cloud Functions usage
        for resource in resources.get("serverless", []):
            res_type = resource.get("type", "")
            res_name = resource.get("name", "")
            
            if "lambda" in res_type.lower() or "function" in res_type.lower():
                res_key = f"{res_type}.{res_name}"
                usage["resource_usage"][res_key] = {
                    "monthly_requests": base_profile["requests_per_month"],
                    "request_duration_ms": base_profile["avg_duration_ms"],
                    "memory_size_mb": 512  # Standard default
                }
        
        # Add API Gateway usage
        for resource in resources.get("networking", []):
            res_type = resource.get("type", "")
            res_name = resource.get("name", "")
            
            if "api_gateway" in res_type.lower():
                res_key = f"{res_type}.{res_name}"
                usage["resource_usage"][res_key] = {
                    "monthly_requests": base_profile["requests_per_month"]
                }
        
        # Add CloudFront/CDN usage (for static sites)
        for resource in resources.get("networking", []):
            res_type = resource.get("type", "")
            res_name = resource.get("name", "")
            
            if "cloudfront" in res_type.lower() or "cdn" in res_type.lower():
                res_key = f"{res_type}.{res_name}"
                # Estimate data transfer for static sites
                usage["resource_usage"][res_key] = {
                    "monthly_data_transfer_gb": base_profile["requests_per_month"] / 1000  # ~1KB per request
                }
        
        return usage
    
    def analyze(self, tf_directory):
        """
        Run basic Infracost analysis on Terraform directory
        Returns cost breakdown as JSON
        """
        if not self.api_key:
            return {"totalMonthlyCost": 0, "error": "No API key"}
        
        tf_path = Path(tf_directory).resolve()
        
        try:
            cmd = [
                "infracost",
                "breakdown",
                "--path", str(tf_path),
                "--format", "json"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(tf_path))
            
            if result.returncode == 0:
                cost_data = json.loads(result.stdout)
                return self._extract_summary(cost_data)
            else:
                return {"totalMonthlyCost": 0, "error": result.stderr}
                
        except Exception as e:
            return {"totalMonthlyCost": 0, "error": str(e)}
    
    def _scale_usage(self, baseline_usage, multiplier):
        """Scale usage data by multiplier (0.5 for half, 2.0 for double)"""
        scaled = {
            "version": baseline_usage.get("version", "0.1"),
            "resource_usage": {},
            "metadata": baseline_usage.get("metadata", {}).copy()
        }
        
        # Update metadata
        if "requests_per_month" in scaled["metadata"]:
            scaled["metadata"]["requests_per_month"] = int(
                scaled["metadata"]["requests_per_month"] * multiplier
            )
        scaled["metadata"]["multiplier"] = multiplier
        
        # Scale all resource usage values
        for res_key, res_usage in baseline_usage.get("resource_usage", {}).items():
            scaled_res_usage = {}
            
            for key, value in res_usage.items():
                if isinstance(value, (int, float)):
                    scaled_res_usage[key] = int(value * multiplier) if isinstance(value, int) else value * multiplier
                else:
                    scaled_res_usage[key] = value
            
            scaled["resource_usage"][res_key] = scaled_res_usage
        
        return scaled
    
    def _run_infracost_with_usage(self, tf_path, usage_data):
        """Run infracost with specific usage data"""
        if not usage_data.get("resource_usage"):
            # No usage-based resources, return base cost
            return self.analyze(str(tf_path))
        
        # Create temporary usage file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            yaml.dump(usage_data, f)
            usage_file = f.name
        
        try:
            cmd = [
                "infracost",
                "breakdown",
                "--path", str(tf_path),
                "--usage-file", usage_file,
                "--format", "json"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(tf_path))
            
            if result.returncode == 0:
                cost_data = json.loads(result.stdout)
                return self._extract_summary(cost_data)
            else:
                # Fallback to base analysis
                return {"totalMonthlyCost": 0, "error": "Usage analysis failed"}
        
        finally:
            # Clean up temp file
            if os.path.exists(usage_file):
                os.unlink(usage_file)
    
    def _calculate_railway_cost_with_usage(self, railway_config, usage_data, scenario_name):
        """
        Calculate Railway cost for given usage scenario
        Scales Railway resource estimates based on usage multiplier
        """
        services = railway_config.get("services", [])
        databases = railway_config.get("databases", [])
        functions = railway_config.get("functions", [])
        
        # Get multiplier from metadata
        multiplier = usage_data.get("metadata", {}).get("multiplier", 1.0)
        
        # Railway pricing (per minute)
        RAM_COST_PER_GB_MINUTE = 0.000231
        CPU_COST_PER_VCPU_MINUTE = 0.000463
        MINUTES_PER_MONTH = 43800  # 30.42 days
        
        total_cost = 0
        breakdown = {}
        
        # Calculate service costs (scaled by usage)
        for service in services:
            # Base estimates
            ram_gb = service.get("estimatedRAM_GB", 1.0)
            cpu_vcpu = service.get("estimatedCPU", 1.0)
            
            # Scale based on usage (more usage = more resources needed)
            # Apply square root scaling (doubling usage doesn't double resources)
            import math
            scale_factor = math.sqrt(multiplier) if multiplier > 0 else 1.0
            
            scaled_ram = ram_gb * scale_factor
            scaled_cpu = cpu_vcpu * scale_factor
            
            # Calculate monthly cost
            ram_cost = scaled_ram * RAM_COST_PER_GB_MINUTE * MINUTES_PER_MONTH
            cpu_cost = scaled_cpu * CPU_COST_PER_VCPU_MINUTE * MINUTES_PER_MONTH
            service_cost = ram_cost + cpu_cost
            
            total_cost += service_cost
            breakdown[service.get("name", "service")] = {
                "ram_gb": scaled_ram,
                "cpu_vcpu": scaled_cpu,
                "ram_cost": ram_cost,
                "cpu_cost": cpu_cost,
                "total": service_cost
            }
        
        # Database costs (relatively fixed, slight scaling)
        db_cost_per_instance = 10  # Baseline $10/month per database
        for db in databases:
            # Scale slightly with usage (more connections, more resources)
            scaled_db_cost = db_cost_per_instance * (1.0 + (multiplier - 1.0) * 0.3)
            total_cost += scaled_db_cost
            breakdown[db.get("name", "database")] = {
                "type": "database",
                "cost": scaled_db_cost
            }
        
        # Functions costs (scales linearly with requests)
        function_cost_per_million = 0.40  # $0.40 per million executions
        requests = usage_data.get("metadata", {}).get("requests_per_month", 0)
        if functions and requests > 0:
            functions_cost = (requests / 1000000) * function_cost_per_million
            total_cost += functions_cost
            breakdown["functions"] = {
                "requests": requests,
                "cost": functions_cost
            }
        
        return {
            "totalMonthlyCost": total_cost,
            "breakdown": breakdown,
            "metadata": {
                "scenario": scenario_name,
                "multiplier": multiplier,
                "requests_per_month": usage_data.get("metadata", {}).get("requests_per_month", 0)
            }
        }
    
    def _extract_summary(self, cost_data):
        """Extract useful summary from Infracost output"""
        summary = {
            "totalMonthlyCost": 0,
            "totalHourlyCost": 0,
            "projects": [],
            "resources": []
        }
        
        try:
            if "totalMonthlyCost" in cost_data:
                summary["totalMonthlyCost"] = float(cost_data["totalMonthlyCost"])
            
            if "totalHourlyCost" in cost_data:
                summary["totalHourlyCost"] = float(cost_data["totalHourlyCost"])
            
            if "projects" in cost_data:
                for project in cost_data["projects"]:
                    project_summary = {
                        "name": project.get("name", ""),
                        "totalMonthlyCost": float(project.get("breakdown", {}).get("totalMonthlyCost", 0)),
                        "resources": []
                    }
                    
                    if "breakdown" in project and "resources" in project["breakdown"]:
                        for resource in project["breakdown"]["resources"]:
                            resource_summary = {
                                "name": resource.get("name", ""),
                                "resourceType": resource.get("resourceType", ""),
                                "monthlyCost": float(resource.get("monthlyCost", 0))
                            }
                            project_summary["resources"].append(resource_summary)
                            summary["resources"].append(resource_summary)
                    
                    summary["projects"].append(project_summary)
            
            summary["costByType"] = self._calculate_cost_by_type(summary["resources"])
            
        except Exception as e:
            if self.verbose:
                print(f"   Warning: Error extracting summary: {e}")
        
        return summary
    
    def _calculate_cost_by_type(self, resources):
        """Group costs by resource type"""
        by_type = {}
        
        for resource in resources:
            res_type = resource.get("resourceType", "unknown")
            cost = resource.get("monthlyCost", 0)
            
            if res_type in by_type:
                by_type[res_type] += cost
            else:
                by_type[res_type] = cost
        
        return dict(sorted(by_type.items(), key=lambda x: x[1], reverse=True))
    
    def format_band_comparison(self, results):
        """Format 3-band comparison as markdown table"""
        if not results:
            return "No cost data available"
        
        table = []
        table.append("| Usage Band | Requests/Month | Incumbent Cost | Railway Cost | Difference |")
        table.append("|-----------|----------------|----------------|--------------|------------|")
        
        bands = [
            ("low", "Low (50%)", 0.5),
            ("baseline", "Baseline (100%)", 1.0),
            ("high", "High (200%)", 2.0)
        ]
        
        for band_key, band_label, multiplier in bands:
            band_data = results.get(band_key, {})
            
            requests = band_data.get("usage", {}).get("metadata", {}).get("requests_per_month", 0)
            requests_formatted = f"{requests:,}" if requests > 0 else "N/A"
            
            incumbent_cost = band_data.get("incumbent", {}).get("totalMonthlyCost", 0)
            railway_cost = band_data.get("railway", {}).get("totalMonthlyCost", 0)
            
            diff = railway_cost - incumbent_cost
            diff_pct = (diff / incumbent_cost * 100) if incumbent_cost > 0 else 0
            
            # Format difference with color indicator
            if diff < 0:
                diff_str = f"-${abs(diff):.2f} ({diff_pct:.0f}% cheaper ✅)"
            elif diff > 0:
                diff_str = f"+${diff:.2f} (+{diff_pct:.0f}% ⚠️)"
            else:
                diff_str = "$0 (same)"
            
            table.append(
                f"| **{band_label}** | {requests_formatted} | "
                f"${incumbent_cost:.2f}/mo | ${railway_cost:.2f}/mo | {diff_str} |"
            )
        
        return "\n".join(table)


def test_enhanced_analyzer():
    """Test the enhanced analyzer"""
    analyzer = InfracostAnalyzer(verbose=True)
    
    # Test data
    tf_data = {
        "resources": {
            "serverless": [
                {"type": "aws_lambda_function", "name": "api_handler"}
            ],
            "networking": [
                {"type": "aws_api_gateway_rest_api", "name": "api"}
            ]
        }
    }
    
    railway_config = {
        "services": [
            {"name": "api", "type": "web", "estimatedRAM_GB": 1.0, "estimatedCPU": 0.5}
        ],
        "databases": [
            {"name": "postgres", "type": "postgres"}
        ]
    }
    
    # Generate 3-band comparison
    print("\n🧪 Testing 3-Band Cost Comparison\n")
    
    baseline = analyzer._determine_baseline_usage(tf_data, railway_config)
    print(f"Baseline usage determined: {baseline['metadata']['requests_per_month']:,} requests/month")
    print(f"Scale: {baseline['metadata']['scale']}")
    print(f"Profile: {baseline['metadata']['profile']}")
    
    scenarios = {
        "low": analyzer._scale_usage(baseline, 0.5),
        "baseline": baseline,
        "high": analyzer._scale_usage(baseline, 2.0)
    }
    
    print("\n3 Usage Scenarios:")
    for name, scenario in scenarios.items():
        requests = scenario['metadata']['requests_per_month']
        print(f"  {name.capitalize()}: {requests:,} requests/month")
    
    # Calculate Railway costs
    print("\nRailway Cost Calculations:")
    for name, scenario in scenarios.items():
        railway_cost = analyzer._calculate_railway_cost_with_usage(railway_config, scenario, name)
        print(f"  {name.capitalize()}: ${railway_cost['totalMonthlyCost']:.2f}/month")
    
    print("\n✅ Test complete!")


if __name__ == "__main__":
    test_enhanced_analyzer()

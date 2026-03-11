"""
Comparison Report - Generates migration analysis report
"""

from pathlib import Path
from datetime import datetime


class ComparisonReport:
    def __init__(self, output_dir, verbose=False):
        self.output_dir = Path(output_dir)
        self.verbose = verbose
        
    def _estimate_railway_cost(self, railway_config):
        """
        Calculate Railway cost using official pricing
        Source: https://docs.railway.com/pricing/plans
        """
        # Official Railway pricing (as of 2026)
        RAM_PER_GB_MONTH = 10.0       # $10/GB/month
        CPU_PER_VCPU_MONTH = 20.0     # $20/vCPU/month
        EGRESS_PER_GB = 0.05          # $0.05/GB
        VOLUME_PER_GB_MONTH = 0.15    # $0.15/GB/month
        
        HOBBY_PLAN = 5    # $5/month (includes $5 usage credit)
        PRO_PLAN = 20     # $20/month (includes $20 usage credit)
        
        # Estimate resource usage (conservative estimate)
        total_ram_gb = 0
        total_vcpus = 0
        
        # Services: estimate 1GB RAM, 1 vCPU each
        services = railway_config.get('services', [])
        total_ram_gb += len(services) * 1.0
        total_vcpus += len(services) * 1.0
        
        # Databases: estimate 1GB RAM, 1 vCPU each
        databases = railway_config.get('databases', [])
        total_ram_gb += len(databases) * 1.0
        total_vcpus += len(databases) * 1.0
        
        # Calculate usage cost (24/7 operation)
        ram_cost = total_ram_gb * RAM_PER_GB_MONTH
        cpu_cost = total_vcpus * CPU_PER_VCPU_MONTH
        
        # Add volume storage
        volumes = railway_config.get('volumes', [])
        volume_gb = sum(v.get('size_gb', 0) for v in volumes)
        volume_cost = volume_gb * VOLUME_PER_GB_MONTH
        
        total_usage = ram_cost + cpu_cost + volume_cost
        
        # Calculate final bill (subscription + usage above included amount)
        hobby_bill = HOBBY_PLAN + max(0, total_usage - 5)
        pro_bill = PRO_PLAN + max(0, total_usage - 20)
        
        # Return the most appropriate plan
        if total_usage <= 5:
            recommended_monthly = hobby_bill
            recommended_plan = "Hobby"
        elif total_usage <= 20:
            recommended_monthly = pro_bill
            recommended_plan = "Pro"
        else:
            recommended_monthly = pro_bill
            recommended_plan = "Pro"
        
        return {
            "monthly": recommended_monthly,
            "plan": recommended_plan,
            "hobby_plan": hobby_bill,
            "pro_plan": pro_bill,
            "breakdown": {
                "ram": ram_cost,
                "cpu": cpu_cost,
                "storage": volume_cost,
                "total_usage": total_usage
            },
            "resources": f"{total_ram_gb}GB RAM, {total_vcpus} vCPU, {volume_gb}GB volume"
        }
        
    def generate(self, tf_data, cost_data, railway_config, sensitivity_data=None):
        """Generate comprehensive migration report"""
        try:
            report_lines = self._build_report(tf_data, cost_data, railway_config, sensitivity_data)
            
            # Write markdown report
            output_path = self.output_dir / "migration-report.md"
            with open(output_path, 'w') as f:
                f.write('\n'.join(report_lines))
            
            if self.verbose:
                print(f"   Generated: {output_path}")
            
            return str(output_path)
            
        except Exception as e:
            print(f"   ⚠️  Error generating report: {e}")
            return None
    
    def _build_report(self, tf_data, cost_data, railway_config, sensitivity_data=None):
        """Build the markdown report content"""
        lines = []
        
        # Header
        lines.extend([
            "# Terraform → Railway Migration Report",
            "",
            f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "---",
            ""
        ])
        
        # Executive Summary
        lines.extend(self._build_executive_summary(tf_data, cost_data, railway_config))
        
        # Cost Comparison (with sensitivity analysis if available)
        lines.extend(self._build_cost_comparison(cost_data, railway_config, sensitivity_data))
        
        # Resource Mapping
        lines.extend(self._build_resource_mapping(tf_data, railway_config))
        
        # Migration Steps
        lines.extend(self._build_migration_steps(railway_config))
        
        # Feature Comparison
        lines.extend(self._build_feature_comparison(railway_config))
        
        # Limitations & Considerations
        lines.extend(self._build_limitations(railway_config))
        
        # Next Steps
        lines.extend(self._build_next_steps(railway_config))
        
        return lines
    
    def _build_executive_summary(self, tf_data, cost_data, railway_config):
        """Build executive summary section"""
        metadata = tf_data.get("metadata", {})
        
        lines = [
            "## 📊 Executive Summary",
            ""
        ]
        
        # Current setup
        lines.extend([
            "### Current Infrastructure",
            f"- **Cloud Provider:** {metadata.get('cloud_provider', 'Unknown')}",
            f"- **Application Type:** {metadata.get('app_type', 'Unknown')}",
            f"- **Terraform Files:** {len(tf_data.get('files', []))} files analyzed",
            ""
        ])
        
        # Resource counts
        resource_counts = metadata.get('resource_counts', {})
        total_resources = sum(count for count in resource_counts.values() if isinstance(count, int))
        lines.append(f"**Total Resources:** {total_resources}")
        lines.append("")
        
        for category, count in resource_counts.items():
            if count > 0:
                lines.append(f"- {category.title()}: {count}")
        
        lines.append("")
        
        # Migration summary
        services = railway_config.get("services", [])
        databases = railway_config.get("databases", [])
        buckets = railway_config.get("buckets", [])
        
        lines.extend([
            "### Railway Migration Plan",
            f"- **Services:** {len(services)}",
            f"- **Databases:** {len(databases)}",
            f"- **Storage Buckets:** {len(buckets)}",
            "",
            "---",
            ""
        ])
        
        return lines
    
    def _build_cost_comparison(self, cost_data, railway_config, sensitivity_data=None):
        """Build cost comparison section with 3-band analysis"""
        lines = [
            "## 💰 Cost Analysis - 3-Band Comparison",
            "",
            "_Apples-to-apples cost comparison at three usage levels: Low (50%), Baseline (100%), and High (200%)_",
            ""
        ]
        
        # Check if we have 3-band data
        if sensitivity_data and isinstance(sensitivity_data, dict) and "low" in sensitivity_data:
            # NEW: 3-Band Cost Comparison
            lines.extend([
                "### 📊 Cost Comparison Across Usage Bands",
                "",
                "Both incumbent cloud and Railway costs calculated at same usage levels:",
                ""
            ])
            
            # Build comparison table
            lines.append("| Usage Band | Requests/Month | Incumbent Cost | Railway Cost | Difference |")
            lines.append("|-----------|----------------|----------------|--------------|------------|")
            
            bands = [
                ("low", "Low (50%)", 0.5),
                ("baseline", "Baseline (100%)", 1.0),
                ("high", "High (200%)", 2.0)
            ]
            
            for band_key, band_label, multiplier in bands:
                band_data = sensitivity_data.get(band_key, {})
                
                requests = band_data.get("usage", {}).get("metadata", {}).get("requests_per_month", 0)
                requests_formatted = f"{requests:,}" if requests > 0 else "N/A"
                
                incumbent_cost = band_data.get("incumbent", {}).get("totalMonthlyCost", 0)
                railway_cost = band_data.get("railway", {}).get("totalMonthlyCost", 0)
                
                diff = railway_cost - incumbent_cost
                diff_pct = (diff / incumbent_cost * 100) if incumbent_cost > 0 else 0
                
                # Format difference with indicators
                if diff < 0:
                    diff_str = f"-${abs(diff):.2f} ({abs(diff_pct):.0f}% cheaper) ✅"
                elif diff > 0:
                    diff_str = f"+${diff:.2f} (+{diff_pct:.0f}%) ⚠️"
                else:
                    diff_str = "$0 (same)"
                
                lines.append(
                    f"| **{band_label}** | {requests_formatted} | "
                    f"${incumbent_cost:.2f}/mo | ${railway_cost:.2f}/mo | {diff_str} |"
                )
            
            lines.extend(["", "#### Usage Assumptions", ""])
            
            # Get baseline metadata
            baseline_meta = sensitivity_data.get("baseline", {}).get("usage", {}).get("metadata", {})
            scale = baseline_meta.get("scale", "small")
            profile = baseline_meta.get("profile", "default")
            avg_duration = baseline_meta.get("avg_duration_ms", 200)
            
            lines.extend([
                f"- **Scale category:** {scale.title()}",
                f"- **Usage profile:** {profile}",
                f"- **Average duration:** {avg_duration}ms per request",
                "- **Bands:** Low (50%), Baseline (100%), High (200%) of baseline usage",
                "",
                "_Costs automatically scaled based on service complexity and resource requirements._",
                ""
            ])
        
        else:
            # FALLBACK: Single cost comparison (old style)
            if cost_data:
                iaas_monthly = cost_data.get('totalMonthlyCost', 0)
                lines.extend([
                    "### Current IaaS Costs (via Infracost)",
                    f"**Monthly Total:** ${iaas_monthly:.2f}",
                    ""
                ])
                
                if iaas_monthly == 0:
                    lines.extend([
                        "⚠️ **Note:** $0 cost typically indicates usage-based resources (Lambda, API Gateway)",
                        "without provided usage data. Actual costs depend on API requests, invocations, and duration.",
                        ""
                    ])
                
                # Breakdown by resource type
                if 'costByType' in cost_data and cost_data['costByType']:
                    lines.append("**Cost Breakdown:**")
                    lines.append("")
                    for res_type, cost in list(cost_data['costByType'].items())[:10]:
                        lines.append(f"- `{res_type}`: ${cost:.2f}/month")
                    lines.append("")
            
            # Railway estimated costs
            railway_estimate = self._estimate_railway_cost(railway_config)
            railway_monthly = railway_estimate['monthly']
            
            lines.extend([
                "### Estimated Railway Costs",
                f"**Recommended Plan:** {railway_estimate['plan']}",
                f"**Monthly Total:** ${railway_monthly:.2f}",
                "",
                "**Cost Breakdown:**",
                f"- RAM usage: ${railway_estimate['breakdown']['ram']:.2f}/month",
                f"- CPU usage: ${railway_estimate['breakdown']['cpu']:.2f}/month",
                f"- Volume storage: ${railway_estimate['breakdown']['storage']:.2f}/month",
                "",
                "_Note: Actual costs depend on resource utilization._",
                ""
            ])
            
            # Calculate savings
            if cost_data:
                iaas_cost = cost_data.get('totalMonthlyCost', 0)
                if iaas_cost > 0:
                    savings = iaas_cost - railway_monthly
                    savings_pct = (savings / iaas_cost) * 100
                    
                    if savings > 0:
                        lines.extend([
                            "### 💚 Potential Savings",
                            f"**Monthly Savings:** ${savings:.2f} ({savings_pct:.1f}%)",
                            f"**Annual Savings:** ${savings * 12:.2f}",
                            ""
                        ])
                    elif savings < 0:
                        increase = abs(savings)
                        increase_pct = abs(savings_pct)
                        lines.extend([
                            "### ⚠️ Cost Increase",
                            f"**Monthly Increase:** ${increase:.2f} ({increase_pct:.1f}%)",
                            "",
                            "_Railway may cost more but includes monitoring, logging, and other features._",
                            ""
                        ])
        
        lines.extend(["", "---", ""])
        
        return lines
    
    def _build_resource_mapping(self, tf_data, railway_config):
        """Build resource mapping section"""
        lines = [
            "## 🔄 Resource Mapping",
            "",
            "### How Terraform Resources Map to Railway",
            ""
        ]
        
        resources = tf_data.get("resources", {})
        
        # Compute resources
        if resources.get("compute"):
            lines.append("#### Compute → Railway Services")
            for res in resources["compute"][:5]:
                lines.append(f"- `{res['type']}` → Railway Service")
            lines.append("")
        
        # Database resources
        if resources.get("database"):
            lines.append("#### Databases → Railway Managed Databases")
            for res in resources["database"][:5]:
                lines.append(f"- `{res['type']}` → Railway Database")
            lines.append("")
        
        # Storage resources
        if resources.get("storage"):
            lines.append("#### Storage → Railway Volumes/Buckets")
            for res in resources["storage"][:5]:
                storage_type = "Volume" if "ebs" in res['type'].lower() or "efs" in res['type'].lower() else "Bucket"
                lines.append(f"- `{res['type']}` → Railway {storage_type}")
            lines.append("")
        
        # Networking resources
        if resources.get("networking"):
            lines.append("#### Networking → Railway Built-in Features")
            lines.append("- Load balancers → Automatic load balancing")
            lines.append("- Security groups → Railway's secure-by-default networking")
            lines.append("- VPC → Not required (Railway handles networking)")
            lines.append("")
        
        # CDN resources
        if resources.get("cdn"):
            lines.append("#### CDN → Railway's Edge CDN")
            lines.append("- CloudFront → Railway's built-in global CDN")
            lines.append("")
        
        # DNS resources
        if resources.get("dns"):
            lines.append("#### DNS → Railway Domains")
            lines.append("- Route53 → Railway domain management")
            lines.append("")
        
        # Serverless resources
        if resources.get("serverless"):
            lines.append("#### Serverless → Railway Services")
            lines.append("- Lambda functions → Containerized services")
            lines.append("- API Gateway → Built-in HTTPS endpoints")
            lines.append("")
        
        lines.extend(["---", ""])
        
        return lines
    
    def _build_migration_steps(self, railway_config):
        """Build migration steps section"""
        lines = [
            "## 🚀 Migration Steps",
            "",
            "### 1. Create Railway Project",
            "```bash",
            "railway init",
            "```",
            ""
        ]
        
        # Database provisioning
        if railway_config.get("databases"):
            lines.extend([
                "### 2. Provision Databases",
                "```bash",
                "./provision-databases.sh",
                "```",
                ""
            ])
        
        # Storage provisioning
        if railway_config.get("buckets"):
            lines.extend([
                "### 3. Provision Storage",
                "```bash",
                "./provision-storage.sh",
                "```",
                ""
            ])
        
        # Deploy services
        if railway_config.get("services"):
            lines.extend([
                "### 4. Deploy Services",
                "```bash",
                "railway up",
                "```",
                ""
            ])
        
        # Manual steps
        migration_notes = railway_config.get("migration_notes", {})
        manual_steps = migration_notes.get("manual_steps", [])
        if manual_steps:
            lines.extend([
                "### 5. Manual Configuration",
                ""
            ])
            for step in manual_steps:
                lines.append(f"- {step}")
            lines.append("")
        
        lines.extend(["---", ""])
        
        return lines
    
    def _build_feature_comparison(self, railway_config):
        """Build feature comparison section"""
        lines = [
            "## ✨ Railway Advantages",
            ""
        ]
        
        migration_notes = railway_config.get("migration_notes", {})
        easy_wins = migration_notes.get("easy_wins", [])
        
        if easy_wins:
            for win in easy_wins:
                lines.append(f"- ✅ {win}")
            lines.append("")
        else:
            lines.extend([
                "- ✅ Automatic HTTPS and SSL certificates",
                "- ✅ Built-in CDN and load balancing",
                "- ✅ Simplified database management",
                "- ✅ Usage-based pricing (pay for what you use)",
                "- ✅ Instant rollbacks and deployment history",
                "- ✅ Built-in monitoring and logs",
                ""
            ])
        
        lines.extend(["---", ""])
        
        return lines
    
    def _build_limitations(self, railway_config):
        """Build limitations section"""
        lines = [
            "## ⚠️ Limitations & Trade-offs",
            "",
            "### Features Not Available or Limited in Railway",
            ""
        ]
        
        migration_notes = railway_config.get("migration_notes", {})
        limitations = migration_notes.get("limitations", [])
        
        if limitations:
            for limitation in limitations:
                lines.append(f"- ⚠️ {limitation}")
            lines.append("")
        else:
            lines.extend([
                "- ⚠️ No VPC peering or advanced networking",
                "- ⚠️ Limited database engine customization",
                "- ⚠️ Some AWS-specific services have no direct equivalent",
                "- ⚠️ Less granular infrastructure control",
                ""
            ])
        
        lines.extend([
            "### Recommendation",
            "",
            "Railway is ideal for:",
            "- Modern web applications",
            "- Startups and small-to-medium teams",
            "- Projects that benefit from simplified operations",
            "",
            "Consider staying with traditional IaaS if you need:",
            "- Complex networking (VPC peering, private links)",
            "- Highly customized database configurations",
            "- AWS-specific services with no alternatives",
            "",
            "---",
            ""
        ])
        
        return lines
    
    def _build_next_steps(self, railway_config):
        """Build next steps section"""
        lines = [
            "## 📋 Next Steps",
            "",
            "1. **Review this report** - Understand cost implications and limitations",
            "2. **Check generated files:**",
            "   - `railway.json` - Service configuration",
            "   - `provision-databases.sh` - Database setup",
            "   - `provision-storage.sh` - Storage setup (if applicable)",
            "3. **Create Railway project** - `railway init`",
            "4. **Run provisioning scripts** - Set up databases and storage",
            "5. **Configure environment variables** - `railway variables`",
            "6. **Deploy** - `railway up`",
            "7. **Test thoroughly** - Verify all functionality works",
            "8. **Monitor costs** - Railway dashboard shows real-time usage",
            "",
            "---",
            "",
            "## 📚 Resources",
            "",
            "- [Railway Documentation](https://docs.railway.com/)",
            "- [Railway CLI Reference](https://docs.railway.com/guides/cli)",
            "- [Railway Pricing](https://docs.railway.com/reference/pricing)",
            "- [Railway Community](https://discord.gg/railway)",
            ""
        ]
        
        return lines

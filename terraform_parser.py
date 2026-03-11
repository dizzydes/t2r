"""
Terraform Parser - Extracts resources and metadata from Terraform files
"""

import re
from pathlib import Path


class TerraformParser:
    def __init__(self, tf_directory, verbose=False):
        self.tf_directory = Path(tf_directory)
        self.verbose = verbose
        
    def parse(self):
        """Parse all Terraform files in the directory"""
        tf_files = list(self.tf_directory.glob("*.tf"))
        
        if not tf_files:
            return None
        
        result = {
            "directory": str(self.tf_directory),
            "files": [],
            "resources": [],
            "providers": [],
            "variables": [],
            "modules": [],
            "metadata": {}
        }
        
        # Check for README
        readme_files = list(self.tf_directory.glob("README.md"))
        if readme_files:
            with open(readme_files[0], 'r', encoding='utf-8', errors='ignore') as f:
                result["metadata"]["readme"] = f.read()
        
        # Parse each file
        for tf_file in tf_files:
            if self.verbose:
                print(f"   Parsing: {tf_file.name}")
            
            with open(tf_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            file_data = {
                "name": tf_file.name,
                "path": str(tf_file),
                "content": content
            }
            result["files"].append(file_data)
            
            # Extract resources
            resources = self._extract_resources(content)
            result["resources"].extend(resources)
            
            # Extract providers
            providers = self._extract_providers(content)
            result["providers"].extend(providers)
            
            # Extract variables
            variables = self._extract_variables(content)
            result["variables"].extend(variables)
            
            # Extract modules
            modules = self._extract_modules(content)
            result["modules"].extend(modules)
        
        # Deduplicate and categorize
        result["resources"] = self._categorize_resources(result["resources"])
        result["providers"] = list(set(result["providers"]))
        
        # Extract metadata
        result["metadata"].update(self._extract_metadata(result))
        
        return result
    
    def _extract_resources(self, content):
        """Extract resource blocks from Terraform content"""
        resources = []
        
        # Pattern: resource "type" "name" { ... }
        pattern = r'resource\s+"([^"]+)"\s+"([^"]+)"\s*\{'
        matches = re.finditer(pattern, content)
        
        for match in matches:
            resource_type = match.group(1)
            resource_name = match.group(2)
            resources.append({
                "type": resource_type,
                "name": resource_name,
                "full_name": f"{resource_type}.{resource_name}"
            })
        
        return resources
    
    def _extract_providers(self, content):
        """Extract provider information"""
        providers = []
        
        # Pattern: provider "name" { ... }
        pattern = r'provider\s+"([^"]+)"'
        matches = re.finditer(pattern, content)
        
        for match in matches:
            providers.append(match.group(1))
        
        # Also check for provider in resource types
        resource_pattern = r'resource\s+"([^_]+)_'
        resource_matches = re.finditer(resource_pattern, content)
        for match in resource_matches:
            providers.append(match.group(1))
        
        return providers
    
    def _extract_variables(self, content):
        """Extract variable definitions"""
        variables = []
        
        # Pattern: variable "name" { ... }
        pattern = r'variable\s+"([^"]+)"\s*\{([^}]*(?:\{[^}]*\}[^}]*)*)\}'
        matches = re.finditer(pattern, content, re.DOTALL)
        
        for match in matches:
            var_name = match.group(1)
            var_block = match.group(2)
            
            # Try to extract default value
            default_match = re.search(r'default\s*=\s*"?([^"\n]+)"?', var_block)
            default = default_match.group(1).strip() if default_match else None
            
            variables.append({
                "name": var_name,
                "default": default
            })
        
        return variables
    
    def _extract_modules(self, content):
        """Extract module blocks"""
        modules = []
        
        # Pattern: module "name" { ... }
        pattern = r'module\s+"([^"]+)"\s*\{([^}]*(?:\{[^}]*\}[^}]*)*)\}'
        matches = re.finditer(pattern, content, re.DOTALL)
        
        for match in matches:
            module_name = match.group(1)
            module_block = match.group(2)
            
            # Try to extract source
            source_match = re.search(r'source\s*=\s*"([^"]+)"', module_block)
            source = source_match.group(1) if source_match else None
            
            modules.append({
                "name": module_name,
                "source": source
            })
        
        return modules
    
    def _categorize_resources(self, resources):
        """Categorize resources by type"""
        categorized = {
            "compute": [],
            "database": [],
            "storage": [],
            "networking": [],
            "cdn": [],
            "dns": [],
            "serverless": [],
            "other": []
        }
        
        for resource in resources:
            res_type = resource["type"].lower()
            
            # Compute resources
            if any(x in res_type for x in ["ec2", "instance", "fargate", "ecs", "eks", "container"]):
                categorized["compute"].append(resource)
            # Database resources
            elif any(x in res_type for x in ["rds", "db", "database", "aurora", "dynamodb", "elasticache", "redis"]):
                categorized["database"].append(resource)
            # Storage resources
            elif any(x in res_type for x in ["s3", "ebs", "efs", "storage", "bucket", "volume"]):
                categorized["storage"].append(resource)
            # Networking resources
            elif any(x in res_type for x in ["vpc", "subnet", "security_group", "route", "gateway", "alb", "elb", "load_balancer"]):
                categorized["networking"].append(resource)
            # CDN resources
            elif any(x in res_type for x in ["cloudfront", "cdn"]):
                categorized["cdn"].append(resource)
            # DNS resources
            elif any(x in res_type for x in ["route53", "dns", "domain"]):
                categorized["dns"].append(resource)
            # Serverless resources
            elif any(x in res_type for x in ["lambda", "function", "api_gateway"]):
                categorized["serverless"].append(resource)
            else:
                categorized["other"].append(resource)
        
        return categorized
    
    def _extract_metadata(self, result):
        """Extract useful metadata from parsed data"""
        metadata = {}
        
        # Determine primary cloud provider
        providers = result.get("providers", [])
        if "aws" in providers or any("aws" in p for p in providers):
            metadata["cloud_provider"] = "AWS"
        elif "gcp" in providers or "google" in providers:
            metadata["cloud_provider"] = "GCP"
        elif "azure" in providers or "azurerm" in providers:
            metadata["cloud_provider"] = "Azure"
        else:
            metadata["cloud_provider"] = "Unknown"
        
        # Count resources by category
        resources = result.get("resources", {})
        metadata["resource_counts"] = {
            category: len(items) 
            for category, items in resources.items()
        }
        
        # Determine application type
        if resources.get("serverless"):
            metadata["app_type"] = "Serverless"
        elif resources.get("compute"):
            metadata["app_type"] = "Container/VM-based"
        elif resources.get("storage") and resources.get("cdn"):
            metadata["app_type"] = "Static Site"
        else:
            metadata["app_type"] = "Unknown"
        
        return metadata

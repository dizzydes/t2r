"""
Railway Generator - Creates Railway configuration files
"""

import json
from pathlib import Path


class RailwayGenerator:
    def __init__(self, output_dir, verbose=False):
        self.output_dir = Path(output_dir)
        self.verbose = verbose
        
    def generate(self, railway_config):
        """Generate Railway configuration files from AI translation"""
        generated_files = []
        
        # Generate railway.json
        if railway_config.get("services"):
            railway_json_path = self._generate_railway_json(railway_config["services"])
            if railway_json_path:
                generated_files.append(railway_json_path)
        
        # Generate database provisioning script
        if railway_config.get("databases") or any("database" in cmd for cmd in railway_config.get("cli_commands", [])):
            db_script_path = self._generate_database_script(railway_config)
            if db_script_path:
                generated_files.append(db_script_path)
        
        # Generate storage provisioning script
        if railway_config.get("buckets") or railway_config.get("volumes") or any("bucket" in cmd or "volume" in cmd for cmd in railway_config.get("cli_commands", [])):
            storage_script_path = self._generate_storage_script(railway_config)
            if storage_script_path:
                generated_files.append(storage_script_path)
        
        # Generate raw config for reference
        raw_config_path = self._generate_raw_config(railway_config)
        if raw_config_path:
            generated_files.append(raw_config_path)
        
        return generated_files
    
    def _generate_railway_json(self, services):
        """Generate railway.json configuration file"""
        try:
            # Railway.json format
            railway_json = {
                "$schema": "https://railway.com/railway.schema.json",
                "build": {},
                "deploy": {}
            }
            
            # Process each service
            for service in services:
                service_name = service.get("name", "app")
                
                # Build configuration
                # RAILPACK is the modern default builder (NOT NIXPACKS which is legacy)
                builder = service.get("builder", "RAILPACK")
                if service.get("buildCommand"):
                    railway_json["build"]["builder"] = builder
                    railway_json["build"]["buildCommand"] = service["buildCommand"]
                elif builder:
                    railway_json["build"]["builder"] = builder
                
                # Deploy configuration
                railway_json["deploy"]["startCommand"] = service.get("startCommand", "")
                railway_json["deploy"]["restartPolicyType"] = "ON_FAILURE"
                railway_json["deploy"]["restartPolicyMaxRetries"] = 10
                
                # Cron schedule (for cron jobs)
                if service.get("cronSchedule"):
                    railway_json["deploy"]["cronSchedule"] = service["cronSchedule"]
                
                # Health check
                if service.get("healthcheckPath"):
                    railway_json["deploy"]["healthcheckPath"] = service["healthcheckPath"]
                    railway_json["deploy"]["healthcheckTimeout"] = 300
                elif service.get("healthcheck"):
                    railway_json["deploy"]["healthcheckPath"] = service["healthcheck"]
                    railway_json["deploy"]["healthcheckTimeout"] = 300
                
                # Only include first service in railway.json
                # Additional services would need separate configs
                break
            
            # Write file
            output_path = self.output_dir / "railway.json"
            with open(output_path, 'w') as f:
                json.dump(railway_json, f, indent=2)
            
            if self.verbose:
                print(f"   Generated: {output_path}")
            
            return str(output_path)
            
        except Exception as e:
            print(f"   ⚠️  Error generating railway.json: {e}")
            return None
    
    def _generate_database_script(self, railway_config):
        """Generate database provisioning script"""
        try:
            script_lines = [
                "#!/bin/bash",
                "#",
                "# Database Provisioning Script for Railway",
                "# Run this after creating your Railway project",
                "#",
                "",
                "set -e",
                "",
                "echo '🗄️  Provisioning databases...'",
                ""
            ]
            
            # Add database creation commands
            databases = railway_config.get("databases", [])
            for db in databases:
                db_type = db.get("type", "postgres")
                db_name = db.get("name", db_type)
                
                script_lines.append(f"# {db_name}")
                if db.get("notes"):
                    script_lines.append(f"# Note: {db['notes']}")
                script_lines.append(f"echo 'Creating {db_type} database: {db_name}...'")
                script_lines.append(f"railway add --database {db_type}")
                script_lines.append("")
            
            # Add CLI commands that are database-related
            cli_commands = railway_config.get("cli_commands", [])
            for cmd in cli_commands:
                if "database" in cmd.lower() or "add --database" in cmd:
                    script_lines.append(f"# From Terraform analysis")
                    script_lines.append(f"echo 'Running: {cmd}'")
                    script_lines.append(cmd)
                    script_lines.append("")
            
            script_lines.append("echo '✅ Database provisioning complete!'")
            script_lines.append("echo ''")
            script_lines.append("echo 'Database credentials are automatically injected as environment variables:'")
            script_lines.append("echo '  - DATABASE_URL'")
            script_lines.append("echo '  - REDIS_URL (if Redis was added)'")
            script_lines.append("echo ''")
            script_lines.append("echo 'View variables with: railway variables'")
            
            # Write script
            output_path = self.output_dir / "provision-databases.sh"
            with open(output_path, 'w') as f:
                f.write('\n'.join(script_lines))
            
            # Make executable
            output_path.chmod(0o755)
            
            if self.verbose:
                print(f"   Generated: {output_path}")
            
            return str(output_path)
            
        except Exception as e:
            print(f"   ⚠️  Error generating database script: {e}")
            return None
    
    def _generate_storage_script(self, railway_config):
        """Generate storage (buckets/volumes) provisioning script"""
        try:
            script_lines = [
                "#!/bin/bash",
                "#",
                "# Storage Provisioning Script for Railway",
                "# Run this after creating your Railway project",
                "#",
                "",
                "set -e",
                "",
                "echo '💾 Provisioning storage...'",
                ""
            ]
            
            # Add bucket creation commands
            buckets = railway_config.get("buckets", [])
            for bucket in buckets:
                bucket_name = bucket.get("name", "storage")
                region = bucket.get("region", "sjc")
                
                script_lines.append(f"# {bucket_name}")
                if bucket.get("notes"):
                    script_lines.append(f"# Note: {bucket['notes']}")
                script_lines.append(f"echo 'Creating S3-compatible bucket: {bucket_name}...'")
                script_lines.append(f"railway bucket create {bucket_name} --region {region}")
                script_lines.append("")
            
            # Add volume documentation (NO CLI COMMANDS - use config patches)
            volumes = railway_config.get("volumes", [])
            if volumes:
                script_lines.append("")
                script_lines.append("# ========================================")
                script_lines.append("# VOLUME CONFIGURATION")
                script_lines.append("# ========================================")
                script_lines.append("#")
                script_lines.append("# IMPORTANT: Railway volumes have NO CLI commands!")
                script_lines.append("# Volumes must be configured via JSON config patches.")
                script_lines.append("#")
                script_lines.append("# Steps to add volumes:")
                script_lines.append("#")
                script_lines.append("# 1. Get your service ID:")
                script_lines.append("#    railway status --json")
                script_lines.append("#")
                script_lines.append("# 2. Apply volume configuration via JSON patch:")
                script_lines.append("#")
                
                for volume in volumes:
                    volume_name = volume.get("name", "data-volume")
                    mount_path = volume.get("mount_path", "/data")
                    size_gb = volume.get("size_gb", 10)
                    
                    script_lines.append(f"# Volume: {volume_name}")
                    script_lines.append(f"# Mount path: {mount_path}")
                    script_lines.append(f"# Size: {size_gb}GB")
                    script_lines.append("#")
                    script_lines.append("# railway environment edit --json <<'JSON'")
                    script_lines.append("# {")
                    script_lines.append("#   \"services\": {")
                    script_lines.append("#     \"<YOUR-SERVICE-ID>\": {")
                    script_lines.append("#       \"volumeMounts\": {")
                    script_lines.append("#         \"<VOLUME-ID>\": {")
                    script_lines.append(f"#           \"mountPath\": \"{mount_path}\"")
                    script_lines.append("#         }")
                    script_lines.append("#       }")
                    script_lines.append("#     }")
                    script_lines.append("#   }")
                    script_lines.append("# }")
                    script_lines.append("# JSON")
                    script_lines.append("#")
                    script_lines.append("# Or configure volumes via the Railway dashboard:")
                    script_lines.append("# https://railway.app/project/<project-id>")
                    script_lines.append("#")
                
                script_lines.append("")
            
            script_lines.append("echo '✅ Storage provisioning complete!'")
            script_lines.append("echo ''")
            
            if buckets:
                script_lines.append("echo 'Bucket credentials are available via:'")
                script_lines.append("echo '  railway bucket credentials --bucket <bucket-name> --json'")
                script_lines.append("echo ''")
            
            if volumes:
                script_lines.append("echo '⚠️  VOLUMES REQUIRE MANUAL CONFIGURATION'")
                script_lines.append("echo 'Railway volumes have no CLI commands.'")
                script_lines.append("echo 'Configure them via:'")
                script_lines.append("echo '  1. Railway dashboard: https://railway.app'")
                script_lines.append("echo '  2. JSON config patches (see comments in this script)'")
                script_lines.append("echo '  3. Docs: https://docs.railway.com/reference/volumes'")
            
            # Write script
            output_path = self.output_dir / "provision-storage.sh"
            with open(output_path, 'w') as f:
                f.write('\n'.join(script_lines))
            
            # Make executable
            output_path.chmod(0o755)
            
            if self.verbose:
                print(f"   Generated: {output_path}")
            
            return str(output_path)
            
        except Exception as e:
            print(f"   ⚠️  Error generating storage script: {e}")
            return None
    
    def _generate_raw_config(self, railway_config):
        """Save raw Railway config as JSON for reference"""
        try:
            output_path = self.output_dir / "railway-config.json"
            with open(output_path, 'w') as f:
                json.dump(railway_config, f, indent=2)
            
            if self.verbose:
                print(f"   Generated: {output_path}")
            
            return str(output_path)
            
        except Exception as e:
            print(f"   ⚠️  Error generating raw config: {e}")
            return None

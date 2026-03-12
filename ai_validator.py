"""
AI Validator - Post-translation validation against known patterns
Ensures AI output matches best practices from learnings.md
"""

import json


class AIValidator:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.critical_issues = []
        self.warnings = []
        self.suggestions = []
    
    def validate_translation(self, railway_config, tf_data=None):
        """Validate AI output against known patterns from learnings.md"""
        self.critical_issues = []
        self.warnings = []
        self.suggestions = []
        
        # Check for deprecated builders
        self._check_builders(railway_config)
        
        # Check database naming
        self._check_database_naming(railway_config)
        
        # Check for fake CLI commands
        self._check_cli_commands(railway_config)
        
        # Validate Functions vs Services decision
        self._check_functions_logic(railway_config, tf_data)
        
        # Check pricing accuracy
        self._check_pricing_references(railway_config)
        
        # Check for required migration notes
        self._check_migration_notes(railway_config)
        
        # Return validation results
        return {
            'valid': len(self.critical_issues) == 0,
            'critical': self.critical_issues,
            'warnings': self.warnings,
            'suggestions': self.suggestions,
            'total_issues': len(self.critical_issues) + len(self.warnings)
        }
    
    def _check_builders(self, config):
        """Check for deprecated NIXPACKS builder"""
        services = config.get('services', [])
        
        for service in services:
            builder = service.get('builder', '')
            if builder == 'NIXPACKS':
                self.critical_issues.append(
                    f"Service '{service.get('name')}' uses deprecated NIXPACKS builder. "
                    "Should use RAILPACK or DOCKERFILE."
                )
    
    def _check_database_naming(self, config):
        """Check for incorrect database naming"""
        databases = config.get('databases', [])
        
        for db in databases:
            db_type = db.get('type', '')
            if db_type == 'mongodb':
                self.critical_issues.append(
                    f"Database uses 'mongodb' - should be 'mongo' (Railway naming convention)"
                )
    
    def _check_cli_commands(self, config):
        """Check for fake volume CLI commands"""
        cli_commands = config.get('cli_commands', [])
        
        for cmd in cli_commands:
            if isinstance(cmd, str) and 'railway volume' in cmd.lower():
                self.critical_issues.append(
                    "Contains 'railway volume' CLI command - Railway has NO volume CLI commands! "
                    "Volumes must be configured via JSON patches."
                )
    
    def _check_functions_logic(self, config, tf_data):
        """Validate Lambda → Functions vs Services decision"""
        functions = config.get('functions', [])
        services = config.get('services', [])
        
        # Check if Functions are appropriately sized
        for func in functions:
            size = func.get('estimatedSize_KB', 0)
            if size > 96:
                self.warnings.append(
                    f"Function '{func.get('name')}' estimated at {size}KB exceeds 96KB limit. "
                    "Consider using a Service instead."
                )
        
        # Check if lambda_analysis is present
        migration_notes = config.get('migration_notes', {})
        lambda_analysis = migration_notes.get('lambda_analysis')
        
        if tf_data and self._has_lambda(tf_data):
            if not lambda_analysis:
                self.warnings.append(
                    "Terraform contains Lambda resources but no lambda_analysis in migration_notes. "
                    "Should include analysis of Functions vs Service decision."
                )
    
    def _check_pricing_references(self, config):
        """Check for accurate Railway pricing references"""
        notes = str(config.get('migration_notes', {}))
        
        # Check for old pricing
        if '$0.10/GB' in notes and 'Network Egress' in notes:
            self.warnings.append(
                "References old Network Egress pricing ($0.10/GB). "
                "Current pricing is $0.05/GB on Railway Metal."
            )
    
    def _check_migration_notes(self, config):
        """Ensure migration notes are comprehensive"""
        notes = config.get('migration_notes', {})
        
        required_keys = ['easy_wins', 'limitations', 'manual_steps']
        missing = [key for key in required_keys if key not in notes]
        
        if missing:
            self.suggestions.append(
                f"Migration notes missing recommended sections: {', '.join(missing)}"
            )
        
        # Check for honest limitations
        limitations = notes.get('limitations', [])
        if not limitations:
            self.suggestions.append(
                "No limitations documented. Consider adding honest assessment of "
                "what Railway can't do (e.g., MSK, BigQuery, complex VPC)."
            )
    
    def _has_lambda(self, tf_data):
        """Check if Terraform data contains Lambda resources"""
        if not tf_data:
            return False
        
        resources = tf_data.get('resources', {})
        compute = resources.get('compute', [])
        
        for resource in compute:
            if 'lambda' in resource.get('type', '').lower():
                return True
        
        return False
    
    def print_results(self, results):
        """Pretty print validation results"""
        if results['valid']:
            print("   ✅ Validation passed - no critical issues")
        else:
            print(f"   ❌ Validation found {len(results['critical'])} critical issue(s)")
        
        for issue in results['critical']:
            print(f"   🔴 CRITICAL: {issue}")
        
        for warning in results['warnings']:
            print(f"   ⚠️  WARNING: {warning}")
        
        if self.verbose:
            for suggestion in results['suggestions']:
                print(f"   💡 SUGGESTION: {suggestion}")

"""
Confidence Scorer - Calculates confidence score for AI translations
Flags uncertain translations for human review
"""


class ConfidenceScorer:
    def __init__(self, verbose=False):
        self.verbose = verbose
    
    def calculate_confidence(self, tf_data, railway_config):
        """
        Calculate confidence score (0-100) for the translation
        Returns: {
            'score': int,
            'level': str,  # 'high', 'medium', 'low'
            'reasons': [str],  # List of reasons affecting score
            'recommendation': str
        }
        """
        score = 100
        reasons = []
        
        # Deduct for unsupported services
        score, reasons = self._check_unsupported_services(score, reasons, tf_data)
        
        # Deduct for complexity
        score, reasons = self._check_complexity(score, reasons, tf_data)
        
        # Deduct for migration limitations
        score, reasons = self._check_limitations(score, reasons, railway_config)
        
        # Deduct for services that should stay on cloud
        score, reasons = self._check_keep_on_cloud(score, reasons, railway_config)
        
        # Add points for clear migration path
        score, reasons = self._check_clear_path(score, reasons, railway_config)
        
        # Determine confidence level
        if score >= 85:
            level = 'high'
            recommendation = 'Proceed with migration - high confidence in translation accuracy'
        elif score >= 70:
            level = 'medium'
            recommendation = 'Review carefully before migration - some complexity detected'
        else:
            level = 'low'
            recommendation = 'Manual review required - complex migration with significant limitations'
        
        return {
            'score': max(0, min(100, score)),
            'level': level,
            'reasons': reasons,
            'recommendation': recommendation
        }
    
    def _check_unsupported_services(self, score, reasons, tf_data):
        """Check for AWS/GCP services without Railway equivalents"""
        resources_str = str(tf_data.get('resources', {}))
        
        unsupported = {
            'MSK': 'Amazon MSK (Managed Kafka)',
            'BigQuery': 'Google BigQuery',
            'Pub/Sub': 'Cloud Pub/Sub',
            'ACM-PCA': 'ACM Private CA',
            'kinesis': 'Amazon Kinesis',
            'redshift': 'Amazon Redshift'
        }
        
        for key, name in unsupported.items():
            if key.lower() in resources_str.lower():
                score -= 30
                reasons.append(f"Contains {name} which has no Railway equivalent")
        
        return score, reasons
    
    def _check_complexity(self, score, reasons, tf_data):
        """Check for infrastructure complexity"""
        resources = tf_data.get('resources', {})
        total_resources = sum(len(v) for v in resources.values() if isinstance(v, list))
        
        if total_resources > 100:
            score -= 15
            reasons.append(f"Large infrastructure ({total_resources} resources) increases complexity")
        elif total_resources > 50:
            score -= 10
            reasons.append(f"Medium infrastructure ({total_resources} resources)")
        
        # Check for VPC complexity
        networking = resources.get('networking', [])
        if len(networking) > 10:
            score -= 10
            reasons.append(f"Complex networking ({len(networking)} resources) may not map to Railway")
        
        return score, reasons
    
    def _check_limitations(self, score, reasons, railway_config):
        """Check for migration limitations"""
        notes = railway_config.get('migration_notes', {})
        limitations = notes.get('limitations', [])
        
        if len(limitations) > 5:
            score -= 15
            reasons.append(f"Significant limitations ({len(limitations)} identified)")
        elif len(limitations) > 3:
            score -= 10
            reasons.append(f"Some limitations ({len(limitations)} identified)")
        
        return score, reasons
    
    def _check_keep_on_cloud(self, score, reasons, railway_config):
        """Check if services should stay on cloud provider"""
        notes = str(railway_config.get('migration_notes', {}))
        
        keep_keywords = ['keep on aws', 'keep on gcp', 'hybrid architecture', 'not recommended']
        
        for keyword in keep_keywords:
            if keyword.lower() in notes.lower():
                score -= 20
                reasons.append("Some services recommended to stay on cloud provider")
                break
        
        return score, reasons
    
    def _check_clear_path(self, score, reasons, railway_config):
        """Add points for clear migration indicators"""
        functions = railway_config.get('functions', [])
        services = railway_config.get('services', [])
        databases = railway_config.get('databases', [])
        
        # Clear migration if we have mapped resources
        if functions or services or databases:
            # Small bonus for having clear Railway mappings
            reasons.append("Clear Railway resource mappings identified")
        
        return score, reasons
    
    def print_score(self, result):
        """Pretty print confidence score"""
        score = result['score']
        level = result['level']
        
        # Color output based on level
        if level == 'high':
            icon = '✅'
        elif level == 'medium':
            icon = '⚠️'
        else:
            icon = '❌'
        
        print(f"\n   {icon} Confidence Score: {score}/100 ({level.upper()})")
        
        if self.verbose and result['reasons']:
            print("   Factors:")
            for reason in result['reasons']:
                print(f"     • {reason}")
        
        print(f"   📋 {result['recommendation']}")

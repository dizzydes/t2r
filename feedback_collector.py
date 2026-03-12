"""
Feedback Collector - Tracks deployment outcomes for continuous learning
Enables the AI to learn from real-world migration results
"""

import json
import hashlib
from datetime import datetime
from pathlib import Path


class FeedbackCollector:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.feedback_file = 'deployment-feedback.jsonl'
        self.learnings_file = 'learnings.md'
    
    def record_deployment(self, tf_data, railway_config, success, errors=None, notes=None):
        """
        Record deployment outcome for learning
        
        Args:
            tf_data: Terraform data that was migrated
            railway_config: Railway configuration generated
            success: Boolean - did deployment succeed?
            errors: List of error messages (if any)
            notes: Optional user notes about the migration
        """
        # Create a hash of the config for deduplication
        config_str = json.dumps(railway_config, sort_keys=True)
        config_hash = hashlib.md5(config_str.encode()).hexdigest()[:8]
        
        feedback = {
            'timestamp': datetime.now().isoformat(),
            'config_hash': config_hash,
            'success': success,
            'errors': errors or [],
            'notes': notes or '',
            'metadata': {
                'cloud_provider': tf_data.get('metadata', {}).get('cloud_provider', 'unknown'),
                'app_type': tf_data.get('metadata', {}).get('app_type', 'unknown'),
                'resource_count': sum(
                    len(v) for v in tf_data.get('resources', {}).values() 
                    if isinstance(v, list)
                ),
                'has_lambda': self._has_lambda(tf_data),
                'has_database': len(railway_config.get('databases', [])) > 0,
                'has_functions': len(railway_config.get('functions', [])) > 0,
                'has_services': len(railway_config.get('services', [])) > 0
            },
            'resource_types': self._extract_resource_types(tf_data),
            'confidence_score': None  # Will be added if available
        }
        
        # Append to JSONL file
        with open(self.feedback_file, 'a') as f:
            f.write(json.dumps(feedback) + '\n')
        
        if self.verbose:
            print(f"   📝 Recorded deployment feedback (hash: {config_hash})")
        
        return feedback
    
    def analyze_patterns(self):
        """
        Analyze collected feedback to identify patterns
        Returns insights that can improve future migrations
        """
        if not Path(self.feedback_file).exists():
            return {
                'total_deployments': 0,
                'success_rate': 0,
                'insights': ['No deployment data collected yet']
            }
        
        feedbacks = []
        with open(self.feedback_file, 'r') as f:
            for line in f:
                try:
                    feedbacks.append(json.loads(line.strip()))
                except json.JSONDecodeError:
                    continue
        
        if not feedbacks:
            return {
                'total_deployments': 0,
                'success_rate': 0,
                'insights': ['No valid feedback data']
            }
        
        # Calculate metrics
        total = len(feedbacks)
        successes = sum(1 for f in feedbacks if f['success'])
        success_rate = (successes / total * 100) if total > 0 else 0
        
        # Analyze by resource type
        lambda_success = self._calculate_success_rate(
            feedbacks, lambda f: f['metadata'].get('has_lambda', False)
        )
        
        function_success = self._calculate_success_rate(
            feedbacks, lambda f: f['metadata'].get('has_functions', False)
        )
        
        service_success = self._calculate_success_rate(
            feedbacks, lambda f: f['metadata'].get('has_services', False)
        )
        
        # Common error patterns
        error_patterns = self._extract_error_patterns(feedbacks)
        
        # Generate insights
        insights = []
        
        if lambda_success['total'] > 0:
            insights.append(
                f"Lambda migrations: {lambda_success['rate']:.1f}% success "
                f"({lambda_success['successes']}/{lambda_success['total']})"
            )
        
        if function_success['total'] > 0:
            insights.append(
                f"Railway Functions: {function_success['rate']:.1f}% success "
                f"({function_success['successes']}/{function_success['total']})"
            )
        
        if service_success['total'] > 0:
            insights.append(
                f"Railway Services: {service_success['rate']:.1f}% success "
                f"({service_success['successes']}/{service_success['total']})"
            )
        
        if error_patterns:
            insights.append(f"Common errors: {', '.join(error_patterns[:3])}")
        
        return {
            'total_deployments': total,
            'success_rate': success_rate,
            'successes': successes,
            'failures': total - successes,
            'lambda_migrations': lambda_success,
            'function_usage': function_success,
            'service_usage': service_success,
            'error_patterns': error_patterns,
            'insights': insights
        }
    
    def update_learnings(self, analysis):
        """
        Update learnings.md with insights from deployment feedback
        """
        if not analysis or analysis['total_deployments'] == 0:
            return
        
        # Generate learnings section
        learnings_update = f"""

## Deployment Feedback Analysis (Auto-Generated)

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  
**Total Deployments Tracked:** {analysis['total_deployments']}  
**Overall Success Rate:** {analysis['success_rate']:.1f}%

### Key Insights

"""
        for insight in analysis['insights']:
            learnings_update += f"- {insight}\n"
        
        if analysis['error_patterns']:
            learnings_update += "\n### Common Error Patterns\n\n"
            for i, error in enumerate(analysis['error_patterns'][:5], 1):
                learnings_update += f"{i}. {error}\n"
        
        learnings_update += "\n---\n"
        
        # Append to learnings.md if it exists
        if Path(self.learnings_file).exists():
            with open(self.learnings_file, 'a') as f:
                f.write(learnings_update)
            
            if self.verbose:
                print(f"   ✅ Updated {self.learnings_file} with deployment insights")
    
    def get_recommendations(self, tf_data, railway_config):
        """
        Get recommendations based on past deployment patterns
        """
        analysis = self.analyze_patterns()
        
        if analysis['total_deployments'] < 5:
            return ["Insufficient deployment data for recommendations (need 5+ deployments)"]
        
        recommendations = []
        
        # Check Lambda → Functions success rate
        if self._has_lambda(tf_data):
            func_rate = analysis['function_usage']['rate']
            if func_rate < 70 and analysis['function_usage']['total'] > 3:
                recommendations.append(
                    f"⚠️  Railway Functions have {func_rate:.0f}% success rate. "
                    "Consider using Services for Lambda migrations."
                )
        
        # Check overall success rate of similar migrations
        cloud = tf_data.get('metadata', {}).get('cloud_provider', '')
        if cloud:
            # Could filter by cloud provider in the future
            pass
        
        if not recommendations:
            recommendations.append("✅ No issues detected based on historical patterns")
        
        return recommendations
    
    def _has_lambda(self, tf_data):
        """Check if Terraform contains Lambda resources"""
        resources = tf_data.get('resources', {})
        compute = resources.get('compute', [])
        
        for resource in compute:
            if 'lambda' in resource.get('type', '').lower():
                return True
        return False
    
    def _extract_resource_types(self, tf_data):
        """Extract list of Terraform resource types"""
        resources = tf_data.get('resources', {})
        types = []
        
        for category, items in resources.items():
            if isinstance(items, list):
                for item in items:
                    resource_type = item.get('type', 'unknown')
                    if resource_type not in types:
                        types.append(resource_type)
        
        return types
    
    def _calculate_success_rate(self, feedbacks, filter_func):
        """Calculate success rate for filtered subset"""
        filtered = [f for f in feedbacks if filter_func(f)]
        total = len(filtered)
        successes = sum(1 for f in filtered if f['success'])
        rate = (successes / total * 100) if total > 0 else 0
        
        return {
            'total': total,
            'successes': successes,
            'failures': total - successes,
            'rate': rate
        }
    
    def _extract_error_patterns(self, feedbacks):
        """Extract most common error patterns"""
        error_counts = {}
        
        for feedback in feedbacks:
            if not feedback['success']:
                for error in feedback['errors']:
                    # Normalize error message
                    error_key = error.lower()[:50]  # First 50 chars
                    error_counts[error_key] = error_counts.get(error_key, 0) + 1
        
        # Sort by frequency
        sorted_errors = sorted(
            error_counts.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        return [error for error, count in sorted_errors if count >= 2]
    
    def print_analysis(self, analysis):
        """Pretty print analysis results"""
        print("\n" + "=" * 60)
        print("📊 DEPLOYMENT FEEDBACK ANALYSIS")
        print("=" * 60)
        
        print(f"\nTotal Deployments: {analysis['total_deployments']}")
        print(f"Success Rate: {analysis['success_rate']:.1f}% "
              f"({analysis['successes']} ✅ / {analysis['failures']} ❌)")
        
        if analysis['insights']:
            print("\n💡 Key Insights:")
            for insight in analysis['insights']:
                print(f"   • {insight}")
        
        if analysis.get('error_patterns'):
            print("\n⚠️  Common Error Patterns:")
            for i, error in enumerate(analysis['error_patterns'][:3], 1):
                print(f"   {i}. {error}")
        
        print("\n" + "=" * 60)

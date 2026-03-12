"""
Documentation Validator - Checks if railway-official-docs.md is current
Ensures AI has access to the latest Railway platform documentation
"""

import hashlib
import os
from datetime import datetime
from pathlib import Path


class DocValidator:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.docs_file = 'railway-official-docs.md'
        self.docs_url = 'https://docs.railway.com/api/llms-docs.md'
    
    def check_freshness(self):
        """
        Verify railway-official-docs.md exists and check last modified time
        Returns: {
            'status': str,  # 'CURRENT', 'MISSING', 'STALE'
            'file_age_days': int,
            'file_size_kb': int,
            'recommendation': str
        }
        """
        if not Path(self.docs_file).exists():
            return {
                'status': 'MISSING',
                'file_age_days': None,
                'file_size_kb': 0,
                'recommendation': f'Download Railway docs: curl -s {self.docs_url} > {self.docs_file}'
            }
        
        # Get file stats
        file_stat = os.stat(self.docs_file)
        file_size_kb = file_stat.st_size // 1024
        
        # Calculate age
        modified_time = datetime.fromtimestamp(file_stat.st_mtime)
        age_days = (datetime.now() - modified_time).days
        
        # Determine status
        if age_days > 30:
            status = 'STALE'
            recommendation = (
                f'Documentation is {age_days} days old. '
                f'Consider refreshing: curl -s {self.docs_url} > {self.docs_file}'
            )
        elif age_days > 14:
            status = 'AGING'
            recommendation = (
                f'Documentation is {age_days} days old. '
                'May want to refresh soon for latest Railway features.'
            )
        else:
            status = 'CURRENT'
            recommendation = f'Documentation is fresh ({age_days} days old).'
        
        return {
            'status': status,
            'file_age_days': age_days,
            'file_size_kb': file_size_kb,
            'recommendation': recommendation
        }
    
    def print_status(self, result):
        """Pretty print documentation status"""
        status = result['status']
        
        if status == 'MISSING':
            print("   ❌ Railway documentation not found!")
            print(f"   📥 {result['recommendation']}")
        elif status == 'STALE':
            print(f"   ⚠️  Railway documentation is {result['file_age_days']} days old")
            print(f"   📥 {result['recommendation']}")
        elif status == 'AGING':
            print(f"   ⏰ Railway documentation is {result['file_age_days']} days old")
            if self.verbose:
                print(f"   💡 {result['recommendation']}")
        else:
            if self.verbose:
                print(f"   ✅ Railway documentation is current ({result['file_age_days']} days old, {result['file_size_kb']}KB)")
    
    def validate_content(self):
        """Validate that docs contain expected Railway features"""
        if not Path(self.docs_file).exists():
            return {'valid': False, 'missing_features': ['File not found']}
        
        with open(self.docs_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for critical Railway features
        required_features = {
            'Functions': 'Railway Functions',
            'Services': 'Service',
            'Databases': 'postgres|mysql|redis|mongo',
            'Buckets': 'bucket',
            'Volumes': 'volume',
            'Cron': 'cronSchedule',
            'RAILPACK': 'RAILPACK',
            'Pricing': 'RAM.*GB.*month|CPU.*vCPU.*month'
        }
        
        missing = []
        for feature, pattern in required_features.items():
            if pattern.lower() not in content.lower():
                missing.append(feature)
        
        return {
            'valid': len(missing) == 0,
            'missing_features': missing,
            'content_size_kb': len(content) // 1024
        }

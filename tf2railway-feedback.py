#!/usr/bin/env python3
"""
Terraform to Railway Feedback Tool
Record deployment outcomes and analyze patterns for continuous improvement
"""

import argparse
import json
import sys
from pathlib import Path
from feedback_collector import FeedbackCollector


def main():
    parser = argparse.ArgumentParser(
        description='Record and analyze deployment feedback for Terraform → Railway migrations'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # Record feedback command
    record_parser = subparsers.add_parser('record', help='Record deployment outcome')
    record_parser.add_argument(
        '--config',
        required=True,
        help='Path to railway-config.json from migration'
    )
    record_parser.add_argument(
        '--success',
        action='store_true',
        help='Deployment was successful'
    )
    record_parser.add_argument(
        '--failure',
        action='store_true',
        help='Deployment failed'
    )
    record_parser.add_argument(
        '--error',
        action='append',
        help='Error message (can specify multiple times)'
    )
    record_parser.add_argument(
        '--notes',
        help='Additional notes about the deployment'
    )
    
    # Analyze feedback command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze deployment patterns')
    analyze_parser.add_argument(
        '--update-learnings',
        action='store_true',
        help='Update learnings.md with insights'
    )
    
    # List feedback command
    list_parser = subparsers.add_parser('list', help='List recent deployments')
    list_parser.add_argument(
        '--limit',
        type=int,
        default=10,
        help='Number of recent deployments to show'
    )
    
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    collector = FeedbackCollector(verbose=args.verbose)
    
    # Handle commands
    if args.command == 'record':
        handle_record(collector, args)
    elif args.command == 'analyze':
        handle_analyze(collector, args)
    elif args.command == 'list':
        handle_list(collector, args)


def handle_record(collector, args):
    """Record deployment feedback"""
    
    # Validate success/failure flags
    if not args.success and not args.failure:
        print("❌ Error: Must specify either --success or --failure")
        sys.exit(1)
    
    if args.success and args.failure:
        print("❌ Error: Cannot specify both --success and --failure")
        sys.exit(1)
    
    # Load railway config
    config_path = Path(args.config)
    if not config_path.exists():
        print(f"❌ Error: Railway config not found: {config_path}")
        sys.exit(1)
    
    try:
        with open(config_path, 'r') as f:
            railway_config = json.load(f)
    except json.JSONDecodeError:
        print(f"❌ Error: Invalid JSON in {config_path}")
        sys.exit(1)
    
    # Try to find tf_data from the same directory
    output_dir = config_path.parent
    tf_data = {'metadata': {}, 'resources': {}}
    
    # Try to infer from migration-report.md if it exists
    report_path = output_dir / 'migration-report.md'
    if report_path.exists():
        # Extract basic info from report
        content = report_path.read_text()
        if 'AWS' in content:
            tf_data['metadata']['cloud_provider'] = 'AWS'
        elif 'GCP' in content:
            tf_data['metadata']['cloud_provider'] = 'GCP'
    
    # Record feedback
    success = args.success
    errors = args.error or []
    notes = args.notes or ''
    
    feedback = collector.record_deployment(
        tf_data=tf_data,
        railway_config=railway_config,
        success=success,
        errors=errors,
        notes=notes
    )
    
    # Print confirmation
    print("\n✅ Deployment feedback recorded!")
    print(f"   Status: {'✅ Success' if success else '❌ Failure'}")
    print(f"   Hash: {feedback['config_hash']}")
    
    if errors:
        print(f"   Errors: {len(errors)}")
        for error in errors:
            print(f"      - {error}")
    
    if notes:
        print(f"   Notes: {notes}")
    
    print(f"\n📝 Feedback saved to: {collector.feedback_file}")
    
    # Show recommendation to analyze
    print("\n💡 Tip: Run 'python3 tf2railway-feedback.py analyze' to see patterns")


def handle_analyze(collector, args):
    """Analyze deployment patterns"""
    
    print("\n🔍 Analyzing deployment feedback...")
    
    analysis = collector.analyze_patterns()
    collector.print_analysis(analysis)
    
    if args.update_learnings and analysis['total_deployments'] > 0:
        print("\n📝 Updating learnings.md...")
        collector.update_learnings(analysis)
        print(f"   ✅ Updated {collector.learnings_file}")
    elif analysis['total_deployments'] > 0:
        print(f"\n💡 Tip: Add --update-learnings to append insights to {collector.learnings_file}")


def handle_list(collector, args):
    """List recent deployments"""
    
    if not Path(collector.feedback_file).exists():
        print("📭 No deployment feedback recorded yet")
        print("\nRecord your first deployment:")
        print("  python3 tf2railway-feedback.py record --config path/to/railway-config.json --success")
        return
    
    feedbacks = []
    with open(collector.feedback_file, 'r') as f:
        for line in f:
            try:
                feedbacks.append(json.loads(line.strip()))
            except json.JSONDecodeError:
                continue
    
    if not feedbacks:
        print("📭 No valid deployment feedback found")
        return
    
    # Show most recent
    recent = feedbacks[-args.limit:]
    recent.reverse()  # Newest first
    
    print(f"\n📊 Recent {len(recent)} Deployments\n")
    print("=" * 80)
    
    for i, feedback in enumerate(recent, 1):
        timestamp = feedback['timestamp'][:19]  # Remove microseconds
        status = '✅ SUCCESS' if feedback['success'] else '❌ FAILURE'
        cloud = feedback['metadata'].get('cloud_provider', 'unknown')
        resources = feedback['metadata'].get('resource_count', 0)
        
        print(f"\n{i}. {timestamp} | {status} | {cloud} | {resources} resources")
        print(f"   Hash: {feedback['config_hash']}")
        
        if feedback['metadata'].get('has_lambda'):
            func_or_svc = 'Functions' if feedback['metadata'].get('has_functions') else 'Services'
            print(f"   Lambda → {func_or_svc}")
        
        if feedback['errors']:
            print(f"   Errors: {len(feedback['errors'])}")
            for error in feedback['errors'][:2]:  # Show first 2
                print(f"      - {error[:70]}...")
        
        if feedback['notes']:
            print(f"   Notes: {feedback['notes'][:70]}...")
    
    print("\n" + "=" * 80)
    print(f"\nTotal feedback entries: {len(feedbacks)}")
    print("\n💡 Run 'python3 tf2railway-feedback.py analyze' for insights")


if __name__ == "__main__":
    main()

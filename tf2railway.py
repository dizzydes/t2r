#!/usr/bin/env python3
"""
Terraform to Railway Migration Tool
Analyzes Terraform files and generates Railway configurations with cost comparisons
"""

import argparse
import json
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import our modules
from infracost_analyzer import InfracostAnalyzer
from terraform_parser import TerraformParser
from ai_translator import AITranslator
from railway_generator import RailwayGenerator
from comparison_report import ComparisonReport
from ai_validator import AIValidator
from confidence_scorer import ConfidenceScorer
from doc_validator import DocValidator


def main():
    parser = argparse.ArgumentParser(
        description='Convert Terraform configurations to Railway with cost analysis'
    )
    parser.add_argument(
        '--input',
        '-i',
        required=True,
        help='Path to Terraform directory'
    )
    parser.add_argument(
        '--output',
        '-o',
        default='./railway-migration',
        help='Output directory for Railway files (default: ./railway-migration)'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    # Validate input directory
    input_path = Path(args.input).resolve()
    if not input_path.exists():
        print(f"❌ Error: Input directory '{input_path}' does not exist")
        sys.exit(1)
    
    # Create output directory
    output_path = Path(args.output).resolve()
    output_path.mkdir(parents=True, exist_ok=True)
    
    print("🚀 Terraform → Railway Migration Tool")
    print("=" * 60)
    print(f"📁 Input:  {input_path}")
    print(f"📁 Output: {output_path}")
    print("=" * 60)
    
    # Step 1: Parse Terraform files
    print("\n📋 Step 1: Parsing Terraform files...")
    tf_parser = TerraformParser(input_path, verbose=args.verbose)
    tf_data = tf_parser.parse()
    
    if not tf_data:
        print("❌ No Terraform files found or parsing failed")
        sys.exit(1)
    
    print(f"✅ Found {len(tf_data.get('files', []))} Terraform files")
    print(f"   Resources: {len(tf_data.get('resources', []))}")
    
    # Step 1.5: Validate Railway documentation freshness
    print("\n📚 Step 1.5: Validating Railway documentation...")
    doc_validator = DocValidator(verbose=args.verbose)
    doc_status = doc_validator.check_freshness()
    doc_validator.print_status(doc_status)
    
    if doc_status['status'] == 'MISSING':
        print("   ❌ Cannot proceed without Railway documentation")
        print(f"   Run: curl -s {doc_validator.docs_url} > {doc_validator.docs_file}")
        sys.exit(1)
    
    # Step 2: AI Translation (before cost analysis, since we need railway_config)
    print("\n🤖 Step 2: Translating to Railway using AI...")
    translator = AITranslator(verbose=args.verbose)
    
    # Initial translation without cost data
    railway_config = translator.translate(tf_data, None)
    
    if not railway_config:
        print("❌ AI translation failed")
        sys.exit(1)
    
    print("✅ Translation complete")
    
    # Step 2.5: Validate AI translation
    print("\n🔍 Step 2.5: Validating AI translation...")
    validator = AIValidator(verbose=args.verbose)
    validation_results = validator.validate_translation(railway_config, tf_data)
    validator.print_results(validation_results)
    
    if not validation_results['valid']:
        print("   ⚠️  Critical issues found but continuing with migration...")
    
    # Step 2.6: Calculate confidence score
    print("\n📊 Step 2.6: Calculating migration confidence score...")
    scorer = ConfidenceScorer(verbose=args.verbose)
    confidence = scorer.calculate_confidence(tf_data, railway_config)
    scorer.print_score(confidence)
    
    # Step 3: Run Enhanced Infracost analysis with 3-band comparison
    print("\n💰 Step 3: Running 3-Band Cost Analysis (50%/100%/200% usage)...")
    infracost = InfracostAnalyzer(verbose=args.verbose)
    
    if not infracost.api_key:
        print("⚠️  INFRACOST_API_KEY not set. Skipping cost analysis.")
        cost_data = None
        band_results = None
    else:
        # Run 3-band analysis with Railway config for context
        band_results = infracost.analyze_with_bands(input_path, tf_data, railway_config)
        
        if band_results:
            # Extract baseline cost for display
            cost_data = band_results.get("baseline", {}).get("incumbent", {})
            
            print("✅ 3-Band Cost Analysis Complete:")
            for band in ["low", "baseline", "high"]:
                band_data = band_results.get(band, {})
                incumbent = band_data.get("incumbent", {}).get("totalMonthlyCost", 0)
                railway = band_data.get("railway", {}).get("totalMonthlyCost", 0)
                requests = band_data.get("usage", {}).get("metadata", {}).get("requests_per_month", 0)
                
                if requests > 0:
                    print(f"   {band.title():<10} ({requests:>12,} req/mo): Incumbent ${incumbent:>7.2f} | Railway ${railway:>7.2f}")
                else:
                    print(f"   {band.title():<10}: Incumbent ${incumbent:>7.2f} | Railway ${railway:>7.2f}")
        else:
            cost_data = None
            print("⚠️  Cost analysis unavailable (continuing without it)")
    
    # Step 4: Generate Railway files
    print("\n📝 Step 4: Generating Railway configuration files...")
    generator = RailwayGenerator(output_path, verbose=args.verbose)
    generated_files = generator.generate(railway_config)
    
    print(f"✅ Generated {len(generated_files)} files:")
    for file in generated_files:
        print(f"   📄 {file}")
    
    # Step 5: Generate comparison report with 3-band data
    print("\n📊 Step 5: Generating migration report with 3-band cost comparison...")
    report = ComparisonReport(output_path, verbose=args.verbose)
    report_file = report.generate(tf_data, cost_data, railway_config, band_results)
    
    print(f"✅ Report generated: {report_file}")
    
    # Summary
    print("\n" + "=" * 60)
    print("✨ Migration analysis complete!")
    print("=" * 60)
    print(f"\n📂 Output directory: {output_path}")
    print("\nNext steps:")
    print("1. Review the migration-report.md for cost & feature comparison")
    print("2. Review railway.json for service configuration")
    print("3. Run provision-*.sh scripts to create databases/storage")
    print("4. Deploy to Railway with: railway up")
    print("\n⚠️  Important: Review limitations section before migrating!")
    

if __name__ == "__main__":
    main()

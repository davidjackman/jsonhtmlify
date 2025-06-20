#!/usr/bin/env python3
"""
Complete CLI Demonstration Script
This script demonstrates all features of the Dashboard CLI tool including:
1. Dataset discovery and listing
2. Data preview functionality
3. Single table generation
4. Multi-dataset dashboard creation
5. Custom dashboard configurations
"""

import subprocess
import os
import sys
import time
from pathlib import Path


def run_command(command, description):
    """Run a CLI command and display results."""
    print(f"\n{'='*60}")
    print(f"🔧 {description}")
    print(f"💻 Command: {command}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=os.getcwd())
        if result.returncode == 0:
            print(result.stdout)
            if result.stderr:
                print(f"⚠️ Warnings: {result.stderr}")
        else:
            print(f"❌ Error: {result.stderr}")
            print(f"📤 Return code: {result.returncode}")
    except Exception as e:
        print(f"❌ Exception: {e}")


def main():
    """Run complete CLI demonstration."""
    print("🚀 Dashboard CLI - Complete Feature Demonstration")
    print("=" * 80)
    print()
    print("This demonstration will show all CLI features:")
    print("1. 📋 List available datasets")
    print("2. 🔍 Preview dataset contents")
    print("3. 📊 Generate single tables")
    print("4. 🏢 Create comprehensive dashboards")
    print("5. 🎯 Custom dashboard configurations")
    print()
    
    print("🎬 Starting demonstration...")
    
    # Change to project directory
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # 1. List available datasets
    run_command(
        "python dashboard_cli.py list",
        "Step 1: List All Available Datasets"
    )
    
    # 2. Preview different datasets
    datasets_to_preview = ["employee_data", "key_metrics", "quarterly_performance"]
    for dataset in datasets_to_preview:
        run_command(
            f"python dashboard_cli.py preview {dataset}",
            f"Step 2: Preview {dataset} Dataset"
        )
    
    # 3. Generate single tables
    print(f"\n{'='*60}")
    print("📊 Step 3: Generate Single HTML Tables")
    print(f"{'='*60}")
    
    single_table_commands = [
        ("python dashboard_cli.py table employee_data --output demo_employees.html", 
         "Employee Directory Table"),
        ("python dashboard_cli.py table quarterly_performance --output demo_quarterly.html", 
         "Quarterly Performance Table"),
        ("python dashboard_cli.py table key_metrics --output demo_metrics.html", 
         "Key Metrics Table")
    ]
    
    for command, description in single_table_commands:
        run_command(command, f"Generate: {description}")
    
    # 4. Generate comprehensive dashboard
    run_command(
        "python dashboard_cli.py dashboard --output demo_full_dashboard.html",
        "Step 4: Generate Complete Business Dashboard (All Datasets)"
    )
    
    # 5. Generate custom dashboards
    print(f"\n{'='*60}")
    print("🎯 Step 5: Generate Custom Dashboard Configurations")
    print(f"{'='*60}")
    
    custom_dashboard_commands = [
        ("python dashboard_cli.py dashboard --datasets key_metrics employee_data --output demo_executive_summary.html",
         "Executive Summary Dashboard (Metrics + Employees)"),
        ("python dashboard_cli.py dashboard --datasets quarterly_performance regional_performance product_performance --output demo_sales_analysis.html",
         "Sales Analysis Dashboard (Performance Data)"),
        ("python dashboard_cli.py dashboard --datasets regional_performance product_performance --output demo_market_analysis.html",
         "Market Analysis Dashboard (Regional + Product)")
    ]
    
    for command, description in custom_dashboard_commands:
        run_command(command, description)
    
    # 6. Show generated files
    print(f"\n{'='*60}")
    print("📁 Step 6: Summary of Generated Files")
    print(f"{'='*60}")
    
    generated_files = [
        "demo_employees.html",
        "demo_quarterly.html", 
        "demo_metrics.html",
        "demo_full_dashboard.html",
        "demo_executive_summary.html",
        "demo_sales_analysis.html",
        "demo_market_analysis.html"
    ]
    
    print("✅ Generated HTML Files:")
    for filename in generated_files:
        filepath = Path(filename)
        if filepath.exists():
            size = filepath.stat().st_size
            print(f"  📄 {filename:<35} ({size:,} bytes)")
            print(f"      🌐 file://{filepath.absolute()}")
        else:
            print(f"  ❌ {filename:<35} (not found)")
    
    # 7. CLI Help Information
    run_command(
        "python dashboard_cli.py --help",
        "Step 7: CLI Help Information"
    )
    
    # 8. Individual command help
    help_commands = [
        ("python dashboard_cli.py list --help", "List Command Help"),
        ("python dashboard_cli.py preview --help", "Preview Command Help"),
        ("python dashboard_cli.py table --help", "Table Command Help"),
        ("python dashboard_cli.py dashboard --help", "Dashboard Command Help")
    ]
    
    for command, description in help_commands:
        run_command(command, description)
    
    # Final summary
    print(f"\n{'='*80}")
    print("🎉 CLI DEMONSTRATION COMPLETE!")
    print(f"{'='*80}")
    print()
    print("📊 What was demonstrated:")
    print("  ✅ Dataset discovery and listing")
    print("  ✅ Data preview functionality")
    print("  ✅ Single table generation with custom output")
    print("  ✅ Comprehensive multi-dataset dashboards")
    print("  ✅ Custom dashboard configurations")
    print("  ✅ All command-line options and help")
    print()
    print("🎯 Key Features Showcased:")
    print("  ✅ Interactive sortable columns")
    print("  ✅ Responsive mobile-friendly design")
    print("  ✅ Professional styling and animations")
    print("  ✅ Collapsible dashboard sections")
    print("  ✅ Color-coded data visualization")
    print("  ✅ JSON-driven data architecture")
    print()
    print("🌐 Generated Files Ready for Browser:")
    for filename in generated_files:
        if Path(filename).exists():
            print(f"  📄 {filename}")
    print()
    print("🚀 Next Steps:")
    print("  1. Open any generated HTML file in your browser")
    print("  2. Click column headers to test sorting functionality")
    print("  3. Try the dashboard collapsible sections")
    print("  4. Test responsive design on mobile devices")
    print("  5. Add your own JSON data files to the /data directory")
    print()
    print("📖 For detailed usage instructions, see: CLI_USAGE_GUIDE.md")


if __name__ == "__main__":
    main()

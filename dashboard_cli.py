#!/usr/bin/env python3
"""
Interactive Dashboard CLI
A command-line interface for generating HTML dashboards from JSON data sources.
"""

import json
import os
import argparse
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from src.table_generator import TableGenerator
from datetime import datetime


class DashboardCLI:
    def __init__(self):
        self.data_dir = Path(__file__).parent / "data"
        self.output_dir = Path(__file__).parent
        self.available_datasets = self._discover_datasets()
        
    def _discover_datasets(self) -> Dict[str, str]:
        """Discover available JSON datasets."""
        datasets = {}
        if self.data_dir.exists():
            for json_file in self.data_dir.glob("*.json"):
                key = json_file.stem
                datasets[key] = str(json_file)
        return datasets
    
    def load_dataset(self, dataset_name: str) -> Dict[str, Any]:
        """Load a JSON dataset."""
        if dataset_name not in self.available_datasets:
            raise ValueError(f"Dataset '{dataset_name}' not found. Available: {list(self.available_datasets.keys())}")
        
        with open(self.available_datasets[dataset_name], 'r') as f:
            return json.load(f)
    
    def list_datasets(self):
        """List all available datasets."""
        print("📊 Available Datasets:")
        print("=" * 50)
        
        for name, path in self.available_datasets.items():
            data = self.load_dataset(name)
            
            # Get dataset info
            if isinstance(data, dict):
                if len(data) == 1:
                    # Single key dataset
                    key = list(data.keys())[0]
                    value = data[key]
                    if isinstance(value, list):
                        count = len(value)
                        item_type = "records"
                    elif isinstance(value, dict):
                        count = len(value)
                        item_type = "metrics"
                    else:
                        count = 1
                        item_type = "item"
                else:
                    count = len(data)
                    item_type = "top-level keys"
            elif isinstance(data, list):
                count = len(data)
                item_type = "records"
            else:
                count = 1
                item_type = "item"
            
            print(f"  • {name:<25} {count:>3} {item_type}")
        
        print(f"\n💾 Data files location: {self.data_dir}")
    
    def preview_dataset(self, dataset_name: str, limit: int = 3):
        """Preview a dataset."""
        try:
            data = self.load_dataset(dataset_name)
            print(f"🔍 Preview of '{dataset_name}':")
            print("=" * 50)
            
            if isinstance(data, dict) and len(data) == 1:
                # Single key dataset
                key = list(data.keys())[0]
                value = data[key]
                print(f"Dataset key: {key}")
                
                if isinstance(value, list) and value:
                    print(f"Records: {len(value)}")
                    print(f"Sample records (showing {min(limit, len(value))}):")
                    for i, record in enumerate(value[:limit]):
                        print(f"  Record {i+1}: {record}")
                elif isinstance(value, dict):
                    print(f"Metrics: {len(value)}")
                    print("Sample metrics:")
                    for i, (k, v) in enumerate(list(value.items())[:limit]):
                        print(f"  {k}: {v}")
            else:
                print(f"Structure: {type(data).__name__}")
                if isinstance(data, dict):
                    print("Keys:", list(data.keys())[:limit])
                elif isinstance(data, list):
                    print(f"Items: {len(data)}")
                    print("Sample:", data[:limit])
                    
        except Exception as e:
            print(f"❌ Error previewing dataset: {e}")
    
    def generate_single_table(self, dataset_name: str, output_file: str = None, 
                            sortable: bool = True, striped: bool = True):
        """Generate a single HTML table from a dataset."""
        try:
            data = self.load_dataset(dataset_name)
            
            # Extract the data array
            if isinstance(data, dict) and len(data) == 1:
                key = list(data.keys())[0]
                table_data = data[key]
                table_title = key.replace('_', ' ').title()
            else:
                table_data = data
                table_title = dataset_name.replace('_', ' ').title()
            
            # Handle key_metrics special case (convert to list format)
            if dataset_name == 'key_metrics' and isinstance(table_data, dict):
                formatted_data = []
                for metric_key, metric_data in table_data.items():
                    if isinstance(metric_data, dict):
                        row = {
                            'Metric': metric_key.replace('_', ' ').title(),
                            'Value': metric_data.get('formatted', str(metric_data.get('value', ''))),
                            'Description': metric_data.get('description', ''),
                            'Trend': metric_data.get('trend', '').title()
                        }
                        formatted_data.append(row)
                table_data = formatted_data
            
            # Generate table
            generator = TableGenerator(
                sortable=sortable,
                striped=striped,
                responsive=True,
                table_class=f'{dataset_name}-table'
            )
            
            table_html = generator.generate_table(table_data)
            
            # Create styled HTML document
            css = self._get_basic_css()
            content = f"""
            <div class="container">
                <h1>📊 {table_title}</h1>
                <p class="subtitle">Generated from {dataset_name}.json</p>
                <div class="table-section">
                    <p class="help-text">💡 Click column headers to sort data</p>
                    {table_html}
                </div>
                <div class="footer">
                    <p>Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
                    <p>✨ Powered by HTML Table Generator</p>
                </div>
            </div>
            """
            
            complete_html = generator.render_html(content, title=f"{table_title} - Data Table", css=css)
            
            # Save file
            if not output_file:
                output_file = f"{dataset_name}_table.html"
            
            output_path = self.output_dir / output_file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(complete_html)
            
            print(f"✅ Table generated: {output_path}")
            print(f"📊 Records: {len(table_data) if isinstance(table_data, list) else 'N/A'}")
            print(f"🌐 Open in browser: file://{output_path.absolute()}")
            
        except Exception as e:
            print(f"❌ Error generating table: {e}")
    
    def generate_dashboard(self, datasets: List[str] = None, output_file: str = "interactive_dashboard.html"):
        """Generate a comprehensive dashboard from multiple datasets."""
        try:
            if not datasets:
                datasets = list(self.available_datasets.keys())
            
            print(f"🚀 Generating dashboard with datasets: {', '.join(datasets)}")
            
            # Load all datasets
            all_data = {}
            for dataset_name in datasets:
                if dataset_name in self.available_datasets:
                    all_data[dataset_name] = self.load_dataset(dataset_name)
                else:
                    print(f"⚠️ Warning: Dataset '{dataset_name}' not found, skipping...")
            
            # Generate tables for each dataset
            sections = []
            
            for dataset_name, data in all_data.items():
                section_html = self._generate_dashboard_section(dataset_name, data)
                sections.append(section_html)
            
            # Create dashboard
            dashboard_content = self._create_dashboard_layout(sections)
            
            # Generate complete HTML
            generator = TableGenerator(sortable=True, striped=True)
            complete_html = generator.render_html(
                dashboard_content,
                title="Interactive Business Dashboard",
                css=self._get_dashboard_css()
            )
            
            # Save file
            output_path = self.output_dir / output_file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(complete_html)
            
            print(f"✅ Dashboard generated: {output_path}")
            print(f"📊 Sections: {len(sections)}")
            print(f"🌐 Open in browser: file://{output_path.absolute()}")
            
        except Exception as e:
            print(f"❌ Error generating dashboard: {e}")
    
    def _generate_dashboard_section(self, dataset_name: str, data: Dict[str, Any]) -> str:
        """Generate a dashboard section for a dataset."""
        # Extract the data array
        if isinstance(data, dict) and len(data) == 1:
            key = list(data.keys())[0]
            table_data = data[key]
            section_title = key.replace('_', ' ').title()
        else:
            table_data = data
            section_title = dataset_name.replace('_', ' ').title()
        
        # Handle key_metrics special case
        if dataset_name == 'key_metrics' and isinstance(table_data, dict):
            formatted_data = []
            for metric_key, metric_data in table_data.items():
                if isinstance(metric_data, dict):
                    row = {
                        'Metric': metric_key.replace('_', ' ').title(),
                        'Value': metric_data.get('formatted', str(metric_data.get('value', ''))),
                        'Description': metric_data.get('description', ''),
                        'Trend': metric_data.get('trend', '').title()
                    }
                    formatted_data.append(row)
            table_data = formatted_data
        
        # Create generator with dataset-specific styling
        color_map = {
            'quarterly_performance': '#4a90e2',
            'regional_performance': '#5cb85c',
            'product_performance': '#d9534f',
            'key_metrics': '#8e44ad',
            'employee_data': '#f39c12'
        }
        
        color = color_map.get(dataset_name, '#6c757d')
        
        generator = TableGenerator(
            sortable=True,
            striped=True,
            responsive=True,
            table_class=f'{dataset_name}-table',
            styles={
                'th': f'background-color: {color}; color: white; padding: 12px; border: 1px solid #ddd;',
                'td': 'padding: 10px; border: 1px solid #ddd;'
            }
        )
        
        table_html = generator.generate_table(table_data)
        
        # Create collapsible section
        collapsible_section = generator.make_collapsible_with_css(
            table_html,
            title=f"📊 {section_title}",
            collapsed=dataset_name != 'key_metrics',  # Keep key_metrics expanded
            container_class=f'{dataset_name}-section'
        )
        
        return collapsible_section
    
    def _create_dashboard_layout(self, sections: List[str]) -> str:
        """Create the dashboard layout."""
        current_time = datetime.now().strftime('%B %d, %Y at %I:%M %p')
        
        return f"""
        <div class="dashboard-container">
            <div class="dashboard-header">
                <h1>🏢 Interactive Business Dashboard</h1>
                <p class="dashboard-subtitle">Generated from JSON Data Sources</p>
                <div class="dashboard-timestamp">📅 Generated: {current_time}</div>
            </div>
            
            <div class="dashboard-sections">
                {''.join(sections)}
            </div>
            
            <div class="dashboard-footer">
                <div>✨ Powered by HTML Table Generator - Interactive Data Visualization</div>
                <div class="footer-info">
                    <span>📊 {len(sections)} Data Sources</span>
                    <span>🔄 Real-time Sorting</span>
                    <span>📱 Mobile Responsive</span>
                    <span>💾 JSON Data Driven</span>
                </div>
            </div>
        </div>
        """
    
    def _get_basic_css(self) -> str:
        """Get basic CSS for single table views."""
        return """
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
            line-height: 1.6;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            color: #6c757d;
            margin-bottom: 30px;
            font-style: italic;
        }
        .help-text {
            color: #6c757d;
            font-style: italic;
            margin-bottom: 15px;
            background: #f8f9fa;
            padding: 8px 12px;
            border-radius: 4px;
            border-left: 4px solid #4a90e2;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #e9ecef;
            color: #7f8c8d;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        .sortable tbody tr:hover {
            background-color: #f8f9fa;
        }
        """
    
    def _get_dashboard_css(self) -> str:
        """Get CSS for dashboard layout."""
        return """
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f0f2f5;
            line-height: 1.6;
        }
        .dashboard-container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            padding: 40px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            border-top: 4px solid #4a90e2;
        }
        .dashboard-header {
            text-align: center;
            margin-bottom: 40px;
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 8px;
            border-left: 4px solid #4a90e2;
        }
        .dashboard-header h1 {
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        .dashboard-subtitle {
            color: #6c757d;
            font-size: 1.2em;
            margin-bottom: 10px;
        }
        .dashboard-timestamp {
            color: #7f8c8d;
            font-style: italic;
        }
        .dashboard-sections {
            margin-bottom: 30px;
        }
        .dashboard-footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #e9ecef;
            color: #7f8c8d;
        }
        .footer-info {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin-top: 15px;
        }
        .footer-info span {
            background: #f8f9fa;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.85em;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        .sortable tbody tr:hover {
            background-color: #f8f9fa;
        }
        @media (max-width: 768px) {
            .dashboard-container {
                margin: 10px;
                padding: 20px;
            }
            .footer-info {
                flex-direction: column;
                align-items: center;
                gap: 10px;
            }
        }
        """


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Interactive Dashboard CLI - Generate HTML dashboards from JSON data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s list                                    # List available datasets
  %(prog)s preview quarterly_performance           # Preview a dataset
  %(prog)s table employee_data                     # Generate single table
  %(prog)s dashboard                               # Generate full dashboard
  %(prog)s dashboard --datasets key_metrics regional_performance
  %(prog)s table product_performance --output products.html
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List available datasets')
    
    # Preview command
    preview_parser = subparsers.add_parser('preview', help='Preview a dataset')
    preview_parser.add_argument('dataset', help='Dataset name to preview')
    preview_parser.add_argument('--limit', type=int, default=3, help='Number of records to show')
    
    # Single table command
    table_parser = subparsers.add_parser('table', help='Generate single HTML table')
    table_parser.add_argument('dataset', help='Dataset name to generate table from')
    table_parser.add_argument('--output', help='Output HTML file name')
    table_parser.add_argument('--no-sort', action='store_true', help='Disable sorting')
    table_parser.add_argument('--no-stripe', action='store_true', help='Disable striped rows')
    
    # Dashboard command
    dashboard_parser = subparsers.add_parser('dashboard', help='Generate comprehensive dashboard')
    dashboard_parser.add_argument('--datasets', nargs='+', help='Specific datasets to include')
    dashboard_parser.add_argument('--output', default='interactive_dashboard.html', help='Output HTML file name')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Initialize CLI
    cli = DashboardCLI()
    
    try:
        if args.command == 'list':
            cli.list_datasets()
            
        elif args.command == 'preview':
            cli.preview_dataset(args.dataset, args.limit)
            
        elif args.command == 'table':
            cli.generate_single_table(
                args.dataset,
                args.output,
                sortable=not args.no_sort,
                striped=not args.no_stripe
            )
            
        elif args.command == 'dashboard':
            cli.generate_dashboard(args.datasets, args.output)
            
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

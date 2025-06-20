#!/usr/bin/env python3
"""
Multi-Table HTML Document Generator
This demonstrates how to create a complete HTML document with multiple tables
from a list of table configurations, perfect for reports and dashboards.
"""

from src.table_generator import TableGenerator


def create_multi_table_document():
    """Create an HTML document with multiple tables from a list configuration."""
    
    # Define multiple table configurations
    table_configs = [
        {
            'title': '📊 Q1 2025 Sales Performance',
            'data': [
                ['Region', 'Product', 'Revenue', 'Units Sold', 'Growth'],
                ['North', 'Laptops', '$245,000', 245, '+15%'],
                ['North', 'Accessories', '$89,000', 1780, '+8%'],
                ['South', 'Laptops', '$189,000', 189, '+12%'],
                ['South', 'Software', '$156,000', 312, '+22%'],
                ['West', 'Laptops', '$289,000', 289, '+18%'],
                ['West', 'Accessories', '$95,000', 1900, '+7%']
            ],
            'generator_config': {
                'table_class': 'sales-table',
                'striped': True,
                'responsive': True,
                'custom_headers': {
                    'Revenue': 'Revenue ($)',
                    'Units Sold': 'Units',
                    'Growth': 'Growth Rate'
                }
            },
            'collapsible': {
                'enabled': True,
                'collapsed': False,
                'container_class': 'sales-section'
            }
        },
        {
            'title': '👥 Employee Performance Dashboard',
            'data': [
                {'ID': 'EMP001', 'Name': 'Sarah Johnson', 'Department': 'Engineering', 'Performance': 'Excellent', 'Salary': 125000},
                {'ID': 'EMP002', 'Name': 'Mike Chen', 'Department': 'Product', 'Performance': 'Outstanding', 'Salary': 135000},
                {'ID': 'EMP003', 'Name': 'Lisa Rodriguez', 'Department': 'Design', 'Performance': 'Excellent', 'Salary': 115000},
                {'ID': 'EMP004', 'Name': 'David Kim', 'Department': 'Engineering', 'Performance': 'Outstanding', 'Salary': 145000},
                {'ID': 'EMP005', 'Name': 'Anna Petrov', 'Department': 'Marketing', 'Performance': 'Good', 'Salary': 98000}
            ],
            'generator_config': {
                'table_class': 'employee-table',
                'striped': True,
                'sortable': True,
                'custom_headers': {
                    'ID': 'Employee ID',
                    'Name': 'Full Name',
                    'Performance': 'Rating',
                    'Salary': 'Annual Salary'
                }
            },
            'collapsible': {
                'enabled': True,
                'collapsed': True,
                'container_class': 'employee-section'
            }
        },
        {
            'title': '💰 Financial Summary - Key Metrics',
            'data': {
                'Total Revenue': '$1,052,000',
                'Operating Expenses': '$789,000',
                'Net Profit': '$263,000',
                'Profit Margin': '25.0%',
                'ROI': '18.5%',
                'Cash Flow': '$445,000'
            },
            'generator_config': {
                'table_class': 'financial-table',
                'custom_headers': {
                    'Total Revenue': 'Total Revenue (YTD)',
                    'Operating Expenses': 'Op. Expenses',
                    'Net Profit': 'Net Profit',
                    'Profit Margin': 'Margin %',
                    'ROI': 'Return on Investment',
                    'Cash Flow': 'Cash Flow'
                }
            },
            'collapsible': {
                'enabled': True,
                'collapsed': False,
                'container_class': 'financial-section'
            }
        },
        {
            'title': '📈 Product Inventory Status',
            'data': [
                ('Product Code', 'Product Name', 'Category', 'Stock', 'Status', 'Reorder Level'),
                ('PRD-001', 'ThinkPad X1 Carbon', 'Laptops', 45, 'In Stock', 20),
                ('PRD-002', 'Wireless Mouse Pro', 'Accessories', 230, 'In Stock', 50),
                ('PRD-003', 'USB-C Hub 8-in-1', 'Accessories', 89, 'In Stock', 30),
                ('PRD-004', 'Webcam 4K Ultra', 'Electronics', 12, 'Low Stock', 25),
                ('PRD-005', 'Keyboard Mechanical', 'Accessories', 0, 'Out of Stock', 15)
            ],
            'generator_config': {
                'table_class': 'inventory-table',
                'striped': True,
                'responsive': True
            },
            'collapsible': {
                'enabled': True,
                'collapsed': True,
                'container_class': 'inventory-section'
            }
        },
        {
            'title': '🎯 Project Status Overview',
            'data': [
                {'Project': 'Website Redesign', 'Status': 'In Progress', 'Completion': '75%', 'Lead': 'Sarah Johnson', 'Due Date': '2025-07-15'},
                {'Project': 'Mobile App Launch', 'Status': 'Planning', 'Completion': '25%', 'Lead': 'Mike Chen', 'Due Date': '2025-08-30'},
                {'Project': 'API Integration', 'Status': 'Complete', 'Completion': '100%', 'Lead': 'David Kim', 'Due Date': '2025-06-01'},
                {'Project': 'User Research', 'Status': 'In Progress', 'Completion': '60%', 'Lead': 'Lisa Rodriguez', 'Due Date': '2025-07-01'},
                {'Project': 'Marketing Campaign', 'Status': 'Planning', 'Completion': '15%', 'Lead': 'Anna Petrov', 'Due Date': '2025-09-15'}
            ],
            'generator_config': {
                'table_class': 'project-table',
                'striped': True,
                'responsive': True,
                'custom_headers': {
                    'Project': 'Project Name',
                    'Status': 'Current Status',
                    'Completion': 'Progress',
                    'Lead': 'Project Lead',
                    'Due Date': 'Target Date'
                }
            },
            'collapsible': {
                'enabled': False  # This one stays always visible
            }
        }
    ]
    
    print("🏗️  Building Multi-Table HTML Document...")
    print(f"📋 Processing {len(table_configs)} table sections...")
    
    # Process each table configuration
    html_sections = []
    
    for i, config in enumerate(table_configs, 1):
        print(f"  {i}. {config['title']}")
        
        # Create generator with specific configuration
        generator = TableGenerator(**config['generator_config'])
        
        # Generate the table
        table_html = generator.generate_table(config['data'])
        
        # Make collapsible if configured
        if config['collapsible']['enabled']:
            section_html = generator.make_collapsible_with_css(
                table_html,
                title=config['title'],
                collapsed=config['collapsible']['collapsed'],
                container_class=config['collapsible']['container_class']
            )
        else:
            # Non-collapsible section with custom styling
            section_html = f"""
            <div class="table-section">
                <h2 class="section-title">{config['title']}</h2>
                <div class="table-container">
                    {table_html}
                </div>
            </div>
            """
        
        html_sections.append(section_html)
    
    # Create the complete document
    document_body = '\n\n'.join(html_sections)
    
    # Custom CSS for the multi-table document
    document_css = """
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    .main-container {
        max-width: 1400px;
        margin: 0 auto;
        background: white;
        border-radius: 12px;
        padding: 40px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .document-header {
        text-align: center;
        margin-bottom: 40px;
        padding-bottom: 20px;
        border-bottom: 3px solid #e9ecef;
    }
    
    .document-title {
        font-size: 3em;
        font-weight: 300;
        color: #2c3e50;
        margin-bottom: 10px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .document-subtitle {
        font-size: 1.2em;
        color: #7f8c8d;
        font-weight: 400;
    }
    
    .table-section {
        margin-bottom: 30px;
        background: #f8f9fa;
        border-radius: 8px;
        padding: 20px;
        border-left: 4px solid #28a745;
    }
    
    .section-title {
        color: #2c3e50;
        font-size: 1.8em;
        margin-bottom: 15px;
        font-weight: 600;
    }
    
    .table-container {
        background: white;
        border-radius: 6px;
        padding: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Enhanced table styling */
    .sales-table, .employee-table, .financial-table, .inventory-table, .project-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 14px;
    }
    
    .sales-table th {
        background: linear-gradient(135deg, #28a745, #20c997);
        color: white;
        padding: 12px;
        text-align: left;
        font-weight: 600;
    }
    
    .employee-table th {
        background: linear-gradient(135deg, #007bff, #0056b3);
        color: white;
        padding: 12px;
        text-align: left;
        font-weight: 600;
    }
    
    .financial-table th {
        background: linear-gradient(135deg, #fd7e14, #e55100);
        color: white;
        padding: 12px;
        text-align: left;
        font-weight: 600;
    }
    
    .inventory-table th {
        background: linear-gradient(135deg, #6610f2, #6f42c1);
        color: white;
        padding: 12px;
        text-align: left;
        font-weight: 600;
    }
    
    .project-table th {
        background: linear-gradient(135deg, #dc3545, #c82333);
        color: white;
        padding: 12px;
        text-align: left;
        font-weight: 600;
    }
    
    .sales-table td, .employee-table td, .financial-table td, 
    .inventory-table td, .project-table td {
        padding: 10px 12px;
        border-bottom: 1px solid #e9ecef;
    }
    
    .sales-table.striped tr:nth-child(even),
    .employee-table.striped tr:nth-child(even),
    .inventory-table.striped tr:nth-child(even),
    .project-table.striped tr:nth-child(even) {
        background-color: #f8f9fa;
    }
    
    .document-footer {
        text-align: center;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 2px solid #e9ecef;
        color: #6c757d;
        font-style: italic;
    }
    
    .stats-summary {
        display: flex;
        justify-content: space-around;
        margin: 30px 0;
        padding: 20px;
        background: linear-gradient(135deg, #f8f9fa, #e9ecef);
        border-radius: 8px;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        font-size: 2em;
        font-weight: bold;
        color: #495057;
    }
    
    .stat-label {
        color: #6c757d;
        font-size: 0.9em;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-container {
            padding: 20px;
            margin: 10px;
        }
        
        .document-title {
            font-size: 2em;
        }
        
        .stats-summary {
            flex-direction: column;
            gap: 15px;
        }
    }
    """
    
    # Create header and footer content
    header_content = """
    <div class="document-header">
        <h1 class="document-title">📊 Executive Dashboard</h1>
        <p class="document-subtitle">Comprehensive Business Intelligence Report - June 2025</p>
    </div>
    
    <div class="stats-summary">
        <div class="stat-item">
            <div class="stat-number">5</div>
            <div class="stat-label">Data Sources</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">$1.05M</div>
            <div class="stat-label">Total Revenue</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">25%</div>
            <div class="stat-label">Profit Margin</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">5</div>
            <div class="stat-label">Active Projects</div>
        </div>
    </div>
    """
    
    footer_content = """
    <div class="document-footer">
        <p>📈 Generated with HTML Table Generator v2.0 | 📅 June 19, 2025</p>
        <p>This report contains live data from multiple business systems and is updated automatically.</p>
    </div>
    """
    
    # Wrap everything in a container
    complete_body = f"""
    <div class="main-container">
        {header_content}
        {document_body}
        {footer_content}
    </div>
    """
    
    # Generate the complete HTML document
    generator = TableGenerator()  # Use default generator for document creation
    complete_html = generator.render_html(
        complete_body,
        title="Executive Dashboard - Multi-Table Report",
        css=document_css
    )
    
    return complete_html


def main():
    """Create and save the multi-table HTML document."""
    print("🚀 Multi-Table HTML Document Generator")
    print("=" * 50)
    
    # Generate the document
    html_document = create_multi_table_document()
    
    # Save to file
    output_file = '/Users/david/htmldictify/html-table-generator/multi_table_dashboard.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_document)
    
    print(f"\n✅ Multi-table document created successfully!")
    print(f"📁 File saved as: {output_file}")
    print(f"📊 Document size: {len(html_document):,} characters")
    print(f"🌐 Open the file in your browser to see the interactive dashboard")
    
    # Display summary
    print(f"\n📋 Document Contents:")
    print(f"  • Sales Performance (CSV format, collapsible)")
    print(f"  • Employee Dashboard (Dict format, collapsible)")
    print(f"  • Financial Metrics (Single dict, collapsible)")
    print(f"  • Inventory Status (Tuple format, collapsible)")
    print(f"  • Project Overview (Dict format, always visible)")
    print(f"\n🎨 Features Demonstrated:")
    print(f"  • Multiple data formats in one document")
    print(f"  • Mix of collapsible and static sections")
    print(f"  • Professional styling with gradients")
    print(f"  • Responsive design for mobile")
    print(f"  • Interactive elements and animations")


if __name__ == "__main__":
    main()

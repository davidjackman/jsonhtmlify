#!/usr/bin/env python3
"""
Complete Workflow Demo: From Raw Data to Interactive Collapsible Tables
This demonstrates the full power of the HTML Table Generator including:
1. Multiple data formats (dict, CSV-like)
2. Advanced styling and configuration
3. Collapsible table functionality
4. Complete HTML document generation
"""

from src.table_generator import TableGenerator


def demo_complete_workflow():
    """Demonstrate a complete real-world workflow."""
    print("🚀 Complete Workflow Demo: Interactive Dashboard")
    print("=" * 60)
    
    # === 1. Raw Data in Different Formats ===
    print("\n📊 Step 1: Processing Multiple Data Sources")
    
    # Sales data from CSV export
    sales_csv = [
        ['Quarter', 'Product', 'Revenue', 'Units', 'Growth'],
        ['Q1 2025', 'Laptops', 245000, 245, '+15%'],
        ['Q1 2025', 'Accessories', 89000, 1780, '+8%'],
        ['Q1 2025', 'Software', 156000, 312, '+22%'],
        ['Q2 2025', 'Laptops', 289000, 289, '+18%'],
        ['Q2 2025', 'Accessories', 95000, 1900, '+7%'],
        ['Q2 2025', 'Software', 178000, 356, '+14%']
    ]
    
    # Employee data from database (dict format)
    employee_data = [
        {'ID': 'EMP001', 'Name': 'Sarah Johnson', 'Department': 'Engineering', 
         'Level': 'Senior', 'Salary': 125000, 'Performance': 'Excellent'},
        {'ID': 'EMP002', 'Name': 'Mike Chen', 'Department': 'Product', 
         'Level': 'Manager', 'Salary': 135000, 'Performance': 'Outstanding'},
        {'ID': 'EMP003', 'Name': 'Lisa Rodriguez', 'Department': 'Design', 
         'Level': 'Lead', 'Salary': 115000, 'Performance': 'Excellent'},
        {'ID': 'EMP004', 'Name': 'David Kim', 'Department': 'Engineering', 
         'Level': 'Principal', 'Salary': 145000, 'Performance': 'Outstanding'},
        {'ID': 'EMP005', 'Name': 'Anna Petrov', 'Department': 'Marketing', 
         'Level': 'Senior', 'Salary': 98000, 'Performance': 'Good'}
    ]
    
    # Financial metrics (mixed format)
    financial_metrics = {
        'Total Revenue': '$1,052,000',
        'Operating Expenses': '$789,000', 
        'Net Profit': '$263,000',
        'Profit Margin': '25.0%',
        'ROI': '18.5%'
    }
    
    print("✅ Data loaded: Sales (CSV), Employees (Dict), Metrics (Single Dict)")
    
    # === 2. Create Styled Tables ===
    print("\n🎨 Step 2: Generating Styled Tables")
    
    # Sales table with custom styling
    sales_generator = TableGenerator(
        table_class='sales-data',
        striped=True,
        responsive=True,
        sortable=True,  # Enable sorting for sales data
        custom_headers={
            'Quarter': 'Period',
            'Revenue': 'Revenue ($)',
            'Units': 'Units Sold',
            'Growth': 'Growth Rate'
        },
        styles={
            'table': 'width: 100%; font-family: "Segoe UI", sans-serif;',
            'th': 'background: linear-gradient(135deg, #4CAF50, #45a049); color: white; padding: 12px;',
            'td': 'padding: 10px; border-bottom: 1px solid #e0e0e0;'
        }
    )
    
    # Employee table with different styling
    employee_generator = TableGenerator(
        table_class='employee-roster',
        striped=True,
        sortable=True,
        custom_headers={
            'ID': 'Employee ID',
            'Name': 'Full Name',
            'Level': 'Job Level',
            'Salary': 'Annual Salary',
            'Performance': 'Rating'
        },
        styles={
            'table': 'width: 100%; font-family: "Segoe UI", sans-serif;',
            'th': 'background: linear-gradient(135deg, #2196F3, #1976D2); color: white; padding: 12px;',
            'td': 'padding: 10px; border-bottom: 1px solid #e3f2fd;'
        }
    )
    
    # Financial metrics table
    metrics_generator = TableGenerator(
        table_class='financial-summary',
        sortable=True,  # Enable sorting for financial metrics
        styles={
            'table': 'width: 100%; font-family: "Segoe UI", sans-serif;',
            'th': 'background: linear-gradient(135deg, #FF9800, #F57C00); color: white; padding: 12px;',
            'td': 'padding: 10px; font-weight: 600; font-size: 16px;'
        }
    )
    
    # Generate tables
    sales_table = sales_generator.generate_table(sales_csv)
    employee_table = employee_generator.generate_table(employee_data)
    metrics_table = metrics_generator.generate_table(financial_metrics)
    
    print("✅ Tables generated with custom styling and headers")
    
    # === 3. Create Collapsible Sections ===
    print("\n📋 Step 3: Creating Interactive Collapsible Sections")
    
    # Sales section (expanded by default)
    sales_collapsible = sales_generator.make_collapsible_with_css(
        sales_table,
        title="📈 Sales Performance Dashboard - Q1 & Q2 2025",
        collapsed=False,
        container_class="sales-section"
    )
    
    # Employee section (collapsed by default)
    employee_collapsible = employee_generator.make_collapsible_with_css(
        employee_table,
        title="👥 Employee Directory & Performance",
        collapsed=True,
        container_class="employee-section"
    )
    
    # Financial metrics (expanded)
    metrics_collapsible = metrics_generator.make_collapsible_with_css(
        metrics_table,
        title="💰 Financial Summary - Key Metrics",
        collapsed=False,
        container_class="metrics-section"
    )
    
    print("✅ Collapsible sections created with professional styling")
    
    # === 4. Create Complete Dashboard ===
    print("\n🌐 Step 4: Building Complete Interactive Dashboard")
    
    # Custom CSS for the enhanced dashboard
    dashboard_css = """
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    .dashboard-container {
        max-width: 1400px;
        margin: 0 auto;
        background: white;
        border-radius: 16px;
        padding: 40px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.15);
        position: relative;
        overflow: hidden;
    }
    
    .dashboard-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #4CAF50, #2196F3, #FF9800, #E91E63);
    }
    
    h1 {
        text-align: center;
        color: #2c3e50;
        margin-bottom: 40px;
        font-size: 3.2em;
        font-weight: 300;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        letter-spacing: -0.5px;
    }
    
    .dashboard-header {
        text-align: center;
        margin-bottom: 40px;
        padding: 20px;
        background: linear-gradient(135deg, #f8f9fa, #e9ecef);
        border-radius: 12px;
        border-left: 4px solid #4CAF50;
    }
    
    .dashboard-subtitle {
        color: #6c757d;
        font-size: 1.3em;
        margin-bottom: 20px;
        font-weight: 400;
    }
    
    .stats-overview {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #ffffff, #f8f9fa);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border-left: 4px solid #4CAF50;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .stat-number {
        font-size: 2.5em;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 5px;
    }
    
    .stat-label {
        color: #6c757d;
        font-size: 0.9em;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .dashboard-section {
        margin-bottom: 35px;
        position: relative;
    }
    
    .section-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 15px;
        padding: 0 5px;
    }
    
    .section-title {
        font-size: 1.4em;
        color: #2c3e50;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .sort-help {
        font-size: 0.85em;
        color: #6c757d;
        font-style: italic;
        display: flex;
        align-items: center;
        gap: 5px;
    }
    
    .timestamp {
        text-align: center;
        color: #7f8c8d;
        font-style: italic;
        margin-top: 50px;
        padding-top: 30px;
        border-top: 2px solid #e9ecef;
        font-size: 1.1em;
    }
    
    /* Enhanced sortable table styling */
    .sortable th[data-sortable] {
        position: relative;
        cursor: pointer;
        user-select: none;
        transition: all 0.3s ease;
    }
    
    .sortable th[data-sortable]:hover {
        filter: brightness(1.15);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    
    .sortable th[data-sortable]:active {
        transform: translateY(0px);
    }
    
    /* Sort indicator styling */
    .sort-indicator {
        font-size: 0.8em;
        margin-left: 8px;
        transition: all 0.2s ease;
    }
    
    .sortable th.sort-asc .sort-indicator::after {
        content: ' ↑';
        color: #fff;
        font-weight: bold;
        opacity: 1;
        animation: sortPulse 0.3s ease;
    }
    
    .sortable th.sort-desc .sort-indicator::after {
        content: ' ↓';
        color: #fff;
        font-weight: bold;
        opacity: 1;
        animation: sortPulse 0.3s ease;
    }
    
    @keyframes sortPulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .dashboard-container {
            margin: 10px;
            padding: 20px;
            border-radius: 12px;
        }
        
        h1 {
            font-size: 2.2em;
        }
        
        .stats-overview {
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
        }
        
        .stat-number {
            font-size: 2em;
        }
        
        .section-header {
            flex-direction: column;
            align-items: flex-start;
            gap: 10px;
        }
    }
    """
    
    # Combine all sections
    dashboard_content = f"""
    <div class="dashboard-container">
        <h1>🏢 Executive Dashboard</h1>
        
        <div class="dashboard-section">
            {metrics_collapsible}
        </div>
        
        <div class="dashboard-section">
            {sales_collapsible}
        </div>
        
        <div class="dashboard-section">
            {employee_collapsible}
        </div>
        
        <div class="timestamp">
            📅 Generated on June 19, 2025 | HTML Table Generator v2.0
        </div>
    </div>
    """
    
    # Create complete HTML document
    complete_dashboard = sales_generator.render_html(
        dashboard_content,
        title="Executive Dashboard - Interactive Report",
        css=dashboard_css
    )
    
    print("✅ Complete interactive dashboard assembled")
    
    # === 5. Save Results ===
    print("\n💾 Step 5: Saving Results")
    
    # Save the complete dashboard
    dashboard_file = '/Users/david/htmldictify/html-table-generator/executive_dashboard.html'
    with open(dashboard_file, 'w', encoding='utf-8') as f:
        f.write(complete_dashboard)
    
    print(f"✅ Dashboard saved as: {dashboard_file}")
    print(f"📊 Document size: {len(complete_dashboard):,} characters")
    
    # === 6. Display Summary ===
    print("\n📋 Step 6: Workflow Summary")
    print("=" * 60)
    print("🎯 Data Sources Processed:")
    print("  • Sales data (CSV format) - 6 records")
    print("  • Employee data (Dict format) - 5 records") 
    print("  • Financial metrics (Single dict) - 5 metrics")
    print()
    print("🎨 Features Demonstrated:")
    print("  • Multiple data format support")
    print("  • Custom headers and styling")
    print("  • Collapsible table sections")
    print("  • Professional CSS animations")
    print("  • Complete HTML document generation")
    print("  • Responsive design")
    print()
    print("✨ Interactive Features:")
    print("  • Expandable/collapsible sections")
    print("  • Hover effects and transitions")
    print("  • Mobile-responsive design")
    print("  • Professional styling")
    
    return complete_dashboard


def main():
    """Run the complete workflow demonstration."""
    dashboard = demo_complete_workflow()
    
    print("\n" + "=" * 60)
    print("🎉 COMPLETE WORKFLOW DEMONSTRATION FINISHED!")
    print("=" * 60)
    print("✅ Interactive dashboard created successfully")
    print("🌐 Open 'executive_dashboard.html' in your browser to see the results")
    print("📱 The dashboard is fully responsive and interactive")
    print()
    print("🚀 This demonstrates the full power of the HTML Table Generator:")
    print("   → Multiple data format support")
    print("   → Professional styling and animations") 
    print("   → Collapsible interactive sections")
    print("   → Complete HTML document generation")
    print("   → Production-ready output")


if __name__ == "__main__":
    main()

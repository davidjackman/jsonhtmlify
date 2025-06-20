#!/usr/bin/env python3
"""
Simple Browser Compatible Dashboard Demo
This creates a dashboard optimized for VS Code Simple Browser while maintaining functionality
"""

from src.table_generator import TableGenerator
from datetime import datetime


def create_simple_browser_dashboard():
    """Create a dashboard optimized for Simple Browser compatibility."""
    print("🚀 Creating Simple Browser Compatible Dashboard")
    print("=" * 60)
    
    # Same data as enhanced version
    quarterly_data = [
        ['Quarter', 'Revenue', 'Profit', 'Growth', 'Customers', 'Market Share'],
        ['Q1 2024', '$2.1M', '$420K', '+12%', '1,250', '15.2%'],
        ['Q2 2024', '$2.4M', '$480K', '+14%', '1,380', '16.1%'],
        ['Q3 2024', '$2.8M', '$560K', '+17%', '1,520', '17.8%'],
        ['Q4 2024', '$3.2M', '$640K', '+15%', '1,690', '18.5%'],
        ['Q1 2025', '$3.6M', '$720K', '+13%', '1,840', '19.2%'],
        ['Q2 2025', '$4.1M', '$820K', '+14%', '2,010', '20.1%']
    ]
    
    regional_data = [
        {'Region': 'North America', 'Revenue': '$1.8M', 'Units': '2,450', 'Growth': '+18%', 'Profit': '$360K'},
        {'Region': 'Europe', 'Revenue': '$1.2M', 'Units': '1,680', 'Growth': '+15%', 'Profit': '$240K'},
        {'Region': 'Asia Pacific', 'Revenue': '$900K', 'Units': '1,320', 'Growth': '+22%', 'Profit': '$180K'},
        {'Region': 'Latin America', 'Revenue': '$200K', 'Units': '280', 'Growth': '+8%', 'Profit': '$40K'}
    ]
    
    product_data = [
        {'Product': 'Enterprise Software', 'Revenue': '$1.5M', 'Units': '850', 'Margin': '42%', 'Rating': '4.8/5'},
        {'Product': 'Cloud Services', 'Revenue': '$1.2M', 'Units': '1,200', 'Margin': '38%', 'Rating': '4.7/5'},
        {'Product': 'Mobile Apps', 'Revenue': '$800K', 'Units': '2,100', 'Margin': '35%', 'Rating': '4.6/5'},
        {'Product': 'Consulting', 'Revenue': '$600K', 'Units': '120', 'Margin': '45%', 'Rating': '4.9/5'}
    ]
    
    key_metrics = {
        'Total Revenue': '$4.1M',
        'Net Profit': '$820K',
        'Profit Margin': '20.0%',
        'Customer Retention': '94.5%',
        'Market Share': '20.1%',
        'Employee Count': '285',
        'Customer Satisfaction': '4.7/5',
        'Revenue Growth': '+14%'
    }
    
    print("✅ Data sources loaded")
    
    # Create table generators with simpler styling
    quarterly_gen = TableGenerator(
        table_class='quarterly-performance',
        striped=True,
        responsive=True,
        sortable=True,
        styles={
            'table': 'width: 100%; font-family: Arial, sans-serif; border-collapse: collapse;',
            'th': 'background-color: #4a90e2; color: white; padding: 12px; text-align: center; border: 1px solid #ddd;',
            'td': 'padding: 10px; text-align: center; border: 1px solid #ddd;'
        }
    )
    
    regional_gen = TableGenerator(
        table_class='regional-performance',
        striped=True,
        sortable=True,
        styles={
            'table': 'width: 100%; font-family: Arial, sans-serif; border-collapse: collapse;',
            'th': 'background-color: #5cb85c; color: white; padding: 12px; border: 1px solid #ddd;',
            'td': 'padding: 10px; border: 1px solid #ddd;'
        }
    )
    
    product_gen = TableGenerator(
        table_class='product-performance',
        striped=True,
        sortable=True,
        styles={
            'table': 'width: 100%; font-family: Arial, sans-serif; border-collapse: collapse;',
            'th': 'background-color: #d9534f; color: white; padding: 12px; border: 1px solid #ddd;',
            'td': 'padding: 10px; border: 1px solid #ddd;'
        }
    )
    
    metrics_gen = TableGenerator(
        table_class='key-metrics',
        sortable=True,
        styles={
            'table': 'width: 100%; font-family: Arial, sans-serif; border-collapse: collapse;',
            'th': 'background-color: #8e44ad; color: white; padding: 12px; border: 1px solid #ddd;',
            'td': 'padding: 12px; font-weight: bold; font-size: 16px; text-align: center; border: 1px solid #ddd;'
        }
    )
    
    # Generate tables
    quarterly_table = quarterly_gen.generate_table(quarterly_data)
    regional_table = regional_gen.generate_table(regional_data)
    product_table = product_gen.generate_table(product_data)
    metrics_table = metrics_gen.generate_table(key_metrics)
    
    # Create collapsible sections
    metrics_section = metrics_gen.make_collapsible_with_css(
        metrics_table,
        title="📊 Key Performance Indicators",
        collapsed=False
    )
    
    quarterly_section = quarterly_gen.make_collapsible_with_css(
        quarterly_table,
        title="📈 Quarterly Performance Trends",
        collapsed=False
    )
    
    regional_section = regional_gen.make_collapsible_with_css(
        regional_table,
        title="🌍 Regional Performance Breakdown",
        collapsed=True
    )
    
    product_section = product_gen.make_collapsible_with_css(
        product_table,
        title="🛍️ Top Product Performance",
        collapsed=True
    )
    
    print("✅ Tables and sections created")
    
    # Simple Browser compatible CSS - no complex gradients or animations
    simple_css = """
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 20px;
        background-color: #f5f5f5;
        line-height: 1.6;
    }
    
    .dashboard-container {
        max-width: 1200px;
        margin: 0 auto;
        background: white;
        border-radius: 8px;
        padding: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
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
    
    .dashboard-title {
        font-size: 2.5em;
        color: #2c3e50;
        margin-bottom: 15px;
        font-weight: normal;
    }
    
    .dashboard-subtitle {
        color: #6c757d;
        font-size: 1.2em;
        margin-bottom: 15px;
    }
    
    .dashboard-timestamp {
        color: #7f8c8d;
        font-size: 1em;
        font-style: italic;
    }
    
    .stats-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        margin: 30px 0;
        justify-content: center;
    }
    
    .stat-card {
        background: white;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #4a90e2;
        min-width: 180px;
        flex: 1;
        max-width: 220px;
    }
    
    .stat-card:hover {
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        transform: translateY(-2px);
        transition: all 0.2s ease;
    }
    
    .stat-number {
        font-size: 2.2em;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 8px;
    }
    
    .stat-label {
        color: #6c757d;
        font-size: 0.9em;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .dashboard-section {
        margin-bottom: 30px;
    }
    
    .section-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 15px;
        flex-wrap: wrap;
        gap: 10px;
    }
    
    .section-title {
        font-size: 1.4em;
        color: #2c3e50;
        font-weight: 600;
    }
    
    .sort-help {
        font-size: 0.85em;
        color: #6c757d;
        font-style: italic;
        background: rgba(108, 117, 125, 0.1);
        padding: 6px 10px;
        border-radius: 4px;
    }
    
    /* Sortable table styling - simplified for Simple Browser */
    .sortable th[data-sortable] {
        cursor: pointer;
        user-select: none;
        position: relative;
    }
    
    .sortable th[data-sortable]:hover {
        background-color: rgba(255, 255, 255, 0.2);
    }
    
    .sort-indicator {
        font-size: 0.8em;
        margin-left: 8px;
    }
    
    .sortable th.sort-asc .sort-indicator::after {
        content: ' ↑';
        color: #fff;
        font-weight: bold;
    }
    
    .sortable th.sort-desc .sort-indicator::after {
        content: ' ↓';
        color: #fff;
        font-weight: bold;
    }
    
    /* Table hover effects - simplified */
    .sortable tbody tr:hover {
        background-color: #f8f9fa;
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
        align-items: center;
        gap: 20px;
        flex-wrap: wrap;
        margin-top: 15px;
    }
    
    .footer-item {
        padding: 6px 12px;
        background-color: #f8f9fa;
        border-radius: 4px;
        font-size: 0.85em;
        border: 1px solid #dee2e6;
    }
    
    /* Responsive design - simplified */
    @media (max-width: 768px) {
        .dashboard-container {
            margin: 10px;
            padding: 20px;
        }
        
        .dashboard-title {
            font-size: 2em;
        }
        
        .stats-grid {
            flex-direction: column;
            align-items: center;
        }
        
        .stat-card {
            max-width: 100%;
            min-width: 200px;
        }
        
        .section-header {
            flex-direction: column;
            align-items: flex-start;
        }
        
        .footer-info {
            flex-direction: column;
            gap: 10px;
        }
    }
    """
    
    # Build dashboard content
    current_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    
    dashboard_content = f"""
    <div class="dashboard-container">
        <div class="dashboard-header">
            <h1 class="dashboard-title">🏢 Executive Dashboard</h1>
            <p class="dashboard-subtitle">Business Intelligence & Analytics Portal</p>
            <div class="dashboard-timestamp">📅 Last Updated: {current_time}</div>
        </div>
        
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">$4.1M</div>
                <div class="stat-label">Total Revenue</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">$820K</div>
                <div class="stat-label">Net Profit</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">20.1%</div>
                <div class="stat-label">Market Share</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">2,010</div>
                <div class="stat-label">Customers</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">94.5%</div>
                <div class="stat-label">Retention Rate</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">4.7/5</div>
                <div class="stat-label">Satisfaction</div>
            </div>
        </div>
        
        <div class="dashboard-section">
            <div class="section-header">
                <div class="section-title">Key Performance Indicators</div>
                <div class="sort-help">💡 Click column headers to sort</div>
            </div>
            {metrics_section}
        </div>
        
        <div class="dashboard-section">
            <div class="section-header">
                <div class="section-title">Quarterly Performance Analysis</div>
                <div class="sort-help">📈 Track revenue trends</div>
            </div>
            {quarterly_section}
        </div>
        
        <div class="dashboard-section">
            <div class="section-header">
                <div class="section-title">Regional Market Performance</div>
                <div class="sort-help">🌍 Compare regions</div>
            </div>
            {regional_section}
        </div>
        
        <div class="dashboard-section">
            <div class="section-header">
                <div class="section-title">Top Product Categories</div>
                <div class="sort-help">🛍️ Analyze products</div>
            </div>
            {product_section}
        </div>
        
        <div class="dashboard-footer">
            <div>✨ Powered by HTML Table Generator v2.0 - Compatible Dashboard</div>
            <div class="footer-info">
                <div class="footer-item">📊 Interactive Sorting</div>
                <div class="footer-item">🔄 Real-time Updates</div>
                <div class="footer-item">📱 Mobile Responsive</div>
                <div class="footer-item">🖥️ Simple Browser Compatible</div>
            </div>
        </div>
    </div>
    """
    
    # Create complete HTML document
    complete_dashboard = quarterly_gen.render_html(
        dashboard_content,
        title="Executive Dashboard - Simple Browser Compatible",
        css=simple_css
    )
    
    print("✅ Simple Browser compatible dashboard created")
    
    # Save the dashboard
    dashboard_file = '/Users/david/htmldictify/html-table-generator/simple_browser_dashboard.html'
    with open(dashboard_file, 'w', encoding='utf-8') as f:
        f.write(complete_dashboard)
    
    print(f"✅ Dashboard saved: {dashboard_file}")
    print(f"📊 Document size: {len(complete_dashboard):,} characters")
    
    return complete_dashboard


def main():
    """Run the Simple Browser compatible demo."""
    dashboard = create_simple_browser_dashboard()
    
    print("\n" + "=" * 60)
    print("🎉 SIMPLE BROWSER COMPATIBLE DASHBOARD COMPLETED!")
    print("=" * 60)
    print("✨ Optimized for VS Code Simple Browser:")
    print("  • No complex CSS gradients or animations")
    print("  • Standard CSS properties for maximum compatibility")
    print("  • Interactive sorting functionality maintained")
    print("  • All responsive features preserved")
    print("  • Clean, professional appearance")
    print()
    print("🌐 Open 'simple_browser_dashboard.html' in VS Code Simple Browser")
    print("🦎 Also works perfectly in Safari, Chrome, and other browsers")


if __name__ == "__main__":
    main()

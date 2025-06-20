#!/usr/bin/env python3
"""
Enhanced Executive Dashboard Demo
This creates a comprehensive executive dashboard with:
1. Interactive sortable tables
2. Statistical summaries
3. Advanced styling and animations
4. Responsive design
5. Professional hover effects
"""

from src.table_generator import TableGenerator
from datetime import datetime


def create_enhanced_dashboard():
    """Create an enhanced executive dashboard with advanced features."""
    print("🚀 Creating Enhanced Executive Dashboard")
    print("=" * 60)
    
    # === Enhanced Data Sources ===
    
    # Quarterly Performance Data
    quarterly_data = [
        ['Quarter', 'Revenue', 'Profit', 'Growth', 'Customers', 'Market Share'],
        ['Q1 2024', '$2.1M', '$420K', '+12%', '1,250', '15.2%'],
        ['Q2 2024', '$2.4M', '$480K', '+14%', '1,380', '16.1%'],
        ['Q3 2024', '$2.8M', '$560K', '+17%', '1,520', '17.8%'],
        ['Q4 2024', '$3.2M', '$640K', '+15%', '1,690', '18.5%'],
        ['Q1 2025', '$3.6M', '$720K', '+13%', '1,840', '19.2%'],
        ['Q2 2025', '$4.1M', '$820K', '+14%', '2,010', '20.1%']
    ]
    
    # Regional Performance
    regional_data = [
        {'Region': 'North America', 'Revenue': '$1.8M', 'Units': '2,450', 'Growth': '+18%', 'Profit': '$360K'},
        {'Region': 'Europe', 'Revenue': '$1.2M', 'Units': '1,680', 'Growth': '+15%', 'Profit': '$240K'},
        {'Region': 'Asia Pacific', 'Revenue': '$900K', 'Units': '1,320', 'Growth': '+22%', 'Profit': '$180K'},
        {'Region': 'Latin America', 'Revenue': '$200K', 'Units': '280', 'Growth': '+8%', 'Profit': '$40K'}
    ]
    
    # Top Products
    product_data = [
        {'Product': 'Enterprise Software', 'Revenue': '$1.5M', 'Units': '850', 'Margin': '42%', 'Rating': '4.8/5'},
        {'Product': 'Cloud Services', 'Revenue': '$1.2M', 'Units': '1,200', 'Margin': '38%', 'Rating': '4.7/5'},
        {'Product': 'Mobile Apps', 'Revenue': '$800K', 'Units': '2,100', 'Margin': '35%', 'Rating': '4.6/5'},
        {'Product': 'Consulting', 'Revenue': '$600K', 'Units': '120', 'Margin': '45%', 'Rating': '4.9/5'}
    ]
    
    # Key Metrics
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
    
    print("✅ Enhanced data sources loaded")
    
    # === Create Enhanced Table Generators ===
    
    # Quarterly performance table
    quarterly_gen = TableGenerator(
        table_class='quarterly-performance',
        striped=True,
        responsive=True,
        sortable=True,
        custom_headers={
            'Revenue': 'Total Revenue',
            'Profit': 'Net Profit',
            'Growth': 'YoY Growth',
            'Customers': 'Total Customers',
            'Market Share': 'Market Share'
        },
        styles={
            'table': 'width: 100%; font-family: "Segoe UI", sans-serif;',
            'th': 'background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 15px; text-align: center;',
            'td': 'padding: 12px; text-align: center; font-weight: 500;'
        }
    )
    
    # Regional performance table
    regional_gen = TableGenerator(
        table_class='regional-performance',
        striped=True,
        sortable=True,
        styles={
            'table': 'width: 100%; font-family: "Segoe UI", sans-serif;',
            'th': 'background: linear-gradient(135deg, #4CAF50, #45a049); color: white; padding: 15px;',
            'td': 'padding: 12px; font-weight: 500;'
        }
    )
    
    # Product performance table
    product_gen = TableGenerator(
        table_class='product-performance',
        striped=True,
        sortable=True,
        custom_headers={
            'Revenue': 'Total Revenue',
            'Units': 'Units Sold',
            'Margin': 'Profit Margin',
            'Rating': 'Customer Rating'
        },
        styles={
            'table': 'width: 100%; font-family: "Segoe UI", sans-serif;',
            'th': 'background: linear-gradient(135deg, #FF6B6B, #FF8E8E); color: white; padding: 15px;',
            'td': 'padding: 12px; font-weight: 500;'
        }
    )
    
    # Key metrics table
    metrics_gen = TableGenerator(
        table_class='key-metrics',
        sortable=True,
        styles={
            'table': 'width: 100%; font-family: "Segoe UI", sans-serif;',
            'th': 'background: linear-gradient(135deg, #9C27B0, #8E24AA); color: white; padding: 15px;',
            'td': 'padding: 15px; font-weight: 600; font-size: 18px; text-align: center;'
        }
    )
    
    # Generate tables
    quarterly_table = quarterly_gen.generate_table(quarterly_data)
    regional_table = regional_gen.generate_table(regional_data)
    product_table = product_gen.generate_table(product_data)
    metrics_table = metrics_gen.generate_table(key_metrics)
    
    print("✅ Enhanced tables generated")
    
    # === Create Collapsible Sections ===
    
    # Key Metrics (always expanded)
    metrics_section = metrics_gen.make_collapsible_with_css(
        metrics_table,
        title="📊 Key Performance Indicators",
        collapsed=False,
        container_class="metrics-section"
    )
    
    # Quarterly Performance (expanded)
    quarterly_section = quarterly_gen.make_collapsible_with_css(
        quarterly_table,
        title="📈 Quarterly Performance Trends",
        collapsed=False,
        container_class="quarterly-section"
    )
    
    # Regional Performance (collapsed)
    regional_section = regional_gen.make_collapsible_with_css(
        regional_table,
        title="🌍 Regional Performance Breakdown",
        collapsed=True,
        container_class="regional-section"
    )
    
    # Product Performance (collapsed)
    product_section = product_gen.make_collapsible_with_css(
        product_table,
        title="🛍️ Top Product Performance",
        collapsed=True,
        container_class="product-section"
    )
    
    print("✅ Collapsible sections created")
    
    # === Enhanced Dashboard CSS ===
    enhanced_css = """
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    .dashboard-container {
        max-width: 1600px;
        margin: 0 auto;
        background: white;
        border-radius: 20px;
        padding: 50px;
        box-shadow: 0 25px 80px rgba(0,0,0,0.2);
        position: relative;
        overflow: hidden;
    }
    
    .dashboard-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 6px;
        background: linear-gradient(90deg, #667eea, #4CAF50, #FF6B6B, #9C27B0, #FF9800);
        animation: gradientShift 3s ease-in-out infinite;
    }
    
    @keyframes gradientShift {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    .dashboard-header {
        text-align: center;
        margin-bottom: 50px;
        padding: 30px;
        background: linear-gradient(135deg, #f8f9fa, #e9ecef);
        border-radius: 16px;
        border-left: 6px solid #667eea;
        position: relative;
    }
    
    .dashboard-title {
        font-size: 3.5em;
        font-weight: 300;
        color: #2c3e50;
        margin-bottom: 15px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        letter-spacing: -1px;
    }
    
    .dashboard-subtitle {
        color: #6c757d;
        font-size: 1.4em;
        margin-bottom: 20px;
        font-weight: 400;
    }
    
    .dashboard-timestamp {
        color: #7f8c8d;
        font-size: 1.1em;
        font-style: italic;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 25px;
        margin: 40px 0;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #ffffff, #f8f9fa);
        border-radius: 16px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        border-left: 5px solid #667eea;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .stat-card:hover::before {
        opacity: 1;
    }
    
    .stat-card:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 40px rgba(0,0,0,0.2);
    }
    
    .stat-number {
        font-size: 2.8em;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 8px;
        position: relative;
        z-index: 1;
    }
    
    .stat-label {
        color: #6c757d;
        font-size: 0.95em;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 500;
        position: relative;
        z-index: 1;
    }
    
    .dashboard-section {
        margin-bottom: 40px;
        position: relative;
    }
    
    .section-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 20px;
        padding: 0 10px;
    }
    
    .section-title {
        font-size: 1.6em;
        color: #2c3e50;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .sort-help {
        font-size: 0.9em;
        color: #6c757d;
        font-style: italic;
        display: flex;
        align-items: center;
        gap: 8px;
        background: rgba(108, 117, 125, 0.1);
        padding: 8px 12px;
        border-radius: 8px;
    }
    
    /* Enhanced sortable styling */
    .sortable th[data-sortable] {
        position: relative;
        cursor: pointer;
        user-select: none;
        transition: all 0.3s ease;
    }
    
    .sortable th[data-sortable]:hover {
        filter: brightness(1.15);
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    .sortable th[data-sortable]:active {
        transform: translateY(-1px);
    }
    
    .sort-indicator {
        font-size: 0.85em;
        margin-left: 10px;
        transition: all 0.2s ease;
    }
    
    .sortable th.sort-asc .sort-indicator::after {
        content: ' ↑';
        color: #fff;
        font-weight: bold;
        opacity: 1;
        animation: sortBounce 0.4s ease;
    }
    
    .sortable th.sort-desc .sort-indicator::after {
        content: ' ↓';
        color: #fff;
        font-weight: bold;
        opacity: 1;
        animation: sortBounce 0.4s ease;
    }
    
    @keyframes sortBounce {
        0% { transform: scale(1); }
        50% { transform: scale(1.3); }
        100% { transform: scale(1); }
    }
    
    /* Table hover effects */
    .sortable tbody tr {
        transition: all 0.2s ease;
    }
    
    .sortable tbody tr:hover {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1)) !important;
        transform: scale(1.01);
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* Footer styling */
    .dashboard-footer {
        text-align: center;
        margin-top: 60px;
        padding-top: 30px;
        border-top: 3px solid #e9ecef;
        color: #7f8c8d;
        font-size: 1.1em;
    }
    
    .footer-info {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 30px;
        flex-wrap: wrap;
        margin-top: 15px;
    }
    
    .footer-item {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 8px 16px;
        background: rgba(108, 117, 125, 0.1);
        border-radius: 20px;
        font-size: 0.9em;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .dashboard-container {
            margin: 10px;
            padding: 25px;
            border-radius: 16px;
        }
        
        .dashboard-title {
            font-size: 2.5em;
        }
        
        .stats-grid {
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 20px;
        }
        
        .stat-number {
            font-size: 2.2em;
        }
        
        .section-header {
            flex-direction: column;
            align-items: flex-start;
            gap: 15px;
        }
        
        .footer-info {
            flex-direction: column;
            gap: 15px;
        }
    }
    """
    
    # === Build Complete Dashboard ===
    current_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    
    dashboard_content = f"""
    <div class="dashboard-container">
        <div class="dashboard-header">
            <h1 class="dashboard-title">🏢 Executive Dashboard</h1>
            <p class="dashboard-subtitle">Comprehensive Business Intelligence & Analytics</p>
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
                <div class="sort-help">💡 Click column headers to sort data</div>
            </div>
            {metrics_section}
        </div>
        
        <div class="dashboard-section">
            <div class="section-header">
                <div class="section-title">Quarterly Performance Analysis</div>
                <div class="sort-help">📈 Track revenue growth trends</div>
            </div>
            {quarterly_section}
        </div>
        
        <div class="dashboard-section">
            <div class="section-header">
                <div class="section-title">Regional Market Performance</div>
                <div class="sort-help">🌍 Compare regional results</div>
            </div>
            {regional_section}
        </div>
        
        <div class="dashboard-section">
            <div class="section-header">
                <div class="section-title">Top Product Categories</div>
                <div class="sort-help">🛍️ Analyze product performance</div>
            </div>
            {product_section}
        </div>
        
        <div class="dashboard-footer">
            <div>✨ Powered by HTML Table Generator v2.0 - Interactive Business Intelligence</div>
            <div class="footer-info">
                <div class="footer-item">📊 4 Data Sources</div>
                <div class="footer-item">🔄 Real-time Sorting</div>
                <div class="footer-item">📱 Mobile Responsive</div>
                <div class="footer-item">🎨 Professional Design</div>
            </div>
        </div>
    </div>
    """
    
    # Create complete HTML document
    complete_dashboard = quarterly_gen.render_html(
        dashboard_content,
        title="Enhanced Executive Dashboard - Business Intelligence Portal",
        css=enhanced_css
    )
    
    print("✅ Enhanced dashboard assembled")
    
    # Save the enhanced dashboard
    dashboard_file = '/Users/david/htmldictify/html-table-generator/enhanced_executive_dashboard.html'
    with open(dashboard_file, 'w', encoding='utf-8') as f:
        f.write(complete_dashboard)
    
    print(f"✅ Enhanced dashboard saved: {dashboard_file}")
    print(f"📊 Document size: {len(complete_dashboard):,} characters")
    
    return complete_dashboard


def main():
    """Run the enhanced dashboard demo."""
    dashboard = create_enhanced_dashboard()
    
    print("\n" + "=" * 60)
    print("🎉 ENHANCED EXECUTIVE DASHBOARD COMPLETED!")
    print("=" * 60)
    print("✨ Features included:")
    print("  • Interactive sortable tables with animations")
    print("  • Statistical summary cards with hover effects")
    print("  • Collapsible sections for better organization")
    print("  • Professional gradient styling")
    print("  • Mobile-responsive design")
    print("  • Real-time data visualization")
    print("  • Advanced CSS animations and transitions")
    print()
    print("🌐 Open 'enhanced_executive_dashboard.html' to explore!")
    print("📱 Try resizing your browser to see responsive design")
    print("🖱️ Click on column headers to sort data")


if __name__ == "__main__":
    main()

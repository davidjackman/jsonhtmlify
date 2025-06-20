#!/usr/bin/env python3
"""
Sortable Tables Demo: Interactive Column Sorting
This demonstrates the new sortable table functionality where users can
click on column headers to sort the data.
"""

from src.table_generator import TableGenerator


def demo_sortable_tables():
    """Demonstrate sortable table functionality with different data types."""
    print("🚀 Sortable Tables Demo")
    print("=" * 50)
    
    # Sample data with different data types for sorting
    employee_data = [
        {'ID': 'EMP001', 'Name': 'Sarah Johnson', 'Department': 'Engineering', 'Salary': 125000, 'Start Date': '2020-03-15', 'Performance': 'Excellent'},
        {'ID': 'EMP002', 'Name': 'Mike Chen', 'Department': 'Product', 'Salary': 135000, 'Start Date': '2019-07-22', 'Performance': 'Outstanding'},
        {'ID': 'EMP003', 'Name': 'Lisa Rodriguez', 'Department': 'Design', 'Salary': 115000, 'Start Date': '2021-01-10', 'Performance': 'Excellent'},
        {'ID': 'EMP004', 'Name': 'David Kim', 'Department': 'Engineering', 'Salary': 145000, 'Start Date': '2018-09-05', 'Performance': 'Outstanding'},
        {'ID': 'EMP005', 'Name': 'Anna Petrov', 'Department': 'Marketing', 'Salary': 98000, 'Start Date': '2022-04-18', 'Performance': 'Good'},
        {'ID': 'EMP006', 'Name': 'James Wilson', 'Department': 'Sales', 'Salary': 110000, 'Start Date': '2021-11-30', 'Performance': 'Excellent'},
        {'ID': 'EMP007', 'Name': 'Maria Garcia', 'Department': 'HR', 'Salary': 95000, 'Start Date': '2020-08-12', 'Performance': 'Good'},
        {'ID': 'EMP008', 'Name': 'Robert Taylor', 'Department': 'Finance', 'Salary': 120000, 'Start Date': '2019-12-03', 'Performance': 'Outstanding'}
    ]
    
    # Create sortable table
    generator = TableGenerator(
        table_class='employee-table',
        sortable=True,  # Enable sorting!
        striped=True,
        responsive=True,
        custom_headers={
            'ID': 'Employee ID',
            'Name': 'Full Name',
            'Salary': 'Annual Salary ($)',
            'Start Date': 'Start Date',
            'Performance': 'Rating'
        },
        styles={
            'table': 'width: 100%; font-family: "Segoe UI", sans-serif; margin-bottom: 20px;',
            'th': 'background: linear-gradient(135deg, #2196F3, #1976D2); color: white; padding: 15px; text-align: left; font-weight: 600;',
            'td': 'padding: 12px 15px; border-bottom: 1px solid #e3f2fd;'
        }
    )
    
    table_html = generator.generate_table(employee_data)
    
    # Create complete HTML document with instructions
    custom_css = """
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 20px;
        padding: 20px;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        min-height: 100vh;
    }
    
    .container {
        max-width: 1200px;
        margin: 0 auto;
        background: white;
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    h1 {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 30px;
        font-size: 2.5em;
        font-weight: 300;
    }
    
    .instructions {
        background: #e8f4f8;
        border-left: 4px solid #2196F3;
        padding: 20px;
        margin-bottom: 30px;
        border-radius: 0 8px 8px 0;
    }
    
    .instructions h2 {
        color: #1976D2;
        margin-top: 0;
        font-size: 1.3em;
    }
    
    .instructions ul {
        margin: 10px 0;
        padding-left: 20px;
    }
    
    .instructions li {
        margin: 8px 0;
        color: #34495e;
    }
    
    .demo-info {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 15px;
        margin-top: 30px;
    }
    
    .demo-info h3 {
        color: #495057;
        margin-top: 0;
        font-size: 1.1em;
    }
    
    .demo-info p {
        color: #6c757d;
        margin: 5px 0;
    }
    
    /* Enhanced sortable styling */
    .employee-table.sortable th[data-sortable] {
        position: relative;
        cursor: pointer;
        user-select: none;
        transition: all 0.2s ease;
    }
    
    .employee-table.sortable th[data-sortable]:hover {
        background: linear-gradient(135deg, #1976D2, #1565C0) !important;
        transform: translateY(-1px);
    }
    """
    
    complete_content = f"""
    <div class="container">
        <h1>🔄 Interactive Sortable Tables Demo</h1>
        
        <div class="instructions">
            <h2>📋 How to Use Sortable Tables</h2>
            <ul>
                <li><strong>Click any column header</strong> to sort the table by that column</li>
                <li><strong>Click again</strong> to reverse the sort order (ascending ↔ descending)</li>
                <li><strong>Look for the arrows</strong>: ↕️ (sortable), ↑ (ascending), ↓ (descending)</li>
                <li><strong>Different data types</strong> are handled automatically:
                    <ul>
                        <li>🔢 Numbers (Salary): Sorted numerically</li>
                        <li>📅 Dates (Start Date): Sorted chronologically</li>
                        <li>📝 Text (Name, Department): Sorted alphabetically</li>
                    </ul>
                </li>
            </ul>
        </div>
        
        {table_html}
        
        <div class="demo-info">
            <h3>🎯 Data Types in This Demo</h3>
            <p><strong>Text Columns:</strong> Employee ID, Full Name, Department, Rating</p>
            <p><strong>Number Column:</strong> Annual Salary (automatically handles $ and commas)</p>
            <p><strong>Date Column:</strong> Start Date (automatically recognizes date format)</p>
            <p><strong>Try clicking different headers to see how each data type sorts!</strong></p>
        </div>
    </div>
    """
    
    complete_html = generator.render_html(
        complete_content,
        title="Sortable Tables Demo - Interactive Column Sorting",
        css=custom_css
    )
    
    # Save to file
    output_file = '/Users/david/htmldictify/html-table-generator/sortable_demo.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(complete_html)
    
    print(f"✅ Sortable table demo created!")
    print(f"📁 File saved as: {output_file}")
    print(f"📊 Document size: {len(complete_html):,} characters")
    print(f"🌐 Open the file in your browser to test sorting functionality")
    print()
    print("🎯 Features Demonstrated:")
    print("  • Click-to-sort column headers")
    print("  • Automatic data type detection (text, numbers, dates)")
    print("  • Visual sort indicators (arrows)")
    print("  • Hover effects on sortable headers")
    print("  • Professional styling with animations")
    
    return complete_html


def main():
    """Run the sortable tables demonstration."""
    demo_sortable_tables()
    
    print("\n" + "=" * 50)
    print("🎉 SORTABLE TABLES DEMO COMPLETE!")
    print("=" * 50)
    print("✅ Interactive sorting functionality added to HTML Table Generator")
    print("🌐 Open 'sortable_demo.html' in your browser to test it out")
    print("📊 Click any column header to sort the data")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Demonstration of CSV-like data format support in HTML Table Generator.
This shows how the generator can handle different data formats including:
1. Traditional list of dictionaries
2. CSV-like data (list of lists with headers)
3. Mixed data types in CSV format
"""

from src.table_generator import TableGenerator


def demo_traditional_vs_csv():
    """Compare traditional dictionary format vs CSV-like format."""
    print("=== Traditional vs CSV Format Comparison ===")
    
    # Traditional format: list of dictionaries
    traditional_data = [
        {'Name': 'Alice', 'Age': 30, 'Department': 'Engineering'},
        {'Name': 'Bob', 'Age': 25, 'Department': 'Marketing'},
        {'Name': 'Carol', 'Age': 35, 'Department': 'Sales'}
    ]
    
    # CSV-like format: list of lists with header row
    csv_data = [
        ['Name', 'Age', 'Department'],  # Header row
        ['Alice', 30, 'Engineering'],
        ['Bob', 25, 'Marketing'],
        ['Carol', 35, 'Sales']
    ]
    
    generator = TableGenerator(table_class='comparison-table', striped=True)
    
    print("Traditional format (list of dictionaries):")
    traditional_result = generator.generate_table(traditional_data)
    print(traditional_result)
    print()
    
    print("CSV-like format (list of lists):")
    csv_result = generator.generate_table(csv_data)
    print(csv_result)
    print()


def demo_csv_from_file_simulation():
    """Simulate processing data that might come from a CSV file."""
    print("=== CSV File Processing Simulation ===")
    
    # Simulate reading from a CSV file
    csv_rows = [
        ['Product ID', 'Product Name', 'Category', 'Price', 'Stock', 'Rating'],
        ['P001', 'Wireless Mouse', 'Electronics', 29.99, 150, 4.5],
        ['P002', 'Mechanical Keyboard', 'Electronics', 89.99, 75, 4.8],
        ['P003', 'USB-C Cable', 'Accessories', 12.99, 200, 4.2],
        ['P004', 'Laptop Stand', 'Accessories', 45.50, 50, 4.6],
        ['P005', 'Webcam HD', 'Electronics', 79.99, 30, 4.3]
    ]
    
    # Custom styling for product catalog
    styles = {
        'table': 'border-collapse: collapse; width: 100%; font-family: Arial, sans-serif;',
        'th': 'background-color: #2196F3; color: white; padding: 12px; text-align: left; border: 1px solid #ddd;',
        'td': 'padding: 10px; border: 1px solid #ddd; text-align: left;'
    }
    
    generator = TableGenerator(
        table_class='product-catalog',
        table_id='inventory-table',
        striped=True,
        responsive=True,
        styles=styles
    )
    
    result = generator.generate_table(csv_rows)
    print("Product catalog from CSV-like data:")
    print(result)
    print()


def demo_spreadsheet_export():
    """Simulate data exported from a spreadsheet application."""
    print("=== Spreadsheet Export Simulation ===")
    
    # Data as tuples (common in spreadsheet exports)
    spreadsheet_data = [
        ('Employee ID', 'Full Name', 'Email', 'Hire Date', 'Salary', 'Active'),
        ('EMP001', 'John Smith', 'john.smith@company.com', '2022-01-15', 75000.00, True),
        ('EMP002', 'Jane Doe', 'jane.doe@company.com', '2021-03-22', 82000.00, True),
        ('EMP003', 'Mike Johnson', 'mike.j@company.com', '2023-07-10', 68000.00, False),
        ('EMP004', 'Sarah Wilson', 'sarah.w@company.com', '2020-11-05', 95000.00, True)
    ]
    
    # Custom headers for better display
    custom_headers = {
        'Employee ID': 'ID',
        'Full Name': 'Name',
        'Hire Date': 'Started',
        'Salary': 'Annual Salary'
    }
    
    generator = TableGenerator(
        table_class='employee-directory',
        custom_headers=custom_headers,
        sortable=True,
        striped=True
    )
    
    result = generator.generate_table(spreadsheet_data)
    print("Employee directory from spreadsheet export:")
    print(result)
    print()


def demo_mixed_data_types():
    """Show handling of mixed data types in CSV format."""
    print("=== Mixed Data Types in CSV Format ===")
    
    # CSV data with various data types
    mixed_csv = [
        ['ID', 'Name', 'Score', 'Passed', 'Notes', 'Date'],
        [1, 'Alice Johnson', 95.5, True, 'Excellent work', '2025-06-15'],
        [2, 'Bob Smith', 87.2, True, None, '2025-06-14'],  # None value
        [3, 'Carol Wilson', 65.8, False, 'Needs improvement', '2025-06-13'],
        [4, 'David Brown', None, None, 'Absent', None]  # Multiple None values
    ]
    
    generator = TableGenerator(
        table_class='student-grades',
        responsive=True
    )
    
    result = generator.generate_table(mixed_csv)
    print("Student grades with mixed data types:")
    print(result)
    print()


def demo_uneven_csv_rows():
    """Show handling of CSV data with uneven row lengths."""
    print("=== Uneven CSV Rows Handling ===")
    
    # CSV data where rows have different lengths
    uneven_csv = [
        ['Name', 'Primary Skill', 'Secondary Skill', 'Years Experience', 'Certification'],
        ['Alice', 'Python', 'JavaScript', 5],  # Missing certification
        ['Bob', 'Java', 'Spring Boot', 3, 'Oracle Certified'],
        ['Carol', 'React'],  # Missing multiple fields
        ['David', 'Node.js', 'Express', 4, 'AWS Certified', 'Extra field']  # Extra field
    ]
    
    generator = TableGenerator(table_class='skills-matrix')
    result = generator.generate_table(uneven_csv)
    
    print("Skills matrix with uneven rows:")
    print(result)
    print()


def demo_complete_html_with_csv():
    """Generate complete HTML document from CSV data."""
    print("=== Complete HTML Document from CSV Data ===")
    
    sales_data = [
        ['Quarter', 'Product Category', 'Revenue', 'Units Sold', 'Growth %'],
        ['Q1 2025', 'Electronics', 125000, 450, '+12%'],
        ['Q1 2025', 'Accessories', 45000, 890, '+8%'],
        ['Q1 2025', 'Software', 78000, 234, '+15%'],
    ]
    
    # Custom CSS for the report
    css = """
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 40px;
        background-color: #f8f9fa;
    }
    
    h1 {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 30px;
    }
    
    .sales-report {
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        overflow: hidden;
        margin: 0 auto;
        max-width: 800px;
    }
    
    .sales-report th {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        text-align: left;
        font-weight: 600;
    }
    
    .sales-report td {
        padding: 12px 15px;
        border-bottom: 1px solid #e9ecef;
    }
    
    .sales-report.striped tr:nth-child(even) {
        background-color: #f8f9fa;
    }
    
    .footer {
        text-align: center;
        margin-top: 20px;
        color: #6c757d;
        font-size: 14px;
    }
    """
    
    generator = TableGenerator(
        table_class='sales-report',
        striped=True,
        responsive=True
    )
    
    table_html = generator.generate_table(sales_data)
    
    # Add a header and footer to the table
    enhanced_html = f"""
    <h1>Q1 2025 Sales Report</h1>
    {table_html}
    <div class="footer">
        Generated on {__import__('datetime').datetime.now().strftime('%B %d, %Y')}
    </div>
    """
    
    complete_html = generator.render_html(
        enhanced_html,
        title="Sales Report Dashboard",
        css=css
    )
    
    print("Complete HTML document generated!")
    print("First 500 characters:")
    print(complete_html[:500] + "...")
    print()
    
    return complete_html


def main():
    """Run all demonstrations."""
    print("HTML Table Generator - CSV Format Support Demonstration")
    print("=" * 60)
    print()
    
    demo_traditional_vs_csv()
    demo_csv_from_file_simulation()
    demo_spreadsheet_export()
    demo_mixed_data_types()
    demo_uneven_csv_rows()
    complete_html = demo_complete_html_with_csv()
    
    # Save the complete HTML example
    with open('/Users/david/htmldictify/html-table-generator/sales_report_demo.html', 'w', encoding='utf-8') as f:
        f.write(complete_html)
    
    print("✅ Complete HTML demo saved as 'sales_report_demo.html'")
    print()
    print("Summary of supported data formats:")
    print("1. Dictionary: {'key': 'value', ...}")
    print("2. List of dictionaries: [{'key': 'value'}, ...]")
    print("3. CSV-like lists: [['header1', 'header2'], ['data1', 'data2'], ...]")
    print("4. CSV-like tuples: [('header1', 'header2'), ('data1', 'data2'), ...]")
    print("5. Mixed formats with proper error handling")


if __name__ == "__main__":
    main()

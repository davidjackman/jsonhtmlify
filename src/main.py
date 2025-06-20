from table_generator import TableGenerator


def demo_basic_usage():
    """Demonstrate basic usage with a single dictionary."""
    print("=== Basic Usage Demo ===")
    data = {
        "Name": "John Doe",
        "Age": 30,
        "Department": "Engineering",
        "Salary": 75000
    }

    generator = TableGenerator()
    html_table = generator.generate_table(data)
    print("Basic table HTML:")
    print(html_table)
    print()


def demo_multiple_records():
    """Demonstrate usage with multiple records."""
    print("=== Multiple Records Demo ===")
    employees = [
        {"Name": "Alice Johnson", "Department": "HR", "Salary": 65000, "Years": 3},
        {"Name": "Bob Smith", "Department": "Engineering", "Salary": 85000, "Years": 5},
        {"Name": "Carol Williams", "Department": "Marketing", "Salary": 70000, "Years": 2},
        {"Name": "David Brown", "Department": "Engineering", "Salary": 95000, "Years": 7}
    ]

    generator = TableGenerator(
        table_class="employee-table",
        striped=True,
        responsive=True
    )
    html_table = generator.generate_table(employees)
    print("Employee table HTML:")
    print(html_table)
    print()


def demo_custom_styling():
    """Demonstrate custom styling options."""
    print("=== Custom Styling Demo ===")
    sales_data = [
        {"Product": "Laptop", "Units": 15, "Revenue": 22500.00, "Margin": "15%"},
        {"Product": "Mouse", "Units": 150, "Revenue": 4500.00, "Margin": "45%"},
        {"Product": "Keyboard", "Units": 75, "Revenue": 7500.00, "Margin": "30%"}
    ]

    # Custom styles
    styles = {
        'table': 'border-collapse: collapse; width: 100%; font-family: Arial, sans-serif;',
        'th': 'background-color: #4CAF50; color: white; padding: 12px; text-align: left;',
        'td': 'padding: 12px; border-bottom: 1px solid #ddd;'
    }

    # Custom headers
    custom_headers = {
        'Product': 'Product Name',
        'Units': 'Units Sold',
        'Revenue': 'Revenue ($)',
        'Margin': 'Profit Margin'
    }

    generator = TableGenerator(
        table_id="sales-report",
        custom_headers=custom_headers,
        styles=styles,
        sortable=True
    )

    html_table = generator.generate_table(sales_data)
    print("Styled sales table HTML:")
    print(html_table)
    print()


def demo_complete_html():
    """Demonstrate generating a complete HTML document."""
    print("=== Complete HTML Document Demo ===")
    project_data = [
        {"Task": "Design UI", "Status": "Complete", "Priority": "High", "Assignee": "Alice"},
        {"Task": "Backend API", "Status": "In Progress", "Priority": "High", "Assignee": "Bob"},
        {"Task": "Testing", "Status": "Pending", "Priority": "Medium", "Assignee": "Carol"},
        {"Task": "Documentation", "Status": "Not Started", "Priority": "Low", "Assignee": "David"}
    ]

    generator = TableGenerator(
        table_class="project-table",
        striped=True,
        responsive=True
    )

    table_html = generator.generate_table(project_data)

    # Custom CSS for the complete document
    css = """
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 40px;
        background-color: #f5f5f5;
    }
    
    .project-table {
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        overflow: hidden;
    }
    
    .project-table th {
        background-color: #2196F3;
        color: white;
        padding: 15px;
        text-align: left;
        font-weight: 600;
    }
    
    .project-table td {
        padding: 12px 15px;
        border-bottom: 1px solid #eee;
    }
    
    .project-table.striped tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    
    h1 {
        color: #333;
        margin-bottom: 20px;
    }
    """

    complete_html = generator.render_html(
        table_html,
        title="Project Management Dashboard",
        css=css
    )

    print("Complete HTML document:")
    print(complete_html)
    print()


def demo_special_cases():
    """Demonstrate handling of special cases."""
    print("=== Special Cases Demo ===")
    
    # Data with special characters and mixed types
    special_data = [
        {"Name": "José María", "Company": "Café & Co.", "Active": True, "Score": None},
        {"Name": "François", "Company": "<B>Bold Corp</B>", "Active": False, "Score": 95.5},
        {"Name": "李小明", "Company": "Tech 公司", "Active": True, "Score": 88}
    ]

    generator = TableGenerator(
        table_class="special-chars-table",
        custom_attributes={"data-test": "special-characters"}
    )

    html_table = generator.generate_table(special_data)
    print("Table with special characters:")
    print(html_table)
    print()


def demo_collapsible_tables():
    """Demonstrate collapsible table functionality."""
    print("=== Collapsible Tables Demo ===")
    
    # Large dataset that benefits from being collapsible
    large_data = [
        {"ID": i, "Name": f"Employee {i}", "Department": f"Dept {i % 5}", 
         "Salary": 50000 + (i * 1000), "Status": "Active" if i % 2 == 0 else "Inactive"}
        for i in range(20)
    ]
    
    generator = TableGenerator(
        table_class="employee-list",
        striped=True,
        responsive=True
    )
    
    # Generate the table
    table_html = generator.generate_table(large_data)
    
    # Make it collapsible - starts expanded
    collapsible_table = generator.make_collapsible(
        table_html, 
        title="Employee Directory (20 records)",
        collapsed=False
    )
    
    print("Collapsible table (basic):")
    print(collapsible_table[:300] + "...")
    print()
    
    # Make it collapsible with built-in styling - starts collapsed
    styled_collapsible = generator.make_collapsible_with_css(
        table_html,
        title="Styled Employee Directory",
        collapsed=True
    )
    
    print("Collapsible table with CSS styling:")
    print("(First 400 characters)")
    print(styled_collapsible[:400] + "...")
    print()


def demo_multiple_collapsible_tables():
    """Demonstrate multiple collapsible tables in one document."""
    print("=== Multiple Collapsible Tables Demo ===")
    
    # Different datasets
    sales_q1 = [
        {"Product": "Laptop", "Q1_Sales": 150, "Revenue": 225000},
        {"Product": "Mouse", "Q1_Sales": 300, "Revenue": 15000},
        {"Product": "Keyboard", "Q1_Sales": 200, "Revenue": 30000}
    ]
    
    sales_q2 = [
        {"Product": "Laptop", "Q2_Sales": 180, "Revenue": 270000},
        {"Product": "Mouse", "Q2_Sales": 350, "Revenue": 17500},
        {"Product": "Keyboard", "Q2_Sales": 250, "Revenue": 37500}
    ]
    
    generator = TableGenerator(
        table_class="sales-table",
        striped=True,
        custom_headers={"Q1_Sales": "Q1 Units", "Q2_Sales": "Q2 Units"}
    )
    
    # Generate tables
    q1_table = generator.generate_table(sales_q1)
    q2_table = generator.generate_table(sales_q2)
    
    # Make them collapsible
    q1_collapsible = generator.make_collapsible_with_css(
        q1_table,
        title="Q1 2025 Sales Report",
        collapsed=False,
        container_class="sales-report-q1"
    )
    
    q2_collapsible = generator.make_collapsible_with_css(
        q2_table,
        title="Q2 2025 Sales Report", 
        collapsed=True,
        container_class="sales-report-q2"
    )
    
    # Combine into a complete document
    complete_doc = generator.render_html(
        q1_collapsible + "\n\n" + q2_collapsible,
        title="Sales Dashboard - Collapsible Reports",
        css="body { font-family: Arial, sans-serif; margin: 20px; background-color: #f8f9fa; }"
    )
    
    print("Complete document with multiple collapsible tables generated!")
    print(f"Document length: {len(complete_doc)} characters")
    print()
    
    return complete_doc


def main():
    """Run all demonstrations."""
    print("HTML Table Generator - Feature Demonstrations")
    print("=" * 50)
    print()

    demo_basic_usage()
    demo_multiple_records()
    demo_custom_styling()
    demo_complete_html()
    demo_special_cases()
    demo_collapsible_tables()
    
    # Generate and save the multiple collapsible tables demo
    collapsible_doc = demo_multiple_collapsible_tables()
    
    # Save the collapsible demo to a file
    with open('/Users/david/htmldictify/html-table-generator/collapsible_demo.html', 'w', encoding='utf-8') as f:
        f.write(collapsible_doc)
    
    print("✅ Collapsible tables demo saved as 'collapsible_demo.html'")
    print("All demonstrations completed!")


if __name__ == "__main__":
    main()
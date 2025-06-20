"""
Example usage tests for the HTML Table Generator.
These tests serve as documentation and ensure common use cases work correctly.
"""

import unittest
from src.table_generator import TableGenerator


class TestExamples(unittest.TestCase):
    """Test common usage examples."""

    def test_basic_usage_single_dict(self):
        """Example: Basic usage with a single dictionary"""
        # Create a simple person record
        person = {
            'Name': 'John Doe',
            'Age': 30,
            'Email': 'john@example.com',
            'Department': 'Engineering'
        }
        
        generator = TableGenerator()
        result = generator.generate_table(person)
        
        # Verify basic structure
        self.assertIn('<table>', result)
        self.assertIn('<thead>', result)
        self.assertIn('<tbody>', result)
        self.assertIn('John Doe', result)

    def test_employee_directory_example(self):
        """Example: Employee directory with multiple records"""
        employees = [
            {'Name': 'Alice Johnson', 'Department': 'HR', 'Salary': 75000, 'Start Date': '2020-01-15'},
            {'Name': 'Bob Smith', 'Department': 'Engineering', 'Salary': 95000, 'Start Date': '2019-03-22'},
            {'Name': 'Carol Williams', 'Department': 'Marketing', 'Salary': 68000, 'Start Date': '2021-07-10'},
            {'Name': 'David Brown', 'Department': 'Engineering', 'Salary': 102000, 'Start Date': '2018-11-05'}
        ]
        
        generator = TableGenerator(
            table_class='employee-table',
            striped=True
        )
        result = generator.generate_table(employees)
        
        # Should contain all employees
        for emp in employees:
            self.assertIn(emp['Name'], result)
        
        # Should have striped styling
        self.assertIn('striped', result)

    def test_sales_report_example(self):
        """Example: Sales report with custom headers and formatting"""
        sales_data = [
            {'product_id': 'P001', 'product_name': 'Laptop', 'units_sold': 15, 'revenue': 22500.00},
            {'product_id': 'P002', 'product_name': 'Mouse', 'units_sold': 150, 'revenue': 4500.00},
            {'product_id': 'P003', 'product_name': 'Keyboard', 'units_sold': 75, 'revenue': 7500.00}
        ]
        
        # Custom headers for better display
        custom_headers = {
            'product_id': 'Product ID',
            'product_name': 'Product Name',
            'units_sold': 'Units Sold',
            'revenue': 'Revenue ($)'
        }
        
        generator = TableGenerator(
            custom_headers=custom_headers,
            table_class='sales-report',
            table_id='monthly-sales'
        )
        result = generator.generate_table(sales_data)
        
        # Should use custom headers
        self.assertIn('Product ID', result)
        self.assertIn('Revenue ($)', result)
        self.assertIn('id="monthly-sales"', result)

    def test_responsive_table_example(self):
        """Example: Responsive table for mobile compatibility"""
        mobile_data = [
            {'Device': 'iPhone 14', 'OS': 'iOS 16', 'Screen': '6.1"', 'Price': '$799'},
            {'Device': 'Samsung Galaxy S23', 'OS': 'Android 13', 'Screen': '6.1"', 'Price': '$899'},
            {'Device': 'Google Pixel 7', 'OS': 'Android 13', 'Screen': '6.3"', 'Price': '$599'}
        ]
        
        generator = TableGenerator(
            responsive=True,
            table_class='device-comparison'
        )
        result = generator.generate_table(mobile_data)
        
        self.assertIn('responsive', result)
        self.assertIn('device-comparison', result)

    def test_styled_table_example(self):
        """Example: Table with custom CSS styles"""
        data = [
            {'Task': 'Design UI', 'Status': 'Complete', 'Priority': 'High'},
            {'Task': 'Write Tests', 'Status': 'In Progress', 'Priority': 'Medium'},
            {'Task': 'Deploy', 'Status': 'Pending', 'Priority': 'Low'}
        ]
        
        styles = {
            'table': 'border-collapse: collapse; width: 100%; font-family: Arial, sans-serif;',
            'th': 'background-color: #4CAF50; color: white; padding: 12px; text-align: left;',
            'td': 'padding: 12px; border-bottom: 1px solid #ddd;'
        }
        
        generator = TableGenerator(styles=styles)
        result = generator.generate_table(data)
        
        self.assertIn('border-collapse: collapse', result)
        self.assertIn('background-color: #4CAF50', result)

    def test_complete_html_document_example(self):
        """Example: Generate complete HTML document"""
        data = {'Title': 'Sample Report', 'Date': '2025-06-19', 'Status': 'Published'}
        
        generator = TableGenerator()
        table_html = generator.generate_table(data)
        
        # Create complete HTML with custom CSS
        css = """
        body { font-family: Arial, sans-serif; margin: 40px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        """
        
        complete_html = generator.render_html(
            table_html, 
            title="Sample Report Dashboard", 
            css=css
        )
        
        self.assertIn('<!DOCTYPE html>', complete_html)
        self.assertIn('Sample Report Dashboard', complete_html)
        self.assertIn('font-family: Arial', complete_html)

    def test_data_with_special_characters_example(self):
        """Example: Handling data with special characters"""
        data = [
            {'Name': 'José María', 'Company': 'Café & Co.', 'Email': 'jose@café.com'},
            {'Name': 'François', 'Company': '<Script>Alert</Script>', 'Email': 'françois@test.com'},
            {'Name': '李小明', 'Company': 'Tech 公司', 'Email': 'ming@tech.cn'}
        ]
        
        generator = TableGenerator()
        result = generator.generate_table(data)
        
        # Should handle Unicode properly
        self.assertIn('José María', result)
        self.assertIn('François', result)
        self.assertIn('李小明', result)
        
        # Should escape HTML
        self.assertIn('&lt;Script&gt;', result)
        self.assertNotIn('<Script>', result)

    def test_large_dataset_example(self):
        """Example: Performance with larger datasets"""
        # Generate sample data
        large_dataset = []
        for i in range(100):
            large_dataset.append({
                'ID': f'USER_{i:03d}',
                'Name': f'User {i}',
                'Email': f'user{i}@example.com',
                'Score': i * 10 + (i % 7),
                'Active': i % 3 == 0
            })
        
        generator = TableGenerator(striped=True, table_class='large-table')
        result = generator.generate_table(large_dataset)
        
        # Should handle large datasets
        self.assertIn('<table', result)
        # Count all TR tags (including those with classes)
        import re
        tr_count = len(re.findall(r'<tr(?:[^>]*)?>', result))
        self.assertEqual(tr_count, 101)  # 1 header + 100 data rows
        self.assertIn('USER_099', result)  # Last user should be present

    def test_mixed_data_types_example(self):
        """Example: Table with mixed data types"""
        mixed_data = [
            {'ID': 1, 'Name': 'Product A', 'Price': 29.99, 'In Stock': True, 'Category': None},
            {'ID': 2, 'Name': 'Product B', 'Price': 0, 'In Stock': False, 'Category': 'Electronics'},
            {'ID': 3, 'Name': 'Product C', 'Price': 199.50, 'In Stock': True, 'Category': ''}
        ]
        
        generator = TableGenerator()
        result = generator.generate_table(mixed_data)
        
        # Should handle various data types
        self.assertIn('<td>1</td>', result)  # Integer
        self.assertIn('<td>29.99</td>', result)  # Float
        self.assertIn('<td>True</td>', result)  # Boolean
        self.assertIn('<td>False</td>', result)  # Boolean
        self.assertIn('<td></td>', result)  # None and empty string

    def test_configuration_chaining_example(self):
        """Example: Method chaining for configuration"""
        data = [
            {'Name': 'Alice', 'Score': 95},
            {'Name': 'Bob', 'Score': 87},
            {'Name': 'Carol', 'Score': 92}
        ]
        
        # While we don't have method chaining in current implementation,
        # test that multiple configurations work together
        generator = TableGenerator(
            table_class='scores',
            table_id='student-scores',
            sortable=True,
            striped=True,
            responsive=True,
            custom_attributes={'data-sort': 'true'}
        )
        
        result = generator.generate_table(data)
        
        # All configurations should be applied
        self.assertIn('class="scores sortable striped responsive"', result)
        self.assertIn('id="student-scores"', result)
        self.assertIn('data-sort="true"', result)

    def test_csv_format_example(self):
        """Example: CSV-like data format (list of lists with headers)"""
        # Simulate data that might come from a CSV file or spreadsheet
        csv_data = [
            ['Employee ID', 'Full Name', 'Department', 'Salary', 'Start Date'],  # Headers
            ['EMP001', 'John Smith', 'Engineering', 85000, '2022-01-15'],
            ['EMP002', 'Jane Doe', 'Marketing', 72000, '2022-03-22'],
            ['EMP003', 'Mike Johnson', 'Sales', 68000, '2021-11-08'],
            ['EMP004', 'Sarah Wilson', 'Engineering', 92000, '2020-05-14']
        ]
        
        generator = TableGenerator(
            table_class='csv-table',
            striped=True,
            responsive=True
        )
        result = generator.generate_table(csv_data)
        
        # Should handle CSV format correctly
        self.assertIn('<table', result)
        self.assertIn('csv-table', result)
        
        # Should use first row as headers
        self.assertIn('<th>Employee ID</th>', result)
        self.assertIn('<th>Full Name</th>', result)
        self.assertIn('<th>Department</th>', result)
        
        # Should include all data rows
        self.assertIn('<td>EMP001</td>', result)
        self.assertIn('<td>John Smith</td>', result)
        self.assertIn('<td>Sarah Wilson</td>', result)
        
        # Count TR tags properly for CSV data
        import re
        tr_count = len(re.findall(r'<tr(?:[^>]*)?>', result))
        self.assertEqual(tr_count, 5)  # 1 header + 4 data rows

    def test_spreadsheet_like_data_example(self):
        """Example: Spreadsheet-like data with mixed types"""
        # Simulate data from a spreadsheet export
        spreadsheet_data = [
            ('Product Code', 'Product Name', 'Price', 'In Stock', 'Last Updated'),
            ('PRD-001', 'Wireless Mouse', 29.99, True, '2025-06-15'),
            ('PRD-002', 'Mechanical Keyboard', 129.99, False, '2025-06-10'),
            ('PRD-003', 'USB-C Hub', 45.50, True, '2025-06-18'),
            ('PRD-004', 'Webcam HD', 79.99, True, None)  # Missing date
        ]
        
        generator = TableGenerator(
            table_class='inventory-table',
            custom_headers={
                'Product Code': 'SKU',
                'In Stock': 'Available',
                'Last Updated': 'Updated'
            }
        )
        result = generator.generate_table(spreadsheet_data)
        
        # Should use custom headers when provided
        self.assertIn('<th>SKU</th>', result)  # Custom header for 'Product Code'
        self.assertIn('<th>Available</th>', result)  # Custom header for 'In Stock'
        
        # Should handle mixed data types
        self.assertIn('<td>29.99</td>', result)  # Float
        self.assertIn('<td>True</td>', result)   # Boolean
        self.assertIn('<td></td>', result)       # None value

    def test_collapsible_table_example(self):
        """Example: Creating collapsible tables for better UX"""
        # Large dataset that benefits from being collapsible
        large_dataset = [
            {'Employee': f'Worker {i}', 'Department': f'Dept {i % 3}', 
             'Salary': 50000 + (i * 1000), 'Years': i % 10}
            for i in range(15)
        ]
        
        generator = TableGenerator(
            table_class='employee-data',
            striped=True,
            responsive=True
        )
        
        table_html = generator.generate_table(large_dataset)
        
        # Create basic collapsible version
        basic_collapsible = generator.make_collapsible(
            table_html,
            title="Employee Data (15 records)",
            collapsed=False
        )
        
        # Should contain collapsible structure
        self.assertIn('<details', basic_collapsible)
        self.assertIn('Employee Data', basic_collapsible)
        self.assertIn('open', basic_collapsible)  # Starts expanded
        
        # Create styled collapsible version
        styled_collapsible = generator.make_collapsible_with_css(
            table_html,
            title="Styled Employee Data",
            collapsed=True,
            container_class="staff-table"
        )
        
        # Should include CSS and styling
        self.assertIn('<style>', styled_collapsible)
        self.assertIn('.staff-table', styled_collapsible)
        self.assertNotIn('open', styled_collapsible.split('</style>')[1])  # Starts collapsed

    def test_dashboard_with_multiple_collapsible_sections(self):
        """Example: Dashboard with multiple collapsible table sections"""
        # Different data sets for dashboard
        sales_data = [
            {'Region': 'North', 'Sales': 125000, 'Target': 120000},
            {'Region': 'South', 'Sales': 98000, 'Target': 100000},
            {'Region': 'East', 'Sales': 142000, 'Target': 130000}
        ]
        
        expense_data = [
            {'Category': 'Marketing', 'Budget': 50000, 'Spent': 45000},
            {'Category': 'Operations', 'Budget': 80000, 'Spent': 75000},
            {'Category': 'Technology', 'Budget': 60000, 'Spent': 58000}
        ]
        
        generator = TableGenerator(striped=True, responsive=True)
        
        # Generate individual tables
        sales_table = generator.generate_table(sales_data)
        expense_table = generator.generate_table(expense_data)
        
        # Make them collapsible with different settings
        sales_collapsible = generator.make_collapsible_with_css(
            sales_table,
            title="Sales Performance by Region",
            collapsed=False,
            container_class="sales-section"
        )
        
        expense_collapsible = generator.make_collapsible_with_css(
            expense_table,
            title="Expense Tracking by Category",
            collapsed=True,
            container_class="expense-section"
        )
        
        # Combine into dashboard
        dashboard = sales_collapsible + "\n\n" + expense_collapsible
        
        # Should contain both sections
        self.assertIn('Sales Performance', dashboard)
        self.assertIn('Expense Tracking', dashboard)
        self.assertIn('.sales-section', dashboard)
        self.assertIn('.expense-section', dashboard)
        
        # Sales should be open, expenses closed
        sales_part = dashboard.split('Expense Tracking')[0]
        expense_part = dashboard.split('Sales Performance')[1]
        
        self.assertIn('open', sales_part)
        self.assertNotIn('open', expense_part.split('</style>')[1] if '</style>' in expense_part else expense_part)

if __name__ == '__main__':
    unittest.main()

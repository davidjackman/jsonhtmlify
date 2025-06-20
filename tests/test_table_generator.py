import unittest
from src.table_generator import TableGenerator

class TestTableGenerator(unittest.TestCase):

    def setUp(self):
        self.table_generator = TableGenerator()

    # Basic functionality tests
    def test_generate_table_single_dict(self):
        """Test generating table from a single dictionary"""
        data = {'Name': 'Alice', 'Age': 30, 'City': 'New York'}
        result = self.table_generator.generate_table(data)
        
        # Should contain table structure
        self.assertIn('<table>', result)
        self.assertIn('</table>', result)
        self.assertIn('<thead>', result)
        self.assertIn('<tbody>', result)
        
        # Should contain headers
        self.assertIn('<th>Name</th>', result)
        self.assertIn('<th>Age</th>', result)
        self.assertIn('<th>City</th>', result)
        
        # Should contain data
        self.assertIn('<td>Alice</td>', result)
        self.assertIn('<td>30</td>', result)
        self.assertIn('<td>New York</td>', result)

    def test_generate_table_list_of_dicts(self):
        """Test generating table from list of dictionaries"""
        data = [
            {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
            {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
            {'Name': 'Carol', 'Age': 35, 'City': 'Chicago'}
        ]
        result = self.table_generator.generate_table(data)
        
        # Should contain table structure
        self.assertIn('<table>', result)
        self.assertIn('</table>', result)
        self.assertIn('<thead>', result)
        self.assertIn('<tbody>', result)
        
        # Should contain all names
        self.assertIn('<td>Alice</td>', result)
        self.assertIn('<td>Bob</td>', result)
        self.assertIn('<td>Carol</td>', result)
        
        # Should have multiple rows
        self.assertEqual(result.count('<tr>'), 4)  # 1 header + 3 data rows

    def test_generate_table_empty_dict(self):
        """Test generating table from empty dictionary"""
        data = {}
        result = self.table_generator.generate_table(data)
        
        # Should still create basic table structure
        self.assertIn('<table>', result)
        self.assertIn('</table>', result)

    def test_generate_table_empty_list(self):
        """Test generating table from empty list"""
        data = []
        result = self.table_generator.generate_table(data)
        
        # Should still create basic table structure
        self.assertIn('<table>', result)
        self.assertIn('</table>', result)

    # Table attributes tests
    def test_table_with_css_class(self):
        """Test adding CSS class to table"""
        data = {'Name': 'Alice', 'Age': 30}
        generator = TableGenerator(table_class='my-table')
        result = generator.generate_table(data)
        
        self.assertIn('class="my-table"', result)

    def test_table_with_id(self):
        """Test adding ID to table"""
        data = {'Name': 'Alice', 'Age': 30}
        generator = TableGenerator(table_id='data-table')
        result = generator.generate_table(data)
        
        self.assertIn('id="data-table"', result)

    def test_table_with_custom_attributes(self):
        """Test adding custom attributes to table"""
        data = {'Name': 'Alice', 'Age': 30}
        generator = TableGenerator(custom_attributes={'border': '1', 'cellpadding': '5'})
        result = generator.generate_table(data)
        
        self.assertIn('border="1"', result)
        self.assertIn('cellpadding="5"', result)

    # Header customization tests
    def test_custom_headers(self):
        """Test using custom headers instead of dictionary keys"""
        data = [
            {'name': 'Alice', 'age': 30},
            {'name': 'Bob', 'age': 25}
        ]
        headers = {'name': 'Full Name', 'age': 'Years Old'}
        generator = TableGenerator(custom_headers=headers)
        result = generator.generate_table(data)
        
        self.assertIn('<th>Full Name</th>', result)
        self.assertIn('<th>Years Old</th>', result)

    def test_header_order(self):
        """Test specifying header order"""
        data = {'age': 30, 'name': 'Alice', 'city': 'New York'}
        headers_order = ['name', 'city', 'age']
        generator = TableGenerator(headers_order=headers_order)
        result = generator.generate_table(data)
        
        # Check that headers appear in specified order
        name_pos = result.find('<th>name</th>')
        city_pos = result.find('<th>city</th>')
        age_pos = result.find('<th>age</th>')
        
        self.assertTrue(name_pos < city_pos < age_pos)

    # Data formatting tests
    def test_escape_html_characters(self):
        """Test that HTML characters are properly escaped"""
        data = {'Name': '<script>alert("xss")</script>', 'Description': 'A & B > C'}
        result = self.table_generator.generate_table(data)
        
        self.assertIn('&lt;script&gt;', result)
        self.assertIn('&amp;', result)
        self.assertIn('&gt;', result)
        self.assertNotIn('<script>', result)

    def test_handle_none_values(self):
        """Test handling None values in data"""
        data = {'Name': 'Alice', 'Age': None, 'City': 'New York'}
        result = self.table_generator.generate_table(data)
        
        self.assertIn('<td></td>', result)  # None should render as empty cell

    def test_handle_boolean_values(self):
        """Test handling boolean values"""
        data = {'Name': 'Alice', 'Active': True, 'Premium': False}
        result = self.table_generator.generate_table(data)
        
        self.assertIn('<td>True</td>', result)
        self.assertIn('<td>False</td>', result)

    def test_handle_numeric_values(self):
        """Test handling various numeric types"""
        data = {'Integer': 42, 'Float': 3.14, 'Scientific': 1.5e-10}
        result = self.table_generator.generate_table(data)
        
        self.assertIn('<td>42</td>', result)
        self.assertIn('<td>3.14</td>', result)
        self.assertIn('<td>1.5e-10</td>', result)

    # Error handling tests
    def test_invalid_input_type(self):
        """Test error handling for invalid input types"""
        with self.assertRaises(ValueError):
            self.table_generator.generate_table("invalid input")
        
        with self.assertRaises(ValueError):
            self.table_generator.generate_table(123)

    def test_inconsistent_dictionary_keys(self):
        """Test handling dictionaries with different keys"""
        data = [
            {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
            {'Name': 'Bob', 'Department': 'IT'},  # Missing Age and City, has Department
            {'Age': 25, 'Country': 'USA'}  # Missing Name, has Country
        ]
        result = self.table_generator.generate_table(data)
        
        # Should handle missing values gracefully
        self.assertIn('<table>', result)
        self.assertIn('</table>', result)

    # Advanced features tests
    def test_sortable_table(self):
        """Test generating sortable table"""
        data = [
            {'Name': 'Charlie', 'Age': 35},
            {'Name': 'Alice', 'Age': 30},
            {'Name': 'Bob', 'Age': 25}
        ]
        generator = TableGenerator(sortable=True)
        result = generator.generate_table(data)
        
        self.assertIn('sortable', result.lower())

    def test_sortable_table_javascript_inclusion(self):
        """Test that sortable tables include JavaScript code"""
        data = [
            {'Name': 'Alice', 'Age': 30, 'Salary': 50000},
            {'Name': 'Bob', 'Age': 25, 'Salary': 45000}
        ]
        
        sortable_generator = TableGenerator(sortable=True)
        table_html = sortable_generator.generate_table(data)
        complete_html = sortable_generator.render_html(table_html)
        
        # Check for sortable class
        self.assertIn('class="sortable"', table_html)
        
        # Check for JavaScript inclusion
        self.assertIn('<script>', complete_html)
        self.assertIn('sortTable', complete_html)
        self.assertIn('initializeSortableTables', complete_html)
        
        # Check for CSS inclusion
        self.assertIn('cursor: pointer', complete_html)
        self.assertIn('sort-asc', complete_html)

    def test_sortable_table_html_structure(self):
        """Test that sortable tables have correct HTML structure"""
        data = [
            {'Product': 'Laptop', 'Price': 1200, 'Stock': 15},
            {'Product': 'Mouse', 'Price': 25, 'Stock': 100}
        ]
        
        generator = TableGenerator(
            table_class='products',
            sortable=True,
            striped=True
        )
        
        result = generator.generate_table(data)
        
        # Should include both sortable and custom classes
        self.assertIn('class="products sortable striped"', result)
        
        # Should have proper table structure
        self.assertIn('<thead>', result)
        self.assertIn('<tbody>', result)
        self.assertIn('<th', result)
        self.assertIn('<td', result)

    def test_non_sortable_table_no_javascript(self):
        """Test that non-sortable tables don't include JavaScript"""
        data = {'Name': 'Alice', 'Age': 30}
        
        regular_generator = TableGenerator(sortable=False)
        table_html = regular_generator.generate_table(data)
        complete_html = regular_generator.render_html(table_html)
        
        # Should not include sortable class
        self.assertNotIn('sortable', table_html)
        
        # Should not include JavaScript
        self.assertNotIn('sortTable', complete_html)
        self.assertNotIn('<script>', complete_html)

    def test_sortable_with_collapsible(self):
        """Test that sortable tables work with collapsible functionality"""
        data = [
            {'Employee': 'John Doe', 'Department': 'IT', 'Salary': 75000},
            {'Employee': 'Jane Smith', 'Department': 'HR', 'Salary': 65000}
        ]
        
        generator = TableGenerator(
            table_class='employee-data',
            sortable=True,
            striped=True
        )
        
        table_html = generator.generate_table(data)
        collapsible_html = generator.make_collapsible_with_css(
            table_html,
            title="Employee Directory",
            collapsed=False
        )
        
        # Should maintain sortable functionality within collapsible
        self.assertIn('class="employee-data sortable striped"', collapsible_html)
        self.assertIn('<details', collapsible_html)
        self.assertIn('Employee Directory', collapsible_html)

    # Styling tests
    def test_inline_styles(self):
        """Test adding inline styles"""
        data = {'Name': 'Alice', 'Age': 30}
        styles = {
            'table': 'border-collapse: collapse; width: 100%;',
            'th': 'background-color: #f2f2f2; padding: 8px;',
            'td': 'padding: 8px; border: 1px solid #ddd;'
        }
        generator = TableGenerator(styles=styles)
        result = generator.generate_table(data)
        
        self.assertIn('border-collapse: collapse', result)
        self.assertIn('background-color: #f2f2f2', result)

    # Complete HTML document tests
    def test_render_complete_html(self):
        """Test rendering complete HTML document"""
        data = {'Name': 'Alice', 'Age': 30}
        table_html = self.table_generator.generate_table(data)
        result = self.table_generator.render_html(table_html)
        
        self.assertIn('<!DOCTYPE html>', result)
        self.assertIn('<html>', result)
        self.assertIn('<head>', result)
        self.assertIn('<body>', result)
        self.assertIn('</html>', result)

    def test_render_html_with_title(self):
        """Test rendering HTML with custom title"""
        data = {'Name': 'Alice', 'Age': 30}
        table_html = self.table_generator.generate_table(data)
        result = self.table_generator.render_html(table_html, title="My Data Table")
        
        self.assertIn('<title>My Data Table</title>', result)

    def test_render_html_with_css(self):
        """Test rendering HTML with custom CSS"""
        data = {'Name': 'Alice', 'Age': 30}
        table_html = self.table_generator.generate_table(data)
        css = "table { border-collapse: collapse; }"
        result = self.table_generator.render_html(table_html, css=css)
        
        self.assertIn('<style>', result)
        self.assertIn('border-collapse: collapse', result)

    # Performance and edge case tests
    def test_large_dataset(self):
        """Test with large dataset"""
        data = [{'ID': i, 'Name': f'User{i}', 'Value': i * 10} for i in range(1000)]
        result = self.table_generator.generate_table(data)
        
        # Should handle large datasets without errors
        self.assertIn('<table>', result)
        self.assertIn('</table>', result)
        self.assertEqual(result.count('<tr>'), 1001)  # 1 header + 1000 data rows

    def test_unicode_characters(self):
        """Test handling Unicode characters"""
        data = {'Name': '中文', 'Emoji': '🎉', 'Symbol': '©'}
        result = self.table_generator.generate_table(data)
        
        self.assertIn('中文', result)
        self.assertIn('🎉', result)
        self.assertIn('©', result)

    def test_very_long_strings(self):
        """Test handling very long strings"""
        long_string = 'A' * 10000
        data = {'Short': 'test', 'Long': long_string}
        result = self.table_generator.generate_table(data)
        
        self.assertIn(long_string, result)
        self.assertIn('<table>', result)

    # CSV-like data format tests
    def test_csv_like_data_format(self):
        """Test handling CSV-like data (list of lists with header row)"""
        csv_data = [
            ['Name', 'Age', 'City'],  # Header row
            ['Alice', 30, 'New York'],
            ['Bob', 25, 'Los Angeles'],
            ['Carol', 35, 'Chicago']
        ]
        result = self.table_generator.generate_table(csv_data)
        
        # Should contain table structure
        self.assertIn('<table>', result)
        self.assertIn('</table>', result)
        self.assertIn('<thead>', result)
        self.assertIn('<tbody>', result)
        
        # Should contain headers from first row
        self.assertIn('<th>Name</th>', result)
        self.assertIn('<th>Age</th>', result)
        self.assertIn('<th>City</th>', result)
        
        # Should contain data from subsequent rows
        self.assertIn('<td>Alice</td>', result)
        self.assertIn('<td>30</td>', result)
        self.assertIn('<td>New York</td>', result)
        self.assertIn('<td>Bob</td>', result)
        self.assertIn('<td>Carol</td>', result)

    def test_csv_like_data_with_tuples(self):
        """Test handling CSV-like data with tuples"""
        csv_data = [
            ('Product', 'Price', 'Stock'),  # Header row as tuple
            ('Laptop', 999.99, 50),
            ('Mouse', 29.99, 100),
            ('Keyboard', 79.99, 75)
        ]
        result = self.table_generator.generate_table(csv_data)
        
        # Should handle tuples correctly
        self.assertIn('<th>Product</th>', result)
        self.assertIn('<th>Price</th>', result)
        self.assertIn('<th>Stock</th>', result)
        self.assertIn('<td>Laptop</td>', result)
        self.assertIn('<td>999.99</td>', result)

    def test_csv_like_data_uneven_rows(self):
        """Test CSV-like data with uneven row lengths"""
        csv_data = [
            ['Name', 'Age', 'City', 'Country'],  # Header row with 4 columns
            ['Alice', 30, 'New York'],           # Row with 3 columns
            ['Bob', 25, 'Los Angeles', 'USA'],   # Row with 4 columns
            ['Carol']                            # Row with 1 column
        ]
        result = self.table_generator.generate_table(csv_data)
        
        # Should handle missing values gracefully
        self.assertIn('<table>', result)
        self.assertIn('<th>Country</th>', result)  # All headers should be present
        self.assertIn('<td>Alice</td>', result)
        self.assertIn('<td></td>', result)  # Empty cells for missing values

    def test_csv_like_data_empty_header(self):
        """Test CSV-like data with empty or None headers"""
        csv_data = [
            ['Name', '', 'Age', None],  # Headers with empty string and None
            ['Alice', 'Data1', 30, 'Data2'],
            ['Bob', 'Data3', 25, 'Data4']
        ]
        result = self.table_generator.generate_table(csv_data)
        
        # Should handle empty headers by converting to strings
        self.assertIn('<th>Name</th>', result)
        self.assertIn('<th></th>', result)  # Empty string header
        self.assertIn('<th>Age</th>', result)
        self.assertIn('<th>None</th>', result)  # None converted to string

    def test_mixed_data_types_in_csv(self):
        """Test CSV-like data with mixed data types"""
        csv_data = [
            ['ID', 'Name', 'Active', 'Score', 'Data'],
            [1, 'Alice', True, 95.5, None],
            [2, 'Bob', False, 87.2, 'Some text'],
            [3, 'Carol', True, None, 92]
        ]
        result = self.table_generator.generate_table(csv_data)
        
        # Should handle various data types correctly
        self.assertIn('<td>1</td>', result)
        self.assertIn('<td>Alice</td>', result)
        self.assertIn('<td>True</td>', result)
        self.assertIn('<td>95.5</td>', result)
        self.assertIn('<td></td>', result)  # None values

    # Collapsible table tests
    def test_make_collapsible_basic(self):
        """Test basic collapsible table functionality"""
        data = {'Name': 'Alice', 'Age': 30}
        table_html = self.table_generator.generate_table(data)
        
        collapsible = self.table_generator.make_collapsible(
            table_html, 
            title="Test Table"
        )
        
        # Should contain collapsible structure
        self.assertIn('<details', collapsible)
        self.assertIn('<summary', collapsible)
        self.assertIn('Test Table', collapsible)
        self.assertIn('collapsible-content', collapsible)
        self.assertIn(table_html, collapsible)
        
        # Should be open by default
        self.assertIn('open', collapsible)

    def test_make_collapsible_collapsed(self):
        """Test collapsible table starting collapsed"""
        data = {'Name': 'Bob', 'Age': 25}
        table_html = self.table_generator.generate_table(data)
        
        collapsible = self.table_generator.make_collapsible(
            table_html,
            title="Collapsed Table",
            collapsed=True
        )
        
        # Should not be open
        self.assertNotIn('open', collapsible)
        self.assertIn('Collapsed Table', collapsible)

    def test_make_collapsible_with_css(self):
        """Test collapsible table with built-in CSS"""
        data = [
            {'Product': 'Laptop', 'Price': 999},
            {'Product': 'Mouse', 'Price': 25}
        ]
        table_html = self.table_generator.generate_table(data)
        
        collapsible_with_css = self.table_generator.make_collapsible_with_css(
            table_html,
            title="Products",
            container_class="product-table"
        )
        
        # Should contain CSS styles
        self.assertIn('<style>', collapsible_with_css)
        self.assertIn('.product-table', collapsible_with_css)
        self.assertIn('border-radius', collapsible_with_css)
        self.assertIn('transition', collapsible_with_css)
        
        # Should contain the collapsible structure
        self.assertIn('<details', collapsible_with_css)
        self.assertIn('Products', collapsible_with_css)

    def test_collapsible_html_escaping(self):
        """Test that collapsible titles are properly HTML escaped"""
        data = {'Name': 'Test'}
        table_html = self.table_generator.generate_table(data)
        
        collapsible = self.table_generator.make_collapsible(
            table_html,
            title="<script>alert('xss')</script> & Test"
        )
        
        # Title should be escaped
        self.assertIn('&lt;script&gt;', collapsible)
        self.assertIn('&amp;', collapsible)
        self.assertNotIn('<script>', collapsible)

    def test_multiple_collapsible_unique_ids(self):
        """Test that multiple collapsible tables get unique IDs"""
        data = {'Name': 'Test'}
        table_html = self.table_generator.generate_table(data)
        
        collapsible1 = self.table_generator.make_collapsible(table_html, "Table 1")
        collapsible2 = self.table_generator.make_collapsible(table_html, "Table 2")
        
        # Both should contain collapsible structure
        self.assertIn('Table 1', collapsible1)
        self.assertIn('Table 2', collapsible2)
        
        # Should be different (though we can't easily test unique IDs without parsing)
        self.assertNotEqual(collapsible1, collapsible2)

if __name__ == '__main__':
    unittest.main()
"""
Performance tests for the HTML Table Generator.
These tests ensure the generator performs well with various data sizes and types.
"""

import unittest
import time
from src.table_generator import TableGenerator


class TestPerformance(unittest.TestCase):
    """Performance and stress tests."""

    def test_small_dataset_performance(self):
        """Test performance with small dataset (< 100 rows)"""
        data = [
            {'Name': f'User {i}', 'Age': 20 + i, 'City': f'City {i % 10}'}
            for i in range(50)
        ]
        
        generator = TableGenerator()
        
        start_time = time.time()
        result = generator.generate_table(data)
        end_time = time.time()
        
        # Should complete quickly
        self.assertLess(end_time - start_time, 0.1)  # Less than 100ms
        self.assertIn('<table>', result)
        self.assertEqual(result.count('<tr>'), 51)  # 1 header + 50 data rows

    def test_medium_dataset_performance(self):
        """Test performance with medium dataset (1000 rows)"""
        data = [
            {
                'ID': i,
                'Name': f'User {i}',
                'Email': f'user{i}@example.com',
                'Department': f'Dept {i % 5}',
                'Salary': 50000 + (i * 100),
                'Active': i % 2 == 0
            }
            for i in range(1000)
        ]
        
        generator = TableGenerator(striped=True, table_class='medium-table')
        
        start_time = time.time()
        result = generator.generate_table(data)
        end_time = time.time()
        
        # Should complete in reasonable time
        self.assertLess(end_time - start_time, 1.0)  # Less than 1 second
        self.assertIn('<table class="medium-table striped">', result)
        # Count all TR tags (including those with classes)
        import re
        tr_count = len(re.findall(r'<tr(?:[^>]*)?>', result))
        self.assertEqual(tr_count, 1001)  # 1 header + 1000 data rows

    def test_large_dataset_performance(self):
        """Test performance with large dataset (5000 rows)"""
        data = [
            {
                'ID': i,
                'Name': f'Record {i}',
                'Value1': i * 1.5,
                'Value2': i * 2.3,
                'Value3': f'String {i}',
                'Flag': i % 3 == 0
            }
            for i in range(5000)
        ]
        
        generator = TableGenerator()
        
        start_time = time.time()
        result = generator.generate_table(data)
        end_time = time.time()
        
        # Should complete in reasonable time even for large datasets
        self.assertLess(end_time - start_time, 5.0)  # Less than 5 seconds
        self.assertIn('<table>', result)
        self.assertEqual(result.count('<tr>'), 5001)  # 1 header + 5000 data rows

    def test_wide_table_performance(self):
        """Test performance with wide tables (many columns)"""
        # Create a single row with many columns
        wide_data = {f'Column_{i}': f'Value_{i}' for i in range(100)}
        
        generator = TableGenerator()
        
        start_time = time.time()
        result = generator.generate_table(wide_data)
        end_time = time.time()
        
        # Should handle wide tables efficiently
        self.assertLess(end_time - start_time, 0.1)  # Less than 100ms
        self.assertIn('<table>', result)
        self.assertEqual(result.count('<th>'), 100)  # 100 headers
        self.assertEqual(result.count('<td>'), 100)  # 100 data cells

    def test_complex_data_performance(self):
        """Test performance with complex data structures"""
        complex_data = []
        for i in range(1000):
            complex_data.append({
                'ID': i,
                'Name': f'User {i}',
                'Description': f'This is a longer description for user {i} with various details and information that might be displayed in the table. It contains multiple sentences and could be quite lengthy.',
                'Tags': f'tag1,tag2,tag{i%10}',
                'Metadata': f'{{"key": "value{i}", "type": "user", "score": {i * 0.1}}}',
                'Status': 'Active' if i % 2 == 0 else 'Inactive',
                'Created': f'2025-{(i%12)+1:02d}-{(i%28)+1:02d}',
                'Updated': f'2025-06-{(i%30)+1:02d}'
            })
        
        generator = TableGenerator(
            table_class='complex-table',
            striped=True,
            responsive=True
        )
        
        start_time = time.time()
        result = generator.generate_table(complex_data)
        end_time = time.time()
        
        # Should handle complex data reasonably well
        self.assertLess(end_time - start_time, 3.0)  # Less than 3 seconds
        self.assertIn('<table class="complex-table striped responsive">', result)

    def test_html_escaping_performance(self):
        """Test performance when HTML escaping is heavily used"""
        # Create data with lots of HTML characters that need escaping
        data = []
        for i in range(1000):
            data.append({
                'HTML': f'<div class="item-{i}">Content & "quotes" > text</div>',
                'Script': f'<script>alert("XSS {i}");</script>',
                'Symbols': f'© ® ™ § ¶ • – — ' " " ' '
            })
        
        generator = TableGenerator()
        
        start_time = time.time()
        result = generator.generate_table(data)
        end_time = time.time()
        
        # HTML escaping shouldn't significantly impact performance
        self.assertLess(end_time - start_time, 2.0)  # Less than 2 seconds
        
        # Verify escaping worked
        self.assertIn('&lt;div', result)
        self.assertIn('&amp;', result)
        self.assertIn('&gt;', result)
        self.assertNotIn('<script>', result)

    def test_unicode_performance(self):
        """Test performance with Unicode characters"""
        unicode_data = []
        for i in range(1000):
            unicode_data.append({
                'Chinese': f'用户 {i}',
                'Japanese': f'ユーザー {i}',
                'Arabic': f'مستخدم {i}',
                'Emoji': f'👤 User {i} 🌟',
                'Mixed': f'Ελληνικά {i} Русский français'
            })
        
        generator = TableGenerator()
        
        start_time = time.time()
        result = generator.generate_table(unicode_data)
        end_time = time.time()
        
        # Unicode handling shouldn't significantly impact performance
        self.assertLess(end_time - start_time, 2.0)  # Less than 2 seconds
        
        # Verify Unicode characters are preserved
        self.assertIn('用户', result)
        self.assertIn('ユーザー', result)
        self.assertIn('👤', result)

    def test_styling_performance(self):
        """Test performance impact of various styling options"""
        data = [
            {'Name': f'User {i}', 'Score': i * 10, 'Level': f'Level {i % 5}'}
            for i in range(1000)
        ]
        
        styles = {
            'table': 'border-collapse: collapse; width: 100%; font-family: Arial, sans-serif;',
            'th': 'background-color: #4CAF50; color: white; padding: 12px; text-align: left; border: 1px solid #ddd;',
            'td': 'padding: 12px; border: 1px solid #ddd; text-align: left;'
        }
        
        generator = TableGenerator(
            table_class='styled-table',
            table_id='performance-test',
            striped=True,
            responsive=True,
            sortable=True,
            styles=styles,
            custom_attributes={'data-test': 'performance'}
        )
        
        start_time = time.time()
        result = generator.generate_table(data)
        end_time = time.time()
        
        # Styling shouldn't significantly impact performance
        self.assertLess(end_time - start_time, 2.0)  # Less than 2 seconds
        
        # Verify styling is applied
        self.assertIn('border-collapse: collapse', result)
        self.assertIn('sortable', result)
        self.assertIn('responsive', result)

    def test_memory_usage_large_dataset(self):
        """Test that large datasets don't cause memory issues"""
        # This test primarily ensures we don't run into memory errors
        # with large datasets
        data = []
        for i in range(10000):
            data.append({
                'ID': i,
                'Data': f'Some data for row {i}',
                'More': f'Additional information {i}',
                'Extra': f'Extra field {i}'
            })
        
        generator = TableGenerator()
        
        # This should complete without memory errors
        result = generator.generate_table(data)
        
        # Basic verification
        self.assertIn('<table>', result)
        self.assertIn('Some data for row 9999', result)  # Last row should be present

    def test_inconsistent_keys_performance(self):
        """Test performance with inconsistent dictionary keys"""
        data = []
        for i in range(1000):
            row = {'ID': i, 'Name': f'User {i}'}
            
            # Add random additional fields
            if i % 3 == 0:
                row['Email'] = f'user{i}@example.com'
            if i % 5 == 0:
                row['Department'] = f'Dept {i % 10}'
            if i % 7 == 0:
                row['Phone'] = f'555-{i:04d}'
            
            data.append(row)
        
        generator = TableGenerator()
        
        start_time = time.time()
        result = generator.generate_table(data)
        end_time = time.time()
        
        # Should handle inconsistent keys efficiently
        self.assertLess(end_time - start_time, 2.0)  # Less than 2 seconds
        self.assertIn('<table>', result)


if __name__ == '__main__':
    unittest.main()

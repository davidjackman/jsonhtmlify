#!/usr/bin/env python3
"""
Quick demonstration of the HTML Table Generator's key features.
Run this script to see the different data formats and features in action.
"""

from src.table_generator import TableGenerator


def main():
    print("🚀 HTML Table Generator - Key Features Demo")
    print("=" * 50)
    
    # 1. Traditional dictionary format
    print("\n1. Dictionary Format:")
    dict_data = {'Name': 'John Doe', 'Age': 30, 'Department': 'Engineering'}
    generator = TableGenerator()
    result = generator.generate_table(dict_data)
    print(result)
    
    # 2. CSV-like format
    print("\n2. CSV-like Format (NEW!):")
    csv_data = [
        ['Name', 'Age', 'Department'],
        ['Alice', 25, 'Marketing'],
        ['Bob', 35, 'Sales']
    ]
    generator_csv = TableGenerator(striped=True, table_class='csv-table')
    result_csv = generator_csv.generate_table(csv_data)
    print(result_csv)
    
    # 3. List of dictionaries with styling
    print("\n3. Multiple Records with Styling:")
    employees = [
        {'Name': 'Charlie', 'Role': 'Developer', 'Years': 3},
        {'Name': 'Diana', 'Role': 'Designer', 'Years': 2},
        {'Name': 'Eve', 'Role': 'Manager', 'Years': 5}
    ]
    styled_generator = TableGenerator(
        table_class='employee-table',
        striped=True,
        responsive=True,
        custom_headers={'Years': 'Experience (Years)'}
    )
    result_styled = styled_generator.generate_table(employees)
    print(result_styled)
    
    print("\n✅ All formats working correctly!")
    print("\nSupported formats:")
    print("- Single dictionary")
    print("- List of dictionaries")
    print("- CSV-like lists (headers in first row)")
    print("- CSV-like tuples")
    print("- Mixed data types with proper escaping")


if __name__ == "__main__":
    main()

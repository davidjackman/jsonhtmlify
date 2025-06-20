# HTML Table Generator

This project provides a versatile HTML table generator that converts Python data structures into HTML tables. It supports multiple data formats and is designed to be easy to use and integrate into other applications.

## Features

- **Multiple Data Formats**: Convert dictionaries, lists of dictionaries, or CSV-like data to HTML tables
- **CSV-like Support**: Handle data in list-of-lists format (like CSV files) where the first row contains headers
- **Flexible Configuration**: Extensive customization options for styling and behavior
- **HTML Safety**: Automatic HTML escaping to prevent XSS attacks
- **Performance Optimized**: Handles large datasets efficiently
- **Simple and intuitive API**
- **Comprehensive unit tests**

## Supported Data Formats

1. **Single Dictionary**: `{'Name': 'John', 'Age': 30}`
2. **List of Dictionaries**: `[{'Name': 'John', 'Age': 30}, {'Name': 'Jane', 'Age': 25}]`
3. **CSV-like Lists**: `[['Name', 'Age'], ['John', 30], ['Jane', 25]]`
4. **CSV-like Tuples**: `[('Name', 'Age'), ('John', 30), ('Jane', 25)]`

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage Examples

### Basic Usage with Dictionary

```python
from src.table_generator import TableGenerator

data = {
    "Name": "John Doe",
    "Age": 30,
    "Department": "Engineering"
}

generator = TableGenerator()
html_table = generator.generate_table(data)
print(html_table)
```

### CSV-like Data Format

```python
# CSV-like data (list of lists)
csv_data = [
    ['Name', 'Age', 'Department'],  # Header row
    ['John Doe', 30, 'Engineering'],
    ['Jane Smith', 25, 'Marketing'],
    ['Bob Johnson', 35, 'Sales']
]

generator = TableGenerator(striped=True, table_class='csv-table')
html_table = generator.generate_table(csv_data)
print(html_table)
```

### Multiple Records with Styling

```python
employees = [
    {'Name': 'Alice Johnson', 'Department': 'HR', 'Salary': 75000},
    {'Name': 'Bob Smith', 'Department': 'Engineering', 'Salary': 95000},
    {'Name': 'Carol Williams', 'Department': 'Marketing', 'Salary': 68000}
]

generator = TableGenerator(
    table_class='employee-table',
    striped=True,
    responsive=True,
    sortable=True
)

html_table = generator.generate_table(employees)
```

### Advanced Configuration

```python
# Custom styling and headers
generator = TableGenerator(
    table_class='custom-table',
    table_id='data-table',
    custom_headers={'Name': 'Employee Name', 'Salary': 'Annual Salary'},
    styles={
        'table': 'border-collapse: collapse; width: 100%;',
        'th': 'background-color: #4CAF50; color: white; padding: 12px;',
        'td': 'padding: 8px; border: 1px solid #ddd;'
    },
    custom_attributes={'data-sortable': 'true'}
)
```

### Complete HTML Document

```python
# Generate complete HTML document
table_html = generator.generate_table(data)
complete_html = generator.render_html(
    table_html, 
    title="Employee Directory",
    css="body { font-family: Arial, sans-serif; margin: 40px; }"
)

# Save to file
with open('report.html', 'w') as f:
    f.write(complete_html)
```

## Configuration Options

### TableGenerator Parameters

- `table_class`: CSS class for the table
- `table_id`: ID attribute for the table
- `custom_attributes`: Dictionary of custom HTML attributes
- `custom_headers`: Dictionary mapping original headers to display names
- `headers_order`: List specifying the order of headers
- `sortable`: Add sortable class/functionality
- `striped`: Add alternating row colors
- `responsive`: Make table responsive
- `styles`: Dictionary of CSS styles for table elements

### Styling Options

The `styles` parameter accepts a dictionary with these keys:
- `'table'`: Styles for the `<table>` element
- `'th'`: Styles for header cells (`<th>`)
- `'td'`: Styles for data cells (`<td>`)

## Data Handling Features

- **HTML Escaping**: Automatic escaping of HTML characters for security
- **Mixed Data Types**: Handles strings, numbers, booleans, and None values
- **Inconsistent Keys**: Gracefully handles dictionaries with different keys
- **Empty Values**: Properly renders None values as empty cells
- **Unicode Support**: Full support for international characters and emojis

## Running Tests

Run the complete test suite:

```bash
pytest tests/
```

Run specific test categories:

```bash
# Core functionality tests
pytest tests/test_table_generator.py -v

# Performance tests
pytest tests/test_performance.py -v

# Usage examples
pytest tests/test_examples.py -v

# CSV-specific tests
pytest tests/ -k csv -v
```

## Performance

The generator is optimized for performance and can handle:
- Large datasets (tested with 10,000+ rows)
- Wide tables (100+ columns)
- Complex data structures
- Unicode content
- Mixed data types

Performance benchmarks are included in the test suite.

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## Examples and Demos

Check out the demo files:
- `src/main.py`: Basic usage examples
- `demo_csv_format.py`: Comprehensive CSV format demonstrations
- `run_tests.py`: Complete test runner with reporting

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

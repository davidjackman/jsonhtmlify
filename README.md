# HTML Table Generator

This project provides a versatile HTML table generator that converts Python data structures into HTML tables. It supports multiple data formats and is designed to be easy to use and integrate into other applications.

## Features

- **Multiple Data Formats**: Convert dictionaries, lists of dictionaries, or CSV-like data to HTML tables
- **CSV-like Support**: Handle data in list-of-lists format (like CSV files) where the first row contains headers
- **Interactive Sorting**: Click column headers to sort table data dynamically (NEW!)
- **Collapsible Tables**: Create expandable/collapsible table sections for better UX and performance
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

### Collapsible Tables (NEW!)

```python
# Create a collapsible table for better UX
employees = [
    {'Name': 'Alice Johnson', 'Department': 'HR', 'Salary': 75000},
    {'Name': 'Bob Smith', 'Department': 'Engineering', 'Salary': 95000},
    # ... more data
]

generator = TableGenerator(striped=True, responsive=True)
table_html = generator.generate_table(employees)

# Basic collapsible
collapsible = generator.make_collapsible(
    table_html,
    title="Employee Directory",
    collapsed=False
)

# Styled collapsible with built-in CSS
styled_collapsible = generator.make_collapsible_with_css(
    table_html,
    title="Styled Employee Directory",
    collapsed=True
)
```

### Interactive Sortable Tables (NEW!)

```python
# Enable click-to-sort functionality
employee_data = [
    {'ID': 'EMP001', 'Name': 'Sarah Johnson', 'Salary': 125000, 'Department': 'Engineering'},
    {'ID': 'EMP002', 'Name': 'Mike Chen', 'Salary': 135000, 'Department': 'Product'},
    {'ID': 'EMP003', 'Name': 'Lisa Rodriguez', 'Salary': 115000, 'Department': 'Design'}
]

generator = TableGenerator(
    sortable=True,  # Enable interactive sorting!
    striped=True,
    custom_headers={
        'ID': 'Employee ID',
        'Name': 'Full Name',
        'Salary': 'Annual Salary ($)'
    }
)

table_html = generator.generate_table(employee_data)
complete_html = generator.render_html(table_html, title="Sortable Employee Data")

# Users can now click any column header to sort the data!
# Handles text, numbers, and dates automatically
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
- `sortable`: Enable interactive column sorting (click headers to sort)
- `striped`: Add alternating row colors
- `responsive`: Make table responsive
- `styles`: Dictionary of CSS styles for table elements

### Collapsible Table Methods

#### `make_collapsible(table_html, title, collapsed, container_class)`
- Basic collapsible functionality using HTML5 `<details>` element
- Returns table wrapped in collapsible container

#### `make_collapsible_with_css(table_html, title, collapsed, container_class)`
- Styled collapsible with professional CSS
- Includes animations, hover effects, and modern design
- Ready to use without additional styling

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

# Collapsible table tests
pytest tests/ -k collapsible -v
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
- `src/main.py`: Basic usage examples including collapsible tables
- `demo_csv_format.py`: Comprehensive CSV format demonstrations
- `collapsible_demo.html`: Interactive collapsible table demonstration
- `run_tests.py`: Complete test runner with reporting

## Demo Files

The project includes several comprehensive demo files showcasing different features:

### 1. **Enhanced Executive Dashboard** (`enhanced_dashboard_demo.py`)
**NEW!** - A comprehensive business intelligence dashboard featuring:
- Multiple interactive sortable tables
- Statistical summary cards with hover effects
- Professional gradient styling and animations
- Responsive design for all devices
- Real-time data sorting and analysis
- Collapsible sections for organized data presentation

```bash
python enhanced_dashboard_demo.py
# Creates: enhanced_executive_dashboard.html
```

### 2. **Complete Workflow Demo** (`complete_workflow_demo.py`)
Demonstrates the full power of the table generator:
- Multiple data formats (CSV, dict, single values)
- Interactive sortable tables
- Professional styling and animations
- Collapsible sections
- Complete HTML document generation

```bash
python complete_workflow_demo.py
# Creates: executive_dashboard.html
```

### 3. **Sortable Tables Demo** (`sortable_demo.py`)
Interactive demonstration of sorting functionality:
- Click-to-sort column headers
- Visual sort indicators with animations
- Smart data type detection (text, numbers, dates)
- Professional hover effects

```bash
python sortable_demo.py
# Creates: sortable_demo.html
```

### 4. **Multi-Table Dashboard** (`multi_table_document_demo.py`)
Shows how to create documents with multiple tables:
- Different data sources in one document
- Varied styling for each table
- Professional document layout

```bash
python multi_table_document_demo.py
# Creates: multi_table_dashboard.html
```

### 5. **Basic Examples**
- `quick_demo.py` - Simple usage examples
- `demo_csv_format.py` - CSV-like data handling
- `sales_report_demo.py` - Business report example

## 📊 Business Intelligence Features

The enhanced dashboard provides enterprise-level features:

### **Interactive Data Analysis**
- Sort any column by clicking headers
- Visual feedback with animations
- Smart data type recognition
- Mobile-responsive design

### **Professional Presentation**
- Statistical summary cards
- Gradient backgrounds and hover effects
- Clean, modern design
- Print-friendly layouts

### **Comprehensive Data Sources**
- Quarterly performance metrics
- Regional breakdown analysis  
- Product category performance
- Key performance indicators

## What's New

### Version 2.0 Features
- ✅ **CSV-like data support** - Handle list-of-lists format
- ✅ **Collapsible tables** - Expandable/collapsible sections
- ✅ **Enhanced styling** - Professional CSS with animations
- ✅ **Better performance** - Optimized for large datasets
- ✅ **Comprehensive testing** - 59 tests covering all functionality

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
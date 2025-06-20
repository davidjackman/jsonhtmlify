# HTML Table Generator

This project provides a simple HTML table generator that converts Python dictionaries into HTML tables. It is designed to be easy to use and integrate into other applications.

## Features

- Convert dictionaries to HTML tables.
- Simple and intuitive API.
- Unit tests to ensure functionality.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To use the HTML table generator, you can import the `TableGenerator` class from the `table_generator` module in your Python script. Here’s a quick example:

```python
from src.table_generator import TableGenerator

data = {
    "Header1": "Value1",
    "Header2": "Value2",
    "Header3": "Value3"
}

table_gen = TableGenerator()
html_table = table_gen.generate_table(data)
print(html_table)
```

## Running Tests

To run the unit tests for the project, use the following command:

```
pytest tests/test_table_generator.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bugs.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
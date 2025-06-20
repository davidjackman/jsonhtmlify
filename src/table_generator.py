import html
from typing import Dict, List, Union, Any, Optional, Tuple


class TableGenerator:
    def __init__(self, 
                 table_class: Optional[str] = None,
                 table_id: Optional[str] = None,
                 custom_attributes: Optional[Dict[str, str]] = None,
                 custom_headers: Optional[Dict[str, str]] = None,
                 headers_order: Optional[List[str]] = None,
                 sortable: bool = False,
                 striped: bool = False,
                 responsive: bool = False,
                 styles: Optional[Dict[str, str]] = None):
        """
        Initialize the HTML Table Generator.
        
        Args:
            table_class: CSS class for the table
            table_id: ID attribute for the table
            custom_attributes: Custom attributes for the table element
            custom_headers: Custom header names mapping
            headers_order: Order of headers to display
            sortable: Whether to make table sortable
            striped: Whether to add striped row styling
            responsive: Whether to make table responsive
            styles: Custom CSS styles for table elements
        """
        self.table_class = table_class
        self.table_id = table_id
        self.custom_attributes = custom_attributes or {}
        self.custom_headers = custom_headers or {}
        self.headers_order = headers_order
        self.sortable = sortable
        self.striped = striped
        self.responsive = responsive
        self.styles = styles or {}

    def _escape_html(self, value: Any) -> str:
        """Escape HTML characters in values."""
        if value is None:
            return ""
        return html.escape(str(value))

    def _get_table_attributes(self) -> str:
        """Generate table attributes string."""
        attributes = []
        
        if self.table_class:
            class_list = [self.table_class]
            if self.sortable:
                class_list.append('sortable')
            if self.striped:
                class_list.append('striped')
            if self.responsive:
                class_list.append('responsive')
            attributes.append(f'class="{" ".join(class_list)}"')
        else:
            class_list = []
            if self.sortable:
                class_list.append('sortable')
            if self.striped:
                class_list.append('striped')
            if self.responsive:
                class_list.append('responsive')
            if class_list:
                attributes.append(f'class="{" ".join(class_list)}"')
        
        if self.table_id:
            attributes.append(f'id="{self.table_id}"')
        
        for key, value in self.custom_attributes.items():
            attributes.append(f'{key}="{self._escape_html(value)}"')
        
        if 'table' in self.styles:
            attributes.append(f'style="{self.styles["table"]}"')
        
        return ' ' + ' '.join(attributes) if attributes else ''

    def _get_header_style(self) -> str:
        """Get header style string."""
        return f' style="{self.styles["th"]}"' if 'th' in self.styles else ''

    def _get_cell_style(self) -> str:
        """Get cell style string."""
        return f' style="{self.styles["td"]}"' if 'td' in self.styles else ''

    def _get_row_class(self, row_index: int) -> str:
        """Get row class for striping."""
        if self.striped:
            return f' class="{"odd" if row_index % 2 == 1 else "even"}"'
        return ''

    def _extract_headers(self, data: Union[Dict, List[Dict], List[List]]) -> List[str]:
        """Extract headers from data."""
        if isinstance(data, dict):
            headers = list(data.keys())
        elif isinstance(data, list) and data:
            # Check if it's CSV-like data
            if self._is_csv_like_data(data):
                # First row contains headers
                headers = [str(header) for header in data[0]]
            else:
                # Get all unique keys from all dictionaries
                all_keys = set()
                for item in data:
                    if isinstance(item, dict):
                        all_keys.update(item.keys())
                headers = list(all_keys)
        else:
            return []
        
        # Apply custom ordering if specified
        if self.headers_order:
            ordered_headers = []
            for header in self.headers_order:
                if header in headers:
                    ordered_headers.append(header)
            # Add any remaining headers not in the order
            for header in headers:
                if header not in ordered_headers:
                    ordered_headers.append(header)
            return ordered_headers
        
        return headers

    def _get_display_header(self, header: str) -> str:
        """Get display name for header."""
        return self.custom_headers.get(header, header)

    def _is_csv_like_data(self, data: List) -> bool:
        """
        Check if data is CSV-like (list of lists/tuples where first row is headers).
        
        Args:
            data: List to check
            
        Returns:
            True if data appears to be CSV-like format
        """
        if not isinstance(data, list) or len(data) < 2:
            return False
        
        # Check if all elements are lists or tuples
        return all(isinstance(row, (list, tuple)) for row in data)

    def _convert_csv_to_dicts(self, data: List) -> List[Dict]:
        """
        Convert CSV-like data (list of lists/tuples) to list of dictionaries.
        
        Args:
            data: List where first row contains headers, subsequent rows contain data
            
        Returns:
            List of dictionaries
        """
        if not data:
            return []
        
        headers = data[0]
        rows = data[1:]
        
        result = []
        for row in rows:
            # Create dictionary for this row
            row_dict = {}
            for i, header in enumerate(headers):
                # Use header as key, row value as value (or None if row is shorter)
                row_dict[str(header)] = row[i] if i < len(row) else None
            result.append(row_dict)
        
        return result

    def _get_sort_javascript(self) -> str:
        """Generate JavaScript code for table sorting functionality."""
        return """
function sortTable(table, column, dataType = 'auto') {
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    const isAscending = table.dataset.sortDirection !== 'asc';
    
    // Determine data type if auto
    if (dataType === 'auto') {
        const sampleValue = rows[0]?.cells[column]?.textContent.trim();
        if (sampleValue && !isNaN(sampleValue.replace(/[,$%]/g, ''))) {
            dataType = 'number';
        } else if (sampleValue && !isNaN(Date.parse(sampleValue))) {
            dataType = 'date';
        } else {
            dataType = 'string';
        }
    }
    
    // Sort rows
    rows.sort((a, b) => {
        const aText = a.cells[column]?.textContent.trim() || '';
        const bText = b.cells[column]?.textContent.trim() || '';
        
        let aVal, bVal;
        
        switch (dataType) {
            case 'number':
                aVal = parseFloat(aText.replace(/[,$%]/g, '')) || 0;
                bVal = parseFloat(bText.replace(/[,$%]/g, '')) || 0;
                break;
            case 'date':
                aVal = new Date(aText);
                bVal = new Date(bText);
                break;
            default:
                aVal = aText.toLowerCase();
                bVal = bText.toLowerCase();
        }
        
        if (aVal < bVal) return isAscending ? -1 : 1;
        if (aVal > bVal) return isAscending ? 1 : -1;
        return 0;
    });
    
    // Update tbody with sorted rows
    rows.forEach(row => tbody.appendChild(row));
    
    // Update sort direction
    table.dataset.sortDirection = isAscending ? 'asc' : 'desc';
    
    // Update header indicators
    const headers = table.querySelectorAll('th[data-sortable]');
    headers.forEach((header, index) => {
        header.classList.remove('sort-asc', 'sort-desc');
        if (index === column) {
            header.classList.add(isAscending ? 'sort-asc' : 'sort-desc');
        }
    });
}

function initializeSortableTables() {
    document.querySelectorAll('table.sortable').forEach(table => {
        const headers = table.querySelectorAll('th');
        headers.forEach((header, index) => {
            header.setAttribute('data-sortable', 'true');
            header.style.cursor = 'pointer';
            header.style.userSelect = 'none';
            header.style.position = 'relative';
            
            // Add sort indicator
            const indicator = document.createElement('span');
            indicator.className = 'sort-indicator';
            indicator.innerHTML = ' ↕️';
            indicator.style.opacity = '0.5';
            indicator.style.fontSize = '0.8em';
            indicator.style.marginLeft = '5px';
            header.appendChild(indicator);
            
            header.addEventListener('click', () => {
                sortTable(table, index);
            });
        });
    });
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeSortableTables);
} else {
    initializeSortableTables();
}
"""

    def _get_sort_css(self) -> str:
        """Generate CSS for sortable table styling."""
        return """
/* Sortable table styles */
.sortable th[data-sortable] {
    position: relative;
    cursor: pointer;
    user-select: none;
    transition: all 0.2s ease;
}

.sortable th[data-sortable]:hover {
    filter: brightness(1.1);
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}

.sortable th.sort-asc .sort-indicator::after {
    content: ' ↑';
    color: #fff;
    font-weight: bold;
    opacity: 1;
}

.sortable th.sort-desc .sort-indicator::after {
    content: ' ↓';
    color: #fff;
    font-weight: bold;
    opacity: 1;
}

.sortable th:not(.sort-asc):not(.sort-desc) .sort-indicator {
    opacity: 0.5;
}

.sortable th.sort-asc,
.sortable th.sort-desc {
    filter: brightness(1.05);
}
"""

    def _render_javascript(self) -> str:
        """Render JavaScript for table sorting if sortable."""
        if self.sortable:
            return f"<script>{self._get_sort_javascript()}</script>"
        return ""

    def _render_css(self) -> str:
        """Render CSS for sortable tables if sortable."""
        if self.sortable:
            return f"<style>{self._get_sort_css()}</style>"
        return ""

    def generate_table(self, data: Union[Dict, List[Dict], List[List]]) -> str:
        """
        Generate HTML table from dictionary, list of dictionaries, or CSV-like data.
        
        Args:
            data: Dictionary, list of dictionaries, or CSV-like data (list of lists/tuples 
                  where first row contains headers) to convert to HTML table
            
        Returns:
            HTML table string
            
        Raises:
            ValueError: If data is not a supported format
        """
        if not isinstance(data, (dict, list)):
            raise ValueError("Input must be a dictionary, list of dictionaries, or CSV-like data (list of lists)")
        
        # Handle empty data
        if not data:
            return f'<table{self._get_table_attributes()}>\n</table>'
        
        # Check if data is CSV-like and convert to dictionaries
        if isinstance(data, list) and self._is_csv_like_data(data):
            data_list = self._convert_csv_to_dicts(data)
        elif isinstance(data, dict):
            # Convert single dict to list for uniform processing
            data_list = [data]
        else:
            # Already a list of dictionaries
            data_list = data

        # Check and convert CSV-like data
        if self._is_csv_like_data(data_list):
            data_list = self._convert_csv_to_dicts(data_list)
        
        # Extract headers
        headers = self._extract_headers(data_list)
        if not headers:
            return f'<table{self._get_table_attributes()}>\n</table>'
        
        # Start building HTML
        html_parts = [f'<table{self._get_table_attributes()}>']
        
        # Generate header
        html_parts.append('  <thead>')
        html_parts.append('    <tr>')
        for header in headers:
            display_header = self._get_display_header(header)
            html_parts.append(f'      <th{self._get_header_style()}>{self._escape_html(display_header)}</th>')
        html_parts.append('    </tr>')
        html_parts.append('  </thead>')
        
        # Generate body
        html_parts.append('  <tbody>')
        for row_index, row_data in enumerate(data_list):
            if not isinstance(row_data, dict):
                continue
            
            row_class = self._get_row_class(row_index)
            html_parts.append(f'    <tr{row_class}>')
            
            for header in headers:
                value = row_data.get(header)
                html_parts.append(f'      <td{self._get_cell_style()}>{self._escape_html(value)}</td>')
            
            html_parts.append('    </tr>')
        html_parts.append('  </tbody>')
        html_parts.append('</table>')
        
        return '\n'.join(html_parts)

    def render_html(self, table_html: str, title: str = "HTML Table", css: Optional[str] = None) -> str:
        """
        Render complete HTML document with the table.
        
        Args:
            table_html: The HTML table string
            title: Page title
            css: Additional CSS to include
            
        Returns:
            Complete HTML document string
        """
        css_section = ""
        if css:
            css_section = f"<style>\n{css}\n</style>\n"
        
        # Add sortable functionality if enabled
        sortable_styles = self._render_css()
        sortable_script = self._render_javascript()
        
        return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{self._escape_html(title)}</title>
{css_section}{sortable_styles}</head>
<body>
{table_html}
{sortable_script}</body>
</html>"""

    def _render_javascript(self) -> str:
        """Render JavaScript for table sorting if sortable."""
        if self.sortable:
            return f"<script>{self._get_sort_javascript()}</script>"
        return ""

    def _render_css(self) -> str:
        """Render CSS for sortable tables if sortable."""
        if self.sortable:
            return f"<style>{self._get_sort_css()}</style>"
        return ""

    def make_collapsible(self, table_html: str, title: str = "Table", 
                        collapsed: bool = False, container_class: str = "collapsible-table") -> str:
        """
        Wrap an HTML table in a collapsible container.
        
        Args:
            table_html: The HTML table string to make collapsible
            title: Title text for the collapsible header
            collapsed: Whether the table should start collapsed (default: False)
            container_class: CSS class for the collapsible container
            
        Returns:
            HTML string with table wrapped in collapsible container
        """
        # Generate unique ID for this collapsible
        import random
        collapse_id = f"collapse-{random.randint(1000, 9999)}"
        
        # Determine initial state
        details_attrs = 'open' if not collapsed else ''
        
        collapsible_html = f"""<details class="{container_class}" {details_attrs}>
  <summary class="collapsible-header">
    <span class="collapsible-title">{self._escape_html(title)}</span>
    <span class="collapsible-icon">▼</span>
  </summary>
  <div class="collapsible-content">
    {table_html}
  </div>
</details>"""
        
        return collapsible_html
    
    def make_collapsible_with_css(self, table_html: str, title: str = "Table", 
                                 collapsed: bool = False, 
                                 container_class: str = "collapsible-table") -> str:
        """
        Wrap an HTML table in a collapsible container with built-in CSS styling.
        
        Args:
            table_html: The HTML table string to make collapsible
            title: Title text for the collapsible header
            collapsed: Whether the table should start collapsed (default: False)
            container_class: CSS class for the collapsible container
            
        Returns:
            HTML string with table wrapped in styled collapsible container
        """
        collapsible_html = self.make_collapsible(table_html, title, collapsed, container_class)
        
        # Built-in CSS for collapsible styling
        css = f"""<style>
.{container_class} {{
    border: 1px solid #ddd;
    border-radius: 8px;
    margin: 10px 0;
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}}

.{container_class} summary {{
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 15px 20px;
    cursor: pointer;
    user-select: none;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 7px 7px 0 0;
    font-weight: 600;
    transition: background-color 0.3s ease;
}}

.{container_class} summary:hover {{
    background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
}}

.{container_class} summary:focus {{
    outline: 2px solid #4c51bf;
    outline-offset: 2px;
}}

.{container_class}[open] summary {{
    border-radius: 7px 7px 0 0;
}}

.{container_class}:not([open]) summary {{
    border-radius: 7px;
}}

.collapsible-title {{
    font-size: 16px;
    font-weight: 600;
}}

.collapsible-icon {{
    font-size: 12px;
    transition: transform 0.3s ease;
}}

.{container_class}[open] .collapsible-icon {{
    transform: rotate(180deg);
}}

.collapsible-content {{
    padding: 0;
    animation: slideDown 0.3s ease-out;
}}

@keyframes slideDown {{
    from {{
        opacity: 0;
        max-height: 0;
    }}
    to {{
        opacity: 1;
        max-height: 1000px;
    }}
}}

.{container_class} table {{
    margin: 0;
    border-radius: 0;
    border: none;
}}
</style>
{collapsible_html}"""
        
        return css
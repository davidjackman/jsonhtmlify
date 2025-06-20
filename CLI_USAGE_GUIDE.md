# 📊 Interactive Dashboard CLI - Usage Guide

## Overview

The Dashboard CLI provides a powerful command-line interface for generating interactive HTML dashboards from JSON data sources. Transform your data into beautiful, sortable, and responsive HTML tables with just a few commands!

## 🚀 Quick Start

### 1. List Available Datasets
```bash
python dashboard_cli.py list
```

### 2. Preview a Dataset
```bash
python dashboard_cli.py preview employee_data
python dashboard_cli.py preview key_metrics
```

### 3. Generate Single Table
```bash
python dashboard_cli.py table employee_data
python dashboard_cli.py table quarterly_performance --output quarterly.html
```

### 4. Generate Full Dashboard
```bash
python dashboard_cli.py dashboard
python dashboard_cli.py dashboard --datasets key_metrics employee_data --output executive_summary.html
```

## 📋 Available Commands

### `list` - List Available Datasets
Shows all JSON data files in the `/data` directory with record counts.

```bash
python dashboard_cli.py list
```

**Output Example:**
```
📊 Available Datasets:
==================================================
  • product_performance         4 records
  • quarterly_performance       6 records
  • regional_performance        4 records
  • key_metrics                 8 metrics
  • employee_data               6 records

💾 Data files location: /Users/david/htmldictify/html-table-generator/data
```

### `preview` - Preview Dataset Contents
Shows the structure and sample data for any dataset.

```bash
python dashboard_cli.py preview <dataset_name>
```

**Examples:**
```bash
python dashboard_cli.py preview employee_data
python dashboard_cli.py preview key_metrics
python dashboard_cli.py preview quarterly_performance
```

### `table` - Generate Single HTML Table
Creates a standalone HTML file with an interactive table from one dataset.

```bash
python dashboard_cli.py table <dataset_name> [--output filename.html] [--no-sortable] [--no-striped]
```

**Examples:**
```bash
# Generate with default filename
python dashboard_cli.py table employee_data

# Specify custom output file
python dashboard_cli.py table product_performance --output products.html

# Disable sorting and striping
python dashboard_cli.py table regional_performance --no-sortable --no-striped
```

**Features:**
- ✅ Interactive column sorting (click headers)
- ✅ Responsive design for mobile devices
- ✅ Professional styling and hover effects
- ✅ Automatic data type detection for sorting
- ✅ HTML escaping for security

### `dashboard` - Generate Comprehensive Dashboard
Creates a multi-section dashboard with collapsible tables from multiple datasets.

```bash
python dashboard_cli.py dashboard [--datasets dataset1 dataset2 ...] [--output filename.html]
```

**Examples:**
```bash
# Generate dashboard with all available datasets
python dashboard_cli.py dashboard

# Generate custom dashboard with specific datasets
python dashboard_cli.py dashboard --datasets key_metrics employee_data

# Specify custom output file
python dashboard_cli.py dashboard --output business_dashboard.html --datasets quarterly_performance regional_performance
```

**Features:**
- 🎨 Color-coded sections for different data types
- 📊 Collapsible/expandable table sections
- 🔄 Interactive sorting on all tables
- 📱 Mobile-responsive design
- ⏰ Timestamp and data source information
- 🎯 Executive summary layout

## 📁 Data Structure

### JSON File Requirements

Data files should be in the `/data` directory and follow these structures:

#### Single Dataset Format
```json
{
  "dataset_name": [
    {"field1": "value1", "field2": "value2"},
    {"field1": "value3", "field2": "value4"}
  ]
}
```

#### Metrics Format (for KPIs)
```json
{
  "metrics_name": {
    "metric1": {
      "value": 1000000,
      "formatted": "$1.0M",
      "description": "Revenue description",
      "trend": "up",
      "change": 0.15
    }
  }
}
```

### Supported Data Types
- 📝 **Text**: Names, descriptions, categories
- 🔢 **Numbers**: Revenue, counts, percentages
- 📅 **Dates**: Hiring dates, transaction dates
- 💰 **Currency**: Formatted monetary values
- 📊 **Percentages**: Growth rates, margins
- ✅ **Booleans**: Active/inactive status

## 🎨 Generated Output Features

### Single Table Features
- **Interactive Sorting**: Click any column header to sort
- **Visual Indicators**: Sort arrows (↕️ ↑ ↓) show current state
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Professional Styling**: Clean, modern appearance
- **Data Type Intelligence**: Numbers, dates, and text sort correctly

### Dashboard Features
- **Multi-Section Layout**: Each dataset gets its own collapsible section
- **Color Coding**: Different colors for different data types:
  - 🔵 Quarterly Performance: Blue (#4a90e2)
  - 🟢 Regional Performance: Green (#5cb85c)
  - 🔴 Product Performance: Red (#d9534f)
  - 🟣 Key Metrics: Purple (#8e44ad)
  - 🟠 Employee Data: Orange (#f39c12)
- **Expandable Sections**: Key metrics expanded by default, others collapsed
- **Executive Summary**: Professional business dashboard layout

## 🔧 Customization Options

### Table Options
- `--sortable` / `--no-sortable`: Enable/disable column sorting
- `--striped` / `--no-striped`: Enable/disable alternating row colors
- `--output`: Specify custom output filename

### Dashboard Options
- `--datasets`: Specify which datasets to include
- `--output`: Custom dashboard filename
- Color themes automatically applied based on data type

## 📊 Example Workflows

### Executive Dashboard
```bash
# Generate executive summary with key metrics and employee data
python dashboard_cli.py dashboard --datasets key_metrics employee_data --output executive_summary.html
```

### Sales Analysis
```bash
# Focus on sales and regional performance
python dashboard_cli.py dashboard --datasets quarterly_performance regional_performance product_performance --output sales_analysis.html
```

### HR Dashboard
```bash
# Employee-focused dashboard
python dashboard_cli.py table employee_data --output hr_dashboard.html
```

### Complete Business Overview
```bash
# All datasets in one comprehensive dashboard
python dashboard_cli.py dashboard --output complete_business_dashboard.html
```

## 🌐 Browser Compatibility

Generated HTML files work in:
- ✅ Chrome, Firefox, Safari, Edge (desktop)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)
- ✅ VS Code Simple Browser
- ✅ Any modern HTML5 browser

## 📈 Performance

- **Fast Generation**: Tables generated in milliseconds
- **Efficient Rendering**: Optimized HTML/CSS/JavaScript
- **Large Datasets**: Handles hundreds of records efficiently
- **Responsive**: Smooth interaction on all devices

## 🛠️ Troubleshooting

### Common Issues

**"Dataset not found" error:**
- Run `python dashboard_cli.py list` to see available datasets
- Check that JSON files are in the `/data` directory
- Verify JSON file formatting is correct

**Output file not generated:**
- Check file permissions in the output directory
- Ensure sufficient disk space
- Verify JSON data structure is valid

**Sorting not working:**
- Ensure JavaScript is enabled in your browser
- Check that `--sortable` option is not disabled
- Verify the HTML file loaded completely

### Getting Help
```bash
python dashboard_cli.py --help
python dashboard_cli.py list --help
python dashboard_cli.py table --help
python dashboard_cli.py dashboard --help
```

## 🎉 Success Examples

After running the CLI commands, you'll have:

1. **Professional HTML Tables**: Clean, interactive, and responsive
2. **Executive Dashboards**: Multi-section business intelligence views
3. **Mobile-Ready Output**: Works perfectly on all devices
4. **Real-Time Sorting**: Click any header to sort data instantly
5. **Production-Ready**: Secure, fast, and reliable HTML output

---

🚀 **Ready to create amazing data visualizations? Start with `python dashboard_cli.py list` to see your available data!**

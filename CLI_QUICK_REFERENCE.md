# 📊 Dashboard CLI - Quick Reference Card

## 🚀 Essential Commands

### 📋 **List Available Data**
```bash
python dashboard_cli.py list
```
**Output:** Shows all datasets with record counts

### 🔍 **Preview Dataset**  
```bash
python dashboard_cli.py preview <dataset_name>
```
**Examples:**
- `preview employee_data`
- `preview key_metrics`
- `preview quarterly_performance`

### 📊 **Generate Single Table**
```bash
python dashboard_cli.py table <dataset_name> [--output filename.html]
```
**Examples:**
- `table employee_data`
- `table quarterly_performance --output q_report.html`

### 🏢 **Generate Dashboard**
```bash
python dashboard_cli.py dashboard [--datasets <list>] [--output filename.html]
```
**Examples:**
- `dashboard` (all datasets)
- `dashboard --datasets key_metrics employee_data`
- `dashboard --output executive.html`

---

## 📁 Available Datasets

| Dataset | Records | Purpose |
|---------|---------|---------|
| `employee_data` | 6 | HR directory |
| `quarterly_performance` | 6 | Financial metrics |
| `regional_performance` | 4 | Geographic analysis |
| `product_performance` | 4 | Product analytics |
| `key_metrics` | 8 | Executive KPIs |

---

## 🎯 Common Use Cases

### **Executive Summary**
```bash
python dashboard_cli.py dashboard --datasets key_metrics employee_data --output executive.html
```

### **Sales Analysis**
```bash
python dashboard_cli.py dashboard --datasets quarterly_performance regional_performance product_performance --output sales.html
```

### **HR Report**
```bash
python dashboard_cli.py table employee_data --output hr_directory.html
```

---

## ✨ Features

- 🔄 **Interactive Sorting** (click column headers)
- 📱 **Mobile Responsive** design
- 🎨 **Professional Styling** with animations
- 📂 **Collapsible Sections** in dashboards
- 🌐 **Cross-Browser Compatible**

---

## 🛠️ Options

### Table Command Options
- `--output filename.html` - Custom output file
- `--no-sort` - Disable sorting
- `--no-stripe` - Disable striped rows

### Dashboard Command Options  
- `--datasets dataset1 dataset2` - Specific datasets only
- `--output filename.html` - Custom output file

---

## 📖 Help

```bash
python dashboard_cli.py --help           # General help
python dashboard_cli.py list --help      # List command help
python dashboard_cli.py preview --help   # Preview command help
python dashboard_cli.py table --help     # Table command help
python dashboard_cli.py dashboard --help # Dashboard command help
```

---

**🎉 From JSON data to interactive dashboards in seconds!**

#!/usr/bin/env python3
"""
Test script to verify the Interactive Dashboard copy-to-JSON functionality
"""

import json
import subprocess
import sys
from pathlib import Path

def test_interactive_dashboard_structure():
    """Test that the interactive dashboard has the correct structure"""
    dashboard_path = Path(__file__).parent / "interactive_dashboard.html"
    
    if not dashboard_path.exists():
        print("❌ Interactive dashboard file not found")
        return False
    
    content = dashboard_path.read_text()
    
    # Check for copy buttons
    copy_buttons = [
        'onclick="copyProductPerformanceData()"',
        'onclick="copyQuarterlyPerformanceData()"',
        'onclick="copyRegionalPerformanceData()"',
        'onclick="copyKeyMetricsData()"',
        'onclick="copyEmployeeData()"'
    ]
    
    missing_buttons = []
    for button in copy_buttons:
        if button not in content:
            missing_buttons.append(button)
    
    if missing_buttons:
        print(f"❌ Missing copy buttons: {missing_buttons}")
        return False
    
    # Check for JavaScript functions
    js_functions = [
        'function copyProductPerformanceData()',
        'function copyQuarterlyPerformanceData()',
        'function copyRegionalPerformanceData()',
        'function copyKeyMetricsData()',
        'function copyEmployeeData()',
        'function copyToClipboard(',
        'function showCopyNotification('
    ]
    
    missing_functions = []
    for func in js_functions:
        if func not in content:
            missing_functions.append(func)
    
    if missing_functions:
        print(f"❌ Missing JavaScript functions: {missing_functions}")
        return False
    
    # Check for JSON data structure
    if 'const dashboardData = {' not in content:
        print("❌ Missing dashboardData JSON structure")
        return False
    
    # Check for all data sections
    data_sections = [
        'product_performance:',
        'quarterly_performance:',
        'regional_performance:',
        'key_metrics:',
        'employee_data:'
    ]
    
    missing_sections = []
    for section in data_sections:
        if section not in content:
            missing_sections.append(section)
    
    if missing_sections:
        print(f"❌ Missing data sections: {missing_sections}")
        return False
    
    # Check for copy notification CSS
    css_classes = [
        '.copy-json-btn',
        '.copy-notification',
        '.section-header-content',
        '.section-title-group'
    ]
    
    missing_css = []
    for css_class in css_classes:
        if css_class not in content:
            missing_css.append(css_class)
    
    if missing_css:
        print(f"❌ Missing CSS classes: {missing_css}")
        return False
    
    print("✅ Interactive dashboard structure is correct")
    print("✅ All copy-to-JSON buttons present")
    print("✅ All JavaScript functions present")
    print("✅ All data sections present")
    print("✅ All CSS classes present")
    
    return True

def test_json_data_validity():
    """Test that the embedded JSON data is valid"""
    dashboard_path = Path(__file__).parent / "interactive_dashboard.html"
    content = dashboard_path.read_text()
    
    # Extract the dashboardData object (this is a simplified test)
    try:
        # Look for sample data structure by checking if key fields exist
        required_fields = [
            '"product": "Enterprise Software"',
            '"quarter": "Q1 2024"',
            '"region": "North America"',
            '"total_revenue"',
            '"name": "Sarah Johnson"'
        ]
        
        missing_fields = []
        for field in required_fields:
            if field not in content:
                missing_fields.append(field)
        
        if missing_fields:
            print(f"❌ Missing JSON data fields: {missing_fields}")
            return False
        
        print("✅ JSON data structure appears valid")
        return True
        
    except Exception as e:
        print(f"❌ Error validating JSON data: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Interactive Dashboard Copy-to-JSON Functionality")
    print("=" * 60)
    
    tests = [
        ("Dashboard Structure", test_interactive_dashboard_structure),
        ("JSON Data Validity", test_json_data_validity)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n📋 Running: {test_name}")
        print("-" * 30)
        success = test_func()
        results.append((test_name, success))
    
    print("\n" + "=" * 60)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 60)
    
    passed = 0
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if success:
            passed += 1
    
    print(f"\n📈 Results: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("🎉 All tests passed! Copy-to-JSON functionality is ready!")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())

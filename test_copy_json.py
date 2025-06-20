#!/usr/bin/env python3
"""
Test the JSON copy functionality by creating a simple HTML test page
"""

def create_copy_test_page():
    """Create a simple test page to verify copy-to-JSON functionality."""
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Copy-to-JSON Test</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background: #f5f7fa;
        }
        
        .test-card {
            background: white;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .copy-btn {
            background: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            margin: 10px 5px;
        }
        
        .copy-btn:hover {
            background: #45a049;
        }
        
        .json-output {
            background: #2d3748;
            color: #e2e8f0;
            padding: 15px;
            border-radius: 5px;
            font-family: monospace;
            white-space: pre-wrap;
            margin: 10px 0;
            max-height: 300px;
            overflow-y: auto;
        }
        
        .notification {
            position: fixed;
            top: 20px;
            right: 20px;
            background: #4CAF50;
            color: white;
            padding: 15px;
            border-radius: 5px;
            transform: translateX(400px);
            transition: transform 0.3s ease;
        }
        
        .notification.show {
            transform: translateX(0);
        }
    </style>
</head>
<body>
    <h1>📋 Copy-to-JSON Functionality Test</h1>
    
    <div class="test-card">
        <h3>🧪 Test the Copy Functionality</h3>
        <p>Click the buttons below to test copying different types of JSON data to your clipboard:</p>
        
        <button class="copy-btn" onclick="copyEmployeeData()">📊 Copy Employee Data</button>
        <button class="copy-btn" onclick="copyMetricsData()">📈 Copy Key Metrics</button>
        <button class="copy-btn" onclick="copyPerformanceData()">💰 Copy Performance Data</button>
        
        <div id="output" class="json-output">
            Click a button above to see the JSON data that will be copied to your clipboard...
        </div>
    </div>
    
    <div class="test-card">
        <h3>📝 Instructions</h3>
        <ol>
            <li><strong>Click any button</strong> above to copy JSON data</li>
            <li><strong>Open a text editor</strong> or JSON file</li>
            <li><strong>Paste (Ctrl+V/Cmd+V)</strong> to see the copied data</li>
            <li><strong>Save as .json file</strong> in your /data directory</li>
            <li><strong>Use with CLI tools</strong> to generate new dashboards</li>
        </ol>
    </div>

    <div id="notification" class="notification">
        ✅ JSON data copied to clipboard!
    </div>

    <script>
        const sampleData = {
            employee_data: [
                {
                    "id": "EMP001",
                    "name": "Sarah Johnson", 
                    "department": "Engineering",
                    "level": "Senior",
                    "salary": 125000,
                    "salary_formatted": "$125,000",
                    "performance": "Excellent",
                    "hire_date": "2020-03-15",
                    "location": "New York"
                },
                {
                    "id": "EMP002",
                    "name": "Mike Chen",
                    "department": "Product", 
                    "level": "Manager",
                    "salary": 135000,
                    "salary_formatted": "$135,000",
                    "performance": "Outstanding",
                    "hire_date": "2019-07-22",
                    "location": "San Francisco"
                }
            ],
            key_metrics: {
                "total_revenue": {
                    "value": 4100000,
                    "formatted": "$4.1M",
                    "description": "Total quarterly revenue",
                    "trend": "up",
                    "change": 0.14
                },
                "net_profit": {
                    "value": 820000,
                    "formatted": "$820K", 
                    "description": "Net profit after expenses",
                    "trend": "up",
                    "change": 0.12
                },
                "profit_margin": {
                    "value": 0.2,
                    "formatted": "20.0%",
                    "description": "Profit margin percentage", 
                    "trend": "stable",
                    "change": 0.01
                }
            },
            quarterly_performance: [
                {
                    "quarter": "Q1 2024",
                    "revenue": 2100000,
                    "revenue_formatted": "$2.1M",
                    "profit": 420000,
                    "profit_formatted": "$420K",
                    "growth": 0.12,
                    "growth_formatted": "+12%",
                    "customers": 1250,
                    "profit_margin": 0.2
                },
                {
                    "quarter": "Q2 2024", 
                    "revenue": 2350000,
                    "revenue_formatted": "$2.35M",
                    "profit": 470000,
                    "profit_formatted": "$470K",
                    "growth": 0.119,
                    "growth_formatted": "+11.9%",
                    "customers": 1380,
                    "profit_margin": 0.2
                }
            ]
        };

        function displayAndCopy(dataKey, dataLabel) {
            const data = sampleData[dataKey];
            const wrappedData = {};
            wrappedData[dataKey] = data;
            const jsonString = JSON.stringify(wrappedData, null, 2);
            
            // Display in output area
            document.getElementById('output').textContent = jsonString;
            
            // Copy to clipboard
            navigator.clipboard.writeText(jsonString).then(() => {
                showNotification();
            }).catch(err => {
                console.error('Failed to copy:', err);
                // Fallback for older browsers
                fallbackCopy(jsonString);
            });
        }

        function copyEmployeeData() {
            displayAndCopy('employee_data', 'Employee Data');
        }

        function copyMetricsData() {
            displayAndCopy('key_metrics', 'Key Metrics');
        }

        function copyPerformanceData() {
            displayAndCopy('quarterly_performance', 'Quarterly Performance');
        }

        function fallbackCopy(text) {
            const textArea = document.createElement("textarea");
            textArea.value = text;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            showNotification();
        }

        function showNotification() {
            const notification = document.getElementById('notification');
            notification.classList.add('show');
            setTimeout(() => {
                notification.classList.remove('show');
            }, 3000);
        }
    </script>
</body>
</html>"""

    # Save the test page
    with open('/Users/david/htmldictify/html-table-generator/copy_json_test.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ Copy-to-JSON test page created!")
    print("📁 File: copy_json_test.html")
    print("🌐 Open in browser to test the copy functionality")
    print()
    print("🧪 Test Instructions:")
    print("1. Open copy_json_test.html in your browser")
    print("2. Click any of the copy buttons")
    print("3. Paste in a text editor to verify JSON was copied")
    print("4. The same functionality is now available in demo_index.html")

if __name__ == "__main__":
    create_copy_test_page()

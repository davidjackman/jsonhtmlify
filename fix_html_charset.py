#!/usr/bin/env python3
"""
Fix UTF-8 charset declaration in HTML files
"""

import os
import re
from pathlib import Path

def fix_html_charset(file_path):
    """Add UTF-8 charset declaration to HTML file if missing."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if charset is already present
        if 'charset=' in content.lower():
            print(f"✅ {file_path.name} already has charset declaration")
            return False
        
        # Pattern to match <head> tag
        head_pattern = r'(<head[^>]*>)'
        
        # Replace <head> with <head> + charset
        def add_charset(match):
            head_tag = match.group(1)
            return f'{head_tag}\n<meta charset="UTF-8">'
        
        new_content = re.sub(head_pattern, add_charset, content, flags=re.IGNORECASE)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"🔧 Fixed {file_path.name}")
            return True
        else:
            print(f"⚠️  Could not fix {file_path.name} - no <head> tag found")
            return False
            
    except Exception as e:
        print(f"❌ Error fixing {file_path.name}: {e}")
        return False

def main():
    """Fix charset in all HTML files."""
    current_dir = Path('.')
    html_files = list(current_dir.glob('*.html'))
    
    print(f"🔍 Found {len(html_files)} HTML files")
    print("=" * 50)
    
    fixed_count = 0
    for html_file in html_files:
        if fix_html_charset(html_file):
            fixed_count += 1
    
    print("=" * 50)
    print(f"✨ Fixed {fixed_count} HTML files")
    print("🎉 All HTML files now have proper UTF-8 charset declarations!")

if __name__ == "__main__":
    main()

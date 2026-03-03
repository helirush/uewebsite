#!/usr/bin/env python3
"""
Update 480V Percentage in Portal HTML
Extracts 480V site percentage from Energy Summary markdown and updates index.html
"""

import re
import sys
from pathlib import Path


def extract_480v_percentage(md_file_path):
    """
    Extract 480V site percentage from Energy Summary markdown file.
    
    Looks for the TOTALS line in the Billing Comparison Summary section.
    Format: TOTALS | ... | 79.6% | ...
    
    Args:
        md_file_path: Path to the Energy Summary markdown file
        
    Returns:
        float: The 480V percentage (e.g., 79.6)
        
    Raises:
        FileNotFoundError: If the markdown file doesn't exist
        ValueError: If the percentage cannot be extracted
    """
    try:
        with open(md_file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Energy Summary markdown not found: {md_file_path}")
    
    # Look for the TOTALS line in the Billing Comparison Summary section
    # Handles both pipe-delimited tables and space-separated formats
    # Pattern: TOTALS ... | ... | XX.X% | ...
    totals_pattern = r'TOTALS\s+\|\s+[\d,]+\s+\|\s+[\d,]+\s+\|\s+[\d,]+\s+\|\s+([\d.]+)%'
    
    match = re.search(totals_pattern, content)
    if match:
        percentage = float(match.group(1))
        return percentage
    
    # If pipe format doesn't work, try more flexible pattern
    # Look for "Measured 480V Fields" section which has explicit percentage
    alt_pattern = r'Measured 480V Fields \(4 transformers\):[^(]*\(([\d.]+)%\)'
    match = re.search(alt_pattern, content)
    if match:
        percentage = float(match.group(1))
        return percentage
    
    raise ValueError(f"Could not extract 480V percentage from {md_file_path}")


def update_html_percentage(html_file_path, new_percentage):
    """
    Update the 480V percentage in the index.html file.
    
    Updates the middle highlight card text from "4 - 480v account for X% site"
    to the new percentage value.
    
    Args:
        html_file_path: Path to the index.html file
        new_percentage: The new percentage to insert
        
    Returns:
        bool: True if update was successful, False otherwise
    """
    try:
        with open(html_file_path, 'r') as f:
            html_content = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"HTML file not found: {html_file_path}")
    
    # Pattern to find and replace the 480V percentage text
    # Matches: "4 - 480v account for XX.X% site"
    pattern = r'(4 - 480v account for )[\d.]+(%)'
    replacement = rf'\g<1>{new_percentage}\g<2>'
    
    updated_content = re.sub(pattern, replacement, html_content)
    
    # Check if replacement was made
    if updated_content == html_content:
        raise ValueError(f"Could not find pattern to update in {html_file_path}")
    
    # Write the updated content back
    with open(html_file_path, 'w') as f:
        f.write(updated_content)
    
    return True


def main():
    """Main entry point for the script."""
    
    # Default paths - can be customized
    if len(sys.argv) > 2:
        md_file = sys.argv[1]
        html_file = sys.argv[2]
    elif len(sys.argv) > 1:
        md_file = sys.argv[1]
        html_file = Path(md_file).parent.parent.parent / "cherryave" / "index.html"
    else:
        # Auto-detect based on typical directory structure
        # Assumes script is run from study directory or with explicit paths
        print("Usage: python update_480v_percentage.py <energy_summary.md> [index.html]")
        print("\nExample:")
        print("  python update_480v_percentage.py SITE-FosterFarms-EnergySummary_CherryAve-4_1minRES_oct2025.md")
        sys.exit(1)
    
    try:
        # Extract percentage from markdown
        percentage = extract_480v_percentage(md_file)
        print(f"✓ Extracted 480V percentage: {percentage}%")
        
        # Update HTML
        update_html_percentage(str(html_file), percentage)
        print(f"✓ Updated {html_file} with {percentage}%")
        print(f"\n✅ Success! Portal updated with current 480V site percentage.")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

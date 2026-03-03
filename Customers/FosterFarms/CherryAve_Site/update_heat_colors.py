#!/usr/bin/env python3
"""Apply toned-down professional colors to heat board files."""

import re

files = [
    'SplitView-heat-T12.Main-251001-251031.html',
    'SplitView-heat-T15.Fillet-251001-251031.html',
    'SplitView-heat-T16.Compressor-251001-251031.html'
]

# Color replacements - from bright to muted
replacements = [
    # Border colors - yellow to amber
    ('border-bottom: 2px solid rgb(249, 215, 11)', 'border-bottom: 2px solid #c27803'),
    ('border-right: 4px solid rgb(249, 215, 11)', 'border-right: 4px solid #c27803'),
    
    # Header title - bright orange to muted orange
    ('color: rgb(255, 140, 60)', 'color: #d9894a'),
    
    # Back button gradients - bright to muted
    ('background: linear-gradient(135deg, #ff6b35 0%, #d9534f 100%)', 
     'background: linear-gradient(135deg, #c85a28 0%, #a84532 100%)'),
    ('background: linear-gradient(135deg, #ff8c3c 0%, #e66060 100%)', 
     'background: linear-gradient(135deg, #d96b38 0%, #b85542 100%)'),
    
    # Shadow colors
    ('box-shadow: 0 2px 8px rgba(255, 107, 53, 0.3)', 
     'box-shadow: 0 2px 8px rgba(200, 90, 40, 0.3)'),
    ('box-shadow: 0 4px 12px rgba(255, 107, 53, 0.5)', 
     'box-shadow: 0 4px 12px rgba(200, 90, 40, 0.5)'),
    
    # Resize handle hover
    ('background: #ff6b35', 'background: #c85a28'),
]

for filename in files:
    filepath = f'/Users/mdhowell/eestream/eBehavior/Reports/Study260106r0/FosterFarms/CherryAve_Site/{filename}'
    
    print(f'Processing {filename}...')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply all replacements
    for old_text, new_text in replacements:
        content = content.replace(old_text, new_text)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'  ✓ Updated {filename}')

print('\nAll heat board files updated with toned-down professional colors!')

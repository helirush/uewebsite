#!/usr/bin/env python3
"""Update fluorescent green colors to Unity green theme in energy board files."""

import re

# Files to update
files = [
    'SplitView-energy-T12.Main-251001-251031.html',
    'SplitView-energy-T15.Fillet-251001-251031.html',
    'SplitView-energy-T16.Compressor-251001-251031.html'
]

# Color replacements
replacements = [
    ('#00ff7f', '#B2D235'),  # Spring green to Unity lime green
    ('#00cc66', '#5D701A'),  # Bright green to Unity dark green
    ('#009944', '#4a5a15'),  # Dark green to Unity darker green
    ('#00e673', '#6d8520'),  # Bright green hover to Unity lighter green
    ('#00b359', '#5D701A'),  # Green hover to Unity dark green
    ('rgba(0, 204, 102,', 'rgba(93, 112, 26,'),  # Shadow color
    ('#00ff00', '#B2D235'),  # Pure green to Unity lime green
    ('#7fffd4', '#8fa832'),  # Aquamarine to Unity muted green
]

for filename in files:
    filepath = f'/Users/mdhowell/eestream/eBehavior/Reports/Study260106r0/FosterFarms/CherryAve_Site/{filename}'
    
    print(f'Processing {filename}...')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply all color replacements
    for old_color, new_color in replacements:
        content = content.replace(old_color, new_color)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'  ✓ Updated {filename}')

print('\nAll energy board files updated with Unity green theme!')

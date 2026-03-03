#!/usr/bin/env python3
"""Update Full Size button colors from green to red/orange theme in heat board files."""

# Files to update
files = [
    'SplitView-heat-T12.Main-251001-251031.html',
    'SplitView-heat-T15.Fillet-251001-251031.html',
    'SplitView-heat-T16.Compressor-251001-251031.html'
]

# Color replacements for Full Size buttons
replacements = [
    # Full Size button backgrounds
    ('background: linear-gradient(135deg, #5D701A 0%, #4a5a15 100%)', 
     'background: linear-gradient(135deg, #ff6b35 0%, #d9534f 100%)'),
    
    # Full Size button hover backgrounds
    ('background: linear-gradient(135deg, #6d8520 0%, #5D701A 100%)', 
     'background: linear-gradient(135deg, #ff8c3c 0%, #e66060 100%)'),
    
    # Full Size button shadows
    ('box-shadow: 0 2px 8px rgba(93, 112, 26, 0.3)', 
     'box-shadow: 0 2px 8px rgba(255, 107, 53, 0.3)'),
    
    ('box-shadow: 0 4px 12px rgba(93, 112, 26, 0.5)', 
     'box-shadow: 0 4px 12px rgba(255, 107, 53, 0.5)'),
    
    # Resize handle hover (in context of .resize-handle:hover only)
    # This needs to be done carefully to not affect other elements
]

for filename in files:
    filepath = f'/Users/mdhowell/eestream/eBehavior/Reports/Study260106r0/FosterFarms/CherryAve_Site/{filename}'
    
    print(f'Processing {filename}...')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply replacements
    for old_text, new_text in replacements:
        content = content.replace(old_text, new_text)
    
    # Special handling for resize-handle hover - need to find and replace in context
    # Find .resize-handle:hover block and replace the green color
    import re
    content = re.sub(
        r'(\.resize-handle:hover\s*{[^}]*background:\s*)#5D701A',
        r'\1#ff6b35',
        content
    )
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'  ✓ Updated {filename}')

print('\nAll heat board Full Size buttons updated to red/orange theme!')

#!/usr/bin/env python3
"""Update SplitView files to add pattern image container at top (Cherry Ave standard)."""

import re
import os

# Files to update and their corresponding image patterns
SPLITVIEW_FILES = {
    'SplitView-energy-Rendering-2-260201-260228.html': ('Rend2b_feb26.png', 'Rendering-2', 'ENERGY'),
    'SplitView-energy-Rendering-3-260201-260228.html': ('Rend3b_feb26.png', 'Rendering-3', 'ENERGY'),
    'SplitView-heat-Rendering-1-260201-260228.html': ('Rend1b_feb26.png', 'Rendering-1', 'HEAT'),
    'SplitView-heat-Rendering-2-260201-260228.html': ('Rend2b_feb26.png', 'Rendering-2', 'HEAT'),
    'SplitView-heat-Rendering-3-260201-260228.html': ('Rend3b_feb26.png', 'Rendering-3', 'HEAT'),
    'SplitView-volt-Rendering-1-260201-260228.html': ('Rend1v_feb26.png', 'Rendering-1', 'VOLTAGE'),
    'SplitView-volt-Rendering-2-260201-260228.html': ('Rend2v_feb26.png', 'Rendering-2', 'VOLTAGE'),
    'SplitView-volt-Rendering-3-260201-260228.html': ('Rend3v_feb26.png', 'Rendering-3', 'VOLTAGE'),
}

# CSS to add for pattern image container
CSS_ADDITION = '''
        .pattern-image-container {
            text-align: center;
            padding: 20px;
            background: #0f1629;
            border-bottom: 4px solid #6f880bff;
            flex-shrink: 0;
            width: 100%;
            height: 350px;
            overflow: auto;
            position: relative;
        }

        .pattern-image-container img {
            width: 95%;
            max-width: 95%;
            height: auto;
            border: 2px solid #5D701A;
            border-radius: 8px;
            object-fit: contain;
            cursor: pointer;
        }

        .pattern-image-container p {
            color: #888;
            font-size: 12px;
            margin-top: 8px;
        }

        .fullsize-btn {
            position: absolute;
            top: 10px;
            right: 20px;
            left: auto;
            transform: none;
            background: linear-gradient(135deg, #5D701A 0%, #4a5a15 100%);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 6px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(93, 112, 26, 0.3);
            z-index: 10;
            margin: 0;
        }

        .fullsize-btn:hover {
            background: linear-gradient(135deg, #6d8520 0%, #5D701A 100%);
            box-shadow: 0 4px 12px rgba(93, 112, 26, 0.5);
            transform: translateY(-1px);
        }

        .image-fullscreen-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(10, 14, 39, 0.98);
            z-index: 9999;
            overflow: auto;
        }

        .image-fullscreen-overlay.active {
            display: block;
        }

        .fullscreen-content {
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 60px 40px 40px 40px;
        }

        .fullscreen-content img {
            max-width: 95%;
            max-height: 90vh;
            object-fit: contain;
            border: 2px solid #5D701A;
            border-radius: 8px;
        }

        .fullscreen-content p {
            color: #888;
            font-size: 14px;
            margin-top: 15px;
        }

        .bottom-section {
            display: flex;
            flex: 1;
            overflow: hidden;
        }
'''

# JavaScript functions to add
JS_ADDITION = '''
        function showFullscreen() {
            document.getElementById('imageFullscreenOverlay').classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeFullscreen() {
            document.getElementById('imageFullscreenOverlay').classList.remove('active');
            document.body.style.overflow = '';
        }

        // Close fullscreen on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                closeFullscreen();
                closeMarkdownFullscreen();
                closeDashboardFullscreen();
            }
        });

'''


def update_splitview(filepath, image_name, transformer_name, view_type):
    """Update a single SplitView file."""
    print(f"Processing {filepath}...")
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # 1. Update .split-container to be flex-direction: column
    content = re.sub(
        r'(\.split-container \{)\s*\n\s*display: flex;\s*\n\s*height: calc\(100vh - 50px\);',
        r'\1\n            display: flex;\n            flex-direction: column;\n            height: calc(100vh - 50px);',
        content
    )
    
    # 2. Add CSS for pattern image container (before .markdown-pane)
    content = re.sub(
        r'(\s+\.markdown-pane \{)',
        CSS_ADDITION + r'\n        .markdown-pane {',
        content,
        count=1
    )
    
    # 3. Add pattern image container and bottom-section wrapper in body
    pattern_html = f'''    <div class="split-container">
        <div class="pattern-image-container">
            <button class="fullsize-btn" onclick="showFullscreen()" title="View full size">🔍 Full Size</button>
            <img src="Patterns/{image_name}" alt="{transformer_name} - {view_type} Pattern" onclick="showFullscreen()">
            <p>{transformer_name} - {view_type} Pattern</p>
        </div>
        <div class="bottom-section">
        <div class="markdown-pane">'''
    
    content = re.sub(
        r'<div class="split-container">\s*\n\s*<div class="markdown-pane">',
        pattern_html,
        content,
        count=1
    )
    
    # 4. Close bottom-section div and add image fullscreen overlay before markdown overlay
    image_overlay = f'''        </div>
        </div>
    </div>

    <!-- Fullscreen Image Overlay -->
    <div class="image-fullscreen-overlay" id="imageFullscreenOverlay">
        <button class="close-fullscreen-btn" onclick="closeFullscreen()">✕ Return to Split View</button>
        <div class="fullscreen-content">
            <img src="Patterns/{image_name}" alt="Pattern Analysis">
            <p>{transformer_name} - {view_type} Pattern</p>
        </div>
    </div>    
    <!-- Markdown Fullscreen Overlay -->'''
    
    content = re.sub(
        r'(\s+</div>\s*\n\s+</div>\s*\n\s+</div>)\s*\n\s*<!-- Markdown Fullscreen Overlay -->',
        image_overlay,
        content,
        count=1
    )
    
    # 5. Add JavaScript functions after hideDashboardIfMissing
    content = re.sub(
        r'(\}\)\(\);)\s*\n\s*(function goBack\(\))',
        r'\1\n' + JS_ADDITION + r'        \2',
        content,
        count=1
    )
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"  ✓ Updated {filepath}")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    for filename, (image_name, transformer_name, view_type) in SPLITVIEW_FILES.items():
        filepath = os.path.join(script_dir, filename)
        if os.path.exists(filepath):
            update_splitview(filepath, image_name, transformer_name, view_type)
        else:
            print(f"  ⚠ File not found: {filepath}")
    
    print("\nDone!")


if __name__ == '__main__':
    main()

# Unity Energy - Standardized Color Palette
**Maxwell Library Reference**  
*Last Updated: January 19, 2026*

---

## 🎨 Unity Core Brand Colors

### Primary Unity Green
- **Dark Green**: `#5D701A` - Primary brand color
- **Olive Green**: `#4a5a15` - Darker shade for gradients
- **Light Green**: `#6d8520` - Lighter shade for hover states
- **Lime Green**: `#B2D235` - Accent highlights

### Gradients
- **Button Background**: `linear-gradient(135deg, #5D701A 0%, #4a5a15 100%)`
- **Button Hover**: `linear-gradient(135deg, #6d8520 0%, #5D701A 100%)`

### Shadows
- **Standard**: `rgba(93, 112, 26, 0.3)`
- **Hover**: `rgba(93, 112, 26, 0.5)`

---

## ⚡ Voltage Board Colors

### Primary Colors
- **Header Title**: `#B2D235` (Unity Lime Green)
- **Borders**: `#5D701A` (Unity Dark Green)
- **Section Dividers**: `#2a3f5f` (Slate Blue)

### Buttons
- **Background**: `linear-gradient(135deg, #5D701A 0%, #4a5a15 100%)`
- **Hover**: `linear-gradient(135deg, #6d8520 0%, #5D701A 100%)`
- **Shadow**: `rgba(93, 112, 26, 0.3)`
- **Shadow Hover**: `rgba(93, 112, 26, 0.5)`

### Typography
- **H1 (Page Title)**: `rgb(249, 215, 11)` - Yellow
- **H2 (Sections)**: `#B2D235` - Unity Lime Green
- **H3 (Subsections)**: `#8fa832` - Muted Green
- **Body Text**: `#b0b0b0` - Light Gray
- **Code**: `#B2D235` - Unity Lime Green
- **Strong/Bold**: `#B2D235` - Unity Lime Green

### Resize Handle
- **Default**: `#2a3f5f`
- **Hover**: `#5D701A`

---

## 🔋 Energy Board Colors

### Primary Colors
- **Header Title**: `#B2D235` (Unity Lime Green)
- **Borders**: `#B2D235` (Unity Lime Green)
- **Section Dividers**: `#2a3f5f` (Slate Blue)

### Buttons
- **Background**: `linear-gradient(135deg, #5D701A 0%, #4a5a15 100%)`
- **Hover**: `linear-gradient(135deg, #6d8520 0%, #5D701A 100%)`
- **Shadow**: `rgba(93, 112, 26, 0.3)`
- **Shadow Hover**: `rgba(93, 112, 26, 0.5)`

### Typography
- **H1 (Page Title)**: `rgb(249, 215, 11)` - Yellow
- **H2 (Sections)**: `#B2D235` - Unity Lime Green
- **H3 (Subsections)**: `#8fa832` - Muted Green
- **Body Text**: `#b0b0b0` - Light Gray
- **Code**: `#B2D235` - Unity Lime Green
- **Strong/Bold**: `#B2D235` - Unity Lime Green

### Resize Handle
- **Default**: `#2a3f5f`
- **Hover**: `#5D701A`

---

## 🔥 Heat Board Colors

### Primary Colors
- **Header Title**: `#d9894a` - Muted Orange
- **Borders**: `#c27803` - Amber
- **Section Dividers**: `#2a3f5f` (Slate Blue)

### Buttons
- **Background**: `linear-gradient(135deg, #c85a28 0%, #a84532 100%)`
- **Hover**: `linear-gradient(135deg, #d96b38 0%, #b85542 100%)`
- **Shadow**: `rgba(200, 90, 40, 0.3)`
- **Shadow Hover**: `rgba(200, 90, 40, 0.5)`

### Typography
- **H1 (Page Title)**: `rgb(249, 215, 11)` - Yellow
- **H2 (Sections)**: `rgb(255, 140, 60)` - Orange
- **H3 (Subsections)**: `rgb(255, 180, 100)` - Light Orange
- **Body Text**: `#b0b0b0` - Light Gray
- **Code**: `rgb(255, 100, 0)` - Bright Orange
- **Strong/Bold**: `rgb(255, 140, 60)` - Orange

### Resize Handle
- **Default**: `#2a3f5f`
- **Hover**: `#c85a28`

---

## 📊 Summary Board Colors

### Gauges & Cards
- **Border**: `rgba(178, 210, 53, 1)` - Unity Lime Green
- **Background Gradient**: `linear-gradient(145deg, rgba(42, 47, 62, 1), rgba(31, 36, 51, 1))`
- **Card Hover Border**: `#B2D235` (Unity Light Green)

### Buttons
- **Pattern Buttons**: Unity green with left accent border
  - Background: `linear-gradient(135deg, rgba(93, 112, 26, 0.2), rgba(93, 112, 26, 0.1))`
  - Border: `1px solid #5D701A`
  - Left Border: `3px solid #B2D235`
  - Hover Background: `linear-gradient(135deg, rgba(93, 112, 26, 0.3), rgba(93, 112, 26, 0.2))`

---

## 🎯 Common Dark Theme Background Colors

### Base Colors
- **Page Background**: `#0a0e27` - Deep Navy
- **Panel Background**: `#0f1629` - Navy
- **Header Background**: `linear-gradient(135deg, #1a1f3a 0%, #0d1128 100%)`
- **Card/Modal Background**: `#2d3748` - Slate Gray
- **Code Background**: `#1a1f3a` - Dark Blue

### Neutrals
- **Text Primary**: `#e0e0e0` - Off White
- **Text Secondary**: `#b0b0b0` - Light Gray
- **Text Muted**: `#90a4ae` - Blue Gray
- **Divider Lines**: `#2a3f5f` - Slate Blue

---

## 💡 Usage Guidelines

### Board Type Selection
- **Voltage Analysis**: Use Voltage Board Colors (Unity Green theme)
- **Energy Analysis**: Use Energy Board Colors (Unity Green theme)
- **Heat Analysis**: Use Heat Board Colors (Amber/Orange theme)
- **Site Summary/Dashboard**: Use Summary Board Colors (Unity Green with variance)

### Consistency Rules
1. **Full Size Buttons**: Always match the board type colors
2. **Back Buttons**: Always match the board type colors
3. **Borders**: Match the board type primary color
4. **Hover States**: Use lighter/brighter shade of base color
5. **Shadows**: Use rgba with board type base color at 0.3 opacity

### Accessibility
- All color combinations maintain WCAG AA contrast ratios
- Buttons use gradients for depth and visual hierarchy
- Hover states provide clear visual feedback

---

## 📝 Implementation Notes

### CSS Variables (Recommended)
```css
:root {
  /* Unity Core */
  --unity-green: #5D701A;
  --unity-green-dark: #4a5a15;
  --unity-green-light: #6d8520;
  --unity-lime: #B2D235;
  
  /* Heat Theme */
  --heat-orange: #d9894a;
  --heat-amber: #c27803;
  --heat-button: #c85a28;
  --heat-button-dark: #a84532;
  
  /* Common */
  --bg-dark: #0a0e27;
  --bg-panel: #0f1629;
  --text-primary: #e0e0e0;
  --text-secondary: #b0b0b0;
}
```

### Color Picker Quick Reference
| Color Name | Hex Code | RGB | Use Case |
|------------|----------|-----|----------|
| Unity Green | `#5D701A` | `rgb(93, 112, 26)` | Primary brand, voltage, energy |
| Unity Lime | `#B2D235` | `rgb(178, 210, 53)` | Accents, highlights |
| Heat Amber | `#c27803` | `rgb(194, 120, 3)` | Heat board borders |
| Heat Orange | `#c85a28` | `rgb(200, 90, 40)` | Heat board buttons |

---

*This palette ensures consistent branding across all Unity Energy dashboards and analysis tools.*

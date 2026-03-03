#!/usr/bin/env python3
"""
AI Pattern Analyzer for Unity Energy Field Baseline Images

This module uses Claude AI to automatically analyze baseline energy field images
and generate natural language pattern interpretations for plant managers.

Analyzes:
- Daily production cycles and target performance
- Energy per bird efficiency metrics
- Cost per bird trends
- Overperformance and underperformance periods
- Business context and operational intelligence
"""

import os
import sys
import json
import base64
from pathlib import Path
from datetime import datetime

# Add dashboard directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pattern_analysis_manager import PatternAnalysisManager

# Try to import anthropic for Claude API
try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("⚠️  anthropic package not installed. Run: pip install anthropic")


def encode_image_to_base64(image_path):
    """Encode image file to base64 string for Claude API."""
    with open(image_path, 'rb') as f:
        return base64.standard_b64encode(f.read()).decode('utf-8')


def get_image_media_type(image_path):
    """Determine media type from image extension."""
    ext = Path(image_path).suffix.lower()
    media_types = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.webp': 'image/webp'
    }
    return media_types.get(ext, 'image/png')


def analyze_baseline_image_with_ai(image_path, transformer_info=None, production_target=975000):
    """
    Use Claude AI to analyze a baseline energy field image.
    
    Args:
        image_path: Path to baseline pattern image
        transformer_info: Dict with transformer metadata (name, metrics, etc.)
        production_target: Weekly production target (default 975,000 birds/week for Foster Farms)
    
    Returns:
        dict: Analysis results with pattern_text, confidence, metrics
    """
    if not ANTHROPIC_AVAILABLE:
        return {
            "success": False,
            "error": "Anthropic package not available",
            "pattern_text": "Pattern analysis pending - AI module not configured"
        }
    
    # Get API key from environment
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        return {
            "success": False,
            "error": "ANTHROPIC_API_KEY not set in environment",
            "pattern_text": "Pattern analysis pending - API key not configured"
        }
    
    try:
        # Encode image
        image_data = encode_image_to_base64(image_path)
        media_type = get_image_media_type(image_path)
        
        # Build analysis prompt
        xfmr_name = transformer_info.get('name', 'Unknown') if transformer_info else 'Unknown'
        energy_per_bird = transformer_info.get('energy_per_bird', 'N/A') if transformer_info else 'N/A'
        cost_per_bird = transformer_info.get('cost_per_bird', 'N/A') if transformer_info else 'N/A'
        uptime_pct = transformer_info.get('uptime_pct', 'N/A') if transformer_info else 'N/A'
        tmax_supply = transformer_info.get('tmax_supply', None) if transformer_info else None
        target_validated = transformer_info.get('target_validated', tmax_supply) if transformer_info else None
        target_confidence = transformer_info.get('target_confidence', 'UNKNOWN') if transformer_info else 'UNKNOWN'
        target_note = transformer_info.get('target_validation_note', '') if transformer_info else ''
        
        # Build target baseline text with validation info
        if target_validated:
            if target_confidence == "HIGH":
                target_text = f" - CALCULATED FROM CSV DATA\n- **Target Baseline**: {target_validated:.2f} kVA (VALIDATED - {target_note})\n- This is your ZERO LINE for performance evaluation"
            elif target_confidence == "ADJUSTED_DOWN":
                target_text = f" - CALCULATED FROM CSV DATA\n- **Original tMAX**: {tmax_supply:.2f} kVA (95th percentile)\n- **Adjusted Target**: {target_validated:.2f} kVA (VALIDATED - {target_note})\n- This adjusted target is your ZERO LINE - most days operate at this level"
            else:
                target_text = f" - CALCULATED FROM CSV DATA\n- **Target Baseline**: {target_validated:.2f} kVA ({target_confidence} - {target_note})\n- This is your ZERO LINE for performance evaluation"
        else:
            target_text = ""
        
        prompt = f"""Analyze this Unity Energy baseline pattern image for {xfmr_name}.

CONTEXT:
- Production Target: {production_target:,} birds/week
- Current Metrics: {uptime_pct}% uptime, {energy_per_bird} kWh/bird, ${cost_per_bird}/bird{target_text}
- Timeline: 31 days of January 2025 (250101-250131) at 1-minute resolution
- X-axis progresses left-to-right showing the full month

CHART VISUAL ELEMENTS:
The chart displays stacked area layers showing energy flow:
- **Dark Blue (top)**: Supplied power (kVA) from utility - total apparent power delivered
- **Light Blue (middle)**: Consumed power (kW) - actual productive work being done
- **Green (bottom)**: Reactive/Unconsumed energy (kVAR) - wasted reactive power
- **Orange line (%)**: Power Factor - efficiency of power usage (higher = better)
- **Horizontal dashed line**: Target production baseline

CRITICAL UNDERSTANDING - READING THE ENERGY FIELD:

**HEIGHT = LOAD (NOT DURATION)**
- Taller patterns = higher load (more production demand)
- Shorter patterns = lower load (reduced production)
- Same height = same load level
- A day can run FULL DURATION but at HALF LOAD = half the visual height

**THE 44,640 SLICES**: You're viewing 1-minute resolution across the full month (44,640 data points)

**ENERGY PHYSICS - Understanding the Three Layers:**
- **DARK BLUE (top)**: Supplied power (kVA) - total apparent power DELIVERED from utility
- **LIGHT BLUE (middle)**: Consumed power (kW) - actual PRODUCTIVE WORK (motors, lights, equipment)
- **GREEN (bottom)**: Reactive/Unconsumed power (kVAR) - the WASTE
  - Dark blue TRIES to convert into light blue
  - Due to inefficiencies (motors, inductance), it CAN'T convert all of it
  - What DOESN'T GET CONVERTED = green reactive waste
  - Formula: Dark Blue - Light Blue = Green

**POWER FACTOR (Orange Line) = CONVERSION EFFICIENCY:**
- Shows what % of dark blue successfully converts to light blue
- Example: 86.8% PF = 86.8% of supply becomes productive work, 13.2% becomes waste
- **Smooth orange line** = stable, healthy efficiency
- **Drops in orange line** = efficiency problems, bad energy quality
- **Rapid oscillations/spikes** = possible VFD overreaction, control system issues, or strong negative field draw

**VISUAL INTERPRETATION METHOD:**
As you scan left-to-right across the 31 days:
1. **HEIGHT = LOAD**: Taller = more production demand, not longer hours
2. **FIND THE TARGET**: Identify 15-20 days with SIMILAR patterns (same height, shape, green/blue layers)
   - These consistent days = "healthy/normal" production = YOUR TARGET
   - This is NOT a fixed line - it's derived from visual consistency
3. **COMPARE TO TARGET**: Every other day is above/below this derived target
4. **WEEKLY PATTERNS**: Most sites run Mon-Fri with half-day Saturday
5. **FIND THE BEST WEEK**: Identify the most stable, consistent week = establish weekly target
6. **COMPARE ALL WEEKS**: Rate other weeks against the best week (e.g., "Week 2 ran 40-50% below Week 3 target")
7. **SATURDAY ANALYSIS**: Critical for performance - note full day vs half day vs minimal
8. **ANOMALIES TO FLAG**:
   - Thin, sharp spikes (weekend anomalies)
   - Vertical gaps/streaks (power outages)
   - Orange line oscillations (equipment control issues)
   - Startup struggles (slow ramp-ups)
   - Mid-day crashes (sudden drops)
9. **GREEN LAYER**: Thicker = more waste, thinner = better efficiency
10. **OPERATIONAL STORY**: Describe what happened day-by-day, week-by-week

ANALYSIS REQUIREMENTS - BE SPECIFIC:

STEP 1: USE THE PROVIDED VALIDATED TARGET (Critical First Step)
- **USE THE TARGET BASELINE VALUE PROVIDED ABOVE** - this has been calculated AND VALIDATED from CSV data
- If confidence is HIGH: Most weekdays hit this target (majority validation)
- If ADJUSTED_DOWN: The 95th percentile was too high; target was lowered to where majority actually operates
- This validated target is your ZERO LINE for performance evaluation:
  - Days AT this line = on target (normal production)
  - Days ABOVE this line = overperforming / over-production  
  - Days BELOW this line = underperforming / reduced production
- Scan the chart and identify which days hit, exceed, or fall short of this validated target
- Example: "Target baseline is 1562 kVA (validated - 18/22 weekdays hit target). Most weekdays operate at this level, showing consistent on-target performance."

STEP 2: IDENTIFY THE BEST WEEK (Weekly Benchmark)
- Compare all 4-5 weeks visually
- State which week is MOST STABLE and CONSISTENT
- Example: "Week 3 (Jan 13-19) is the most stable with all 5 weekdays matching"
- This becomes your WEEKLY TARGET for comparisons

STEP 3: WEEK-BY-WEEK ANALYSIS (Compare to Best Week)
- Week 1: Describe patterns, compare to best week ("20% below Week 3 target")
- Week 2: Same approach with percentage estimate
- Week 3 (or best week): Note stability, consistency
- Week 4: Compare and estimate percentage
- Week 5 (if applicable): Final week assessment

STEP 4: SATURDAY ANALYSIS (Critical for Performance)
- Jan 4 (1st Sat): Full day / Half day / Minimal / Off - describe load level
- Jan 11 (2nd Sat): Same analysis
- Jan 18 (3rd Sat): Same analysis  
- Jan 25 (4th Sat): Same analysis
- Impact: "Saturday production boosted monthly performance by X%"

STEP 5: APPLY ORANGE LINE DIAGNOSTIC RULES (Critical - Use All 5 Rules)

When analyzing the orange power factor line, systematically check for ALL 5 diagnostic rules:

1. **SCAN for FULL COLLAPSES** (Rule 1): Look for orange line dropping completely to 0%. If found, measure gap width to quantify outage duration.
2. **SCAN for DIPS** (Rule 2): Look for orange line dropping to 60-80% range without full collapse. Note timing and duration.
3. **SCAN for GREEN SPIKES** (Rule 3): Look for sharp, thin protrusions in green layer (KVAR spikes). Count frequency and timing.
4. **SCAN for NO GAP** (Rule 4): Look for periods where dark blue and light blue layers align tightly with minimal green waste. Identify which dates show this.
5. **SCAN for STANDARD BLOCKS** (Rule 5): Look for repeating 18-hour blocks followed by valleys. These are your baseline healthy operation days.

**In your analysis narrative, explicitly reference which rules you observed:**
- "Rule 1 detected: [if applicable, describe power outage]"
- "Rule 2 detected: [if applicable, describe equipment stress events]"
- "Rule 3 detected: [if applicable, describe KVAR spikes and frequency]"
- "Rule 4 detected: [if applicable, describe 24/7 saturation periods]"
- "Rule 5 detected: [if applicable, describe standard operating blocks]"

If a rule is NOT observed, state: "Rule X: No events detected during analysis period."

STEP 6: FLAG SPECIFIC ANOMALIES (Be Exact - CRITICAL FOR COST ANALYSIS)

**CATEGORIZE SPIKES BY TYPE AND FINANCIAL IMPACT:**

**A. DEMAND CHARGE SPIKES ($$$ - HIGHEST PRIORITY):**
- Look for the HIGHEST peaks of entire month (often during elevated production periods)
- These trigger utility demand charges = thousands of dollars in penalties
- Example: "Jan 23-24 show peak demand spikes reaching 1500 kVA during elevated 1250 kVA baseline operation - HIGHEST peaks of month. These spikes likely triggered demand charge penalties costing $XXX. Recommend load management during high production periods."
- Pattern: Usually during weekdays when already running hot + additional equipment starts
- Impact: Maximum monthly demand charge based on single highest 15-minute interval

**B. WEEKEND ANOMALY SPIKES ($ - MODERATE PRIORITY):**
- Thin, needle-like spikes during shutdown periods (Saturday night/Sunday morning)
- Equipment startup tests, cleaning cycles, refrigeration surges
- Example: "Jan 4-5 and Jan 18-19 show thin spikes to ~1400 kVA during weekend shutdown - likely equipment startup/test cycles. Wasteful but lower financial impact than demand spikes."
- Pattern: Isolated, sharp, brief duration during otherwise-off periods
- Impact: Energy waste, but doesn't set monthly demand

**C. POWER INTERRUPTIONS (OPERATIONAL - HIGH PRIORITY):**
- Vertical gaps, streaks, or lines cutting through pattern
- Power outages, equipment failures, breaker trips
- Example: "Jan 16 shows vertical gap mid-day - power interruption occurred. Jan 28-29 shows brief vertical stripe - momentary power loss or equipment restart."
- Pattern: Visible as vertical lines or gaps in the energy field
- Impact: Production loss, equipment damage risk, revenue loss

|**D. POWER FACTOR DIAGNOSTIC ANALYSIS (ORANGE LINE INTERPRETATION - CRITICAL):**
|
|The ORANGE power factor line is a diagnostic tool revealing electrical events. Apply these 5 rules:
|
|**RULE 1: FULL ORANGE DROP TO ZERO = POWER OUTAGE**
|- Orange line completely collapses to 0% (visible as hard drop)
|- Indicates complete loss of power (utility outage or equipment disconnect)
|- Impact: Total production loss during gap. Can quantify outage duration by measuring gap width on X-axis
|- Example: "Jan 16 shows complete orange line collapse to 0% with 30-minute gap - power outage detected, ~30 min production loss"
|- Action: Investigate with utility company for grid issues or check facility breakers for trips
|
|**RULE 2: ORANGE DIP WITHOUT COLLAPSE = EQUIPMENT STRESS/LOAD REDUCTION**
|- Orange line drops to 60-80% range but doesn't fully collapse
|- Indicates temporary efficiency loss or equipment stress without complete shutdown
|- Usually coincides with sudden load reduction (light blue layer becomes thinner)
|- Impact: Temporary increased waste but equipment still operational
|- Example: "Jan 12 shows orange dip to 75% PF mid-day (without collapse) - equipment stress event, brief 2-hour duration"
|- Likely causes: Motor startup stress, VFD adjustment, compressor cycling, thermal event
|- Action: Review equipment diagnostics for stress events
|
|**RULE 3: ISOLATED SHARP KVAR SPIKES = MOTOR INRUSH / EQUIPMENT STRESS**
|- GREEN layer suddenly thickens into sharp, thin spike (KVAR spike)
|- Orange line may show micro-dip or stay stable
|- Indicates sudden reactive power demand from motor startup or equipment stress
|- Impact: Brief spike in waste energy, no production loss
|- Example: "Jan 8 shows isolated KVAR spike at 14:00 (sharp green spike, 5-min duration) - motor inrush event detected"
|- Pattern: Appears as thin, isolated needle-like protrusion in green layer
|- Action: These are normal for industrial equipment, monitor frequency
|
|**RULE 4: NO GAP BETWEEN DARK BLUE AND LIGHT BLUE = 24/7 SATURATION**
|- Dark blue (supply) and light blue (consumed) layers align closely with minimal gap
|- Green layer (waste) becomes very thin or nearly invisible
|- Indicates facility running at maximum efficiency 24 hours (no shutdown periods)
|- Impact: Highest possible efficiency but indicates non-stop operation
|- Example: "Jan 13-14 shows dark/light blue alignment throughout 24-hour period - full saturation, 24/7 operation detected"
|- Contrast with normal: Usually see clear gaps at night when facility shuts down
|- Action: Verify if this is planned (weekend cleanup/maintenance) or unexpected (equipment malfunction/continuous operation)
|
|**RULE 5: STANDARD 18-HOUR BLOCKS WITH DAILY VALLEYS = NORMAL OPERATION**
|- Energy field shows consistent 18-hour peak blocks followed by 6-hour valleys (shutdown/maintenance periods)
|- Orange line remains smooth and stable (85-92% typical range)
|- Green layer consistent thickness throughout (no spikes or collapses)
|- Impact: Textbook healthy operation, optimal for facility performance
|- Example: "Jan 3, 6, 9 all show standard 18-hour operating blocks with complete shutdown valleys - normal baseline operation"
|- Pattern: Repeating daily cycle, consistent peak height, clean valleys
|- Action: Use these days as operational benchmark
|
|**ORANGE LINE OSCILLATIONS (SECONDARY PATTERN - EQUIPMENT BEHAVIOR):**
|- Orange line shows rapid ups/downs or wild swings (vs smooth curve)
|- VFD issues, control system problems, motor instability, or strong negative field draw
|- Example: "Jan 5, 12 show rapid power factor oscillations - VFD overreaction or control system instability requiring investigation."
|- Pattern: Orange line looks jagged or bouncy instead of smooth
|- Impact: Increased reactive waste, potential equipment damage

**E. PRODUCTION VARIANCE DETECTION:**
- Count days running ABOVE target pattern ("hot" days)
- Calculate percentage above target for those days
- Example: "5 days (Jan 9-10, 23-24) ran 13% above normal 1100 kVA target, reaching ~1250 kVA - likely catch-up production days processing additional birds."
- Pattern: Sustained elevated operation above identified target
- Impact: Higher production but increased costs and demand risk

STEP 6: OPERATIONAL STORY (Day-by-Day for Problem Periods)
For weeks with issues, describe what happened:
- "Monday struggled, Tuesday ran well, Wednesday hit hard spot at 2pm, Thursday peaked then crashed..."
- Use visual cues: "barely got going", "spun up to same level as Monday", "shut down early"

STEP 7: POWER FACTOR & WASTE ANALYSIS
- Orange line behavior: Smooth vs drops vs oscillations
- Green layer: "Consistently thick (~XX% of supply)" or "Varies from XX-YY%"
- Conversion efficiency: "Current 86.8% PF means 13.2% waste - this green layer costs $XXX/month"

OUTPUT FORMAT:
Generate TWO sections:

SECTION 1 - NARRATIVE (6-8 paragraphs, be SPECIFIC):

**Paragraph 1 - TARGET IDENTIFICATION:**
State which days establish the target: "Scanning across the month, I identify 17 days with consistent patterns: [list specific dates]. These days all reach approximately XXX kVA peak height, run for similar duration, and show green waste layer of ~XX% thickness. This establishes our TARGET baseline."

**Paragraph 2 - BEST WEEK IDENTIFICATION:**
"Comparing all weeks, Week X (Jan XX-XX) is the MOST STABLE with all 5 weekdays showing nearly identical patterns. This becomes our weekly benchmark."

**Paragraph 3 - WEEK-BY-WEEK COMPARISON:**
"Week 1 (Jan 1-5): [describe patterns]. Compared to Week X target, this ran approximately XX% below due to [specific visual observations].
Week 2 (Jan 6-12): [describe]. Estimate XX% vs target.
Week 3: [describe stability if this is best week, or compare if not].
Week 4: [describe and compare].
Week 5 (if applicable): [describe]."

**Paragraph 4 - SATURDAY PRODUCTION DETAIL:**
"Saturday analysis shows: Jan 4 ran [full day/half day/minimal] reaching XXX kVA vs weekday target of YYY. Jan 11 was [describe]. Jan 18 [describe]. Jan 25 [describe]. These Saturday patterns boosted/reduced monthly performance by approximately X%."

**Paragraph 5 - SPECIFIC ANOMALIES:**
"Notable anomalies include: [Be exact - Jan 18-19 thin spikes, Jan 16 power outage, Jan 5&12 orange oscillations, etc.]. Each anomaly with specific dates, visual description, and likely cause."

**Paragraph 6 - OPERATIONAL STORY (for problem periods):**
"For Week 2 which showed instability: Monday struggled at startup, Tuesday ran well but hit a hard spot mid-afternoon visible as a dip in the light blue layer, Wednesday barely got going reaching only XXX kVA, Thursday spun up then crashed..." [Continue with visual storytelling]

**Paragraph 7 - POWER FACTOR & EFFICIENCY:**
"The orange power factor line [smooth/variable/oscillating]. Current XX.X% PF means XX.X% conversion efficiency with XX.X% waste (green layer). The green layer [consistently thick/varies/thin], representing approximately XXX kVA of wasted reactive power throughout the month."

**Paragraph 8 - BUSINESS IMPACT:**
"Business implications: This transformer achieved XX% of target production. The XX% waste layer costs approximately $XXX/month in wasted energy. [Specific recommendations based on observed patterns]."

USE EXACT LANGUAGE: "barely got going", "spun up to", "crashed mid-day", "peaked at XXX kVA", "shut down early", "struggled to start", "hit a hard spot", "ran hot"

SECTION 2 - ACTION BULLETS (exactly 10 items):
Extract 10 concise, actionable bullet points from your narrative:
- Start with an action verb when appropriate
- Be specific with dates and measurements
- Reference visual observations ("power factor drops", "consistent daily patterns")
- Suitable for quick management review

Format your response as:

NARRATIVE:
[Your detailed visual analysis walking through the chart]

BULLETS:
- [First actionable point]
- [Second actionable point]
...[continue to 10 bullets]

IMPORTANT: Use the tMAX_SUPPLY target value provided above as your baseline reference. This has been calculated from actual CSV data as the 95th percentile, representing the standard production target. Evaluate all patterns against this known target value."""

        # Call Claude API
        client = anthropic.Anthropic(api_key=api_key)
        
        message = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=2048,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": media_type,
                                "data": image_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ],
                }
            ],
        )
        
        # Extract response
        response_text = message.content[0].text
        
        # Parse narrative and bullets from response
        # Note: standard_pattern_kva (tmax_supply) is provided upfront from CSV data
        narrative = ""
        bullets = []
        
        try:
            
            # Split on NARRATIVE: and BULLETS: markers
            parts = response_text.split('NARRATIVE:')
            if len(parts) > 1:
                content_after_narrative = parts[1]
                bullets_split = content_after_narrative.split('BULLETS:')
                
                if len(bullets_split) > 1:
                    narrative = bullets_split[0].strip()
                    bullets_text = bullets_split[1].strip()
                    
                    # Extract bullet points (lines starting with -)
                    for line in bullets_text.split('\n'):
                        line = line.strip()
                        if line.startswith('-'):
                            bullets.append(line[1:].strip())  # Remove leading dash
                else:
                    # No BULLETS section found, use all as narrative
                    narrative = content_after_narrative.strip()
            else:
                # No NARRATIVE marker found, use entire response as narrative
                narrative = response_text.strip()
        except Exception as e:
            print(f"⚠️  Error parsing AI response structure: {e}")
            narrative = response_text.strip()
        
        result = {
            "success": True,
            "pattern_text": narrative,
            "pattern_summary": bullets,
            "confidence": 0.95,
            "model": "claude-3-5-haiku-20241022",
            "analyzed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Add validated target from provided transformer info (calculated and validated from CSV data)
        if target_validated:
            result['standard_pattern_kva'] = target_validated  # Use validated target
            result['tmax_supply'] = tmax_supply  # Keep original 95th percentile
            result['target_validated'] = target_validated
            result['target_confidence'] = target_confidence
            result['target_validation_note'] = target_note
        
        return result
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "pattern_text": f"Pattern analysis error: {str(e)}"
        }


def analyze_all_transformers(patterns_dir, site_output_dir, transformer_configs=None, analysis_period="Jan2025"):
    """
    Analyze baseline images for all transformers in a facility.
    
    Args:
        patterns_dir: Path to directory containing baseline pattern images
        site_output_dir: Path to site directory for output
        transformer_configs: Dict mapping transformer codes to config info
        analysis_period: Analysis period identifier
    
    Returns:
        dict: Results for all transformers analyzed
    """
    patterns_path = Path(patterns_dir)
    if not patterns_path.exists():
        print(f"❌ Patterns directory not found: {patterns_dir}")
        return None
    
    # Find all baseline images (pattern: t##b###.png where ## is transformer number)
    baseline_images = list(patterns_path.glob("t*b*.png"))
    
    if not baseline_images:
        print(f"⚠️  No baseline images found in {patterns_dir}")
        return None
    
    print(f"\n🔍 AI Pattern Analyzer")
    print(f"   Found {len(baseline_images)} baseline image(s)")
    print(f"   Output: {site_output_dir}")
    
    # Initialize pattern manager
    manager = PatternAnalysisManager(site_output_dir)
    
    results = {}
    patterns_dict = {}
    
    for img_path in baseline_images:
        # Extract transformer code from filename (e.g., "t15b876.png" -> "T15")
        filename = img_path.stem.lower()
        import re
        match = re.match(r't(\d+)b', filename)
        if not match:
            print(f"⚠️  Could not parse transformer code from {img_path.name}")
            continue
        
        xfmr_code = f"T{match.group(1)}"
        
        print(f"\n🔧 Analyzing {xfmr_code}: {img_path.name}")
        
        # Get transformer config if available
        xfmr_info = None
        if transformer_configs and xfmr_code in transformer_configs:
            xfmr_info = transformer_configs[xfmr_code]
        
        # Analyze with AI
        result = analyze_baseline_image_with_ai(
            str(img_path),
            transformer_info=xfmr_info,
            production_target=975000  # Default Foster Farms target
        )
        
        if result.get('success'):
            pattern_text = result['pattern_text']
            pattern_summary = result.get('pattern_summary', [])
            print(f"   ✅ Analysis complete")
            print(f"   📝 {pattern_text[:100]}...")
            print(f"   📋 Generated {len(pattern_summary)} bullet points")
            
            # Build pattern dict entry
            pattern_entry = {
                'pattern_interpretation': pattern_text,
                'pattern_summary': pattern_summary
            }
            
            # Add standard_pattern_kva if available
            if 'standard_pattern_kva' in result:
                pattern_entry['standard_pattern_kva'] = result['standard_pattern_kva']
            
            patterns_dict[xfmr_code] = pattern_entry
            results[xfmr_code] = result
        else:
            error = result.get('error', 'Unknown error')
            print(f"   ❌ Analysis failed: {error}")
            results[xfmr_code] = result
    
    # Save all patterns to JSON
    if patterns_dict:
        manager.update_multiple_patterns(patterns_dict, analysis_period)
        print(f"\n✅ Saved {len(patterns_dict)} pattern(s) to {manager.pattern_file.name}")
    
    return results


def test_analyzer(image_path):
    """Test the analyzer on a single image."""
    print(f"\n🧪 Testing AI Pattern Analyzer")
    print(f"   Image: {image_path}")
    
    if not os.path.exists(image_path):
        print(f"   ❌ Image not found")
        return
    
    # Test with sample transformer info
    test_info = {
        "name": "T15.Fillet",
        "energy_per_bird": "0.524 kWh",
        "cost_per_bird": "$0.115",
        "uptime_pct": "98.5"
    }
    
    result = analyze_baseline_image_with_ai(image_path, test_info)
    
    if result.get('success'):
        print(f"\n   ✅ Analysis successful!")
        print(f"\n   📊 Pattern Analysis:")
        print(f"   {result['pattern_text']}")
    else:
        print(f"\n   ❌ Analysis failed: {result.get('error')}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='AI Pattern Analyzer for Unity Energy Fields')
    parser.add_argument('--test', help='Test analyzer on a single image', metavar='IMAGE_PATH')
    parser.add_argument('--patterns-dir', help='Directory containing baseline pattern images')
    parser.add_argument('--site-dir', help='Site output directory for results')
    parser.add_argument('--period', default='Jan2025', help='Analysis period (default: Jan2025)')
    
    args = parser.parse_args()
    
    if args.test:
        # Test mode
        test_analyzer(args.test)
    elif args.patterns_dir and args.site_dir:
        # Batch analysis mode
        analyze_all_transformers(args.patterns_dir, args.site_dir, analysis_period=args.period)
    else:
        # Show usage
        print("Usage:")
        print("  Test single image:")
        print("    python ai_pattern_analyzer.py --test /path/to/image.png")
        print()
        print("  Analyze all transformers:")
        print("    python ai_pattern_analyzer.py \\")
        print("      --patterns-dir /path/to/Patterns \\")
        print("      --site-dir /path/to/Site \\")
        print("      --period Jan2025")
        print()
        print("Example:")
        print("  python ai_pattern_analyzer.py \\")
        print("    --patterns-dir /Users/mdhowell/energyclips/CherryAve/SITE2025/01_JAN2025/Patterns \\")
        print("    --site-dir /Users/mdhowell/eestream/eBehavior/Reports/Study251217r0/FosterFarms/CherryAve_Site \\")
        print("    --period Jan2025")

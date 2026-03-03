# VOLTAGE & CURRENT HEALTH ANALYSIS

*Electromagnetic Field Analysis: Voltage (E-field), Current (H-field), and Thermal Burden*

**Transformer:** T15 Fillet  
**Generated:** 2026-02-18 15:24:42  
**Data Source:** AN53110845-V-1minRES_43260CLP_251101-251130c.csv  

## 📊 Analysis Period

- **Period:** November 01, 2025 thru November 30, 2025
- **Number of Days:** 30 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 43,260

## 🔋 Facility Information

- **Transformer Capacity:** 2,500 kVA
- **Nominal Voltage:** 480V (3-Phase)
- **Analysis Type:** Voltage & Current Health + Thermal Burden Assessment
- **Technology Focus:** Unity Energy MPTS Solutions

---

## 📈 Voltage Statistics

<details>
<summary><strong>Basic Voltage Metrics</strong></summary>

- **Total Voltage Readings Analyzed:** 43,260
- **Average Line-to-Neutral Voltage:** 277.0V (nominal 277V)
- **Average Line-to-Line Voltage:** 479.7V (nominal 480V)
- **Minimum Voltage:** 0.0V (outage detected)
- **Maximum Voltage:** 504.4V
- **Standard Deviation:** 27.12V

</details>

### Operating Mean Voltage vs Nominal (480V)

- **Operating Mean:** 479.7V (**0.3V, 0.05% below nominal**) ✓
- **Line-to-Neutral Mean:** 277.0V (**At nominal**) ✓

*📌 Note: This transformer operates at nominal voltage - minimal additional heat losses.*

### Voltage Distribution Analysis

| Voltage Zone | L-N Range | Readings | Percentage | Status |
| ------------ | --------- | -------: | ---------: | ------ |
| Outage | < 10V | 120 | 0.28% | ⚠️ POWER LOSS |
| Critical | < 265V | 33 | 0.08% | ✓ Minimal |
| Stressed | 265-271V | 3,580 | 8.28% | ✓ Low |
| Normal-Low | 271-277V | 17,980 | 41.56% | ✓ Acceptable |
| Normal | ≥ 277V | 21,547 | 49.81% | ✓ Optimal |


---

## ⚡ Voltage Drop Pattern Detection

<details>
<summary><strong>Predictive Algorithm Analysis</strong></summary>

### Algorithm 1-3: Sustained Undervoltage Analysis

**Assessment:** T15 does NOT have a sustained undervoltage problem like T10/T12. Average voltage is at nominal (479.7V). The issue here is different.

### Algorithm 4: Motor Inrush Pattern Detection ⚠️

**THIS TRANSFORMER HAS A MOTOR INRUSH PROBLEM**

**Total Motor Inrush Events:** 32 voltage sag events detected
**Voltage Sag Range:** 384.6V to 442.2V (8% to 20% drops from 480V nominal)

</details>

### ⚠️ Motor Inrush Voltage Sag Events

**All 32 Events:**

| Date | Day | Time | Voltage | Drop % | Severity |
| ---- | --- | ---- | ------: | -----: | -------- |
| 2025-11-19 | Wed | 10:25 | 384.6V | 19.9% | ⚠️ SEVERE |
| 2025-11-11 | Tue | 11:55 | 398.1V | 17.1% | ⚠️ SEVERE |
| 2025-11-19 | Wed | 02:40 | 405.6V | 15.5% | ⚠️ SEVERE |
| 2025-11-07 | Fri | 08:38 | 407.0V | 15.2% | ⚠️ SEVERE |
| 2025-11-14 | Fri | 02:09 | 410.4V | 14.5% | ⚠️ SEVERE |
| 2025-11-14 | Fri | 02:15 | 410.3V | 14.5% | ⚠️ SEVERE |
| 2025-11-20 | Thu | 05:14 | 412.3V | 14.1% | ⚠️ SEVERE |
| 2025-11-18 | Tue | 00:31 | 412.6V | 14.0% | ⚠️ SEVERE |
| 2025-11-06 | Thu | 08:17 | 414.8V | 13.6% | ⚠️ SEVERE |
| 2025-11-10 | Mon | 09:07 | 415.0V | 13.5% | ⚠️ SEVERE |
| 2025-11-12 | Wed | 10:24 | 415.6V | 13.4% | ⚠️ SEVERE |
| 2025-11-18 | Tue | 10:32 | 415.8V | 13.4% | ⚠️ SEVERE |
| 2025-11-03 | Mon | 07:46 | 417.0V | 13.1% | ⚠️ SEVERE |
| 2025-11-05 | Wed | 11:36 | 417.4V | 13.0% | ⚠️ SEVERE |
| 2025-11-18 | Tue | 11:59 | 417.7V | 13.0% | ⚠️ SEVERE |
| 2025-11-19 | Wed | 02:21 | 419.0V | 12.7% | ⚠️ SEVERE |
| 2025-11-23 | Sun | 13:20 | 419.1V | 12.7% | ⚠️ SEVERE |
| 2025-11-18 | Tue | 02:11 | 419.3V | 12.6% | ⚠️ SEVERE |
| 2025-11-17 | Mon | 08:11 | 420.2V | 12.5% | Moderate |
| 2025-11-19 | Wed | 02:04 | 421.5V | 12.2% | Moderate |
| 2025-11-20 | Thu | 05:43 | 421.4V | 12.2% | Moderate |
| 2025-11-17 | Mon | 07:24 | 422.7V | 11.9% | Moderate |
| 2025-11-20 | Thu | 22:24 | 424.7V | 11.5% | Moderate |
| 2025-11-13 | Thu | 13:38 | 426.4V | 11.2% | Moderate |
| 2025-11-13 | Thu | 05:53 | 428.2V | 10.8% | Moderate |
| 2025-11-12 | Wed | 08:40 | 430.6V | 10.3% | Moderate |
| 2025-11-13 | Thu | 22:24 | 433.5V | 9.7% | Moderate |
| 2025-11-14 | Fri | 22:24 | 434.3V | 9.5% | Moderate |
| 2025-11-20 | Thu | 05:05 | 435.9V | 9.2% | Moderate |
| 2025-11-15 | Sat | 13:16 | 436.9V | 9.0% | Moderate |
| 2025-11-02 | Sun | 13:16 | 439.2V | 8.5% | Mild |
| 2025-11-16 | Sun | 13:45 | 442.2V | 7.9% | Mild |

### ⚠️ PREDICTIVE PATTERN: Recurring Time Events

**CRITICAL FINDING - Same Time, Different Days:**

| Time | Occurrences | Dates | Min Voltage | Equipment Inference |
| ---- | ----------: | ----- | ----------: | ------------------- |
| **22:24** | 3 | Nov 13, 14, 20 | 424.7V | ⚠️ Timer-controlled motor |
| **13:16** | 2 | Nov 02, 15 | 436.9V | Afternoon process equipment |

**These patterns indicate specific motors on scheduled timers or processes that can be identified and monitored.**

### Shift-Based Pattern Analysis

| Time Window | Events | Description |
| ----------- | -----: | ----------- |
| Early Morning (02:00-06:00) | 10 | Refrigeration compressor cycling |
| Morning Start (06:00-09:00) | 6 | Production line startup |
| Mid-Morning (09:00-12:00) | 7 | Process equipment cycling |
| Afternoon (12:00-15:00) | 5 | Afternoon shift equipment |
| Night (22:00-02:00) | 4 | Timer-controlled processes |

### Outage Events Detected

| Date | Day | Start | End | Duration |
| ---- | --- | ----- | --- | -------: |
| 2025-11-02 | Sunday | 01:00 | 01:59 | 120 min |


---

## 🔍 Motor Stress & Failure Risk Analysis

<details>
<summary><strong>VHI Analysis & Device Stress Indicators</strong></summary>

### Voltage Heat Index (VHI) Analysis

- **Average VHI:** 23.68
- **Maximum VHI:** 994.40
- **High VHI Events (>5.0):** 39,027 (90% of readings)

### Motor Inrush Risk Assessment

| Metric | Value | Impact |
| ------ | ----: | ------ |
| Motor Inrush Events | 32 | ⚠️ Equipment stress |
| Severe Events (>12% drop) | 18 | ⚠️ Large motor stress |
| Deepest Sag | 384.6V (20% drop) | ⚠️ Very large motor |
| Recurring Time Patterns | 2 | ⚠️ Predictable failures |
| **Equipment Failure Risk** | **ELEVATED** | Specific motors at risk |

### Equipment Inference

Based on voltage sag depth and patterns:

| Sag Depth | Estimated Motor Size | Events |
| --------- | -------------------- | -----: |
| 15-20% (380-410V) | 150+ HP | 6 |
| 12-15% (410-425V) | 100-150 HP | 12 |
| 8-12% (425-445V) | 50-100 HP | 14 |

### Worst Event Analysis

**November 19, 2025 at 10:25 AM** - 384.6V (19.9% drop)
- This indicates a **very large motor (150+ HP)** or simultaneous start of multiple motors
- Occurs mid-morning on Wednesday (production peak)
- **This motor should be priority for inspection**

</details>


---

## 📊 Chart Overlay Data Preparation

<details>
<summary><strong>Prepared Chart Overlay Points</strong></summary>

*The following data points have been prepared for chart overlays:*

| Event Type | Count | Description |
| ---------- | ----: | ----------- |
| Complete Outages | 120 | Site-wide event Nov 2nd |
| Motor Inrush Sags (<450V) | 32 | ⚠️ Equipment cycling events |
| Severe Sags (<420V) | 18 | ⚠️ Large motor starts |
| High VHI Events (>5.0) | 39,027 | Current-driven thermal stress |

### Time Pattern Overlay Points

- **22:24 Marker** - Recurring motor start (3 events)
- **13:16 Marker** - Recurring afternoon event (2 events)
- **02:00-06:00 Shading** - Early morning compressor cycling zone
- **07:00-09:00 Shading** - Shift startup zone

</details>

---

## 💡 Voltage Behavior Recommendations

### ⚠️ ALERT: MOTOR INRUSH PATTERN DETECTED

This transformer has a **different problem than T10/T12**. While average voltage is healthy, there are **32 motor inrush events** causing significant voltage sags:

1. **✓ AVERAGE VOLTAGE HEALTHY** — 479.7V average (at nominal)
2. **⚠️ 32 MOTOR INRUSH EVENTS** — Voltage sags to 384-442V range
3. **⚠️ 18 SEVERE EVENTS** — Drops exceeding 12% (motor damage territory)
4. **⚠️ PREDICTABLE PATTERNS** — 22:24 event occurs on multiple days (timer-controlled)
5. **⚠️ LARGE MOTOR DETECTED** — 384.6V event indicates 150+ HP motor

### Problem Type Comparison

| Transformer | Problem Type | Root Cause | Solution |
| ----------- | ------------ | ---------- | -------- |
| T10, T12 | Sustained Undervoltage | Utility grid undersized | Contact PG&E + H490 |
| **T15** | **Motor Inrush Sags** | **Large motor starts** | **Soft starters/VFDs + H490** |

### Recommended Actions

| Priority | Action | Timeline |
| -------- | ------ | -------- |
| 1 | Identify motor running at 22:24 (timer-controlled) | Within 7 days |
| 2 | Thermal imaging on large motors in Fillet area | Within 14 days |
| 3 | Vibration analysis on motors causing 15%+ sags | Within 14 days |
| 4 | Evaluate soft starters for motors >100 HP | Within 30 days |
| 5 | Install H490 MPTS (provides reactive support during inrush) | Per proposal |

### Predictive Maintenance Alert

**The 22:24 motor** (3 recurring events) and **the 384.6V motor** (largest sag) are the highest priority for inspection. These patterns allow us to:
- Predict WHEN the motor will cycle next
- Schedule inspection during that window
- Prevent catastrophic failure and unplanned downtime

### Cost Avoidance Potential

Unplanned motor failure in food processing: **$100,000 - $500,000** in downtime, spoilage, and emergency repairs.

Predictive detection and scheduled replacement: **$10,000 - $30,000** planned maintenance.

**ROI of predictive voltage monitoring: 10-50x cost avoidance.**

---

# END OF REPORT

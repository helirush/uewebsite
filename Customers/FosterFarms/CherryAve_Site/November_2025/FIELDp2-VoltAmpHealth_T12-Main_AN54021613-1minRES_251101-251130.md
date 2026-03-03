# VOLTAGE & CURRENT HEALTH ANALYSIS

*Electromagnetic Field Analysis: Voltage (E-field), Current (H-field), and Thermal Burden*

**Transformer:** T12 Main  
**Generated:** 2026-02-18 15:25:20  
**Data Source:** AN54021613-V-1minRES_43260CLP_251101-251130c.csv  

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
- **Average Line-to-Neutral Voltage:** 269.8V (nominal 277V)
- **Average Line-to-Line Voltage:** 467.4V (nominal 480V)
- **Minimum Voltage:** 0.0V (outage detected)
- **Maximum Voltage:** 495.2V
- **Standard Deviation:** 27.06V

</details>

### Operating Mean Voltage vs Nominal (480V)

- **Operating Mean:** 467.4V (**12.6V, 2.63% below nominal**)
- **Line-to-Neutral Mean:** 269.8V (**2.6% below 277V nominal**)

*📌 Note: At -2.6% voltage, motors experience approximately 5% additional I²R heat losses.*

### Voltage Distribution Analysis

| Voltage Zone | L-N Range | Readings | Percentage | Status |
| ------------ | --------- | -------: | ---------: | ------ |
| Outage | < 10V | 120 | 0.28% | ⚠️ POWER LOSS |
| Critical | < 265V | 11,538 | 26.67% | ⚠️ MOTOR DAMAGE ZONE |
| Stressed | 265-271V | 12,801 | 29.59% | ⚡ EXCESS HEAT |
| Normal-Low | 271-277V | 9,030 | 20.87% | ✓ Acceptable |
| Normal | ≥ 277V | 9,771 | 22.59% | ✓ Optimal |


---

## ⚡ Voltage Drop Pattern Detection

<details>
<summary><strong>Predictive Algorithm Analysis</strong></summary>

### Algorithm 1: Recurring Time Pattern Detection

**Hours with Critical Voltage on Multiple Days:**

| Hour | Days Affected | Percentage | Risk Level |
| ---- | ------------: | ---------: | ---------- |
| 04:00 | 19/30 | 63% | ⚠️ HIGH |
| 05:00 | 19/30 | 63% | ⚠️ HIGH |
| 07:00 | 19/30 | 63% | ⚠️ HIGH |
| 03:00 | 18/30 | 60% | ⚠️ HIGH |
| 06:00 | 18/30 | 60% | ⚠️ HIGH |

**Pattern Identified:** Critical voltage occurs during early morning hours (03:00-07:00) on 60%+ of days.

### Algorithm 2: Event Clustering & Predictive Windows

**High-Risk Time Windows (3+ events starting in same 15-min window):**

| Time Window | Event Starts | Risk Level |
| ----------- | -----------: | ---------- |
| 09:15 | 30 | ⚠️ HIGHEST |
| 00:00 | 26 | ⚠️ HIGH |
| 03:15 | 24 | ⚠️ HIGH |
| 23:45 | 21 | ⚠️ HIGH |
| 07:00 | 20 | ⚠️ HIGH |

**Trigger Time Identified:** 09:15 shows highest event clustering (30 events).

### Algorithm 3: Cumulative Motor Stress Index (CMSI)

- **Total CMSI (November):** 121,703 points
- **Average CMSI per Day:** 4,057 points (threshold: 5,000)

**Critical Days (>7000 CMSI):**

| Date | CMSI Score | Risk Level |
| ---- | ---------: | ---------- |
| 2025-11-02 | 12,481 | ⚠️ CRITICAL |

</details>

### Outage Events Detected

| Date | Day | Start | End | Duration |
| ---- | --- | ----- | --- | -------: |
| 2025-11-02 | Sunday | 01:00 | 01:59 | 120 min |


---

## 🔍 Motor Stress & Failure Risk Analysis

<details>
<summary><strong>VHI Analysis & Device Stress Indicators</strong></summary>

### Voltage Heat Index (VHI) Analysis

- **Average VHI:** 19.64
- **Maximum VHI:** 960.00
- **High VHI Events (>5.0):** 28,495 (66% of readings)

### Motor Failure Risk Assessment

| Metric | Value | Impact |
| ------ | ----: | ------ |
| Monthly Critical Hours | 192.3 hrs | Excessive (threshold: 100 hrs) |
| Monthly Outage Hours | 2.0 hrs | Detected |
| Base Failure Rate | 5.0%/yr | Industry standard |
| + Critical Voltage Penalty | +19.2% | From excessive stress hours |
| + Outage Event Penalty | +10.0% | From power loss events |
| **Projected Monthly Risk** | **34.2%** | ⚠️ ELEVATED |
| **Projected Annual Risk** | **95%** | ⚠️ HIGH |

### Heat Adder Impact

At -2.6% voltage deviation:
- **I²R Loss Increase:** ~5% additional heat
- **Effect:** Accelerated insulation breakdown
- **Recommendation:** Monitor bearing temperatures

</details>


---

## 📊 Chart Overlay Data Preparation

<details>
<summary><strong>Prepared Chart Overlay Points</strong></summary>

*The following data points have been prepared for chart overlays:*

| Event Type | Count | Description |
| ---------- | ----: | ----------- |
| Complete Outages | 120 | Readings at 0.0V |
| Critical Events (<265V L-N) | 11,538 | Motor damage zone |
| Stressed Events (265-271V) | 12,801 | Excess heat operation |
| High VHI Events (>5.0) | 28,495 | Elevated thermal stress |

### Time Pattern Overlay Points

- **Early Morning Critical Zone:** 03:00 - 07:00 (shaded red)
- **Trigger Time Marker:** 09:15 vertical line (highest clustering)

</details>

---

## 💡 Voltage Behavior Recommendations

### ⚠️ ALERT: SIGNIFICANT UNDERVOLTAGE CONDITION DETECTED

This energy field is experiencing **recurring critical voltage depression**:

1. **⚠️ EXCESSIVE CRITICAL VOLTAGE HOURS** — 192.3 hours/month in motor damage zone (threshold: 100 hrs)
2. **⚠️ POWER OUTAGE EVENT** — 2-hour complete power loss detected November 2nd
3. **⚠️ EARLY MORNING PATTERN** — Critical voltage 03:00-07:00 on 60%+ of days
4. **⚠️ HIGH EVENT CLUSTERING** — 30 stress events starting at 09:15 window

### Recommended Actions

| Priority | Action | Timeline |
| -------- | ------ | -------- |
| 1 | Motor thermal imaging inspection | Within 30 days |
| 2 | Bearing analysis and vibration monitoring | Within 30 days |
| 3 | Install H490 MPTS units (reduces current draw) | Per proposal |
| 4 | Investigate early morning load patterns | Within 14 days |

### Root Cause Assessment

The early morning critical voltage pattern (03:00-07:00) suggests this may be related to overnight utility load conditions or early shift startup sequences.

---

# END OF REPORT

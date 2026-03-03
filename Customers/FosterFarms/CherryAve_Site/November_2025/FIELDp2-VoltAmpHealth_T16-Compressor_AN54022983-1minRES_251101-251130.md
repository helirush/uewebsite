# VOLTAGE & CURRENT HEALTH ANALYSIS

*Electromagnetic Field Analysis: Voltage (E-field), Current (H-field), and Thermal Burden*

**Transformer:** T16 Compressor  
**Generated:** 2026-02-18 15:25:06  
**Data Source:** AN54022983-V-1minRES_43260CLP_251101-251130c.csv  

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
- **Average Line-to-Neutral Voltage:** 274.9V (nominal 277V)
- **Average Line-to-Line Voltage:** 476.2V (nominal 480V)
- **Minimum Voltage:** 0.0V (outage detected)
- **Maximum Voltage:** 504.3V
- **Standard Deviation:** 27.49V

</details>

### Operating Mean Voltage vs Nominal (480V)

- **Operating Mean:** 476.2V (**3.8V, 0.79% below nominal**)
- **Line-to-Neutral Mean:** 274.9V (**0.7% below 277V nominal**)

*📌 Note: At -0.7% voltage, motors experience approximately 1.5% additional I²R heat losses - minimal impact.*

### Voltage Distribution Analysis

| Voltage Zone | L-N Range | Readings | Percentage | Status |
| ------------ | --------- | -------: | ---------: | ------ |
| Outage | < 10V | 121 | 0.28% | ⚠️ POWER LOSS |
| Critical | < 265V | 24 | 0.06% | ✓ Minimal |
| Stressed | 265-271V | 14,006 | 32.38% | ⚡ MODERATE |
| Normal-Low | 271-277V | 11,371 | 26.29% | ✓ Acceptable |
| Normal | ≥ 277V | 17,738 | 41.00% | ✓ Optimal |


---

## ⚡ Voltage Drop Pattern Detection

<details>
<summary><strong>Predictive Algorithm Analysis</strong></summary>

### Algorithm 1: Recurring Time Pattern Detection

**Hours with Critical Voltage on Multiple Days:**

No recurring critical voltage patterns detected. Critical events are isolated and infrequent.

**Pattern Assessment:** ✓ No systematic critical voltage pattern. Voltage remains in stressed/normal range.

### Algorithm 2: Event Clustering & Predictive Windows

No significant event clustering detected. Critical events do not follow a predictable time pattern.

**Assessment:** ✓ Random isolated events only - no predictable stress onset.

### Algorithm 3: Cumulative Motor Stress Index (CMSI)

- **Total CMSI (November):** 66,091 points
- **Average CMSI per Day:** 2,203 points (threshold: 5,000) ✓

**Critical Days (>7000 CMSI):**

| Date | CMSI Score | Risk Level |
| ---- | ---------: | ---------- |
| 2025-11-02 | 12,013 | ⚠️ Outage Impact |
| 2025-11-04 | ~7,000 | ⚠️ Brief spike |

*Note: Elevated days are primarily due to outage events.*

</details>

### Outage Events Detected

| Date | Day | Start | End | Duration |
| ---- | --- | ----- | --- | -------: |
| 2025-11-02 | Sunday | 01:00 | 01:59 | 120 min |
| 2025-11-04 | Tuesday | 23:20 | 23:20 | 1 min |


---

## 🔍 Motor Stress & Failure Risk Analysis

<details>
<summary><strong>VHI Analysis & Device Stress Indicators</strong></summary>

### Voltage Heat Index (VHI) Analysis

- **Average VHI:** 26.63
- **Maximum VHI:** 991.65
- **High VHI Events (>5.0):** 38,982 (90% of readings)

### Motor Failure Risk Assessment

| Metric | Value | Impact |
| ------ | ----: | ------ |
| Monthly Critical Hours | 0.4 hrs | ✓ Minimal |
| Monthly Outage Hours | 2.0 hrs | Site-wide + brief event |
| Base Failure Rate | 5.0%/yr | Industry standard |
| + Critical Voltage Penalty | +0.04% | Negligible |
| + Outage Event Penalty | +10.0% | From power loss events |
| **Projected Monthly Risk** | **15.1%** | ✓ MODERATE |
| **Projected Annual Risk** | **95%** | Elevated by outages |

### Heat Adder Impact

At -0.7% voltage deviation:
- **I²R Loss Increase:** ~1.5% additional heat
- **Effect:** Minor - within acceptable range
- **Status:** ✓ ACCEPTABLE

### Stressed Operation Note

While 32% of readings are in the "stressed" zone (265-271V), this is the **mildest stress category** and does not indicate imminent failure risk. Motors are designed to operate in this range.

</details>


---

## 📊 Chart Overlay Data Preparation

<details>
<summary><strong>Prepared Chart Overlay Points</strong></summary>

*The following data points have been prepared for chart overlays:*

| Event Type | Count | Description |
| ---------- | ----: | ----------- |
| Complete Outages | 121 | Site-wide + 1 brief event |
| Critical Events (<265V L-N) | 24 | ✓ Minimal |
| Stressed Events (265-271V) | 14,006 | Moderate - within design range |
| High VHI Events (>5.0) | 38,982 | Current-driven, not voltage |

### Time Pattern Overlay Points

- **No significant critical voltage patterns detected**
- Stressed operation is distributed, not concentrated

</details>

---

## 💡 Voltage Behavior Recommendations

### ✓ VOLTAGE HEALTH: ACCEPTABLE

This transformer operates with moderate stress but no critical patterns:

1. **✓ NEAR NOMINAL** — Average 274.9V L-N (only 0.7% below nominal)
2. **✓ MINIMAL CRITICAL HOURS** — Only 0.4 hours/month in critical zone
3. **✓ LOW STRESS INDEX** — Average 2,203 CMSI/day (well below 5,000 threshold)
4. **⚠️ OUTAGE EVENTS** — Site-wide outage Nov 2nd + brief 1-min event Nov 4th
5. **⚡ STRESSED OPERATION** — 32% of readings in stressed zone (265-271V)

### Status Summary

| Aspect | Status |
| ------ | ------ |
| Voltage Quality | ✓ ACCEPTABLE |
| Motor Stress | ✓ LOW-MODERATE |
| Pattern Risk | ✓ NONE |
| Outage Impact | ⚠️ Two events detected |

### Recommendation

The 32% stressed operation is within motor design tolerances and does not require immediate action. The H490 MPTS solution will improve voltage stability by reducing reactive current draw. Continue normal monitoring.

---

# END OF REPORT

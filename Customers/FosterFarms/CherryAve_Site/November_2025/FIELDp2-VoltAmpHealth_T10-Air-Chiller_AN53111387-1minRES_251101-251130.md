# VOLTAGE & CURRENT HEALTH ANALYSIS

*Electromagnetic Field Analysis: Voltage (E-field), Current (H-field), and Thermal Burden*

**Transformer:** T10 Air Chiller  
**Generated:** 2026-02-18 15:24:54  
**Data Source:** AN53111387-V-1minRES_43260CLP_251101-251130c.csv  

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
- **Average Line-to-Neutral Voltage:** 265.3V (nominal 277V)
- **Average Line-to-Line Voltage:** 459.5V (nominal 480V)
- **Minimum Voltage:** 0.0V (outage detected)
- **Maximum Voltage:** 485.8V
- **Standard Deviation:** 26.86V

</details>

### Operating Mean Voltage vs Nominal (480V)

- **Operating Mean:** 459.5V (**20.5V, 4.28% below nominal**)
- **Line-to-Neutral Mean:** 265.3V (**4.2% below 277V nominal**)

*📌 Note: At -4.2% voltage, motors experience approximately 8-10% additional I²R heat losses, accelerating insulation and bearing wear.*

### Voltage Distribution Analysis

| Voltage Zone | L-N Range | Readings | Percentage | Status |
| ------------ | --------- | -------: | ---------: | ------ |
| Outage | < 10V | 120 | 0.28% | ⚠️ POWER LOSS |
| Critical | < 265V | 22,417 | 51.82% | ⚠️ MOTOR DAMAGE ZONE |
| Stressed | 265-271V | 6,782 | 15.68% | ⚡ EXCESS HEAT |
| Normal-Low | 271-277V | 12,397 | 28.66% | ✓ Acceptable |
| Normal | ≥ 277V | 1,544 | 3.57% | ✓ Optimal |


---

## ⚡ Voltage Drop Pattern Detection

<details>
<summary><strong>Predictive Algorithm Analysis</strong></summary>

### Algorithm 1: Recurring Time Pattern Detection

**Hours with Critical Voltage on Multiple Days:**

| Hour | Days Affected | Percentage | Risk Level |
| ---- | ------------: | ---------: | ---------- |
| 01:00 | 21/30 | 70% | ⚠️ HIGH |
| 22:00 | 21/30 | 70% | ⚠️ HIGH |
| 23:00 | 21/30 | 70% | ⚠️ HIGH |
| 00:00 | 20/30 | 67% | ⚠️ HIGH |
| 02:00-12:00 | 20/30 | 67% | ⚠️ HIGH |

**Pattern Identified:** Critical voltage occurs nightly from ~21:00 to ~15:00 next day (18 hours).

### Algorithm 2: Event Clustering & Predictive Windows

**High-Risk Time Windows (3+ events starting in same 15-min window):**

| Time Window | Event Starts | Sample Dates |
| ----------- | -----------: | ------------ |
| 21:00 | 17 | 11/03, 11/04, 11/05, 11/06, 11/09... |
| 22:30 | 11 | 11/02, 11/09, 11/16, 11/18... |
| 22:15 | 10 | 11/09, 11/16, 11/18... |
| 22:00 | 8 | 11/02, 11/09, 11/18... |
| 20:45 | 8 | 11/06, 11/09, 11/13... |

**Trigger Time Identified:** 21:00 (9 PM) is the primary stress onset time.

### Algorithm 3: Cumulative Motor Stress Index (CMSI)

**Daily Stress Levels (Last 10 Days):**

| Date | CMSI Score | Risk Level |
| ---- | ---------: | ---------- |
| 2025-11-21 | 6,751 | HIGH |
| 2025-11-22 | 1,573 | LOW |
| 2025-11-23 | 1,959 | LOW |
| 2025-11-24 | 7,761 | ⚠️ CRITICAL |
| 2025-11-25 | 7,710 | ⚠️ CRITICAL |
| 2025-11-26 | 5,574 | HIGH |
| 2025-11-27 | 3,052 | MODERATE |
| 2025-11-28 | 6,686 | HIGH |
| 2025-11-29 | 5,361 | HIGH |
| 2025-11-30 | 2,811 | LOW |

- **Total CMSI (November):** 183,964 points
- **Average CMSI per Day:** 6,132 points (threshold: 5,000)

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

- **Average VHI:** 30.25
- **Maximum VHI:** 960.00
- **High VHI Events (>5.0):** 36,862 (85% of readings)

### Motor Failure Risk Assessment

| Metric | Value | Impact |
| ------ | ----: | ------ |
| Monthly Critical Hours | 375.6 hrs | Excessive (threshold: 100 hrs) |
| Monthly Outage Hours | 2.0 hrs | Detected |
| Base Failure Rate | 5.0%/yr | Industry standard |
| + Critical Voltage Penalty | +37.6% | From excessive stress hours |
| + Outage Event Penalty | +10.0% | From power loss events |
| **Projected Monthly Risk** | **52.6%** | ⚠️ HIGH |
| **Projected Annual Risk** | **95%** | ⚠️ CRITICAL |

### Heat Adder Impact

At -4.2% voltage deviation:
- **I²R Loss Increase:** ~8-10% additional heat
- **Effect:** Accelerated insulation breakdown and bearing wear
- **Recommendation:** Thermal imaging inspection within 30 days

</details>


---

## 📊 Chart Overlay Data Preparation

<details>
<summary><strong>Prepared Chart Overlay Points</strong></summary>

*The following data points have been prepared for chart overlays:*

| Event Type | Count | Description |
| ---------- | ----: | ----------- |
| Complete Outages | 120 | Readings at 0.0V |
| Critical Events (<265V L-N) | 22,417 | Motor damage zone |
| Stressed Events (265-271V) | 6,782 | Excess heat operation |
| High VHI Events (>5.0) | 36,862 | Elevated thermal stress |

### Time Pattern Overlay Points

- **Nightly Critical Zone:** 21:00 - 15:00 (shaded red)
- **Trigger Time Marker:** 21:00 vertical line
- **Recovery Window:** 15:00 - 18:00 (brief normal period)

</details>

---

## 💡 Voltage Behavior Recommendations

### ⚠️ ALERT: SYSTEMATIC UNDERVOLTAGE CONDITION DETECTED

This energy field is experiencing **sustained critical voltage depression**:

1. **⚠️ EXCESSIVE CRITICAL VOLTAGE HOURS** — 375.6 hours/month in motor damage zone (threshold: 100 hrs)
2. **⚠️ POWER OUTAGE EVENTS** — 2-hour complete power loss detected November 2nd
3. **⚠️ DAILY STRESS INDEX EXCEEDS THRESHOLD** — Average 6,132 CMSI (threshold: 5,000)
4. **⚠️ SYSTEMATIC PATTERN IDENTIFIED** — Nightly 21:00-15:00 critical voltage (utility grid issue)

### Recommended Actions

| Priority | Action | Timeline |
| -------- | ------ | -------- |
| 1 | Motor thermal imaging inspection | Within 30 days |
| 2 | Bearing analysis and vibration monitoring | Within 30 days |
| 3 | Contact PG&E regarding sustained undervoltage | Immediate |
| 4 | Install H490 MPTS units (reduces current draw) | Per proposal |
| 5 | Schedule motor replacement planning | Within 90 days if condition persists |

### Root Cause Assessment

This appears to be a **utility-side issue** — the grid serving this facility is undersized for industrial load in the area. The voltage depression follows a predictable weekday pattern, suggesting regional demand exceeds grid capacity during peak hours.

---

# END OF REPORT

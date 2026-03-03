# VOLTAGE & CURRENT HEALTH ANALYSIS

*Electromagnetic Field Analysis: Voltage (E-field), Current (H-field), and Thermal Burden*

**Transformer:** T10.AirChiller  
**Generated:** 2026-01-06 13:46:59  
**Data Source:** AN53111387-V-1minRES_44640CLP_251001-251031zth.csv  

## 📊 Analysis Period

- **Period:** October 01, 2025 thru October 31, 2025
- **Number of Days:** 31 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 44,640

## 🔋 Facility Information

- **Transformer Capacity:** 3,000 kVA
- **Nominal Voltage:** 480V (3-Phase)
- **Analysis Type:** Voltage & Current Health + Thermal Burden Assessment
- **Technology Focus:** Unity Energy MPTS Solutions

---

## 📈 Voltage Statistics

<details>
<summary><strong>Basic Voltage Metrics</strong></summary>

- **Total Voltage Readings Analyzed:** 44,640
- **Average Voltage:** 454.4V
- **Minimum Voltage:** 0.0V
- **Maximum Voltage:** 484.2V
- **Standard Deviation:** 33.07V

</details>

### Operating Mean Voltage vs Nominal (480V)

- **Operating Mean:** 454.4V (25.6V, 5.32% below nominal)

*📌 Note: Lower mean voltage for the same kW raises current, increasing BTU/hr and contributing to higher VHI.*

### Voltage Deviation Analysis

| Deviation Level | Readings | Percentage |
| --------------- | -------- | ---------- |
| Under 0% (below 480V) | 43,869 | 98.27% |
| Over 0% (above 480V) | 771 | 1.73% |


---

## ⚡ Voltage Drop Group Detection

<details>
<summary><strong>Group Detection Analysis</strong></summary>

**Voltage Drop Groups Detected:** 1

### T10.AIRCHILLER Group Index

| Group ID | Drop Count | Voltage Range | Amp Range | ΔV | Est. Stall Amps | Estimated HP | Motor Behavior Classification | Days |
| -------- | ---------: | ------------- | --------: | ------: | ---------: | ----------: | --------------------------- | ---: |
| G1 | 36535 | 434.8–460.8V | 174.7–2136.2A | 21.2 | 1400.9 | 180 | Critical Duty | 28 |

### T10.AIRCHILLER Group Nominal Drop Points

G1: Center at 447.8V, 36535 occurrences

</details>


---

## 🔍 Device Inference and Stress Analysis

<details>
<summary><strong>VHI Analysis & Device Stress Indicators</strong></summary>

### Voltage Heat Index (VHI) Analysis

- **Average VHI:** 38.52
- **Maximum VHI:** 960.00
- **High VHI Events (>5.0):** 41,181


</details>


---

## 📊 Chart Overlay Data Preparation

<details>
<summary><strong>Prepared Chart Overlay Points</strong></summary>

*The following data points have been prepared for chart overlays:*

Critical voltage drops (below 440V): 456 events

### Group Annotation Points

G1: Center at 447.8V, 36535 occurrences

</details>


---

## 💡 Voltage Behavior Recommendations

• Voltage behavior appears within normal operating parameters during the analysis period.

---

# END OF REPORT

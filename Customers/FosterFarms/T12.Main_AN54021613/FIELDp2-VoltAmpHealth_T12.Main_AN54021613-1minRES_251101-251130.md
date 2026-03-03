# VOLTAGE & CURRENT HEALTH ANALYSIS

*Electromagnetic Field Analysis: Voltage (E-field), Current (H-field), and Thermal Burden*

**Transformer:** T12.Main  
**Generated:** 2026-01-27 14:32:05  
**Data Source:** AN54021613-V-1minRES_44685CLP_251101-251130zth.csv  

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
- **Average Voltage:** 467.4V
- **Minimum Voltage:** 0.0V
- **Maximum Voltage:** 495.2V
- **Standard Deviation:** 27.06V

</details>

### Operating Mean Voltage vs Nominal (480V)

- **Operating Mean:** 467.4V (12.6V, 2.63% below nominal)

*📌 Note: Lower mean voltage for the same kW raises current, increasing BTU/hr and contributing to higher VHI.*

### Voltage Deviation Analysis

| Deviation Level | Readings | Percentage |
| --------------- | -------- | ---------- |
| Under 0% (below 480V) | 33,765 | 78.05% |
| Over 0% (above 480V) | 9,495 | 21.95% |


---

## ⚡ Voltage Drop Group Detection

<details>
<summary><strong>Group Detection Analysis</strong></summary>

**Voltage Drop Groups Detected:** 1

### T12.MAIN Group Index

| Group ID | Drop Count | Voltage Range | Amp Range | ΔV | Est. Stall Amps | Estimated HP | Motor Behavior Classification | Days |
| -------- | ---------: | ------------- | --------: | ------: | ---------: | ----------: | --------------------------- | ---: |
| G1 | 41431 | 444.8–460.8V | 1181.2–2543.5A | 11.2 | 1865.6 | 290 | Critical Duty | 22 |

### T12.MAIN Group Nominal Drop Points

G1: Center at 452.8V, 41431 occurrences

</details>


---

## 🔍 Device Inference and Stress Analysis

<details>
<summary><strong>VHI Analysis & Device Stress Indicators</strong></summary>

### Voltage Heat Index (VHI) Analysis

- **Average VHI:** 19.64
- **Maximum VHI:** 960.00
- **High VHI Events (>5.0):** 28,495


</details>


---

## 📊 Chart Overlay Data Preparation

<details>
<summary><strong>Prepared Chart Overlay Points</strong></summary>

*The following data points have been prepared for chart overlays:*

Critical voltage drops (below 440V): 120 events

### Group Annotation Points

G1: Center at 452.8V, 41431 occurrences

</details>


---

## 💡 Voltage Behavior Recommendations

• Voltage behavior appears within normal operating parameters during the analysis period.

---

# END OF REPORT

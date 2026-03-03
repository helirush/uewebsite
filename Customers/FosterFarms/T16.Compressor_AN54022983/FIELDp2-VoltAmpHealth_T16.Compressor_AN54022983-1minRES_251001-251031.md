# VOLTAGE & CURRENT HEALTH ANALYSIS

*Electromagnetic Field Analysis: Voltage (E-field), Current (H-field), and Thermal Burden*

**Transformer:** T16.Compressor  
**Generated:** 2026-01-06 13:48:44  
**Data Source:** AN54022983-V-1minRES_44640CLP_251001-251031zth.csv  

## 📊 Analysis Period

- **Period:** October 01, 2025 thru October 31, 2025
- **Number of Days:** 31 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 44,640

## 🔋 Facility Information

- **Transformer Capacity:** 2,500 kVA
- **Nominal Voltage:** 480V (3-Phase)
- **Analysis Type:** Voltage & Current Health + Thermal Burden Assessment
- **Technology Focus:** Unity Energy MPTS Solutions

---

## 📈 Voltage Statistics

<details>
<summary><strong>Basic Voltage Metrics</strong></summary>

- **Total Voltage Readings Analyzed:** 44,640
- **Average Voltage:** 471.6V
- **Minimum Voltage:** 0.0V
- **Maximum Voltage:** 502.9V
- **Standard Deviation:** 31.95V

</details>

### Operating Mean Voltage vs Nominal (480V)

- **Operating Mean:** 471.6V (8.4V, 1.75% below nominal)

*📌 Note: Lower mean voltage for the same kW raises current, increasing BTU/hr and contributing to higher VHI.*

### Voltage Deviation Analysis

| Deviation Level | Readings | Percentage |
| --------------- | -------- | ---------- |
| Under 0% (below 480V) | 32,738 | 73.34% |
| Over 0% (above 480V) | 11,902 | 26.66% |


---

## ⚡ Voltage Drop Group Detection

<details>
<summary><strong>Group Detection Analysis</strong></summary>

**Voltage Drop Groups Detected:** 1

### T16.COMPRESSOR Group Index

| Group ID | Drop Count | Voltage Range | Amp Range | ΔV | Est. Stall Amps | Estimated HP | Motor Behavior Classification | Days |
| -------- | ---------: | ------------- | --------: | ------: | ---------: | ----------: | --------------------------- | ---: |
| G1 | 9385 | 451.9–460.8V | 1383.2–2046.8A | 4.1 | 1915.4 | 300 | Critical Duty | 21 |

### T16.COMPRESSOR Group Nominal Drop Points

G1: Center at 456.4V, 9385 occurrences

</details>


---

## 🔍 Device Inference and Stress Analysis

<details>
<summary><strong>VHI Analysis & Device Stress Indicators</strong></summary>

### Voltage Heat Index (VHI) Analysis

- **Average VHI:** 14.79
- **Maximum VHI:** 960.00
- **High VHI Events (>5.0):** 28,131


</details>


---

## 📊 Chart Overlay Data Preparation

<details>
<summary><strong>Prepared Chart Overlay Points</strong></summary>

*The following data points have been prepared for chart overlays:*

Critical voltage drops (below 440V): 181 events

### Group Annotation Points

G1: Center at 456.4V, 9385 occurrences

</details>


---

## 💡 Voltage Behavior Recommendations

• Voltage behavior appears within normal operating parameters during the analysis period.

---

# END OF REPORT

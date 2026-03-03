# VOLTAGE & CURRENT HEALTH ANALYSIS

*Electromagnetic Field Analysis: Voltage (E-field), Current (H-field), and Thermal Burden*

**Transformer:** T12.Main  
**Generated:** 2026-01-06 13:47:40  
**Data Source:** AN54021613-V-1minRES_44640CLP_251001-251031zth.csv  

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
- **Average Voltage:** 462.8V
- **Minimum Voltage:** 0.0V
- **Maximum Voltage:** 493.2V
- **Standard Deviation:** 33.91V

</details>

### Operating Mean Voltage vs Nominal (480V)

- **Operating Mean:** 462.8V (17.2V, 3.59% below nominal)

*📌 Note: Lower mean voltage for the same kW raises current, increasing BTU/hr and contributing to higher VHI.*

### Voltage Deviation Analysis

| Deviation Level | Readings | Percentage |
| --------------- | -------- | ---------- |
| Under 0% (below 480V) | 37,905 | 84.91% |
| Over 0% (above 480V) | 6,735 | 15.09% |


---

## ⚡ Voltage Drop Group Detection

<details>
<summary><strong>Group Detection Analysis</strong></summary>

**Voltage Drop Groups Detected:** 3

### T12.MAIN Group Index

| Group ID | Drop Count | Voltage Range | Amp Range | ΔV | Est. Stall Amps | Estimated HP | Motor Behavior Classification | Days |
| -------- | ---------: | ------------- | --------: | ------: | ---------: | ----------: | --------------------------- | ---: |
| G1 | 55449 | 444.8–460.8V | 1224.4–2260.1A | 11.2 | 1837.3 | 290 | Critical Duty | 27 |
| G2 | 1 | 434.0–434.0V | 1841.3–1841.3A | 22.0 | 1841.3 | 240 | Intermittent | 1 |
| G3 | 1 | 440.8–440.8V | 1912.8–1912.8A | 15.2 | 1912.8 | 250 | Intermittent | 1 |

### T12.MAIN Group Nominal Drop Points

G1: Center at 452.8V, 55449 occurrences
G2: Center at 434.0V, 1 occurrences
G3: Center at 440.8V, 1 occurrences

</details>


---

## 🔍 Device Inference and Stress Analysis

<details>
<summary><strong>VHI Analysis & Device Stress Indicators</strong></summary>

### Voltage Heat Index (VHI) Analysis

- **Average VHI:** 26.59
- **Maximum VHI:** 960.00
- **High VHI Events (>5.0):** 34,122


</details>


---

## 📊 Chart Overlay Data Preparation

<details>
<summary><strong>Prepared Chart Overlay Points</strong></summary>

*The following data points have been prepared for chart overlays:*

Critical voltage drops (below 440V): 215 events

### Group Annotation Points

G1: Center at 452.8V, 55449 occurrences
G2: Center at 434.0V, 1 occurrences
G3: Center at 440.8V, 1 occurrences

</details>


---

## 💡 Voltage Behavior Recommendations

• Multiple voltage drop groups detected - consider load balancing analysis and power quality assessment.

---

# END OF REPORT

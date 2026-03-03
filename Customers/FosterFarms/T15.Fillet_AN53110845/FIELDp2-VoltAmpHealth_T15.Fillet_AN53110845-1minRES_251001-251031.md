# VOLTAGE & CURRENT HEALTH ANALYSIS

*Electromagnetic Field Analysis: Voltage (E-field), Current (H-field), and Thermal Burden*

**Transformer:** T15.Fillet  
**Generated:** 2026-01-06 13:46:18  
**Data Source:** AN53110845-V-1minRES_44640CLP_251001-251031zth.csv  

## 📊 Analysis Period

- **Period:** October 01, 2025 thru October 31, 2025
- **Number of Days:** 31 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 44,639

## 🔋 Facility Information

- **Transformer Capacity:** 2,500 kVA
- **Nominal Voltage:** 480V (3-Phase)
- **Analysis Type:** Voltage & Current Health + Thermal Burden Assessment
- **Technology Focus:** Unity Energy MPTS Solutions

---

## 📈 Voltage Statistics

<details>
<summary><strong>Basic Voltage Metrics</strong></summary>

- **Total Voltage Readings Analyzed:** 44,639
- **Average Voltage:** 475.5V
- **Minimum Voltage:** 0.0V
- **Maximum Voltage:** 502.5V
- **Standard Deviation:** 32.37V

</details>

### Operating Mean Voltage vs Nominal (480V)

- **Operating Mean:** 475.5V (4.5V, 0.95% below nominal)

*📌 Note: Lower mean voltage for the same kW raises current, increasing BTU/hr and contributing to higher VHI.*

### Voltage Deviation Analysis

| Deviation Level | Readings | Percentage |
| --------------- | -------- | ---------- |
| Under 0% (below 480V) | 29,116 | 65.23% |
| Over 0% (above 480V) | 15,523 | 34.77% |


---

## ⚡ Voltage Drop Group Detection

<details>
<summary><strong>Group Detection Analysis</strong></summary>

**Voltage Drop Groups Detected:** 10

### T15.FILLET Group Index

| Group ID | Drop Count | Voltage Range | Amp Range | ΔV | Est. Stall Amps | Estimated HP | Motor Behavior Classification | Days |
| -------- | ---------: | ------------- | --------: | ------: | ---------: | ----------: | --------------------------- | ---: |
| G1 | 76 | 458.4–460.8V | 1491.7–1857.3A | -2.4 | 1654.1 | 260 | Light Duty | 3 |
| G2 | 8 | 413.1–418.4V | 1296.2–1672.8A | 42.9 | 1533.6 | 170 | Intermittent | 7 |
| G3 | 7 | 421.1–426.9V | 314.6–1772.2A | 34.9 | 1391.3 | 150 | Intermittent | 7 |
| G4 | 3 | 405.6–406.6V | 1128.2–1528.7A | 50.4 | 1326.5 | 140 | Intermittent | 3 |
| G5 | 3 | 439.6–441.1V | 228.7–1112.5A | 16.4 | 758.0 | 100 | Intermittent | 2 |
| G6 | 3 | 445.2–447.5V | 239.7–1622.3A | 10.8 | 1146.8 | 150 | Intermittent | 2 |
| G7 | 2 | 394.1–394.3V | 1187.4–1641.7A | 61.9 | 1414.5 | 150 | Intermittent | 2 |
| G8 | 2 | 408.7–408.8V | 1421.1–1639.5A | 47.3 | 1530.3 | 170 | Intermittent | 2 |
| G9 | 2 | 429.5–431.5V | 198.3–1498.4A | 26.5 | 848.3 | 90 | Intermittent | 2 |
| G10 | 1 | 390.4–390.4V | 1446.9–1446.9A | 65.6 | 1446.9 | 150 | Intermittent | 1 |

### T15.FILLET Group Nominal Drop Points

G1: Center at 459.6V, 76 occurrences
G2: Center at 415.8V, 8 occurrences
G3: Center at 424.0V, 7 occurrences
G4: Center at 406.1V, 3 occurrences
G5: Center at 440.4V, 3 occurrences
G6: Center at 446.4V, 3 occurrences
G7: Center at 394.2V, 2 occurrences
G8: Center at 408.8V, 2 occurrences
G9: Center at 430.5V, 2 occurrences
G10: Center at 390.4V, 1 occurrences

</details>


---

## 🔍 Device Inference and Stress Analysis

<details>
<summary><strong>VHI Analysis & Device Stress Indicators</strong></summary>

### Voltage Heat Index (VHI) Analysis

- **Average VHI:** 10.49
- **Maximum VHI:** 960.00
- **High VHI Events (>5.0):** 23,345

### ⚠️ Critical Voltage Stress Indicators

**Critical voltage groups detected:** 5

*These voltage levels may indicate:*

- Motor starting stress events
- Transformer overloading conditions
- Potential device failure precursors
- Power quality degradation


</details>


---

## 📊 Chart Overlay Data Preparation

<details>
<summary><strong>Prepared Chart Overlay Points</strong></summary>

*The following data points have been prepared for chart overlays:*

Critical voltage drops (below 440V): 214 events

### Group Annotation Points

G1: Center at 459.6V, 76 occurrences
G2: Center at 415.7V, 8 occurrences
G3: Center at 424.0V, 7 occurrences
G4: Center at 406.1V, 3 occurrences
G5: Center at 440.4V, 3 occurrences
G6: Center at 446.3V, 3 occurrences
G7: Center at 394.2V, 2 occurrences
G8: Center at 408.8V, 2 occurrences
G9: Center at 430.5V, 2 occurrences
G10: Center at 390.4V, 1 occurrences

</details>


---

## 💡 Voltage Behavior Recommendations

• Multiple voltage drop groups detected - consider load balancing analysis and power quality assessment.

---

# END OF REPORT

# VOLTAGE & CURRENT HEALTH ANALYSIS

*Electromagnetic Field Analysis: Voltage (E-field), Current (H-field), and Thermal Burden*

**Transformer:** T15.Fillet  
**Generated:** 2026-01-27 14:28:40  
**Data Source:** AN53110845-V-1minRES_44696CLP_251101-251130zth.csv  

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
- **Average Voltage:** 479.7V
- **Minimum Voltage:** 0.0V
- **Maximum Voltage:** 504.4V
- **Standard Deviation:** 27.12V

</details>

### Operating Mean Voltage vs Nominal (480V)

- **Operating Mean:** 479.7V (0.3V, 0.05% below nominal)

*📌 Note: Lower mean voltage for the same kW raises current, increasing BTU/hr and contributing to higher VHI.*

### Voltage Deviation Analysis

| Deviation Level | Readings | Percentage |
| --------------- | -------- | ---------- |
| Under 0% (below 480V) | 22,007 | 50.87% |
| Over 0% (above 480V) | 21,253 | 49.13% |


---

## ⚡ Voltage Drop Group Detection

<details>
<summary><strong>Group Detection Analysis</strong></summary>

**Voltage Drop Groups Detected:** 12

### T15.FILLET Group Index

| Group ID | Drop Count | Voltage Range | Amp Range | ΔV | Est. Stall Amps | Estimated HP | Motor Behavior Classification | Days |
| -------- | ---------: | ------------- | --------: | ------: | ---------: | ----------: | --------------------------- | ---: |
| G1 | 41713 | 463.5–477.3V | 283.1–2049.6A | 8.9 | 1461.2 | 230 | Critical Duty | 25 |
| G2 | 14 | 414.8–422.7V | 317.7–1575.2A | 57.5 | 1210.9 | 120 | Intermittent | 10 |
| G3 | 4 | 410.3–412.6V | 1142.5–1609.9A | 62.0 | 1336.8 | 140 | Intermittent | 3 |
| G4 | 4 | 433.5–436.9V | 285.8–1606.2A | 38.8 | 735.9 | 80 | Intermittent | 4 |
| G5 | 3 | 424.7–428.2V | 748.2–1359.6A | 47.6 | 1145.2 | 130 | Intermittent | 2 |
| G6 | 2 | 405.6–407.0V | 1225.7–1498.0A | 66.8 | 1361.8 | 140 | Intermittent | 2 |
| G7 | 1 | 384.6–384.6V | 1124.4–1124.4A | 87.7 | 1124.4 | 110 | Intermittent | 1 |
| G8 | 1 | 398.2–398.2V | 1005.3–1005.3A | 74.2 | 1005.3 | 100 | Intermittent | 1 |
| G9 | 1 | 430.6–430.6V | 1272.3–1272.3A | 41.7 | 1272.3 | 140 | Intermittent | 1 |
| G10 | 1 | 439.2–439.2V | 246.0–246.0A | 33.2 | 246.0 | 20 | Intermittent | 1 |
| G11 | 1 | 442.2–442.2V | 293.2–293.2A | 30.1 | 293.2 | 30 | Intermittent | 1 |
| G12 | 1 | 457.9–457.9V | 599.4–599.4A | 14.5 | 599.4 | 70 | Intermittent | 1 |

### T15.FILLET Group Nominal Drop Points

G1: Center at 470.4V, 41713 occurrences
G2: Center at 418.8V, 14 occurrences
G3: Center at 411.5V, 4 occurrences
G4: Center at 435.2V, 4 occurrences
G5: Center at 426.4V, 3 occurrences
G6: Center at 406.3V, 2 occurrences
G7: Center at 384.6V, 1 occurrences
G8: Center at 398.2V, 1 occurrences
G9: Center at 430.6V, 1 occurrences
G10: Center at 439.2V, 1 occurrences
G11: Center at 442.2V, 1 occurrences
G12: Center at 457.9V, 1 occurrences

</details>


---

## 🔍 Device Inference and Stress Analysis

<details>
<summary><strong>VHI Analysis & Device Stress Indicators</strong></summary>

### Voltage Heat Index (VHI) Analysis

- **Average VHI:** 23.68
- **Maximum VHI:** 994.40
- **High VHI Events (>5.0):** 39,027

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

Critical voltage drops (below 440V): 151 events

### Group Annotation Points

G1: Center at 470.4V, 41713 occurrences
G2: Center at 418.8V, 14 occurrences
G3: Center at 411.5V, 4 occurrences
G4: Center at 435.2V, 4 occurrences
G5: Center at 426.5V, 3 occurrences
G6: Center at 406.3V, 2 occurrences
G7: Center at 384.6V, 1 occurrences
G8: Center at 398.2V, 1 occurrences
G9: Center at 430.6V, 1 occurrences
G10: Center at 439.2V, 1 occurrences
G11: Center at 442.2V, 1 occurrences
G12: Center at 457.9V, 1 occurrences

</details>


---

## 💡 Voltage Behavior Recommendations

• Multiple voltage drop groups detected - consider load balancing analysis and power quality assessment.

---

# END OF REPORT

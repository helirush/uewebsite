# VOLTAGE & CURRENT HEALTH ANALYSIS

*Electromagnetic Field Analysis: Voltage (E-field), Current (H-field), and Thermal Burden*

**Transformer:** Deli F  
**Generated:** 2026-03-09 17:27:50  
**Data Source:** AN55050323-V-1minRES_40320CLP_260201-260228c.csv  

## 📊 Analysis Period

- **Period:** February 01, 2026 thru February 28, 2026
- **Number of Days:** 28 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 40,320

## 🔋 Facility Information

- **Transformer Capacity:** 2,500 kVA
- **Nominal Voltage:** 480V (3-Phase)
- **Analysis Type:** Voltage & Current Health + Thermal Burden Assessment
- **Technology Focus:** Unity Energy MPTS Solutions

---

## 📈 Voltage Statistics

<details>
<summary><strong>Basic Voltage Metrics</strong></summary>

- **Total Voltage Readings Analyzed:** 40,320
- **Average Voltage:** 480.9V
- **Minimum Voltage:** 0.0V
- **Maximum Voltage:** 499.9V
- **Standard Deviation:** 15.23V

</details>

### Operating Mean Voltage vs Nominal (480V)

- **Operating Mean:** 480.9V (0.9V, 0.18% above nominal)

*📌 Note: Lower mean voltage for the same kW raises current, increasing BTU/hr and contributing to higher VHI.*

### Voltage Deviation Analysis

| Deviation Band | Readings | Percentage |
| -------------- | -------: | ---------: |
| Below 460V | 42 | 0.10% |
| 460–470V | 36 | 0.09% |
| 470–480V | 12,533 | 31.08% |
| 480–490V | 27,698 | 68.70% |
| 490–500V | 11 | 0.03% |
| 500V+ | 0 | 0.00% |

**Threshold highlights (cumulative):**
- Below 470V: 78 (0.19%)
- Below 460V: 42 (0.10%)
- Above 490V: 11 (0.03%)
- Above 500V: 0 (0.00%)


---

## ⚡ Voltage Drop Group Detection

<details>
<summary><strong>Group Detection Analysis</strong></summary>

**Voltage Drop Groups Detected:** 2

### DELI F Group Index

| Group ID | Drop Count | Voltage Range | Amp Range | ΔV | Est. Stall Amps | Estimated HP | Motor Behavior Classification | Days |
| -------- | ---------: | ------------- | --------: | ------: | ---------: | ----------: | --------------------------- | ---: |
| G1 | 8 | 458.0–458.3V | 872.8–1811.2A | -2.0 | 1342.0 | 210 | Intermittent | 2 |
| G2 | 1 | 446.8–446.8V | 1601.2–1601.2A | 9.2 | 1601.2 | 210 | Intermittent | 1 |

### DELI F Group Nominal Drop Points

G1: Center at 458.1V, 8 occurrences
G2: Center at 446.8V, 1 occurrences

</details>


---

## 🔍 Device Inference and Stress Analysis

<details>
<summary><strong>VHI Analysis & Device Stress Indicators</strong></summary>

### Voltage Heat Index (VHI) Analysis

- **Average VHI:** 1.54
- **Maximum VHI:** 960.00
- **High VHI Events (>5.0):** 684


</details>


---

## 📊 Chart Overlay Data Preparation

<details>
<summary><strong>Prepared Chart Overlay Points</strong></summary>

*The following data points have been prepared for chart overlays:*

Critical voltage drops (below 440V): 39 events

### Group Annotation Points

G1: Center at 458.2V, 8 occurrences
G2: Center at 446.8V, 1 occurrences

</details>


---

## 💡 Voltage Behavior Recommendations

• Voltage behavior appears within normal operating parameters during the analysis period.

---

# END OF REPORT

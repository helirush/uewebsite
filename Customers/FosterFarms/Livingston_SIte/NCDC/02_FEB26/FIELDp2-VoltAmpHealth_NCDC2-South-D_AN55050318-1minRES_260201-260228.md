# VOLTAGE & CURRENT HEALTH ANALYSIS

*Electromagnetic Field Analysis: Voltage (E-field), Current (H-field), and Thermal Burden*

**Transformer:** NCDC2 South D  
**Generated:** 2026-03-10 00:49:33  
**Data Source:** AN55050318-V-1minRES_40320CLP_260201-260228c.csv  

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
- **Average Voltage:** 481.6V
- **Minimum Voltage:** 0.0V
- **Maximum Voltage:** 499.8V
- **Standard Deviation:** 5.60V

</details>

### Operating Mean Voltage vs Nominal (480V)

- **Operating Mean:** 481.6V (1.6V, 0.34% above nominal)

*📌 Note: Lower mean voltage for the same kW raises current, increasing BTU/hr and contributing to higher VHI.*

### Voltage Deviation Analysis

| Deviation Band | Readings | Percentage |
| -------------- | -------: | ---------: |
| Below 460V | 6 | 0.01% |
| 460–470V | 6 | 0.01% |
| 470–480V | 6,552 | 16.25% |
| 480–490V | 33,749 | 83.70% |
| 490–500V | 7 | 0.02% |
| 500V+ | 0 | 0.00% |

**Threshold highlights (cumulative):**
- Below 470V: 12 (0.03%)
- Below 460V: 6 (0.01%)
- Above 490V: 7 (0.02%)
- Above 500V: 0 (0.00%)


---

## ⚡ Voltage Drop Group Detection

<details>
<summary><strong>Group Detection Analysis</strong></summary>

**Voltage Drop Groups Detected:** 1

### NCDC2 SOUTH D Group Index

| Group ID | Drop Count | Voltage Range | Amp Range | ΔV | Est. Stall Amps | Estimated HP | Motor Behavior Classification | Days |
| -------- | ---------: | ------------- | --------: | ------: | ---------: | ----------: | --------------------------- | ---: |
| G1 | 1 | 452.1–452.1V | 2736.5–2736.5A | 3.9 | 2736.5 | 360 | Intermittent | 1 |

### NCDC2 SOUTH D Group Nominal Drop Points

G1: Center at 452.1V, 1 occurrences

</details>


---

## 🔍 Device Inference and Stress Analysis

<details>
<summary><strong>VHI Analysis & Device Stress Indicators</strong></summary>

### Voltage Heat Index (VHI) Analysis

- **Average VHI:** 0.24
- **Maximum VHI:** 960.00
- **High VHI Events (>5.0):** 12


</details>


---

## 📊 Chart Overlay Data Preparation

<details>
<summary><strong>Prepared Chart Overlay Points</strong></summary>

*The following data points have been prepared for chart overlays:*

Critical voltage drops (below 440V): 5 events

### Group Annotation Points

G1: Center at 452.1V, 1 occurrences

</details>


---

## 💡 Voltage Behavior Recommendations

• Voltage behavior appears within normal operating parameters during the analysis period.

---

# END OF REPORT

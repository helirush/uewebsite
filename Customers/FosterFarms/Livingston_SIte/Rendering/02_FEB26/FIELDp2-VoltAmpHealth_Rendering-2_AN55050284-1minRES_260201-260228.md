# VOLTAGE & CURRENT HEALTH ANALYSIS

*Electromagnetic Field Analysis: Voltage (E-field), Current (H-field), and Thermal Burden*

**Transformer:** Rendering-2  
**Generated:** 2026-03-05 11:21:10  
**Data Source:** AN55050284-V-1minRES_40320CLP_260201-260228c.csv  

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
- **Average Voltage:** 471.4V
- **Minimum Voltage:** 0.0V
- **Maximum Voltage:** 490.1V
- **Standard Deviation:** 7.41V

</details>

### Operating Mean Voltage vs Nominal (480V)

- **Operating Mean:** 471.4V (8.6V, 1.80% below nominal)

*📌 Note: Lower mean voltage for the same kW raises current, increasing BTU/hr and contributing to higher VHI.*

### Voltage Deviation Analysis

| Deviation Band | Readings | Percentage |
| -------------- | -------: | ---------: |
| Below 460V | 14 | 0.03% |
| 460–470V | 22,725 | 56.36% |
| 470–480V | 12,168 | 30.18% |
| 480–490V | 5,412 | 13.42% |
| 490–500V | 1 | 0.00% |
| 500V+ | 0 | 0.00% |

**Threshold highlights (cumulative):**
- Below 470V: 22,739 (56.40%)
- Below 460V: 14 (0.03%)
- Above 490V: 1 (0.00%)
- Above 500V: 0 (0.00%)


---

## ⚡ Voltage Drop Group Detection

<details>
<summary><strong>Group Detection Analysis</strong></summary>

**Voltage Drop Groups Detected:** 1

### RENDERING-2 Group Index

| Group ID | Drop Count | Voltage Range | Amp Range | ΔV | Est. Stall Amps | Estimated HP | Motor Behavior Classification | Days |
| -------- | ---------: | ------------- | --------: | ------: | ---------: | ----------: | --------------------------- | ---: |
| G1 | 2 | 450.9–452.5V | 2033.0–2108.9A | 28.3 | 345 | 275 | Intermittent | 2 |

### RENDERING-2 Group Nominal Drop Points

G1: Center at 451.7V, 2 occurrences

*Note: One group of minor voltage variations (454-460V) was excluded as normal operational fluctuations.*

</details>


---

## 🔍 Device Inference and Stress Analysis

<details>
<summary><strong>VHI Analysis & Device Stress Indicators</strong></summary>

### Voltage Heat Index (VHI) Analysis

- **Average VHI:** 10.95
- **Maximum VHI:** 960.00
- **High VHI Events (>5.0):** 32,387


</details>


---

## 📊 Chart Overlay Data Preparation

<details>
<summary><strong>Prepared Chart Overlay Points</strong></summary>

*The following data points have been prepared for chart overlays:*

Critical voltage drops (below 440V): 4 events

### Group Annotation Points

G1: Center at 457.6V, 44 occurrences
G2: Center at 451.7V, 2 occurrences

</details>


---

## 💡 Voltage Behavior Recommendations

• Voltage behavior appears within normal operating parameters during the analysis period.

---

# END OF REPORT

# VOLTAGE & CURRENT HEALTH ANALYSIS

*Electromagnetic Field Analysis: Voltage (E-field), Current (H-field), and Thermal Burden*

**Transformer:** T16.Compressor  
**Generated:** 2026-01-27 14:33:30  
**Data Source:** AN54022983-V-1minRES_43260CLP_251101-251130zth.csv  

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
- **Average Voltage:** 476.2V
- **Minimum Voltage:** 0.0V
- **Maximum Voltage:** 504.3V
- **Standard Deviation:** 27.49V

</details>

### Operating Mean Voltage vs Nominal (480V)

- **Operating Mean:** 476.2V (3.8V, 0.79% below nominal)

*📌 Note: Lower mean voltage for the same kW raises current, increasing BTU/hr and contributing to higher VHI.*

### Voltage Deviation Analysis

| Deviation Level | Readings | Percentage |
| --------------- | -------- | ---------- |
| Under 0% (below 480V) | 25,749 | 59.52% |
| Over 0% (above 480V) | 17,511 | 40.48% |


---

## ⚡ Voltage Drop Group Detection

<details>
<summary><strong>Group Detection Analysis</strong></summary>

**Voltage Drop Groups Detected:** 1

### T16.COMPRESSOR Group Index

| Group ID | Drop Count | Voltage Range | Amp Range | ΔV | Est. Stall Amps | Estimated HP | Motor Behavior Classification | Days |
| -------- | ---------: | ------------- | --------: | ------: | ---------: | ----------: | --------------------------- | ---: |
| G1 | 37696 | 456.6–476.0V | 860.3–1998.2A | 14.4 | 1460.8 | 190 | Critical Duty | 26 |

### T16.COMPRESSOR Group Nominal Drop Points

G1: Center at 466.3V, 37696 occurrences

</details>


---

## 🔍 Device Inference and Stress Analysis

<details>
<summary><strong>VHI Analysis & Device Stress Indicators</strong></summary>

### Voltage Heat Index (VHI) Analysis

- **Average VHI:** 26.63
- **Maximum VHI:** 991.65
- **High VHI Events (>5.0):** 38,982


</details>


---

## 📊 Chart Overlay Data Preparation

<details>
<summary><strong>Prepared Chart Overlay Points</strong></summary>

*The following data points have been prepared for chart overlays:*

Critical voltage drops (below 440V): 121 events

### Group Annotation Points

G1: Center at 466.3V, 37696 occurrences

</details>


---

## 💡 Voltage Behavior Recommendations

• Voltage behavior appears within normal operating parameters during the analysis period.

---

# END OF REPORT

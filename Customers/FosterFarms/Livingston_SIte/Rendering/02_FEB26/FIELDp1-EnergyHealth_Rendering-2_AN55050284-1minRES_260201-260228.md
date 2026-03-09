# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 594,713.1 kWh (Usage per period)
- **Consumption Cost per unit:** $0.175/kWh (Cost per kWh)
- **Consumption Total Cost:** $103,896.38 (Cost per period)
- **Consumption Total Cost:** $196.85 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** Rendering-2  
**Generated:** 2026-03-05 11:21:00  
**Data Source:** AN55050284-V-1minRES_40320CLP_260201-260228c.csv  

## Time Period

- **Period:** February 01, 2026 thru February 28, 2026
- **Number of Days:** 27 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 31,667

- **Dataset Coverage:** Complete month (96.4% of 28-day month)
- **Billing Scale Factor:** 1.000x (no normalization needed)

## Facility Information

- **Facility:** Foster Farms
- **Location:** Livingston HQ Facility
- **Analysis Type:** Energy Field Performance Assessment
- **Technology Focus:** Unity Energy Management Solutions

---

## Executive Summary

*Brief overview of key transformer performance metrics and energy consumption.*

- **Transformer:** Rendering-2
- **Power Factor:** 0.718
- **Total Energy (Actual):** 594,713.12 kWh (per period), 1126.81 kW (per hour)
- **Total Waste (Actual):** 232,405.20 kWh (per period), 440.34 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_Rendering-2_AN55050284-1minRES_260201-260228.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_Rendering-2_AN55050284-1minRES_260201-260228.md


## UNITY MANAGEMENT Rendering-2 SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 440.34 kW/hr
- **Blended Electricity Rate:** $0.1747/kWh (all-inclusive)
- **Rendering-2 Utility Cost Offset:** $76.93/hour
- **Annual Offset Savings:** $673887/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 1,724,317 BTU/hr
- **Total Cooling kW No Longer Needed:** 151.24 kW
- **Cooling Energy Cost Avoided:** $26.42/hour
- **Annual Cooling Savings:** $231448/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 591.58 kW
- **CO2e Emissions Avoided:** 1934.56 metric tons/year
- **Monthly CO2e Reduction:** 161.21 metric tons/month
- **Hourly CO2e Reduction:** 0.2208 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $74481/year

### Total Rendering-2 Unity Savings

- **Per Hour:** $111.85
- **Per Day:** $2684.43
- **Per Month:** $80532.85
- **Per Year:** $979816

### Rendering-2 Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 1,409.8 kVAR Max (Avg: 1,089.2 kVAR/hr ; 784,195 kVAR/mo)
- **Max Harmonic Distortion:** 32.2% Max (range: 3.3% - 32.2%)
- **Max Amperage:** 2,672A Max (range: 1310A - 2672A)

---

# Rendering-2 DETAILED PERFORMANCE ANALYSIS

## Unity Technology Status

- **Unity Technology Configuration:** 0.0% reactive energy target
- **Unity Applied:** No (measuring current problem state)
- **Analysis Mode:** Pre-Unity baseline analysis

## Transformer Specifications

- **Capacity:** 2,500 kVA
- **Voltage:** 480V, 3-Phase

## Fundamental Energy Values

| Metric | Average | MIN | MAX |
| ------ | ------- | --- | --- |
| Line to Neutral Voltage (277v) |   270.67 |   260.35 |   282.98 |
| Line to Line Voltage (480v) |   468.81 |   450.93 |   490.13 |
| Current (AMPS) |  1930.58 |  1309.68 |  2671.86 |
| Phase Angle (degrees) |    44.07 |    38.74 |    53.27 |
| Total Harmonic Distortion (PCT) |    16.65 |     3.31 |    32.24 |

## 🔀 Total Harmonic Distortion — Unity Translation

In traditional electrical engineering, Total Harmonic Distortion (THD) is calculated per phase, based on the sum of non-fundamental frequency components divided by the fundamental:

```
THD_A = √(V₂² + V₃² + ...) / V₁
```

This results in a percentage value for each phase (A, B, and C), and by standard IEEE practice, these percentages are not directly additive because they are non-linear and phase-relative.

However, at Unity, we take a **field-level view of harmonic behavior** — aligning with Maxwell's electromagnetic theory rather than purely scalar wave math.

We define:

```
THD_Field_Composite = THD_A + THD_B + THD_C
```

This is not a textbook THD, but a **Unity Composite Index** — a metric designed to:
• Reflect total harmonic stress on the energy field,
• Enable fast field diagnostics,
• Map distortion across the 3-phase envelope as a combined entity.

Think of it as a **harmonic heat index**, not a scalar voltage quantity.

| Metric | Value | Notes |
| ------ | ----- | ----- |
| THD Phase A (%) | 5.5% | IEEE standard per-phase calculation |
| THD Phase B (%) | 5.6% | IEEE standard per-phase calculation |
| THD Phase C (%) | 5.6% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 16.6% | Field-level stress indicator |
| Max Phase THD | 5.6% | Highest THD among all three phases |
| Min Phase THD | 5.5% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 1,457.67 kW
  - **Maximum Load:** 1,976.93 kVA
  - **Percentage of Capacity (MAX):** 79.1%
- **Average Load:** 1,567.16 kVA
  - **Percentage of Capacity (Avg):** 62.7%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 1,567.16 kVA
- **Average Power Factor (PF):** 0.718

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 1,567.62 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 468.81 V
- Average Current (Iavg_A): 1930.58 A
- Average kW (Psum_kW): 1126.81 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 0.47 kVA (0.0%)
- **Calculated PF (kW/kVA from averages):** 0.719
- **Power Factor Difference:** 0.001 (0.1%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (1567.16) and measured PF (0.718) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA | 1,567.16 |        62.7% | 827,118.32 kVA | 3,844,845.93 TOTAL-HEAT |
| kW | 1,126.81 |        45.1% | 594,713.12 kWh | 1,080,331.76 Load-Heat |
| kVAR | 1,089.16 |        43.6% | 574,839.99 kVARh | - |
| WASTE |   440.34 |        17.6% | 232,405.20 WASTE | 422,177.87 Field-Heat |

### Heat Unit Notes

- **TOTAL-HEAT (BTU/hr):** 3,844,845.93
- **Load-Heat (BTU/hr):** 1,080,331.76
- **Field-Heat (BTU/hr):** 422,177.87
- **Load-Heat (BTU, period total):** 570,181,097.71
- **Field-Heat (BTU, period total):** 222,818,445.26

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 2 | 1,567.16 | 1,126.81 | 1,088.36 |     0.72 |   62.7% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 | 1,554.05 | 1,114.80 | 1,082.38 |     0.72 |   62.2% |
| 01 | 1,546.57 | 1,105.67 | 1,080.98 |     0.71 |   61.9% |
| 02 | 1,566.38 | 1,123.30 | 1,091.23 |     0.72 |   62.7% |
| 03 | 1,555.90 | 1,116.77 | 1,082.66 |     0.72 |   62.2% |
| 04 | 1,583.32 | 1,140.16 | 1,098.06 |     0.72 |   63.3% |
| 05 | 1,581.62 | 1,136.26 | 1,099.67 |     0.72 |   63.3% |
| 06 | 1,603.83 | 1,151.60 | 1,115.57 |     0.72 |   64.2% |
| 07 | 1,591.37 | 1,139.07 | 1,110.38 |     0.72 |   63.7% |
| 08 | 1,613.27 | 1,155.22 | 1,124.94 |     0.72 |   64.5% |
| 09 | 1,585.95 | 1,131.66 | 1,110.34 |     0.71 |   63.4% |
| 10 | 1,604.04 | 1,150.13 | 1,117.12 |     0.72 |   64.2% |
| 11 | 1,613.12 | 1,154.28 | 1,126.16 |     0.72 |   64.5% |
| 12 | 1,607.35 | 1,148.94 | 1,123.30 |     0.71 |   64.3% |
| 13 | 1,573.14 | 1,129.10 | 1,094.67 |     0.72 |   62.9% |
| 14 | 1,572.05 | 1,132.59 | 1,089.38 |     0.72 |   62.9% |
| 15 | 1,596.52 | 1,157.14 | 1,098.77 |     0.72 |   63.9% |
| 16 | 1,611.44 | 1,174.63 | 1,102.05 |     0.73 |   64.5% |
| 17 | 1,593.48 | 1,165.26 | 1,085.99 |     0.73 |   63.7% |
| 18 | 1,490.88 | 1,072.39 | 1,034.88 |     0.72 |   59.6% |
| 19 | 1,428.45 | 1,018.21 | 1,000.95 |     0.71 |   57.1% |
| 20 | 1,495.77 | 1,086.73 | 1,026.95 |     0.73 |   59.8% |
| 21 | 1,518.74 | 1,095.80 | 1,051.02 |     0.72 |   60.7% |
| 22 | 1,541.30 | 1,105.52 | 1,073.41 |     0.72 |   61.7% |
| 23 | 1,571.58 | 1,129.75 | 1,091.88 |     0.72 |   62.9% |

---

# END OF REPORT

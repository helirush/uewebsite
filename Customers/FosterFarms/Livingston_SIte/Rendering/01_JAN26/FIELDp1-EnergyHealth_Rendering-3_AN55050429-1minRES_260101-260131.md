# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 390,617.8 kWh (Usage per period)
- **Consumption Cost per unit:** $0.177/kWh (Cost per kWh)
- **Consumption Total Cost:** $69,022.17 (Cost per period)
- **Consumption Total Cost:** $100.71 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** Rendering-3  
**Generated:** 2026-02-26 09:45:15  
**Data Source:** AN55050429-V-1minRES_44640CLP_260101-260131c.csv  

## Time Period

- **Period:** January 01, 2026 thru January 31, 2026
- **Number of Days:** 31 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 41,122

- **Dataset Coverage:** Complete month (100.0% of 31-day month)
- **Billing Scale Factor:** 1.000x (no normalization needed)

## Facility Information

- **Facility:** Foster Farms
- **Location:** Livingston HQ Facility
- **Analysis Type:** Energy Field Performance Assessment
- **Technology Focus:** Unity Energy Management Solutions

---

## Executive Summary

*Brief overview of key transformer performance metrics and energy consumption.*

- **Transformer:** Rendering-3
- **Power Factor:** 0.767
- **Total Energy (Actual):** 390,617.81 kWh (per period), 569.94 kW (per hour)
- **Total Waste (Actual):** 118,069.59 kWh (per period), 172.27 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_Rendering-3_AN55050429-1minRES_260101-260131.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_Rendering-3_AN55050429-1minRES_260101-260131.md


## UNITY MANAGEMENT Rendering-3 SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 172.27 kW/hr
- **Blended Electricity Rate:** $0.1767/kWh (all-inclusive)
- **Rendering-3 Utility Cost Offset:** $30.44/hour
- **Annual Offset Savings:** $266659/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 638,366 BTU/hr
- **Total Cooling kW No Longer Needed:** 93.34 kW
- **Cooling Energy Cost Avoided:** $16.49/hour
- **Annual Cooling Savings:** $144483/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 265.61 kW
- **CO2e Emissions Avoided:** 868.60 metric tons/year
- **Monthly CO2e Reduction:** 72.38 metric tons/month
- **Hourly CO2e Reduction:** 0.0992 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $33441/year

### Total Rendering-3 Unity Savings

- **Per Hour:** $50.75
- **Per Day:** $1218.04
- **Per Month:** $36541.05
- **Per Year:** $444583

### Rendering-3 Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 681.2 kVAR Max (Avg: 475.4 kVAR/hr ; 342,320 kVAR/mo)
- **Max Harmonic Distortion:** 30.7% Max (range: 3.1% - 30.7%)
- **Max Amperage:** 1,086A Max (range: 720A - 1086A)

---

# Rendering-3 DETAILED PERFORMANCE ANALYSIS

## Unity Technology Status

- **Unity Technology Configuration:** 0.0% reactive energy target
- **Unity Applied:** No (measuring current problem state)
- **Analysis Mode:** Pre-Unity baseline analysis

## Transformer Specifications

- **Capacity:** 2,500.0 kVA
- **Voltage:** 480V, 3-Phase

## Fundamental Energy Values

| Metric | Average | MIN | MAX |
| ------ | ------- | --- | --- |
| Line to Neutral Voltage (277v) |   275.54 |   266.01 |   285.87 |
| Line to Line Voltage (480v) |   477.25 |   460.74 |   495.14 |
| Current (AMPS) |   897.92 |   720.22 |  1086.35 |
| Phase Angle (degrees) |    39.83 |    34.11 |    54.13 |
| Total Harmonic Distortion (PCT) |    16.41 |     3.14 |    30.70 |

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
| THD Phase B (%) | 5.5% | IEEE standard per-phase calculation |
| THD Phase C (%) | 5.5% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 16.4% | Field-level stress indicator |
| Max Phase THD | 5.5% | Highest THD among all three phases |
| Min Phase THD | 5.5% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 689.61 kW
  - **Maximum Load:** 883.31 kVA
  - **Percentage of Capacity (MAX):** 35.3%
- **Average Load:** 742.21 kVA
  - **Percentage of Capacity (Avg):** 29.7%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 742.21 kVA
- **Average Power Factor (PF):** 0.767

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 742.25 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 477.25 V
- Average Current (Iavg_A): 897.92 A
- Average kW (Psum_kW): 569.94 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 0.04 kVA (0.0%)
- **Calculated PF (kW/kVA from averages):** 0.768
- **Power Factor Difference:** 0.001 (0.1%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (742.21) and measured PF (0.767) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA |   742.21 |        29.7% | 508,687.40 kVA | 1,944,715.89 TOTAL-HEAT |
| kW |   569.94 |        22.8% | 390,617.81 kWh | 309,361,466.67 Load-Heat |
| kVAR |   475.44 |        19.0% | 325,853.65 kVARh | - |
| WASTE |   172.27 |         6.9% | 118,069.59 WASTE | 93,508,746.77 Field-Heat |

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 1 |   742.21 |   569.94 |   474.49 |     0.77 |   29.7% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   740.13 |   569.75 |   471.48 |     0.77 |   29.6% |
| 01 |   733.09 |   569.29 |   461.15 |     0.78 |   29.3% |
| 02 |   739.43 |   575.87 |   463.21 |     0.78 |   29.6% |
| 03 |   743.01 |   578.12 |   465.78 |     0.78 |   29.7% |
| 04 |   739.85 |   576.23 |   463.18 |     0.78 |   29.6% |
| 05 |   741.58 |   574.37 |   467.90 |     0.77 |   29.7% |
| 06 |   764.44 |   585.91 |   489.99 |     0.77 |   30.6% |
| 07 |   750.73 |   579.52 |   476.52 |     0.77 |   30.0% |
| 08 |   758.15 |   582.58 |   484.21 |     0.77 |   30.3% |
| 09 |   752.60 |   577.91 |   481.11 |     0.77 |   30.1% |
| 10 |   763.99 |   581.05 |   495.09 |     0.76 |   30.6% |
| 11 |   755.58 |   572.48 |   492.15 |     0.76 |   30.2% |
| 12 |   746.85 |   569.19 |   482.48 |     0.76 |   29.9% |
| 13 |   736.80 |   560.45 |   477.19 |     0.76 |   29.5% |
| 14 |   740.96 |   558.48 |   486.00 |     0.75 |   29.6% |
| 15 |   739.02 |   559.08 |   482.33 |     0.76 |   29.6% |
| 16 |   738.71 |   564.88 |   475.02 |     0.76 |   29.5% |
| 17 |   731.54 |   563.37 |   465.91 |     0.77 |   29.3% |
| 18 |   723.72 |   554.42 |   464.54 |     0.77 |   28.9% |
| 19 |   718.66 |   548.79 |   463.29 |     0.76 |   28.7% |
| 20 |   737.66 |   567.53 |   470.44 |     0.77 |   29.5% |
| 21 |   734.32 |   567.57 |   465.15 |     0.77 |   29.4% |
| 22 |   744.36 |   572.84 |   474.49 |     0.77 |   29.8% |
| 23 |   738.60 |   568.63 |   470.54 |     0.77 |   29.5% |

---

# END OF REPORT

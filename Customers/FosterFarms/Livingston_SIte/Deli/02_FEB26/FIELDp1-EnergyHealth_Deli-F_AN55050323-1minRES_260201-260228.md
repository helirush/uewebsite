# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 535,864.5 kWh (Usage per period)
- **Consumption Cost per unit:** $0.146/kWh (Cost per kWh)
- **Consumption Total Cost:** $78,343.38 (Cost per period)
- **Consumption Total Cost:** $116.70 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** Deli F  
**Generated:** 2026-03-09 17:27:43  
**Data Source:** AN55050323-V-1minRES_40320CLP_260201-260228c.csv  

## Time Period

- **Period:** February 01, 2026 thru February 28, 2026
- **Number of Days:** 28 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 40,281

- **Dataset Coverage:** Complete month (100.0% of 28-day month)
- **Billing Scale Factor:** 1.000x (no normalization needed)

## Facility Information

- **Facility:** Foster Farms
- **Location:** Livingston HQ Facility
- **Analysis Type:** Energy Field Performance Assessment
- **Technology Focus:** Unity Energy Management Solutions

---

## Executive Summary

*Brief overview of key transformer performance metrics and energy consumption.*

- **Transformer:** Deli F
- **Power Factor:** 0.869
- **Total Energy (Actual):** 535,864.46 kWh (per period), 798.19 kW (per hour)
- **Total Waste (Actual):** 65,672.54 kWh (per period), 97.82 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_Deli-F_AN55050323-1minRES_260201-260228.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_Deli-F_AN55050323-1minRES_260201-260228.md


## UNITY MANAGEMENT Deli F SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 97.82 kW/hr
- **Blended Electricity Rate:** $0.1462/kWh (all-inclusive)
- **Deli F Utility Cost Offset:** $14.30/hour
- **Annual Offset Savings:** $125281/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 352,622 BTU/hr
- **Total Cooling kW No Longer Needed:** 30.93 kW
- **Cooling Energy Cost Avoided:** $4.52/hour
- **Annual Cooling Savings:** $39607/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 128.75 kW
- **CO2e Emissions Avoided:** 421.03 metric tons/year
- **Monthly CO2e Reduction:** 35.09 metric tons/month
- **Hourly CO2e Reduction:** 0.0481 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $16210/year

### Total Deli F Unity Savings

- **Per Hour:** $20.67
- **Per Day:** $496.16
- **Per Month:** $14884.77
- **Per Year:** $181098

### Deli F Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 1,660.0 kVAR Max (Avg: 407.1 kVAR/hr ; 293,111 kVAR/mo)
- **Max Harmonic Distortion:** 28.6% Max (range: 3.0% - 28.6%)
- **Max Amperage:** 2,683A Max (range: 13A - 2683A)

---

# Deli F DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   277.90 |   257.96 |   288.59 |
| Line to Line Voltage (480v) |   481.33 |   446.80 |   499.86 |
| Current (AMPS) |  1077.28 |    12.64 |  2682.78 |
| Phase Angle (degrees) |    29.17 |     0.00 |    80.68 |
| Total Harmonic Distortion (PCT) |    14.71 |     3.00 |    28.57 |

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
| THD Phase A (%) | 4.9% | IEEE standard per-phase calculation |
| THD Phase B (%) | 4.9% | IEEE standard per-phase calculation |
| THD Phase C (%) | 4.9% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 14.7% | Field-level stress indicator |
| Max Phase THD | 4.9% | Highest THD among all three phases |
| Min Phase THD | 4.9% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 1,767.62 kW
  - **Maximum Load:** 2,165.46 kVA
  - **Percentage of Capacity (MAX):** 86.6%
- **Average Load:** 896.01 kVA
  - **Percentage of Capacity (Avg):** 35.8%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 896.01 kVA
- **Average Power Factor (PF):** 0.869

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 898.13 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 481.33 V
- Average Current (Iavg_A): 1077.28 A
- Average kW (Psum_kW): 798.19 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 2.12 kVA (0.2%)
- **Calculated PF (kW/kVA from averages):** 0.889
- **Power Factor Difference:** 0.019 (2.2%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (896.01) and measured PF (0.869) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA |   896.01 |        35.8% | 601,537.00 kVA | 2,723,535.58 TOTAL-HEAT |
| kW |   798.19 |        31.9% | 535,864.46 kWh | 297,340.82 Load-Heat |
| kVAR |   407.10 |        16.3% | 273,305.77 kVARh | - |
| WASTE |    97.82 |         3.9% | 65,672.54 WASTE | 36,440.42 Field-Heat |

### Heat Unit Notes

- **TOTAL-HEAT (BTU/hr):** 2,723,535.58
- **Load-Heat (BTU/hr):** 297,340.82
- **Field-Heat (BTU/hr):** 36,440.42
- **Load-Heat (BTU, period total):** 199,619,760.56
- **Field-Heat (BTU, period total):** 24,464,278.18

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 2 |   896.01 |   798.19 |   403.18 |     0.89 |   35.8% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   822.13 |   687.63 |   449.16 |     0.84 |   32.9% |
| 01 |   343.93 |   278.73 |   200.38 |     0.81 |   13.8% |
| 02 |    64.38 |    54.05 |    34.25 |     0.84 |    2.6% |
| 03 |    54.90 |    46.51 |    28.25 |     0.85 |    2.2% |
| 04 |    47.94 |    40.36 |    25.19 |     0.84 |    1.9% |
| 05 |   173.42 |   134.14 |   108.45 |     0.77 |    6.9% |
| 06 | 1,061.27 |   959.94 |   446.34 |     0.90 |   42.5% |
| 07 | 1,118.69 | 1,009.06 |   481.04 |     0.90 |   44.7% |
| 08 | 1,083.19 |   967.10 |   484.74 |     0.89 |   43.3% |
| 09 | 1,134.30 | 1,022.87 |   487.52 |     0.90 |   45.4% |
| 10 | 1,040.48 |   918.55 |   485.07 |     0.88 |   41.6% |
| 11 | 1,105.59 |   995.56 |   478.95 |     0.90 |   44.2% |
| 12 | 1,151.20 | 1,034.93 |   502.07 |     0.90 |   46.0% |
| 13 | 1,136.37 | 1,019.07 |   500.62 |     0.90 |   45.5% |
| 14 | 1,175.96 | 1,060.19 |   507.17 |     0.90 |   47.0% |
| 15 | 1,080.56 |   957.75 |   497.00 |     0.89 |   43.2% |
| 16 | 1,106.46 |   993.57 |   484.89 |     0.90 |   44.3% |
| 17 | 1,116.24 |   995.46 |   502.02 |     0.89 |   44.6% |
| 18 | 1,144.19 | 1,030.57 |   495.14 |     0.90 |   45.8% |
| 19 | 1,070.29 |   944.94 |   498.51 |     0.88 |   42.8% |
| 20 | 1,093.21 |   978.84 |   484.22 |     0.90 |   43.7% |
| 21 | 1,157.91 | 1,041.47 |   504.00 |     0.90 |   46.3% |
| 22 | 1,101.95 |   982.22 |   496.65 |     0.89 |   44.1% |
| 23 | 1,123.28 | 1,006.53 |   495.72 |     0.90 |   44.9% |

---

# END OF REPORT

# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 241,439.3 kWh (Usage per period)
- **Consumption Cost per unit:** $0.177/kWh (Cost per kWh)
- **Consumption Total Cost:** $42,662.32 (Cost per period)
- **Consumption Total Cost:** $70.70 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** NCDC1 West11c  
**Generated:** 2026-03-10 00:53:04  
**Data Source:** AN55031702-V-1minRES_40320CLP_260201-260228c.csv  

## Time Period

- **Period:** February 01, 2026 thru February 28, 2026
- **Number of Days:** 28 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 36,208

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

- **Transformer:** NCDC1 West11c
- **Power Factor:** 0.837
- **Total Energy (Actual):** 241,439.25 kWh (per period), 400.09 kW (per hour)
- **Total Waste (Actual):** 46,791.68 kWh (per period), 77.54 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_NCDC1-West11c_AN55031702-1minRES_260201-260228.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_NCDC1-West11c_AN55031702-1minRES_260201-260228.md


## UNITY MANAGEMENT NCDC1 West11c SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 77.54 kW/hr
- **Blended Electricity Rate:** $0.1767/kWh (all-inclusive)
- **NCDC1 West11c Utility Cost Offset:** $13.70/hour
- **Annual Offset Savings:** $120021/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 282,021 BTU/hr
- **Total Cooling kW No Longer Needed:** 24.73 kW
- **Cooling Energy Cost Avoided:** $4.37/hour
- **Annual Cooling Savings:** $38286/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 102.27 kW
- **CO2e Emissions Avoided:** 334.45 metric tons/year
- **Monthly CO2e Reduction:** 27.87 metric tons/month
- **Hourly CO2e Reduction:** 0.0382 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $12876/year

### Total NCDC1 West11c Unity Savings

- **Per Hour:** $19.54
- **Per Day:** $468.99
- **Per Month:** $14069.79
- **Per Year:** $171182

### NCDC1 West11c Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 333.7 kVAR Max (Avg: 260.9 kVAR/hr ; 187,831 kVAR/mo)
- **Max Harmonic Distortion:** 29.1% Max (range: 3.3% - 29.1%)
- **Max Amperage:** 685A Max (range: 460A - 685A)

---

# NCDC1 West11c DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   278.90 |   268.83 |   289.38 |
| Line to Line Voltage (480v) |   483.07 |   465.63 |   501.22 |
| Current (AMPS) |   570.87 |   460.02 |   684.87 |
| Phase Angle (degrees) |    33.14 |    29.66 |    39.01 |
| Total Harmonic Distortion (PCT) |    16.32 |     3.29 |    29.09 |

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
| THD Phase A (%) | 5.4% | IEEE standard per-phase calculation |
| THD Phase B (%) | 5.4% | IEEE standard per-phase calculation |
| THD Phase C (%) | 5.4% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 16.3% | Field-level stress indicator |
| Max Phase THD | 5.4% | Highest THD among all three phases |
| Min Phase THD | 5.4% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 487.63 kW
  - **Maximum Load:** 567.45 kVA
  - **Percentage of Capacity (MAX):** 22.7%
- **Average Load:** 477.63 kVA
  - **Percentage of Capacity (Avg):** 19.1%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 477.63 kVA
- **Average Power Factor (PF):** 0.837

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 477.65 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 483.07 V
- Average Current (Iavg_A): 570.87 A
- Average kW (Psum_kW): 400.09 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 0.02 kVA (0.0%)
- **Calculated PF (kW/kVA from averages):** 0.838
- **Power Factor Difference:** 0.001 (0.1%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (477.63) and measured PF (0.837) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA |   477.63 |        19.1% | 288,230.93 kVA | 1,365,154.14 TOTAL-HEAT |
| kW |   400.09 |        16.0% | 241,439.25 kWh | 221,620.39 Load-Heat |
| kVAR |   260.88 |        10.4% | 157,429.84 kVARh | - |
| WASTE |    77.54 |         3.1% | 46,791.68 WASTE | 42,950.72 Field-Heat |

### Heat Unit Notes

- **TOTAL-HEAT (BTU/hr):** 1,365,154.14
- **Load-Heat (BTU/hr):** 221,620.39
- **Field-Heat (BTU/hr):** 42,950.72
- **Load-Heat (BTU, period total):** 133,740,515.68
- **Field-Heat (BTU, period total):** 25,919,326.40

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 2 |   477.63 |   400.09 |   260.54 |     0.84 |   19.1% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   461.14 |   384.00 |   255.12 |     0.83 |   18.4% |
| 01 |   454.09 |   376.61 |   253.52 |     0.83 |   18.2% |
| 02 |   448.43 |   371.19 |   251.41 |     0.83 |   17.9% |
| 03 |   441.76 |   364.76 |   248.99 |     0.83 |   17.7% |
| 04 |   440.63 |   363.00 |   249.49 |     0.82 |   17.6% |
| 05 |   451.50 |   375.69 |   250.06 |     0.83 |   18.1% |
| 06 |   479.04 |   403.29 |   258.23 |     0.84 |   19.2% |
| 07 |   468.35 |   391.98 |   256.05 |     0.84 |   18.7% |
| 08 |   473.59 |   396.53 |   258.61 |     0.84 |   18.9% |
| 09 |   472.82 |   395.69 |   258.54 |     0.84 |   18.9% |
| 10 |   478.69 |   401.01 |   261.14 |     0.84 |   19.1% |
| 11 |   478.76 |   401.15 |   261.11 |     0.84 |   19.2% |
| 12 |   485.45 |   407.60 |   263.38 |     0.84 |   19.4% |
| 13 |   488.81 |   411.61 |   263.38 |     0.84 |   19.6% |
| 14 |   496.14 |   418.32 |   266.49 |     0.84 |   19.8% |
| 15 |   500.07 |   420.55 |   270.27 |     0.84 |   20.0% |
| 16 |   503.09 |   422.95 |   272.10 |     0.84 |   20.1% |
| 17 |   506.71 |   427.50 |   271.70 |     0.84 |   20.3% |
| 18 |   502.99 |   423.84 |   270.38 |     0.84 |   20.1% |
| 19 |   504.83 |   425.70 |   270.98 |     0.84 |   20.2% |
| 20 |   494.69 |   416.78 |   266.13 |     0.84 |   19.8% |
| 21 |   487.58 |   411.18 |   261.79 |     0.84 |   19.5% |
| 22 |   477.74 |   401.36 |   258.86 |     0.84 |   19.1% |
| 23 |   470.56 |   393.87 |   257.17 |     0.84 |   18.8% |

---

# END OF REPORT

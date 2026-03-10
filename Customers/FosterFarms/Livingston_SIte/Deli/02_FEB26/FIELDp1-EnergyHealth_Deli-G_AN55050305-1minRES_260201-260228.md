# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 403,388.4 kWh (Usage per period)
- **Consumption Cost per unit:** $0.146/kWh (Cost per kWh)
- **Consumption Total Cost:** $58,975.38 (Cost per period)
- **Consumption Total Cost:** $87.78 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** Deli G  
**Generated:** 2026-03-09 17:27:25  
**Data Source:** AN55050305-V-1minRES_40320CLP_260201-260228c.csv  

## Time Period

- **Period:** February 01, 2026 thru February 28, 2026
- **Number of Days:** 28 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 40,309

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

- **Transformer:** Deli G
- **Power Factor:** 0.866
- **Total Energy (Actual):** 403,388.39 kWh (per period), 600.44 kW (per hour)
- **Total Waste (Actual):** 47,270.17 kWh (per period), 70.36 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_Deli-G_AN55050305-1minRES_260201-260228.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_Deli-G_AN55050305-1minRES_260201-260228.md


## UNITY MANAGEMENT Deli G SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 70.36 kW/hr
- **Blended Electricity Rate:** $0.1462/kWh (all-inclusive)
- **Deli G Utility Cost Offset:** $10.29/hour
- **Annual Offset Savings:** $90113/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 252,574 BTU/hr
- **Total Cooling kW No Longer Needed:** 22.15 kW
- **Cooling Energy Cost Avoided:** $3.24/hour
- **Annual Cooling Savings:** $28370/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 92.51 kW
- **CO2e Emissions Avoided:** 302.53 metric tons/year
- **Monthly CO2e Reduction:** 25.21 metric tons/month
- **Hourly CO2e Reduction:** 0.0345 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $11648/year

### Total Deli G Unity Savings

- **Per Hour:** $14.86
- **Per Day:** $356.52
- **Per Month:** $10695.65
- **Per Year:** $130130

### Deli G Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 1,546.8 kVAR Max (Avg: 299.1 kVAR/hr ; 215,336 kVAR/mo)
- **Max Harmonic Distortion:** 28.7% Max (range: 3.0% - 28.7%)
- **Max Amperage:** 2,381A Max (range: 70A - 2381A)

---

# Deli G DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   277.18 |   264.12 |   288.73 |
| Line to Line Voltage (480v) |   480.09 |   457.46 |   500.10 |
| Current (AMPS) |   809.10 |    70.29 |  2380.87 |
| Phase Angle (degrees) |    28.71 |     3.62 |    69.02 |
| Total Harmonic Distortion (PCT) |    13.94 |     3.00 |    28.73 |

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
| THD Phase A (%) | 4.6% | IEEE standard per-phase calculation |
| THD Phase B (%) | 4.6% | IEEE standard per-phase calculation |
| THD Phase C (%) | 4.6% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 13.9% | Field-level stress indicator |
| Max Phase THD | 4.6% | Highest THD among all three phases |
| Min Phase THD | 4.6% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 1,833.63 kW
  - **Maximum Load:** 1,954.84 kVA
  - **Percentage of Capacity (MAX):** 78.2%
- **Average Load:** 670.81 kVA
  - **Percentage of Capacity (Avg):** 26.8%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 670.81 kVA
- **Average Power Factor (PF):** 0.866

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 672.80 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 480.09 V
- Average Current (Iavg_A): 809.10 A
- Average kW (Psum_kW): 600.44 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 2.00 kVA (0.3%)
- **Calculated PF (kW/kVA from averages):** 0.892
- **Power Factor Difference:** 0.026 (3.0%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (670.81) and measured PF (0.866) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA |   670.81 |        26.8% | 450,658.56 kVA | 2,048,800.73 TOTAL-HEAT |
| kW |   600.44 |        24.0% | 403,388.39 kWh | 214,901.41 Load-Heat |
| kVAR |   299.08 |        12.0% | 200,925.22 kVARh | - |
| WASTE |    70.36 |         2.8% | 47,270.17 WASTE | 25,182.74 Field-Heat |

### Heat Unit Notes

- **TOTAL-HEAT (BTU/hr):** 2,048,800.73
- **Load-Heat (BTU/hr):** 214,901.41
- **Field-Heat (BTU/hr):** 25,182.74
- **Load-Heat (BTU, period total):** 144,374,348.59
- **Field-Heat (BTU, period total):** 16,918,186.63

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 2 |   670.81 |   600.44 |   284.51 |     0.90 |   26.8% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   491.03 |   424.76 |   234.32 |     0.87 |   19.6% |
| 01 |   317.15 |   245.72 |   199.73 |     0.77 |   12.7% |
| 02 |   295.43 |   221.92 |   193.86 |     0.75 |   11.8% |
| 03 |   301.08 |   227.16 |   194.91 |     0.75 |   12.0% |
| 04 |   319.08 |   237.19 |   208.85 |     0.74 |   12.8% |
| 05 |   342.50 |   259.76 |   219.83 |     0.76 |   13.7% |
| 06 |   908.11 |   803.38 |   408.36 |     0.88 |   36.3% |
| 07 |   951.30 |   865.65 |   385.53 |     0.91 |   38.1% |
| 08 |   922.79 |   828.59 |   397.32 |     0.90 |   36.9% |
| 09 |   886.58 |   811.25 |   352.51 |     0.92 |   35.5% |
| 10 |   823.23 |   743.11 |   344.68 |     0.90 |   32.9% |
| 11 |   762.56 |   687.06 |   321.05 |     0.90 |   30.5% |
| 12 |   868.45 |   797.72 |   336.82 |     0.92 |   34.7% |
| 13 |   777.65 |   694.65 |   337.29 |     0.89 |   31.1% |
| 14 |   822.23 |   758.23 |   311.20 |     0.92 |   32.9% |
| 15 |   664.77 |   581.49 |   310.15 |     0.87 |   26.6% |
| 16 |   778.48 |   721.15 |   287.17 |     0.93 |   31.1% |
| 17 |   751.95 |   690.51 |   288.34 |     0.92 |   30.1% |
| 18 |   723.43 |   668.18 |   268.92 |     0.92 |   28.9% |
| 19 |   699.13 |   645.46 |   259.94 |     0.92 |   28.0% |
| 20 |   606.56 |   551.50 |   241.32 |     0.91 |   24.3% |
| 21 |   726.73 |   683.04 |   242.95 |     0.94 |   29.1% |
| 22 |   649.80 |   600.82 |   238.20 |     0.92 |   26.0% |
| 23 |   709.91 |   662.91 |   245.22 |     0.93 |   28.4% |

---

# END OF REPORT

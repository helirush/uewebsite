# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 606,058.1 kWh (Usage per period)
- **Consumption Cost per unit:** $0.175/kWh (Cost per kWh)
- **Consumption Total Cost:** $105,878.35 (Cost per period)
- **Consumption Total Cost:** $188.54 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** Rendering-1  
**Generated:** 2026-03-05 11:20:10  
**Data Source:** AN55050434-V-1minRES_40320CLP_260201-260228c.csv  

## Time Period

- **Period:** February 01, 2026 thru February 28, 2026
- **Number of Days:** 28 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 33,694

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

- **Transformer:** Rendering-1
- **Power Factor:** 0.818
- **Total Energy (Actual):** 606,058.12 kWh (per period), 1079.23 kW (per hour)
- **Total Waste (Actual):** 134,855.83 kWh (per period), 240.14 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_Rendering-1_AN55050434-1minRES_260201-260228.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_Rendering-1_AN55050434-1minRES_260201-260228.md


## UNITY MANAGEMENT Rendering-1 SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 240.14 kW/hr
- **Blended Electricity Rate:** $0.1747/kWh (all-inclusive)
- **Rendering-1 Utility Cost Offset:** $41.95/hour
- **Annual Offset Savings:** $367507/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 921,981 BTU/hr
- **Total Cooling kW No Longer Needed:** 80.87 kW
- **Cooling Energy Cost Avoided:** $14.13/hour
- **Annual Cooling Savings:** $123754/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 321.01 kW
- **CO2e Emissions Avoided:** 1049.75 metric tons/year
- **Monthly CO2e Reduction:** 87.48 metric tons/month
- **Hourly CO2e Reduction:** 0.1198 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $40415/year

### Total Rendering-1 Unity Savings

- **Per Hour:** $60.69
- **Per Day:** $1456.65
- **Per Month:** $43699.41
- **Per Year:** $531676

### Rendering-1 Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 1,073.5 kVAR Max (Avg: 758.9 kVAR/hr ; 546,444 kVAR/mo)
- **Max Harmonic Distortion:** 29.8% Max (range: 3.1% - 29.8%)
- **Max Amperage:** 2,041A Max (range: 1219A - 2041A)

---

# Rendering-1 DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   272.60 |   262.89 |   283.40 |
| Line to Line Voltage (480v) |   472.16 |   455.33 |   490.87 |
| Current (AMPS) |  1613.51 |  1219.49 |  2041.33 |
| Phase Angle (degrees) |    35.14 |    29.77 |    46.29 |
| Total Harmonic Distortion (PCT) |    16.87 |     3.09 |    29.79 |

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
| THD Phase A (%) | 5.6% | IEEE standard per-phase calculation |
| THD Phase B (%) | 5.6% | IEEE standard per-phase calculation |
| THD Phase C (%) | 5.6% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 16.9% | Field-level stress indicator |
| Max Phase THD | 5.6% | Highest THD among all three phases |
| Min Phase THD | 5.6% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 1,307.31 kW
  - **Maximum Load:** 1,619.73 kVA
  - **Percentage of Capacity (MAX):** 64.8%
- **Average Load:** 1,319.37 kVA
  - **Percentage of Capacity (Avg):** 52.8%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 1,319.37 kVA
- **Average Power Factor (PF):** 0.818

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 1,319.53 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 472.16 V
- Average Current (Iavg_A): 1613.51 A
- Average kW (Psum_kW): 1079.23 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 0.16 kVA (0.0%)
- **Calculated PF (kW/kVA from averages):** 0.818
- **Power Factor Difference:** 0.000 (0.0%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (1319.37) and measured PF (0.818) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA | 1,319.37 |        52.8% | 740,913.95 kVA | 3,682,477.05 TOTAL-HEAT |
| kW | 1,079.23 |        43.2% | 606,058.12 kWh | 670,257.99 Load-Heat |
| kVAR |   758.95 |        30.4% | 426,200.70 kVARh | - |
| WASTE |   240.14 |         9.6% | 134,855.83 WASTE | 149,141.14 Field-Heat |

### Heat Unit Notes

- **TOTAL-HEAT (BTU/hr):** 3,682,477.05
- **Load-Heat (BTU/hr):** 670,257.99
- **Field-Heat (BTU/hr):** 149,141.14
- **Load-Heat (BTU, period total):** 376,394,545.31
- **Field-Heat (BTU, period total):** 83,752,690.75

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 2 | 1,319.37 | 1,079.23 |   758.48 |     0.82 |   52.8% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 | 1,329.16 | 1,086.22 |   765.62 |     0.82 |   53.2% |
| 01 | 1,352.62 | 1,104.65 |   780.20 |     0.82 |   54.1% |
| 02 | 1,333.07 | 1,086.83 |   771.53 |     0.82 |   53.3% |
| 03 | 1,339.51 | 1,093.52 |   773.38 |     0.82 |   53.6% |
| 04 | 1,328.74 | 1,085.83 |   765.57 |     0.82 |   53.1% |
| 05 | 1,329.11 | 1,087.52 |   763.88 |     0.82 |   53.2% |
| 06 | 1,347.57 | 1,101.71 |   775.80 |     0.82 |   53.9% |
| 07 | 1,338.73 | 1,095.03 |   769.86 |     0.82 |   53.5% |
| 08 | 1,350.90 | 1,104.65 |   777.37 |     0.82 |   54.0% |
| 09 | 1,341.79 | 1,096.40 |   773.25 |     0.82 |   53.7% |
| 10 | 1,343.52 | 1,097.30 |   774.88 |     0.82 |   53.7% |
| 11 | 1,339.68 | 1,095.58 |   770.57 |     0.82 |   53.6% |
| 12 | 1,336.87 | 1,092.97 |   769.39 |     0.82 |   53.5% |
| 13 | 1,336.32 | 1,091.53 |   770.46 |     0.82 |   53.5% |
| 14 | 1,329.07 | 1,083.10 |   769.81 |     0.81 |   53.2% |
| 15 | 1,328.17 | 1,084.27 |   766.44 |     0.82 |   53.1% |
| 16 | 1,333.50 | 1,094.82 |   760.87 |     0.82 |   53.3% |
| 17 | 1,311.49 | 1,078.95 |   745.07 |     0.82 |   52.5% |
| 18 | 1,249.46 | 1,014.34 |   728.91 |     0.81 |   50.0% |
| 19 | 1,217.63 |   983.46 |   717.42 |     0.81 |   48.7% |
| 20 | 1,254.45 | 1,030.31 |   714.90 |     0.82 |   50.2% |
| 21 | 1,263.90 | 1,046.67 |   707.91 |     0.83 |   50.6% |
| 22 | 1,289.19 | 1,063.94 |   727.57 |     0.83 |   51.6% |
| 23 | 1,325.44 | 1,089.43 |   754.48 |     0.82 |   53.0% |

---

# END OF REPORT

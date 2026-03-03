# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 680,754.7 kWh (Usage per period)
- **Consumption Cost per unit:** $0.338/kWh (Cost per kWh)
- **Consumption Total Cost:** $230,197.81 (Cost per period)
- **Consumption Total Cost:** $320.16 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** T12.Main  
**Generated:** 2026-01-27 14:32:00  
**Data Source:** AN54021613-V-1minRES_44685CLP_251101-251130zth.csv  

## Time Period

- **Period:** November 01, 2025 thru November 30, 2025
- **Number of Days:** 30 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 43,140

- **Dataset Coverage:** Complete month (100.0% of 30-day month)
- **Billing Scale Factor:** 1.000x (no normalization needed)

## Facility Information

- **Facility:** Foster Farms: Cherry Ave Facility
- **Location:** Fresno, CA 93706
- **Analysis Type:** Energy Field Performance Assessment
- **Technology Focus:** Unity Energy Management Solutions

---

## Executive Summary

*Brief overview of key transformer performance metrics and energy consumption.*

- **Transformer:** T12.Main
- **Power Factor:** 0.829
- **Total Energy (Actual):** 680,754.67 kWh (per period), 946.81 kW (per hour)
- **Total Waste (Actual):** 135,124.48 kWh (per period), 187.93 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_T12.Main_AN54021613-1minRES_251101-251130.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_T12.Main_AN54021613-1minRES_251101-251130.md


## UNITY MANAGEMENT T12.Main SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 187.93 kW/hr
- **Blended Electricity Rate:** $0.3382/kWh (all-inclusive)
- **T12.Main Utility Cost Offset:** $63.55/hour
- **Annual Offset Savings:** $556698/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 799,556 BTU/hr
- **Total Cooling kW No Longer Needed:** 104.91 kW
- **Cooling Energy Cost Avoided:** $35.47/hour
- **Annual Cooling Savings:** $310752/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 292.84 kW
- **CO2e Emissions Avoided:** 957.63 metric tons/year
- **Monthly CO2e Reduction:** 79.80 metric tons/month
- **Hourly CO2e Reduction:** 0.1093 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $36869/year

### Total T12.Main Unity Savings

- **Per Hour:** $103.23
- **Per Day:** $2477.59
- **Per Month:** $74327.58
- **Per Year:** $904319

### T12.Main Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 1,025.5 kVAR Max (Avg: 625.5 kVAR/hr ; 450,327 kVAR/mo)
- **Max Harmonic Distortion:** 31.3% Max (range: 3.8% - 31.3%)
- **Max Amperage:** 2,544A Max (range: 409A - 2544A)

---

# T12.Main DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   270.59 |   256.81 |   285.91 |
| Line to Line Voltage (480v) |   468.67 |   444.81 |   495.21 |
| Current (AMPS) |  1408.85 |   408.86 |  2543.52 |
| Phase Angle (degrees) |    33.91 |    27.25 |    44.03 |
| Total Harmonic Distortion (PCT) |    15.93 |     3.80 |    31.34 |

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
| THD Phase A (%) | 5.3% | IEEE standard per-phase calculation |
| THD Phase B (%) | 5.3% | IEEE standard per-phase calculation |
| THD Phase C (%) | 5.3% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 15.9% | Field-level stress indicator |
| Max Phase THD | 5.3% | Highest THD among all three phases |
| Min Phase THD | 5.3% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 1,443.33 kW
  - **Maximum Load:** 1,768.92 kVA
  - **Percentage of Capacity (MAX):** 70.8%
- **Average Load:** 1,134.74 kVA
  - **Percentage of Capacity (Avg):** 45.4%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 1,134.74 kVA
- **Average Power Factor (PF):** 0.829

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 1,143.66 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 468.67 V
- Average Current (Iavg_A): 1408.85 A
- Average kW (Psum_kW): 946.81 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 8.92 kVA (0.8%)
- **Calculated PF (kW/kVA from averages):** 0.828
- **Power Factor Difference:** 0.001 (0.1%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (1134.74) and measured PF (0.829) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA | 1,134.74 |        45.4% | 815,879.15 kVA | 3,230,642.01 TOTAL-HEAT |
| kW |   946.81 |        37.9% | 680,754.67 kWh | 384,703,315.47 Load-Heat |
| kVAR |   625.45 |        25.0% | 449,701.98 kVARh | - |
| WASTE |   187.93 |         7.5% | 135,124.48 WASTE | 76,360,601.04 Field-Heat |

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 11 | 1,134.74 |   946.81 |   623.82 |     0.83 |   45.4% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 | 1,215.29 | 1,005.74 |   681.03 |     0.83 |   48.6% |
| 01 | 1,255.80 | 1,042.68 |   698.78 |     0.83 |   50.2% |
| 02 | 1,247.09 | 1,042.25 |   683.71 |     0.84 |   49.9% |
| 03 | 1,234.65 | 1,028.58 |   681.98 |     0.83 |   49.4% |
| 04 | 1,226.45 | 1,024.65 |   673.05 |     0.84 |   49.1% |
| 05 | 1,232.89 | 1,030.24 |   676.20 |     0.84 |   49.3% |
| 06 | 1,232.22 | 1,032.63 |   671.49 |     0.84 |   49.3% |
| 07 | 1,206.55 | 1,006.04 |   665.30 |     0.83 |   48.3% |
| 08 | 1,198.90 |   997.62 |   664.19 |     0.83 |   48.0% |
| 09 | 1,145.36 |   957.08 |   627.84 |     0.84 |   45.8% |
| 10 | 1,196.17 |   995.69 |   661.63 |     0.83 |   47.8% |
| 11 | 1,173.91 |   976.12 |   651.02 |     0.83 |   47.0% |
| 12 | 1,108.51 |   925.32 |   609.16 |     0.83 |   44.3% |
| 13 |   972.08 |   810.30 |   535.25 |     0.83 |   38.9% |
| 14 |   889.79 |   746.17 |   482.12 |     0.84 |   35.6% |
| 15 | 1,028.50 |   872.27 |   542.04 |     0.85 |   41.1% |
| 16 | 1,070.26 |   913.92 |   554.65 |     0.85 |   42.8% |
| 17 | 1,020.76 |   872.22 |   528.58 |     0.85 |   40.8% |
| 18 |   982.22 |   833.98 |   517.28 |     0.85 |   39.3% |
| 19 |   919.50 |   773.98 |   495.28 |     0.84 |   36.8% |
| 20 | 1,125.74 |   924.72 |   640.61 |     0.82 |   45.0% |
| 21 | 1,174.59 |   959.49 |   676.44 |     0.82 |   47.0% |
| 22 | 1,157.77 |   944.44 |   668.98 |     0.82 |   46.3% |
| 23 | 1,222.83 | 1,010.45 |   687.62 |     0.83 |   48.9% |

---

# END OF REPORT

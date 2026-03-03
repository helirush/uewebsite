# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 749,503.7 kWh (Usage per period)
- **Consumption Cost per unit:** $0.318/kWh (Cost per kWh)
- **Consumption Total Cost:** $238,478.45 (Cost per period)
- **Consumption Total Cost:** $322.08 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** T12.Main  
**Generated:** 2026-01-06 13:47:36  
**Data Source:** AN54021613-V-1minRES_44640CLP_251001-251031zth.csv  

## Time Period

- **Period:** October 01, 2025 thru October 31, 2025
- **Number of Days:** 31 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 44,426

- **Dataset Coverage:** Partial month (0.0% of 0-day month)
- **Billing Scale Factor:** 1.000x (normalization applied for monthly comparison)

## Facility Information

- **Facility:** Foster Farms: Cherry Ave Facility
- **Location:** Fresno, CA 93706
- **Analysis Type:** Energy Field Performance Assessment
- **Technology Focus:** Unity Energy Management Solutions

---

## Executive Summary

*Brief overview of key transformer performance metrics and energy consumption.*

- **Transformer:** T12.Main
- **Power Factor:** 0.829
- **Total Energy (Actual):** 749,503.69 kWh (31 days), 1012.25 kW (per hour)
- **Total Energy (Monthly Equivalent):** 749,503.69 kWh
- **Total Waste (Actual):** 149,010.77 kWh (31 days), 201.25 kW (per hour)
- **Total Waste (Monthly Equivalent):** 149,010.77 kWh

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_T12.Main_AN54021613-1minRES_251001-251031.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_T12.Main_AN54021613-1minRES_251001-251031.md


## UNITY MANAGEMENT T12.Main SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 201.25 kW/hr (actual)
- **Monthly Equivalent Waste:** 201.25 kW/hr
- **Blended Electricity Rate:** $0.3182/kWh (all-inclusive)
- **T12.Main Utility Cost Offset (Monthly Equivalent):** $64.03/hour
- **Annual Offset Savings:** $560933/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 873,779 BTU/hr
- **Total Cooling kW No Longer Needed:** 101.94 kW
- **Cooling Energy Cost Avoided:** $32.44/hour
- **Annual Cooling Savings:** $284137/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 303.19 kW
- **CO2e Emissions Avoided:** 991.48 metric tons/year
- **Monthly CO2e Reduction:** 82.62 metric tons/month
- **Hourly CO2e Reduction:** 0.1132 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $38172/year

### Total T12.Main Unity Savings

- **Per Hour:** $100.83
- **Per Day:** $2419.84
- **Per Month:** $72595.26
- **Per Year:** $883242

### T12.Main Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 1,006.1 kVAR Max (Avg: 669.3 kVAR/hr ; 481,877 kVAR/mo)
- **Max Harmonic Distortion:** 39.7% Max (range: 8.8% - 39.7%)
- **Max Amperage:** 2,260A Max (range: 486A - 2260A)

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
| Line to Neutral Voltage (277v) |   268.46 |   250.56 |   284.77 |
| Line to Line Voltage (480v) |   464.99 |   433.99 |   493.23 |
| Current (AMPS) |  1516.87 |   486.37 |  2260.14 |
| Phase Angle (degrees) |    33.88 |    27.87 |    43.70 |
| Total Harmonic Distortion (PCT) |    15.67 |     8.77 |    39.68 |

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
| THD Phase A (%) | 5.2% | IEEE standard per-phase calculation |
| THD Phase B (%) | 5.7% | IEEE standard per-phase calculation |
| THD Phase C (%) | 4.8% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 15.7% | Field-level stress indicator |
| Max Phase THD | 5.7% | Highest THD among all three phases |
| Min Phase THD | 4.8% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 1,409.92 kW
  - **Maximum Load:** 1,729.61 kVA
  - **Percentage of Capacity (MAX):** 69.2%
- **Average Load:** 1,213.50 kVA
  - **Percentage of Capacity (Avg):** 48.5%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 1,213.50 kVA
- **Average Power Factor (PF):** 0.829

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 1,221.66 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 464.99 V
- Average Current (Iavg_A): 1516.87 A
- Average kW (Psum_kW): 1012.25 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 8.16 kVA (0.7%)
- **Calculated PF (kW/kVA from averages):** 0.829
- **Power Factor Difference:** 0.001 (0.1%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (1213.50) and measured PF (0.829) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA | 1,213.50 |        48.5% | 898,514.47 kVA | 3,453,940.98 TOTAL-HEAT |
| kW | 1,012.25 |        40.5% | 749,503.69 kWh | 424,124,608.34 Load-Heat |
| kVAR |   669.27 |        26.8% | 495,552.68 kVARh | - |
| WASTE |   201.25 |         8.0% | 149,010.77 WASTE | 84,321,314.07 Field-Heat |

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 10 | 1,214.79 | 1,013.31 |   668.55 |     0.83 |   48.6% |
| 11 |   960.32 |   804.34 |   524.21 |     0.84 |   38.4% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 | 1,181.06 |   973.37 |   667.45 |     0.82 |   47.2% |
| 01 | 1,257.06 | 1,033.71 |   714.02 |     0.82 |   50.3% |
| 02 | 1,227.79 | 1,007.36 |   700.96 |     0.82 |   49.1% |
| 03 | 1,265.66 | 1,043.23 |   715.83 |     0.82 |   50.6% |
| 04 | 1,282.01 | 1,059.84 |   720.42 |     0.83 |   51.3% |
| 05 | 1,309.34 | 1,081.73 |   736.78 |     0.83 |   52.4% |
| 06 | 1,327.97 | 1,102.98 |   738.62 |     0.83 |   53.1% |
| 07 | 1,313.07 | 1,088.73 |   733.10 |     0.83 |   52.5% |
| 08 | 1,314.24 | 1,092.47 |   729.68 |     0.83 |   52.6% |
| 09 | 1,289.62 | 1,074.11 |   712.79 |     0.83 |   51.6% |
| 10 | 1,293.76 | 1,078.93 |   712.83 |     0.83 |   51.8% |
| 11 | 1,269.50 | 1,055.38 |   704.55 |     0.83 |   50.8% |
| 12 | 1,266.25 | 1,053.16 |   702.28 |     0.83 |   50.6% |
| 13 | 1,224.65 | 1,024.01 |   670.56 |     0.84 |   49.0% |
| 14 | 1,300.01 | 1,085.57 |   714.47 |     0.84 |   52.0% |
| 15 | 1,292.32 | 1,077.30 |   713.09 |     0.83 |   51.7% |
| 16 | 1,278.22 | 1,068.31 |   701.14 |     0.84 |   51.1% |
| 17 | 1,177.35 |   984.61 |   644.69 |     0.84 |   47.1% |
| 18 | 1,029.31 |   864.91 |   556.63 |     0.84 |   41.2% |
| 19 | 1,099.12 |   939.88 |   567.81 |     0.86 |   44.0% |
| 20 | 1,116.99 |   956.39 |   575.02 |     0.86 |   44.7% |
| 21 | 1,053.10 |   897.68 |   548.79 |     0.85 |   42.1% |
| 22 | 1,001.16 |   849.58 |   528.12 |     0.85 |   40.0% |
| 23 |   946.85 |   795.64 |   512.03 |     0.84 |   37.9% |

---

# END OF REPORT

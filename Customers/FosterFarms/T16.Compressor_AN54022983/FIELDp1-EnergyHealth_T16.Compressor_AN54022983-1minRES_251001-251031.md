# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 728,305.0 kWh (Usage per period)
- **Consumption Cost per unit:** $0.318/kWh (Cost per kWh)
- **Consumption Total Cost:** $231,733.40 (Cost per period)
- **Consumption Total Cost:** $313.97 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** T16.Compressor  
**Generated:** 2026-01-06 13:48:41  
**Data Source:** AN54022983-V-1minRES_44640CLP_251001-251031zth.csv  

## Time Period

- **Period:** October 01, 2025 thru October 31, 2025
- **Number of Days:** 31 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 44,284

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

- **Transformer:** T16.Compressor
- **Power Factor:** 0.886
- **Total Energy (Actual):** 728,304.98 kWh (31 days), 986.77 kW (per hour)
- **Total Energy (Monthly Equivalent):** 728,304.98 kWh
- **Total Waste (Actual):** 90,170.91 kWh (31 days), 122.17 kW (per hour)
- **Total Waste (Monthly Equivalent):** 90,170.91 kWh

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_T16.Compressor_AN54022983-1minRES_251001-251031.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_T16.Compressor_AN54022983-1minRES_251001-251031.md


## UNITY MANAGEMENT T16.Compressor SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 122.17 kW/hr (actual)
- **Monthly Equivalent Waste:** 122.17 kW/hr
- **Blended Electricity Rate:** $0.3182/kWh (all-inclusive)
- **T16.Compressor Utility Cost Offset (Monthly Equivalent):** $38.87/hour
- **Annual Offset Savings:** $340526/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 504,757 BTU/hr
- **Total Cooling kW No Longer Needed:** 29.44 kW
- **Cooling Energy Cost Avoided:** $9.37/hour
- **Annual Cooling Savings:** $82069/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 151.62 kW
- **CO2e Emissions Avoided:** 495.81 metric tons/year
- **Monthly CO2e Reduction:** 41.32 metric tons/month
- **Hourly CO2e Reduction:** 0.0566 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $19089/year

### Total T16.Compressor Unity Savings

- **Per Hour:** $50.42
- **Per Day:** $1210.09
- **Per Month:** $36302.76
- **Per Year:** $441684

### T16.Compressor Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 972.9 kVAR Max (Avg: 506.0 kVAR/hr ; 364,321 kVAR/mo)
- **Max Harmonic Distortion:** 33.1% Max (range: 3.0% - 33.1%)
- **Max Amperage:** 2,047A Max (range: 135A - 2047A)

---

# T16.Compressor DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   273.34 |   260.91 |   290.36 |
| Line to Line Voltage (480v) |   473.43 |   451.92 |   502.93 |
| Current (AMPS) |  1362.92 |   134.90 |  2046.79 |
| Phase Angle (degrees) |    27.53 |    24.54 |    46.70 |
| Total Harmonic Distortion (PCT) |    16.00 |     3.00 |    33.07 |

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
| Unity THD Composite (%) | 16.0% | Field-level stress indicator |
| Max Phase THD | 5.3% | Highest THD among all three phases |
| Min Phase THD | 5.3% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 1,476.07 kW
  - **Maximum Load:** 1,637.98 kVA
  - **Percentage of Capacity (MAX):** 65.5%
- **Average Load:** 1,108.95 kVA
  - **Percentage of Capacity (Avg):** 44.4%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 1,108.95 kVA
- **Average Power Factor (PF):** 0.886

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 1,117.61 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 473.43 V
- Average Current (Iavg_A): 1362.92 A
- Average kW (Psum_kW): 986.77 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 8.67 kVA (0.8%)
- **Calculated PF (kW/kVA from averages):** 0.883
- **Power Factor Difference:** 0.003 (0.4%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (1108.95) and measured PF (0.886) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA | 1,108.95 |        44.4% | 818,475.89 kVA | 3,367,012.93 TOTAL-HEAT |
| kW |   986.77 |        39.5% | 728,304.98 kWh | 273,779,501.98 Load-Heat |
| kVAR |   506.00 |        20.2% | 373,463.03 kVARh | - |
| WASTE |   122.17 |         4.9% | 90,170.91 WASTE | 33,896,440.27 Field-Heat |

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 10 | 1,110.44 |   988.22 |   505.12 |     0.89 |   44.4% |
| 11 |   834.47 |   720.35 |   421.06 |     0.86 |   33.4% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   933.21 |   811.88 |   459.48 |     0.87 |   37.3% |
| 01 |   957.15 |   839.21 |   459.08 |     0.88 |   38.3% |
| 02 |   971.39 |   851.93 |   465.56 |     0.88 |   38.9% |
| 03 | 1,053.54 |   933.39 |   487.25 |     0.89 |   42.1% |
| 04 | 1,110.90 |   987.82 |   506.75 |     0.89 |   44.4% |
| 05 | 1,167.40 | 1,038.59 |   531.60 |     0.89 |   46.7% |
| 06 | 1,249.72 | 1,116.85 |   559.61 |     0.89 |   50.0% |
| 07 | 1,217.79 | 1,087.23 |   547.35 |     0.89 |   48.7% |
| 08 | 1,184.31 | 1,057.94 |   531.20 |     0.89 |   47.4% |
| 09 | 1,195.79 | 1,070.07 |   532.93 |     0.89 |   47.8% |
| 10 | 1,183.79 | 1,059.84 |   526.75 |     0.90 |   47.4% |
| 11 | 1,169.42 | 1,046.80 |   520.74 |     0.90 |   46.8% |
| 12 | 1,166.84 | 1,043.68 |   520.79 |     0.89 |   46.7% |
| 13 | 1,170.98 | 1,048.33 |   520.77 |     0.90 |   46.8% |
| 14 | 1,165.57 | 1,043.54 |   518.33 |     0.90 |   46.6% |
| 15 | 1,221.58 | 1,095.53 |   539.86 |     0.90 |   48.9% |
| 16 | 1,202.80 | 1,078.98 |   531.00 |     0.90 |   48.1% |
| 17 | 1,174.79 | 1,053.95 |   518.35 |     0.90 |   47.0% |
| 18 | 1,146.25 | 1,027.28 |   507.77 |     0.90 |   45.9% |
| 19 | 1,054.14 |   941.88 |   472.56 |     0.89 |   42.2% |
| 20 |   979.44 |   871.70 |   445.82 |     0.89 |   39.2% |
| 21 |   989.73 |   874.32 |   462.27 |     0.88 |   39.6% |
| 22 |   994.64 |   872.66 |   476.20 |     0.88 |   39.8% |
| 23 |   954.42 |   830.57 |   469.22 |     0.87 |   38.2% |

---

# END OF REPORT

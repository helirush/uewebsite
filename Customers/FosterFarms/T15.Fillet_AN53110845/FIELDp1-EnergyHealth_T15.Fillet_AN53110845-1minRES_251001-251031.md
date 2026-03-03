# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 658,366.6 kWh (Usage per period)
- **Consumption Cost per unit:** $0.318/kWh (Cost per kWh)
- **Consumption Total Cost:** $209,480.27 (Cost per period)
- **Consumption Total Cost:** $282.76 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** T15.Fillet  
**Generated:** 2026-01-06 13:46:15  
**Data Source:** AN53110845-V-1minRES_44640CLP_251001-251031zth.csv  

## Time Period

- **Period:** October 01, 2025 thru October 31, 2025
- **Number of Days:** 31 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 44,451

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

- **Transformer:** T15.Fillet
- **Power Factor:** 0.837
- **Total Energy (Actual):** 658,366.55 kWh (31 days), 888.66 kW (per hour)
- **Total Energy (Monthly Equivalent):** 658,366.55 kWh
- **Total Waste (Actual):** 110,610.00 kWh (31 days), 149.30 kW (per hour)
- **Total Waste (Monthly Equivalent):** 110,610.00 kWh

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_T15.Fillet_AN53110845-1minRES_251001-251031.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_T15.Fillet_AN53110845-1minRES_251001-251031.md


## UNITY MANAGEMENT T15.Fillet SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 149.30 kW/hr (actual)
- **Monthly Equivalent Waste:** 149.30 kW/hr
- **Blended Electricity Rate:** $0.3182/kWh (all-inclusive)
- **T15.Fillet Utility Cost Offset (Monthly Equivalent):** $47.51/hour
- **Annual Offset Savings:** $416144/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 597,634 BTU/hr
- **Total Cooling kW No Longer Needed:** 104.59 kW
- **Cooling Energy Cost Avoided:** $33.28/hour
- **Annual Cooling Savings:** $291509/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 253.89 kW
- **CO2e Emissions Avoided:** 830.25 metric tons/year
- **Monthly CO2e Reduction:** 69.19 metric tons/month
- **Hourly CO2e Reduction:** 0.0948 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $31965/year

### Total T15.Fillet Unity Savings

- **Per Hour:** $84.43
- **Per Day:** $2026.35
- **Per Month:** $60790.53
- **Per Year:** $739618

### T15.Fillet Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 856.8 kVAR Max (Avg: 536.3 kVAR/hr ; 386,157 kVAR/mo)
- **Max Harmonic Distortion:** 33.5% Max (range: 3.0% - 33.5%)
- **Max Amperage:** 2,146A Max (range: 184A - 2146A)

---

# T15.Fillet DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   275.67 |   225.37 |   290.12 |
| Line to Line Voltage (480v) |   477.47 |   390.36 |   502.51 |
| Current (AMPS) |  1263.97 |   184.03 |  2145.69 |
| Phase Angle (degrees) |    32.66 |    21.96 |    52.87 |
| Total Harmonic Distortion (PCT) |    15.37 |     3.00 |    33.46 |

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
| THD Phase A (%) | 5.1% | IEEE standard per-phase calculation |
| THD Phase B (%) | 5.1% | IEEE standard per-phase calculation |
| THD Phase C (%) | 5.1% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 15.4% | Field-level stress indicator |
| Max Phase THD | 5.1% | Highest THD among all three phases |
| Min Phase THD | 5.1% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 1,580.06 kW
  - **Maximum Load:** 1,744.18 kVA
  - **Percentage of Capacity (MAX):** 69.8%
- **Average Load:** 1,037.97 kVA
  - **Percentage of Capacity (Avg):** 41.5%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 1,037.97 kVA
- **Average Power Factor (PF):** 0.837

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 1,045.30 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 477.47 V
- Average Current (Iavg_A): 1263.97 A
- Average kW (Psum_kW): 888.66 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 7.34 kVA (0.7%)
- **Calculated PF (kW/kVA from averages):** 0.850
- **Power Factor Difference:** 0.013 (1.6%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (1037.97) and measured PF (0.837) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA | 1,037.97 |        41.5% | 768,976.55 kVA | 3,032,246.97 TOTAL-HEAT |
| kW |   888.66 |        35.5% | 658,366.55 kWh | 323,129,157.28 Load-Heat |
| kVAR |   536.33 |        21.5% | 397,339.18 kVARh | - |
| WASTE |   149.30 |         6.0% | 110,610.00 WASTE | 54,287,866.92 Field-Heat |

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 10 | 1,039.39 |   890.25 |   528.48 |     0.86 |   41.6% |
| 11 |   771.68 |   591.21 |   493.98 |     0.77 |   30.9% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   784.57 |   581.64 |   524.63 |     0.74 |   31.4% |
| 01 |   712.44 |   550.45 |   449.82 |     0.77 |   28.5% |
| 02 |   631.33 |   518.17 |   356.56 |     0.82 |   25.3% |
| 03 |   825.50 |   717.10 |   403.79 |     0.87 |   33.0% |
| 04 | 1,208.77 | 1,049.45 |   595.80 |     0.87 |   48.4% |
| 05 | 1,161.03 | 1,002.33 |   582.24 |     0.86 |   46.4% |
| 06 | 1,234.78 | 1,079.42 |   595.63 |     0.87 |   49.4% |
| 07 | 1,129.30 |   974.46 |   567.24 |     0.86 |   45.2% |
| 08 | 1,139.40 |   987.06 |   565.35 |     0.87 |   45.6% |
| 09 | 1,175.82 | 1,025.32 |   571.83 |     0.87 |   47.0% |
| 10 | 1,149.00 | 1,002.53 |   557.55 |     0.87 |   46.0% |
| 11 | 1,167.92 | 1,027.18 |   552.62 |     0.88 |   46.7% |
| 12 | 1,132.69 |   998.33 |   531.92 |     0.88 |   45.3% |
| 13 | 1,126.77 |   991.68 |   531.37 |     0.88 |   45.1% |
| 14 | 1,128.27 |   990.17 |   537.39 |     0.88 |   45.1% |
| 15 | 1,065.17 |   929.31 |   516.76 |     0.87 |   42.6% |
| 16 | 1,056.12 |   917.59 |   518.85 |     0.87 |   42.2% |
| 17 | 1,104.18 |   962.80 |   536.01 |     0.87 |   44.2% |
| 18 | 1,097.85 |   952.98 |   539.85 |     0.87 |   43.9% |
| 19 | 1,118.07 |   969.60 |   551.61 |     0.87 |   44.7% |
| 20 | 1,086.42 |   936.84 |   544.90 |     0.86 |   43.5% |
| 21 | 1,014.40 |   866.72 |   522.39 |     0.85 |   40.6% |
| 22 |   878.92 |   715.54 |   504.27 |     0.81 |   35.2% |
| 23 |   783.81 |   583.15 |   520.42 |     0.74 |   31.4% |

---

# END OF REPORT

# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 614,798.5 kWh (Usage per period)
- **Consumption Cost per unit:** $0.318/kWh (Cost per kWh)
- **Consumption Total Cost:** $195,617.71 (Cost per period)
- **Consumption Total Cost:** $272.08 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** T16 Compressor  
**Generated:** 2026-02-18 15:25:03  
**Data Source:** AN54022983-V-1minRES_43260CLP_251101-251130c.csv  

## Time Period

- **Period:** November 01, 2025 thru November 30, 2025
- **Number of Days:** 30 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 43,139

- **Dataset Coverage:** Complete month (100.0% of 30-day month)
- **Billing Scale Factor:** 1.000x (no normalization needed)

## Facility Information

- **Facility:** Foster Farms
- **Location:** Cherry Ave Facility
- **Analysis Type:** Energy Field Performance Assessment
- **Technology Focus:** Unity Energy Management Solutions

---

## Executive Summary

*Brief overview of key transformer performance metrics and energy consumption.*

- **Transformer:** T16 Compressor
- **Power Factor:** 0.885
- **Total Energy (Actual):** 614,798.53 kWh (per period), 855.09 kW (per hour)
- **Total Waste (Actual):** 78,014.68 kWh (per period), 108.51 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_T16-Compressor_AN54022983-1minRES_251101-251130.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_T16-Compressor_AN54022983-1minRES_251101-251130.md


## UNITY MANAGEMENT T16 Compressor SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 108.51 kW/hr
- **Blended Electricity Rate:** $0.3182/kWh (all-inclusive)
- **T16 Compressor Utility Cost Offset:** $34.52/hour
- **Annual Offset Savings:** $302438/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 396,438 BTU/hr
- **Total Cooling kW No Longer Needed:** 39.01 kW
- **Cooling Energy Cost Avoided:** $12.41/hour
- **Annual Cooling Savings:** $108734/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 147.52 kW
- **CO2e Emissions Avoided:** 482.41 metric tons/year
- **Monthly CO2e Reduction:** 40.20 metric tons/month
- **Hourly CO2e Reduction:** 0.0551 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $18573/year

### Total T16 Compressor Unity Savings

- **Per Hour:** $49.06
- **Per Day:** $1177.38
- **Per Month:** $35321.53
- **Per Year:** $429745

### T16 Compressor Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 821.5 kVAR Max (Avg: 444.2 kVAR/hr ; 319,846 kVAR/mo)
- **Max Harmonic Distortion:** 89.5% Max (range: 0.0% - 89.5%)
- **Max Amperage:** 1,998A Max (range: 107A - 1998A)

---

# T16 Compressor DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   275.72 |   263.64 |   291.18 |
| Line to Line Voltage (480v) |   477.56 |   456.64 |   504.34 |
| Current (AMPS) |  1175.68 |   107.35 |  1998.21 |
| Phase Angle (degrees) |    27.66 |    18.93 |    48.87 |
| Total Harmonic Distortion (PCT) |    14.22 |     0.00 |    89.54 |

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
| THD Phase A (%) | 4.7% | IEEE standard per-phase calculation |
| THD Phase B (%) | 4.9% | IEEE standard per-phase calculation |
| THD Phase C (%) | 4.6% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 14.2% | Field-level stress indicator |
| Max Phase THD | 4.9% | Highest THD among all three phases |
| Min Phase THD | 4.6% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 1,429.92 kW
  - **Maximum Load:** 1,590.69 kVA
  - **Percentage of Capacity (MAX):** 63.6%
- **Average Load:** 963.60 kVA
  - **Percentage of Capacity (Avg):** 38.5%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 963.60 kVA
- **Average Power Factor (PF):** 0.885

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 972.47 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 477.56 V
- Average Current (Iavg_A): 1175.68 A
- Average kW (Psum_kW): 855.09 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 8.87 kVA (0.9%)
- **Calculated PF (kW/kVA from averages):** 0.879
- **Power Factor Difference:** 0.006 (0.6%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (963.60) and measured PF (0.885) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA |   963.60 |        38.5% | 692,813.21 kVA | 2,917,703.08 TOTAL-HEAT |
| kW |   855.09 |        34.2% | 614,798.53 kWh | 236,221,867.96 Load-Heat |
| kVAR |   444.23 |        17.8% | 319,394.61 kVARh | - |
| WASTE |   108.51 |         4.3% | 78,014.68 WASTE | 29,975,305.82 Field-Heat |

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 11 |   963.60 |   855.09 |   443.19 |     0.89 |   38.5% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   976.35 |   865.59 |   450.82 |     0.89 |   39.1% |
| 01 | 1,074.99 |   954.95 |   492.82 |     0.89 |   43.0% |
| 02 | 1,101.41 |   982.71 |   496.47 |     0.89 |   44.1% |
| 03 | 1,088.91 |   970.25 |   493.52 |     0.89 |   43.6% |
| 04 | 1,089.15 |   971.01 |   492.56 |     0.89 |   43.6% |
| 05 | 1,078.53 |   962.33 |   485.93 |     0.89 |   43.1% |
| 06 | 1,072.44 |   958.03 |   481.24 |     0.89 |   42.9% |
| 07 | 1,073.68 |   959.70 |   480.71 |     0.89 |   42.9% |
| 08 | 1,062.31 |   949.31 |   476.11 |     0.89 |   42.5% |
| 09 | 1,046.16 |   935.60 |   467.37 |     0.89 |   41.8% |
| 10 | 1,030.58 |   920.97 |   461.77 |     0.89 |   41.2% |
| 11 | 1,034.81 |   924.70 |   463.71 |     0.89 |   41.4% |
| 12 | 1,022.93 |   914.66 |   457.23 |     0.89 |   40.9% |
| 13 | 1,012.70 |   905.42 |   452.79 |     0.89 |   40.5% |
| 14 |   905.06 |   806.25 |   410.45 |     0.89 |   36.2% |
| 15 |   848.07 |   752.82 |   389.72 |     0.89 |   33.9% |
| 16 |   815.10 |   721.97 |   377.72 |     0.89 |   32.6% |
| 17 |   843.37 |   742.23 |   399.14 |     0.88 |   33.7% |
| 18 |   856.52 |   748.41 |   415.99 |     0.87 |   34.3% |
| 19 |   842.75 |   732.82 |   415.77 |     0.87 |   33.7% |
| 20 |   819.07 |   712.62 |   403.49 |     0.87 |   32.8% |
| 21 |   802.56 |   700.79 |   390.68 |     0.87 |   32.1% |
| 22 |   793.65 |   695.60 |   381.59 |     0.88 |   31.7% |
| 23 |   838.97 |   736.76 |   400.51 |     0.88 |   33.6% |

---

# END OF REPORT

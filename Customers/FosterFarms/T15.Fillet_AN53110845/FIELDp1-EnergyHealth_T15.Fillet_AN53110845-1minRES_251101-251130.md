# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 533,184.4 kWh (Usage per period)
- **Consumption Cost per unit:** $0.338/kWh (Cost per kWh)
- **Consumption Total Cost:** $180,296.77 (Cost per period)
- **Consumption Total Cost:** $250.76 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** T15.Fillet  
**Generated:** 2026-01-27 14:28:36  
**Data Source:** AN53110845-V-1minRES_44696CLP_251101-251130zth.csv  

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

- **Transformer:** T15.Fillet
- **Power Factor:** 0.828
- **Total Energy (Actual):** 533,184.35 kWh (per period), 741.56 kW (per hour)
- **Total Waste (Actual):** 94,159.32 kWh (per period), 130.96 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_T15.Fillet_AN53110845-1minRES_251101-251130.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_T15.Fillet_AN53110845-1minRES_251101-251130.md


## UNITY MANAGEMENT T15.Fillet SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 130.96 kW/hr
- **Blended Electricity Rate:** $0.3382/kWh (all-inclusive)
- **T15.Fillet Utility Cost Offset:** $44.28/hour
- **Annual Offset Savings:** $387926/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 527,269 BTU/hr
- **Total Cooling kW No Longer Needed:** 103.77 kW
- **Cooling Energy Cost Avoided:** $35.09/hour
- **Annual Cooling Savings:** $307389/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 234.73 kW
- **CO2e Emissions Avoided:** 767.60 metric tons/year
- **Monthly CO2e Reduction:** 63.97 metric tons/month
- **Hourly CO2e Reduction:** 0.0876 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $29553/year

### Total T15.Fillet Unity Savings

- **Per Hour:** $82.75
- **Per Day:** $1985.94
- **Per Month:** $59578.15
- **Per Year:** $724868

### T15.Fillet Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 777.2 kVAR Max (Avg: 459.8 kVAR/hr ; 331,027 kVAR/mo)
- **Max Harmonic Distortion:** 84.9% Max (range: 0.0% - 84.9%)
- **Max Amperage:** 2,050A Max (range: 246A - 2050A)

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
| Line to Neutral Voltage (277v) |   277.75 |   222.06 |   291.20 |
| Line to Line Voltage (480v) |   481.07 |   384.62 |   504.37 |
| Current (AMPS) |  1054.65 |   245.95 |  2049.63 |
| Phase Angle (degrees) |    33.54 |    20.10 |    53.71 |
| Total Harmonic Distortion (PCT) |    18.00 |     0.00 |    84.92 |

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
| THD Phase A (%) | 6.2% | IEEE standard per-phase calculation |
| THD Phase B (%) | 6.5% | IEEE standard per-phase calculation |
| THD Phase C (%) | 5.3% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 18.0% | Field-level stress indicator |
| Max Phase THD | 6.5% | Highest THD among all three phases |
| Min Phase THD | 5.3% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 1,492.71 kW
  - **Maximum Load:** 1,671.57 kVA
  - **Percentage of Capacity (MAX):** 66.9%
- **Average Load:** 872.52 kVA
  - **Percentage of Capacity (Avg):** 34.9%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 872.52 kVA
- **Average Power Factor (PF):** 0.828

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 878.78 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 481.07 V
- Average Current (Iavg_A): 1054.65 A
- Average kW (Psum_kW): 741.56 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 6.26 kVA (0.7%)
- **Calculated PF (kW/kVA from averages):** 0.844
- **Power Factor Difference:** 0.016 (1.9%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (872.52) and measured PF (0.828) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA |   872.52 |        34.9% | 627,343.67 kVA | 2,530,320.88 TOTAL-HEAT |
| kW |   741.56 |        29.7% | 533,184.35 kWh | 273,062,645.35 Load-Heat |
| kVAR |   459.76 |        18.4% | 330,566.99 kVARh | - |
| WASTE |   130.96 |         5.2% | 94,159.32 WASTE | 48,222,333.75 Field-Heat |

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 11 |   872.52 |   741.56 |   452.32 |     0.85 |   34.9% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 | 1,022.39 |   885.63 |   506.73 |     0.87 |   40.9% |
| 01 |   989.83 |   855.04 |   495.89 |     0.86 |   39.6% |
| 02 |   983.90 |   852.44 |   487.71 |     0.87 |   39.4% |
| 03 |   955.74 |   825.06 |   478.90 |     0.86 |   38.2% |
| 04 |   980.26 |   847.66 |   488.67 |     0.86 |   39.2% |
| 05 |   993.71 |   862.78 |   489.30 |     0.87 |   39.7% |
| 06 |   979.48 |   851.85 |   480.34 |     0.87 |   39.2% |
| 07 |   971.86 |   852.05 |   464.66 |     0.88 |   38.9% |
| 08 |   963.70 |   843.75 |   462.59 |     0.88 |   38.5% |
| 09 |   955.98 |   832.94 |   465.73 |     0.87 |   38.2% |
| 10 |   963.01 |   841.47 |   465.08 |     0.87 |   38.5% |
| 11 |   921.76 |   796.18 |   460.16 |     0.86 |   36.9% |
| 12 |   927.44 |   800.93 |   463.34 |     0.86 |   37.1% |
| 13 |   938.54 |   811.66 |   466.40 |     0.86 |   37.5% |
| 14 |   917.93 |   787.91 |   465.48 |     0.86 |   36.7% |
| 15 |   890.37 |   762.98 |   453.39 |     0.86 |   35.6% |
| 16 |   868.70 |   739.19 |   450.47 |     0.85 |   34.7% |
| 17 |   764.16 |   629.24 |   428.65 |     0.82 |   30.6% |
| 18 |   689.63 |   526.37 |   441.71 |     0.76 |   27.6% |
| 19 |   678.18 |   500.79 |   454.51 |     0.74 |   27.1% |
| 20 |   674.57 |   504.56 |   444.88 |     0.75 |   27.0% |
| 21 |   609.48 |   478.00 |   374.83 |     0.78 |   24.4% |
| 22 |   551.65 |   459.70 |   300.32 |     0.83 |   22.1% |
| 23 |   752.19 |   653.12 |   367.27 |     0.87 |   30.1% |

---

# END OF REPORT

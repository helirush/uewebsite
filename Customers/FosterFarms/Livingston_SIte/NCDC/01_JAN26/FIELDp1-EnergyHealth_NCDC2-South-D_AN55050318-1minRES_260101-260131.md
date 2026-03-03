# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 412,669.2 kWh (Usage per period)
- **Consumption Cost per unit:** $0.177/kWh (Cost per kWh)
- **Consumption Total Cost:** $72,913.69 (Cost per period)
- **Consumption Total Cost:** $102.12 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** NCDC2 South D  
**Generated:** 2026-02-25 09:07:13  
**Data Source:** AN55050318-V-1minRES_44640CLP_260101-260131c.csv  

## Time Period

- **Period:** January 01, 2026 thru January 31, 2026
- **Number of Days:** 31 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 42,839

- **Dataset Coverage:** Complete month (100.0% of 31-day month)
- **Billing Scale Factor:** 1.000x (no normalization needed)

## Facility Information

- **Facility:** Foster Farms
- **Location:** Livingston HQ Facility
- **Analysis Type:** Energy Field Performance Assessment
- **Technology Focus:** Unity Energy Management Solutions

---

## Executive Summary

*Brief overview of key transformer performance metrics and energy consumption.*

- **Transformer:** NCDC2 South D
- **Power Factor:** 0.903
- **Total Energy (Actual):** 412,669.17 kWh (per period), 577.98 kW (per hour)
- **Total Waste (Actual):** 45,196.61 kWh (per period), 63.30 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_NCDC2-South-D_AN55050318-1minRES_260101-260131.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_NCDC2-South-D_AN55050318-1minRES_260101-260131.md


## UNITY MANAGEMENT NCDC2 South D SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 63.30 kW/hr
- **Blended Electricity Rate:** $0.1767/kWh (all-inclusive)
- **NCDC2 South D Utility Cost Offset:** $11.18/hour
- **Annual Offset Savings:** $97978/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 228,745 BTU/hr
- **Total Cooling kW No Longer Needed:** 33.45 kW
- **Cooling Energy Cost Avoided:** $5.91/hour
- **Annual Cooling Savings:** $51772/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 96.75 kW
- **CO2e Emissions Avoided:** 316.39 metric tons/year
- **Monthly CO2e Reduction:** 26.37 metric tons/month
- **Hourly CO2e Reduction:** 0.0361 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $12181/year

### Total NCDC2 South D Unity Savings

- **Per Hour:** $18.49
- **Per Day:** $443.65
- **Per Month:** $13309.39
- **Per Year:** $161931

### NCDC2 South D Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 387.0 kVAR Max (Avg: 277.8 kVAR/hr ; 200,028 kVAR/mo)
- **Max Harmonic Distortion:** 28.8% Max (range: 3.0% - 28.8%)
- **Max Amperage:** 1,103A Max (range: 501A - 1103A)

---

# NCDC2 South D DETAILED PERFORMANCE ANALYSIS

## Unity Technology Status

- **Unity Technology Configuration:** 0.0% reactive energy target
- **Unity Applied:** No (measuring current problem state)
- **Analysis Mode:** Pre-Unity baseline analysis

## Transformer Specifications

- **Capacity:** 3,000.0 kVA
- **Voltage:** 480V, 3-Phase

## Fundamental Energy Values

| Metric | Average | MIN | MAX |
| ------ | ------- | --- | --- |
| Line to Neutral Voltage (277v) |   277.59 |   268.17 |   288.40 |
| Line to Line Voltage (480v) |   480.80 |   464.49 |   499.52 |
| Current (AMPS) |   770.31 |   501.17 |  1102.92 |
| Phase Angle (degrees) |    25.33 |    19.27 |    33.38 |
| Total Harmonic Distortion (PCT) |    15.16 |     3.00 |    28.82 |

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
| Unity THD Composite (%) | 15.2% | Field-level stress indicator |
| Max Phase THD | 5.1% | Highest THD among all three phases |
| Min Phase THD | 5.1% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 822.12 kW
  - **Maximum Load:** 906.88 kVA
  - **Percentage of Capacity (MAX):** 30.2%
- **Average Load:** 641.28 kVA
  - **Percentage of Capacity (Avg):** 21.4%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 641.28 kVA
- **Average Power Factor (PF):** 0.903

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 641.49 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 480.80 V
- Average Current (Iavg_A): 770.31 A
- Average kW (Psum_kW): 577.98 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 0.20 kVA (0.0%)
- **Calculated PF (kW/kVA from averages):** 0.901
- **Power Factor Difference:** 0.002 (0.2%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (641.28) and measured PF (0.903) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA |   641.28 |        21.4% | 457,865.78 kVA | 1,972,155.00 TOTAL-HEAT |
| kW |   577.98 |        19.3% | 412,669.17 kWh | 138,994,241.84 Load-Heat |
| kVAR |   277.82 |         9.3% | 198,356.32 kVARh | - |
| WASTE |    63.30 |         2.1% | 45,196.61 WASTE | 15,223,014.55 Field-Heat |

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 1 |   641.28 |   577.98 |   276.05 |     0.90 |   21.4% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   637.27 |   572.64 |   277.92 |     0.90 |   21.2% |
| 01 |   645.32 |   581.05 |   278.94 |     0.90 |   21.5% |
| 02 |   650.01 |   585.56 |   280.36 |     0.90 |   21.7% |
| 03 |   641.22 |   576.82 |   278.28 |     0.90 |   21.4% |
| 04 |   638.04 |   574.40 |   276.04 |     0.90 |   21.3% |
| 05 |   656.55 |   593.17 |   279.55 |     0.90 |   21.9% |
| 06 |   629.57 |   566.08 |   273.79 |     0.90 |   21.0% |
| 07 |   635.24 |   571.32 |   276.02 |     0.90 |   21.2% |
| 08 |   620.70 |   556.67 |   272.79 |     0.90 |   20.7% |
| 09 |   633.95 |   570.38 |   274.76 |     0.90 |   21.1% |
| 10 |   641.23 |   577.68 |   276.45 |     0.90 |   21.4% |
| 11 |   642.30 |   577.63 |   279.15 |     0.90 |   21.4% |
| 12 |   647.65 |   582.95 |   280.51 |     0.90 |   21.6% |
| 13 |   661.46 |   598.12 |   280.76 |     0.90 |   22.0% |
| 14 |   634.01 |   571.05 |   273.85 |     0.90 |   21.1% |
| 15 |   643.26 |   580.52 |   275.47 |     0.90 |   21.4% |
| 16 |   632.62 |   570.16 |   272.41 |     0.90 |   21.1% |
| 17 |   652.66 |   591.30 |   274.48 |     0.91 |   21.8% |
| 18 |   650.91 |   589.30 |   274.67 |     0.91 |   21.7% |
| 19 |   634.67 |   572.61 |   272.14 |     0.90 |   21.2% |
| 20 |   638.97 |   577.08 |   272.63 |     0.90 |   21.3% |
| 21 |   653.76 |   591.63 |   276.31 |     0.90 |   21.8% |
| 22 |   633.03 |   570.43 |   272.82 |     0.90 |   21.1% |
| 23 |   637.84 |   574.81 |   274.73 |     0.90 |   21.3% |

---

# END OF REPORT

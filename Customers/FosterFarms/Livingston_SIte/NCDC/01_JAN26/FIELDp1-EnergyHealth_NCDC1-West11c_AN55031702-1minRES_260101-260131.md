# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 294,875.3 kWh (Usage per period)
- **Consumption Cost per unit:** $0.177/kWh (Cost per kWh)
- **Consumption Total Cost:** $52,100.93 (Cost per period)
- **Consumption Total Cost:** $70.05 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** NCDC1 West11c  
**Generated:** 2026-02-25 09:06:55  
**Data Source:** AN55031702-V-1minRES_44640CLP_260101-260131c.csv  

## Time Period

- **Period:** January 01, 2026 thru January 31, 2026
- **Number of Days:** 31 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 44,629

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

- **Transformer:** NCDC1 West11c
- **Power Factor:** 0.826
- **Total Energy (Actual):** 294,875.31 kWh (per period), 396.44 kW (per hour)
- **Total Waste (Actual):** 61,814.43 kWh (per period), 83.10 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_NCDC1-West11c_AN55031702-1minRES_260101-260131.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_NCDC1-West11c_AN55031702-1minRES_260101-260131.md


## UNITY MANAGEMENT NCDC1 West11c SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 83.10 kW/hr
- **Blended Electricity Rate:** $0.1767/kWh (all-inclusive)
- **NCDC1 West11c Utility Cost Offset:** $14.68/hour
- **Annual Offset Savings:** $128628/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 302,713 BTU/hr
- **Total Cooling kW No Longer Needed:** 44.26 kW
- **Cooling Energy Cost Avoided:** $7.82/hour
- **Annual Cooling Savings:** $68509/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 127.37 kW
- **CO2e Emissions Avoided:** 416.51 metric tons/year
- **Monthly CO2e Reduction:** 34.71 metric tons/month
- **Hourly CO2e Reduction:** 0.0475 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $16036/year

### Total NCDC1 West11c Unity Savings

- **Per Hour:** $24.33
- **Per Day:** $584.03
- **Per Month:** $17521.02
- **Per Year:** $213172

### NCDC1 West11c Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 360.7 kVAR Max (Avg: 269.8 kVAR/hr ; 194,263 kVAR/mo)
- **Max Harmonic Distortion:** 31.4% Max (range: 3.0% - 31.4%)
- **Max Amperage:** 741A Max (range: 385A - 741A)

---

# NCDC1 West11c DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   278.89 |   268.47 |   290.07 |
| Line to Line Voltage (480v) |   483.05 |   465.00 |   502.42 |
| Current (AMPS) |   573.26 |   384.68 |   741.46 |
| Phase Angle (degrees) |    34.28 |    28.96 |    41.32 |
| Total Harmonic Distortion (PCT) |    16.58 |     3.00 |    31.43 |

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
| THD Phase A (%) | 5.5% | IEEE standard per-phase calculation |
| THD Phase B (%) | 5.5% | IEEE standard per-phase calculation |
| THD Phase C (%) | 5.5% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 16.6% | Field-level stress indicator |
| Max Phase THD | 5.5% | Highest THD among all three phases |
| Min Phase THD | 5.5% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 521.36 kW
  - **Maximum Load:** 617.89 kVA
  - **Percentage of Capacity (MAX):** 24.7%
- **Average Load:** 479.54 kVA
  - **Percentage of Capacity (Avg):** 19.2%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 479.54 kVA
- **Average Power Factor (PF):** 0.826

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 479.62 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 483.05 V
- Average Current (Iavg_A): 573.26 A
- Average kW (Psum_kW): 396.44 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 0.08 kVA (0.0%)
- **Calculated PF (kW/kVA from averages):** 0.827
- **Power Factor Difference:** 0.001 (0.1%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (479.54) and measured PF (0.826) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA |   479.54 |        19.2% | 356,689.74 kVA | 1,352,694.13 TOTAL-HEAT |
| kW |   396.44 |        15.9% | 294,875.31 kWh | 174,367,178.74 Load-Heat |
| kVAR |   269.81 |        10.8% | 200,689.11 kVARh | - |
| WASTE |    83.10 |         3.3% | 61,814.43 WASTE | 36,552,423.26 Field-Heat |

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 1 |   479.54 |   396.44 |   269.33 |     0.83 |   19.2% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   471.75 |   389.30 |   266.13 |     0.83 |   18.9% |
| 01 |   458.25 |   375.62 |   262.24 |     0.82 |   18.3% |
| 02 |   448.16 |   365.59 |   258.97 |     0.82 |   17.9% |
| 03 |   440.83 |   358.28 |   256.63 |     0.81 |   17.6% |
| 04 |   434.44 |   352.08 |   254.30 |     0.81 |   17.4% |
| 05 |   455.00 |   373.42 |   259.55 |     0.82 |   18.2% |
| 06 |   487.92 |   404.68 |   272.04 |     0.83 |   19.5% |
| 07 |   484.44 |   399.92 |   272.92 |     0.83 |   19.4% |
| 08 |   485.50 |   400.90 |   273.38 |     0.83 |   19.4% |
| 09 |   480.92 |   396.50 |   271.74 |     0.82 |   19.2% |
| 10 |   484.07 |   399.19 |   273.34 |     0.82 |   19.4% |
| 11 |   489.87 |   404.84 |   275.30 |     0.83 |   19.6% |
| 12 |   494.12 |   409.64 |   275.76 |     0.83 |   19.8% |
| 13 |   491.84 |   408.78 |   272.87 |     0.83 |   19.7% |
| 14 |   492.26 |   409.95 |   271.87 |     0.83 |   19.7% |
| 15 |   496.78 |   413.77 |   274.43 |     0.83 |   19.9% |
| 16 |   500.44 |   416.64 |   276.72 |     0.83 |   20.0% |
| 17 |   500.94 |   417.58 |   276.24 |     0.83 |   20.0% |
| 18 |   500.12 |   416.52 |   276.37 |     0.83 |   20.0% |
| 19 |   495.49 |   412.50 |   274.02 |     0.83 |   19.8% |
| 20 |   485.41 |   403.58 |   269.24 |     0.83 |   19.4% |
| 21 |   482.41 |   400.40 |   268.65 |     0.83 |   19.3% |
| 22 |   475.70 |   394.15 |   265.99 |     0.83 |   19.0% |
| 23 |   472.30 |   390.65 |   265.11 |     0.83 |   18.9% |

---

# END OF REPORT

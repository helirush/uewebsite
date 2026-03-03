# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 290,457.8 kWh (Usage per period)
- **Consumption Cost per unit:** $0.177/kWh (Cost per kWh)
- **Consumption Total Cost:** $51,320.40 (Cost per period)
- **Consumption Total Cost:** $70.17 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** NCDC3 North E  
**Generated:** 2026-02-25 09:07:32  
**Data Source:** AN55050395-V-1minRES_44640CLP_260101-260131c.csv  

## Time Period

- **Period:** January 01, 2026 thru January 31, 2026
- **Number of Days:** 31 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 43,880

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

- **Transformer:** NCDC3 North E
- **Power Factor:** 0.872
- **Total Energy (Actual):** 290,457.80 kWh (per period), 397.16 kW (per hour)
- **Total Waste (Actual):** 42,587.56 kWh (per period), 58.23 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_NCDC3-North-E_AN55050395-1minRES_260101-260131.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_NCDC3-North-E_AN55050395-1minRES_260101-260131.md


## UNITY MANAGEMENT NCDC3 North E SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 58.23 kW/hr
- **Blended Electricity Rate:** $0.1767/kWh (all-inclusive)
- **NCDC3 North E Utility Cost Offset:** $10.29/hour
- **Annual Offset Savings:** $90132/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 210,950 BTU/hr
- **Total Cooling kW No Longer Needed:** 30.84 kW
- **Cooling Energy Cost Avoided:** $5.45/hour
- **Annual Cooling Savings:** $47741/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 89.08 kW
- **CO2e Emissions Avoided:** 291.30 metric tons/year
- **Monthly CO2e Reduction:** 24.27 metric tons/month
- **Hourly CO2e Reduction:** 0.0333 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $11215/year

### Total NCDC3 North E Unity Savings

- **Per Hour:** $17.02
- **Per Day:** $408.46
- **Per Month:** $12253.78
- **Per Year:** $149088

### NCDC3 North E Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 361.1 kVAR Max (Avg: 222.8 kVAR/hr ; 160,427 kVAR/mo)
- **Max Harmonic Distortion:** 30.7% Max (range: 3.0% - 30.7%)
- **Max Amperage:** 724A Max (range: 371A - 724A)

---

# NCDC3 North E DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   277.78 |   268.32 |   288.28 |
| Line to Line Voltage (480v) |   481.13 |   464.75 |   499.32 |
| Current (AMPS) |   546.37 |   371.47 |   724.17 |
| Phase Angle (degrees) |    29.23 |    20.77 |    38.74 |
| Total Harmonic Distortion (PCT) |    15.61 |     3.00 |    30.72 |

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
| THD Phase B (%) | 5.2% | IEEE standard per-phase calculation |
| THD Phase C (%) | 5.2% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 15.6% | Field-level stress indicator |
| Max Phase THD | 5.2% | Highest THD among all three phases |
| Min Phase THD | 5.2% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 528.88 kW
  - **Maximum Load:** 601.50 kVA
  - **Percentage of Capacity (MAX):** 20.1%
- **Average Load:** 455.39 kVA
  - **Percentage of Capacity (Avg):** 15.2%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 455.39 kVA
- **Average Power Factor (PF):** 0.872

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 455.32 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 481.13 V
- Average Current (Iavg_A): 546.37 A
- Average kW (Psum_kW): 397.16 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 0.08 kVA (0.0%)
- **Calculated PF (kW/kVA from averages):** 0.872
- **Power Factor Difference:** 0.000 (0.0%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (455.39) and measured PF (0.872) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA |   455.39 |        15.2% | 333,045.36 kVA | 1,355,173.11 TOTAL-HEAT |
| kW |   397.16 |        13.2% | 290,457.80 kWh | 126,732,935.24 Load-Heat |
| kVAR |   222.82 |         7.4% | 162,952.38 kVARh | - |
| WASTE |    58.23 |         1.9% | 42,587.56 WASTE | 18,581,860.06 Field-Heat |

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 1 |   455.39 |   397.16 |   222.16 |     0.87 |   15.2% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   421.89 |   370.50 |   201.19 |     0.88 |   14.1% |
| 01 |   449.27 |   391.36 |   220.08 |     0.87 |   15.0% |
| 02 |   487.25 |   427.85 |   232.38 |     0.88 |   16.2% |
| 03 |   455.85 |   399.51 |   218.96 |     0.88 |   15.2% |
| 04 |   456.35 |   403.59 |   211.92 |     0.88 |   15.2% |
| 05 |   438.96 |   383.73 |   212.51 |     0.87 |   14.6% |
| 06 |   439.11 |   385.13 |   210.23 |     0.88 |   14.6% |
| 07 |   445.61 |   385.58 |   222.74 |     0.87 |   14.9% |
| 08 |   432.97 |   376.61 |   212.98 |     0.87 |   14.4% |
| 09 |   431.03 |   375.42 |   211.13 |     0.87 |   14.4% |
| 10 |   457.89 |   396.86 |   227.86 |     0.87 |   15.3% |
| 11 |   474.90 |   412.04 |   235.39 |     0.87 |   15.8% |
| 12 |   438.22 |   380.72 |   216.53 |     0.87 |   14.6% |
| 13 |   501.62 |   436.00 |   247.39 |     0.87 |   16.7% |
| 14 |   486.00 |   416.36 |   250.35 |     0.86 |   16.2% |
| 15 |   475.28 |   411.14 |   237.97 |     0.87 |   15.8% |
| 16 |   448.01 |   386.16 |   226.71 |     0.86 |   14.9% |
| 17 |   457.34 |   399.70 |   221.64 |     0.87 |   15.2% |
| 18 |   444.79 |   390.24 |   213.05 |     0.88 |   14.8% |
| 19 |   472.18 |   410.32 |   233.28 |     0.87 |   15.7% |
| 20 |   454.76 |   399.82 |   216.10 |     0.88 |   15.2% |
| 21 |   439.47 |   385.66 |   210.36 |     0.88 |   14.6% |
| 22 |   478.54 |   422.51 |   224.20 |     0.88 |   16.0% |
| 23 |   451.31 |   393.51 |   220.46 |     0.87 |   15.0% |

---

# END OF REPORT

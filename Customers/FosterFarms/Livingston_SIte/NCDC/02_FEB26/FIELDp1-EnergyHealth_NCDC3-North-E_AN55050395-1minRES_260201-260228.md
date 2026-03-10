# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 269,117.5 kWh (Usage per period)
- **Consumption Cost per unit:** $0.177/kWh (Cost per kWh)
- **Consumption Total Cost:** $47,553.06 (Cost per period)
- **Consumption Total Cost:** $72.64 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** NCDC3 North E  
**Generated:** 2026-03-10 00:52:45  
**Data Source:** AN55050395-V-1minRES_40320CLP_260201-260228c.csv  

## Time Period

- **Period:** February 01, 2026 thru February 28, 2026
- **Number of Days:** 28 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 39,279

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

- **Transformer:** NCDC3 North E
- **Power Factor:** 0.866
- **Total Energy (Actual):** 269,117.49 kWh (per period), 411.09 kW (per hour)
- **Total Waste (Actual):** 41,474.03 kWh (per period), 63.35 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_NCDC3-North-E_AN55050395-1minRES_260201-260228.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_NCDC3-North-E_AN55050395-1minRES_260201-260228.md


## UNITY MANAGEMENT NCDC3 North E SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 63.35 kW/hr
- **Blended Electricity Rate:** $0.1767/kWh (all-inclusive)
- **NCDC3 North E Utility Cost Offset:** $11.19/hour
- **Annual Offset Savings:** $98064/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 229,551 BTU/hr
- **Total Cooling kW No Longer Needed:** 20.13 kW
- **Cooling Energy Cost Avoided:** $3.56/hour
- **Annual Cooling Savings:** $31162/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 83.48 kW
- **CO2e Emissions Avoided:** 273.01 metric tons/year
- **Monthly CO2e Reduction:** 22.75 metric tons/month
- **Hourly CO2e Reduction:** 0.0312 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $10511/year

### Total NCDC3 North E Unity Savings

- **Per Hour:** $15.95
- **Per Day:** $382.84
- **Per Month:** $11485.20
- **Per Year:** $139737

### NCDC3 North E Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 351.6 kVAR Max (Avg: 236.9 kVAR/hr ; 170,536 kVAR/mo)
- **Max Harmonic Distortion:** 28.4% Max (range: 3.0% - 28.4%)
- **Max Amperage:** 730A Max (range: 410A - 730A)

---

# NCDC3 North E DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   277.78 |   267.96 |   288.18 |
| Line to Line Voltage (480v) |   481.13 |   464.12 |   499.14 |
| Current (AMPS) |   569.24 |   410.09 |   729.91 |
| Phase Angle (degrees) |    29.90 |    20.77 |    38.56 |
| Total Harmonic Distortion (PCT) |    15.65 |     3.00 |    28.40 |

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

- **Maximum UtilityDemand:** 529.84 kW
  - **Maximum Load:** 603.71 kVA
  - **Percentage of Capacity (MAX):** 24.1%
- **Average Load:** 474.44 kVA
  - **Percentage of Capacity (Avg):** 19.0%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 474.44 kVA
- **Average Power Factor (PF):** 0.866

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 474.37 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 481.13 V
- Average Current (Iavg_A): 569.24 A
- Average kW (Psum_kW): 411.09 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 0.07 kVA (0.0%)
- **Calculated PF (kW/kVA from averages):** 0.867
- **Power Factor Difference:** 0.000 (0.0%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (474.44) and measured PF (0.866) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA |   474.44 |        19.0% | 310,591.52 kVA | 1,402,684.00 TOTAL-HEAT |
| kW |   411.09 |        16.4% | 269,117.49 kWh | 187,303.76 Load-Heat |
| kVAR |   236.86 |         9.5% | 155,057.63 kVARh | - |
| WASTE |    63.35 |         2.5% | 41,474.03 WASTE | 28,865.62 Field-Heat |

### Heat Unit Notes

- **TOTAL-HEAT (BTU/hr):** 1,402,684.00
- **Load-Heat (BTU/hr):** 187,303.76
- **Field-Heat (BTU/hr):** 28,865.62
- **Load-Heat (BTU, period total):** 122,618,408.87
- **Field-Heat (BTU, period total):** 18,896,875.92

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 2 |   474.44 |   411.09 |   236.23 |     0.87 |   19.0% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   440.92 |   383.00 |   218.02 |     0.87 |   17.6% |
| 01 |   458.41 |   395.54 |   231.17 |     0.86 |   18.3% |
| 02 |   476.91 |   416.22 |   232.14 |     0.87 |   19.1% |
| 03 |   462.01 |   401.58 |   227.94 |     0.87 |   18.5% |
| 04 |   467.47 |   410.34 |   222.98 |     0.88 |   18.7% |
| 05 |   455.29 |   395.66 |   224.54 |     0.87 |   18.2% |
| 06 |   461.26 |   401.77 |   225.79 |     0.87 |   18.5% |
| 07 |   462.77 |   398.67 |   234.34 |     0.86 |   18.5% |
| 08 |   449.07 |   389.40 |   222.87 |     0.87 |   18.0% |
| 09 |   453.59 |   392.96 |   225.87 |     0.87 |   18.1% |
| 10 |   477.57 |   413.32 |   238.55 |     0.87 |   19.1% |
| 11 |   500.58 |   432.00 |   252.14 |     0.86 |   20.0% |
| 12 |   472.21 |   407.87 |   237.58 |     0.86 |   18.9% |
| 13 |   518.45 |   448.35 |   259.73 |     0.86 |   20.7% |
| 14 |   506.07 |   431.63 |   263.78 |     0.85 |   20.2% |
| 15 |   495.63 |   425.85 |   253.08 |     0.86 |   19.8% |
| 16 |   470.87 |   403.42 |   242.44 |     0.86 |   18.8% |
| 17 |   482.26 |   417.82 |   240.29 |     0.87 |   19.3% |
| 18 |   469.28 |   408.59 |   230.43 |     0.87 |   18.8% |
| 19 |   501.41 |   433.56 |   251.54 |     0.86 |   20.1% |
| 20 |   472.96 |   412.07 |   231.67 |     0.87 |   18.9% |
| 21 |   467.20 |   406.69 |   229.60 |     0.87 |   18.7% |
| 22 |   505.02 |   442.52 |   242.80 |     0.88 |   20.2% |
| 23 |   471.11 |   407.68 |   235.60 |     0.87 |   18.8% |

---

# END OF REPORT

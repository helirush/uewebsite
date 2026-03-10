# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 362,266.4 kWh (Usage per period)
- **Consumption Cost per unit:** $0.177/kWh (Cost per kWh)
- **Consumption Total Cost:** $64,012.47 (Cost per period)
- **Consumption Total Cost:** $96.55 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** NCDC2 South D  
**Generated:** 2026-03-10 00:49:25  
**Data Source:** AN55050318-V-1minRES_40320CLP_260201-260228c.csv  

## Time Period

- **Period:** February 01, 2026 thru February 28, 2026
- **Number of Days:** 28 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 39,780

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

- **Transformer:** NCDC2 South D
- **Power Factor:** 0.922
- **Total Energy (Actual):** 362,266.37 kWh (per period), 546.40 kW (per hour)
- **Total Waste (Actual):** 30,176.64 kWh (per period), 45.52 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_NCDC2-South-D_AN55050318-1minRES_260201-260228.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_NCDC2-South-D_AN55050318-1minRES_260201-260228.md


## UNITY MANAGEMENT NCDC2 South D SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 45.52 kW/hr
- **Blended Electricity Rate:** $0.1767/kWh (all-inclusive)
- **NCDC2 South D Utility Cost Offset:** $8.04/hour
- **Annual Offset Savings:** $70453/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 164,888 BTU/hr
- **Total Cooling kW No Longer Needed:** 14.46 kW
- **Cooling Energy Cost Avoided:** $2.56/hour
- **Annual Cooling Savings:** $22385/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 59.98 kW
- **CO2e Emissions Avoided:** 196.13 metric tons/year
- **Monthly CO2e Reduction:** 16.34 metric tons/month
- **Hourly CO2e Reduction:** 0.0224 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $7551/year

### Total NCDC2 South D Unity Savings

- **Per Hour:** $11.46
- **Per Day:** $275.04
- **Per Month:** $8251.12
- **Per Year:** $100389

### NCDC2 South D Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 343.8 kVAR Max (Avg: 227.6 kVAR/hr ; 163,887 kVAR/mo)
- **Max Harmonic Distortion:** 28.2% Max (range: 3.6% - 28.2%)
- **Max Amperage:** 903A Max (range: 513A - 903A)

---

# NCDC2 South D DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   278.11 |   268.46 |   288.53 |
| Line to Line Voltage (480v) |   481.70 |   464.99 |   499.76 |
| Current (AMPS) |   709.31 |   513.17 |   903.12 |
| Phase Angle (degrees) |    22.69 |    19.09 |    29.19 |
| Total Harmonic Distortion (PCT) |    15.62 |     3.60 |    28.17 |

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

- **Maximum UtilityDemand:** 700.48 kW
  - **Maximum Load:** 746.74 kVA
  - **Percentage of Capacity (MAX):** 29.9%
- **Average Load:** 591.92 kVA
  - **Percentage of Capacity (Avg):** 23.7%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 591.92 kVA
- **Average Power Factor (PF):** 0.922

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 591.80 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 481.70 V
- Average Current (Iavg_A): 709.31 A
- Average kW (Psum_kW): 546.40 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 0.12 kVA (0.0%)
- **Calculated PF (kW/kVA from averages):** 0.923
- **Power Factor Difference:** 0.001 (0.1%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (591.92) and measured PF (0.922) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA |   591.92 |        23.7% | 392,443.01 kVA | 1,864,410.69 TOTAL-HEAT |
| kW |   546.40 |        21.9% | 362,266.37 kWh | 143,362.61 Load-Heat |
| kVAR |   227.62 |         9.1% | 150,912.54 kVARh | - |
| WASTE |    45.52 |         1.8% | 30,176.64 WASTE | 11,942.05 Field-Heat |

### Heat Unit Notes

- **TOTAL-HEAT (BTU/hr):** 1,864,410.69
- **Load-Heat (BTU/hr):** 143,362.61
- **Field-Heat (BTU/hr):** 11,942.05
- **Load-Heat (BTU, period total):** 95,049,410.62
- **Field-Heat (BTU, period total):** 7,917,577.54

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 2 |   591.92 |   546.40 |   227.36 |     0.92 |   23.7% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   573.74 |   528.20 |   223.79 |     0.92 |   22.9% |
| 01 |   581.68 |   535.99 |   225.77 |     0.92 |   23.3% |
| 02 |   594.98 |   549.17 |   228.72 |     0.92 |   23.8% |
| 03 |   574.16 |   528.49 |   224.15 |     0.92 |   23.0% |
| 04 |   578.91 |   533.57 |   224.35 |     0.92 |   23.2% |
| 05 |   599.33 |   554.16 |   228.02 |     0.92 |   24.0% |
| 06 |   572.39 |   527.40 |   222.20 |     0.92 |   22.9% |
| 07 |   577.15 |   532.22 |   222.99 |     0.92 |   23.1% |
| 08 |   565.84 |   520.61 |   221.42 |     0.92 |   22.6% |
| 09 |   585.93 |   540.46 |   226.02 |     0.92 |   23.4% |
| 10 |   599.49 |   553.78 |   229.33 |     0.92 |   24.0% |
| 11 |   591.17 |   545.41 |   227.80 |     0.92 |   23.6% |
| 12 |   605.86 |   559.99 |   230.99 |     0.92 |   24.2% |
| 13 |   616.22 |   570.51 |   232.69 |     0.93 |   24.6% |
| 14 |   593.66 |   547.84 |   228.46 |     0.92 |   23.7% |
| 15 |   599.31 |   553.36 |   229.86 |     0.92 |   24.0% |
| 16 |   590.33 |   544.38 |   228.11 |     0.92 |   23.6% |
| 17 |   614.51 |   568.75 |   232.45 |     0.93 |   24.6% |
| 18 |   621.32 |   575.85 |   233.09 |     0.93 |   24.9% |
| 19 |   592.09 |   546.66 |   227.21 |     0.92 |   23.7% |
| 20 |   597.75 |   552.65 |   227.57 |     0.92 |   23.9% |
| 21 |   616.86 |   571.35 |   232.25 |     0.93 |   24.7% |
| 22 |   584.15 |   538.96 |   225.04 |     0.92 |   23.4% |
| 23 |   581.49 |   536.17 |   224.83 |     0.92 |   23.3% |

---

# END OF REPORT

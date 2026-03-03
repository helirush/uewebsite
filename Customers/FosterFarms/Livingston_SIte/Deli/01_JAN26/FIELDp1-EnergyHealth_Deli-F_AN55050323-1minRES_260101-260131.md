# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 514,179.5 kWh (Usage per period)
- **Consumption Cost per unit:** $0.146/kWh (Cost per kWh)
- **Consumption Total Cost:** $75,187.03 (Cost per period)
- **Consumption Total Cost:** $101.07 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** Deli F  
**Generated:** 2026-02-19 02:23:44  
**Data Source:** AN55050323-V-1minRES_44640CLP_260101-260131c.csv  

## Time Period

- **Period:** January 01, 2026 thru January 31, 2026
- **Number of Days:** 31 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 44,635

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

- **Transformer:** Deli F
- **Power Factor:** 0.851
- **Total Energy (Actual):** 514,179.46 kWh (per period), 691.18 kW (per hour)
- **Total Waste (Actual):** 63,940.91 kWh (per period), 85.95 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_Deli-F_AN55050323-1minRES_260101-260131.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_Deli-F_AN55050323-1minRES_260101-260131.md


## UNITY MANAGEMENT Deli F SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 85.95 kW/hr
- **Blended Electricity Rate:** $0.1462/kWh (all-inclusive)
- **Deli F Utility Cost Offset:** $12.57/hour
- **Annual Offset Savings:** $110100/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 309,318 BTU/hr
- **Total Cooling kW No Longer Needed:** 27.14 kW
- **Cooling Energy Cost Avoided:** $3.97/hour
- **Annual Cooling Savings:** $34761/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 113.09 kW
- **CO2e Emissions Avoided:** 369.82 metric tons/year
- **Monthly CO2e Reduction:** 30.82 metric tons/month
- **Hourly CO2e Reduction:** 0.0422 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $14238/year

### Total Deli F Unity Savings

- **Per Hour:** $18.16
- **Per Day:** $435.89
- **Per Month:** $13076.64
- **Per Year:** $159099

### Deli F Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 1,631.9 kVAR Max (Avg: 355.3 kVAR/hr ; 255,781 kVAR/mo)
- **Max Harmonic Distortion:** 31.9% Max (range: 3.0% - 31.9%)
- **Max Amperage:** 2,798A Max (range: 12A - 2798A)

---

# Deli F DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   278.18 |   266.56 |   288.68 |
| Line to Line Voltage (480v) |   481.82 |   461.69 |   500.01 |
| Current (AMPS) |   934.33 |    12.41 |  2798.32 |
| Phase Angle (degrees) |    30.96 |     0.00 |    80.85 |
| Total Harmonic Distortion (PCT) |    14.41 |     3.03 |    31.90 |

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
| THD Phase A (%) | 4.8% | IEEE standard per-phase calculation |
| THD Phase B (%) | 4.8% | IEEE standard per-phase calculation |
| THD Phase C (%) | 4.8% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 14.4% | Field-level stress indicator |
| Max Phase THD | 4.8% | Highest THD among all three phases |
| Min Phase THD | 4.8% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 1,705.95 kW
  - **Maximum Load:** 2,273.72 kVA
  - **Percentage of Capacity (MAX):** 90.9%
- **Average Load:** 777.13 kVA
  - **Percentage of Capacity (Avg):** 31.1%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 777.13 kVA
- **Average Power Factor (PF):** 0.851

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 779.74 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 481.82 V
- Average Current (Iavg_A): 934.33 A
- Average kW (Psum_kW): 691.18 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 2.61 kVA (0.3%)
- **Calculated PF (kW/kVA from averages):** 0.886
- **Power Factor Difference:** 0.035 (4.2%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (777.13) and measured PF (0.851) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA |   777.13 |        31.1% | 578,120.38 kVA | 2,358,400.38 TOTAL-HEAT |
| kW |   691.18 |        27.6% | 514,179.46 kWh | 194,044,965.15 Load-Heat |
| kVAR |   355.25 |        14.2% | 264,277.60 kVARh | - |
| WASTE |    85.95 |         3.4% | 63,940.91 WASTE | 24,130,508.99 Field-Heat |

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 1 |   777.13 |   691.18 |   351.42 |     0.89 |   31.1% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   712.97 |   595.48 |   391.08 |     0.84 |   28.5% |
| 01 |   272.30 |   220.54 |   158.48 |     0.81 |   10.9% |
| 02 |    55.42 |    45.88 |    29.89 |     0.83 |    2.2% |
| 03 |    52.01 |    43.73 |    27.47 |     0.84 |    2.1% |
| 04 |    39.20 |    33.28 |    20.30 |     0.85 |    1.6% |
| 05 |   182.87 |   142.68 |   110.70 |     0.78 |    7.3% |
| 06 |   906.02 |   819.27 |   378.96 |     0.90 |   36.2% |
| 07 |   986.99 |   889.54 |   425.83 |     0.90 |   39.5% |
| 08 |   959.58 |   854.03 |   434.54 |     0.89 |   38.4% |
| 09 |   999.11 |   898.72 |   434.30 |     0.90 |   40.0% |
| 10 |   902.81 |   792.32 |   429.39 |     0.88 |   36.1% |
| 11 |   972.76 |   872.82 |   427.12 |     0.90 |   38.9% |
| 12 |   999.02 |   896.94 |   437.89 |     0.90 |   40.0% |
| 13 |   962.42 |   858.84 |   431.81 |     0.89 |   38.5% |
| 14 | 1,011.58 |   910.63 |   438.61 |     0.90 |   40.5% |
| 15 |   942.73 |   835.85 |   432.75 |     0.89 |   37.7% |
| 16 |   972.76 |   874.76 |   423.59 |     0.90 |   38.9% |
| 17 |   961.65 |   857.03 |   433.23 |     0.89 |   38.5% |
| 18 |   991.64 |   893.01 |   429.58 |     0.90 |   39.7% |
| 19 |   942.48 |   834.55 |   434.42 |     0.89 |   37.7% |
| 20 |   938.60 |   839.02 |   417.62 |     0.89 |   37.5% |
| 21 | 1,002.32 |   902.06 |   435.16 |     0.90 |   40.1% |
| 22 |   940.70 |   837.02 |   426.32 |     0.89 |   37.6% |
| 23 |   943.13 |   840.23 |   424.92 |     0.89 |   37.7% |

---

# END OF REPORT

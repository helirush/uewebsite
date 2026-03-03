# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 385,231.7 kWh (Usage per period)
- **Consumption Cost per unit:** $0.146/kWh (Cost per kWh)
- **Consumption Total Cost:** $56,331.35 (Cost per period)
- **Consumption Total Cost:** $75.74 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** Deli G  
**Generated:** 2026-02-19 02:23:56  
**Data Source:** AN55050305-V-1minRES_44640CLP_260101-260131c.csv  

## Time Period

- **Period:** January 01, 2026 thru January 31, 2026
- **Number of Days:** 31 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 44,623

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

- **Transformer:** Deli G
- **Power Factor:** 0.862
- **Total Energy (Actual):** 385,231.68 kWh (per period), 517.98 kW (per hour)
- **Total Waste (Actual):** 46,091.27 kWh (per period), 61.97 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_Deli-G_AN55050305-1minRES_260101-260131.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_Deli-G_AN55050305-1minRES_260101-260131.md


## UNITY MANAGEMENT Deli G SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 61.97 kW/hr
- **Blended Electricity Rate:** $0.1462/kWh (all-inclusive)
- **Deli G Utility Cost Offset:** $9.06/hour
- **Annual Offset Savings:** $79386/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 222,126 BTU/hr
- **Total Cooling kW No Longer Needed:** 19.49 kW
- **Cooling Energy Cost Avoided:** $2.85/hour
- **Annual Cooling Savings:** $24963/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 81.46 kW
- **CO2e Emissions Avoided:** 266.39 metric tons/year
- **Monthly CO2e Reduction:** 22.20 metric tons/month
- **Hourly CO2e Reduction:** 0.0304 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $10256/year

### Total Deli G Unity Savings

- **Per Hour:** $13.08
- **Per Day:** $313.99
- **Per Month:** $9419.55
- **Per Year:** $114605

### Deli G Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 1,567.1 kVAR Max (Avg: 260.9 kVAR/hr ; 187,814 kVAR/mo)
- **Max Harmonic Distortion:** 27.9% Max (range: 3.0% - 27.9%)
- **Max Amperage:** 2,293A Max (range: 76A - 2293A)

---

# Deli G DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   277.57 |   264.60 |   289.73 |
| Line to Line Voltage (480v) |   480.76 |   458.31 |   501.82 |
| Current (AMPS) |   699.04 |    76.28 |  2293.20 |
| Phase Angle (degrees) |    29.27 |     5.73 |    69.15 |
| Total Harmonic Distortion (PCT) |    13.65 |     3.00 |    27.87 |

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
| THD Phase A (%) | 4.5% | IEEE standard per-phase calculation |
| THD Phase B (%) | 4.6% | IEEE standard per-phase calculation |
| THD Phase C (%) | 4.5% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 13.6% | Field-level stress indicator |
| Max Phase THD | 4.6% | Highest THD among all three phases |
| Min Phase THD | 4.5% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 1,776.06 kW
  - **Maximum Load:** 1,884.04 kVA
  - **Percentage of Capacity (MAX):** 75.4%
- **Average Load:** 579.96 kVA
  - **Percentage of Capacity (Avg):** 23.2%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 579.96 kVA
- **Average Power Factor (PF):** 0.862

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 582.09 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 480.76 V
- Average Current (Iavg_A): 699.04 A
- Average kW (Psum_kW): 517.98 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 2.13 kVA (0.4%)
- **Calculated PF (kW/kVA from averages):** 0.890
- **Power Factor Difference:** 0.028 (3.2%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (579.96) and measured PF (0.862) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA |   579.96 |        23.2% | 431,322.96 kVA | 1,767,427.39 TOTAL-HEAT |
| kW |   517.98 |        20.7% | 385,231.68 kWh | 140,464,067.10 Load-Heat |
| kVAR |   260.85 |        10.4% | 194,000.11 kVARh | - |
| WASTE |    61.97 |         2.5% | 46,091.27 WASTE | 16,805,907.13 Field-Heat |

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 1 |   579.96 |   517.98 |   247.79 |     0.89 |   23.2% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   428.76 |   369.19 |   208.09 |     0.86 |   17.2% |
| 01 |   286.33 |   220.52 |   181.56 |     0.77 |   11.5% |
| 02 |   264.25 |   198.62 |   173.37 |     0.75 |   10.6% |
| 03 |   268.51 |   203.30 |   172.82 |     0.76 |   10.7% |
| 04 |   273.80 |   209.34 |   172.33 |     0.76 |   11.0% |
| 05 |   306.31 |   236.65 |   191.54 |     0.77 |   12.3% |
| 06 |   813.44 |   715.51 |   370.36 |     0.88 |   32.5% |
| 07 |   785.89 |   708.77 |   328.34 |     0.90 |   31.4% |
| 08 |   790.22 |   703.36 |   349.79 |     0.89 |   31.6% |
| 09 |   738.82 |   674.67 |   295.02 |     0.91 |   29.6% |
| 10 |   687.59 |   621.76 |   284.55 |     0.90 |   27.5% |
| 11 |   612.24 |   550.59 |   257.66 |     0.90 |   24.5% |
| 12 |   703.32 |   646.68 |   269.83 |     0.92 |   28.1% |
| 13 |   636.88 |   569.60 |   274.26 |     0.89 |   25.5% |
| 14 |   707.89 |   649.27 |   274.43 |     0.92 |   28.3% |
| 15 |   571.55 |   500.63 |   264.08 |     0.88 |   22.9% |
| 16 |   687.52 |   636.07 |   254.96 |     0.93 |   27.5% |
| 17 |   682.61 |   624.67 |   266.97 |     0.92 |   27.3% |
| 18 |   639.64 |   587.03 |   245.33 |     0.92 |   25.6% |
| 19 |   652.24 |   605.12 |   237.16 |     0.93 |   26.1% |
| 20 |   524.35 |   475.27 |   210.86 |     0.91 |   21.0% |
| 21 |   650.01 |   610.14 |   220.13 |     0.94 |   26.0% |
| 22 |   565.19 |   517.80 |   217.37 |     0.92 |   22.6% |
| 23 |   643.12 |   598.31 |   226.94 |     0.93 |   25.7% |

---

# END OF REPORT

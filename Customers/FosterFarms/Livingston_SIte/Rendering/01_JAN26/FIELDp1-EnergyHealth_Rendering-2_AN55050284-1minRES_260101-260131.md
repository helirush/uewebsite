# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 701,290.1 kWh (Usage per period)
- **Consumption Cost per unit:** $0.177/kWh (Cost per kWh)
- **Consumption Total Cost:** $123,917.96 (Cost per period)
- **Consumption Total Cost:** $181.01 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** Rendering-2  
**Generated:** 2026-02-26 09:44:55  
**Data Source:** AN55050284-V-1minRES_44640CLP_260101-260131c.csv  

## Time Period

- **Period:** January 01, 2026 thru January 31, 2026
- **Number of Days:** 31 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 41,076

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

- **Transformer:** Rendering-2
- **Power Factor:** 0.705
- **Total Energy (Actual):** 701,290.12 kWh (per period), 1024.38 kW (per hour)
- **Total Waste (Actual):** 287,795.31 kWh (per period), 420.38 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_Rendering-2_AN55050284-1minRES_260101-260131.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_Rendering-2_AN55050284-1minRES_260101-260131.md


## UNITY MANAGEMENT Rendering-2 SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 420.38 kW/hr
- **Blended Electricity Rate:** $0.1767/kWh (all-inclusive)
- **Rendering-2 Utility Cost Offset:** $74.28/hour
- **Annual Offset Savings:** $650710/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 1,629,843 BTU/hr
- **Total Cooling kW No Longer Needed:** 238.31 kW
- **Cooling Energy Cost Avoided:** $42.11/hour
- **Annual Cooling Savings:** $368881/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 658.70 kW
- **CO2e Emissions Avoided:** 2154.05 metric tons/year
- **Monthly CO2e Reduction:** 179.50 metric tons/month
- **Hourly CO2e Reduction:** 0.2459 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $82931/year

### Total Rendering-2 Unity Savings

- **Per Hour:** $125.86
- **Per Day:** $3020.61
- **Per Month:** $90618.25
- **Per Year:** $1102522

### Rendering-2 Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 1,542.7 kVAR Max (Avg: 1,018.8 kVAR/hr ; 733,549 kVAR/mo)
- **Max Harmonic Distortion:** 29.9% Max (range: 3.0% - 29.9%)
- **Max Amperage:** 2,514A Max (range: 905A - 2514A)

---

# Rendering-2 DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   271.38 |   261.09 |   281.98 |
| Line to Line Voltage (480v) |   470.05 |   452.22 |   488.40 |
| Current (AMPS) |  1775.90 |   904.62 |  2514.00 |
| Phase Angle (degrees) |    45.10 |    27.00 |    57.11 |
| Total Harmonic Distortion (PCT) |    16.26 |     3.00 |    29.95 |

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
| THD Phase A (%) | 5.4% | IEEE standard per-phase calculation |
| THD Phase B (%) | 5.4% | IEEE standard per-phase calculation |
| THD Phase C (%) | 5.4% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 16.3% | Field-level stress indicator |
| Max Phase THD | 5.4% | Highest THD among all three phases |
| Min Phase THD | 5.4% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 1,439.77 kW
  - **Maximum Load:** 1,989.07 kVA
  - **Percentage of Capacity (MAX):** 79.6%
- **Average Load:** 1,444.76 kVA
  - **Percentage of Capacity (Avg):** 57.8%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 1,444.76 kVA
- **Average Power Factor (PF):** 0.705

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 1,445.85 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 470.05 V
- Average Current (Iavg_A): 1775.90 A
- Average kW (Psum_kW): 1024.38 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 1.08 kVA (0.1%)
- **Calculated PF (kW/kVA from averages):** 0.708
- **Power Factor Difference:** 0.004 (0.5%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (1444.76) and measured PF (0.705) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA | 1,444.76 |        57.8% | 989,085.43 kVA | 3,495,327.90 TOTAL-HEAT |
| kW | 1,024.38 |        41.0% | 701,290.12 kWh | 696,265,250.87 Load-Heat |
| kVAR | 1,018.82 |        40.8% | 697,482.72 kVARh | - |
| WASTE |   420.38 |        16.8% | 287,795.31 WASTE | 285,733,200.31 Field-Heat |

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 1 | 1,444.76 | 1,024.38 | 1,016.43 |     0.71 |   57.8% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 | 1,454.99 | 1,024.95 | 1,030.53 |     0.70 |   58.2% |
| 01 | 1,462.90 | 1,034.42 | 1,032.97 |     0.71 |   58.5% |
| 02 | 1,451.10 | 1,024.57 | 1,025.72 |     0.71 |   58.0% |
| 03 | 1,443.93 | 1,021.44 | 1,018.42 |     0.71 |   57.8% |
| 04 | 1,447.91 | 1,026.43 | 1,019.42 |     0.71 |   57.9% |
| 05 | 1,418.24 | 1,003.17 | 1,000.54 |     0.71 |   56.7% |
| 06 | 1,433.32 | 1,016.81 | 1,008.19 |     0.71 |   57.3% |
| 07 | 1,426.73 | 1,014.73 | 1,000.76 |     0.71 |   57.1% |
| 08 | 1,460.33 | 1,040.09 | 1,022.96 |     0.71 |   58.4% |
| 09 | 1,465.27 | 1,036.27 | 1,033.58 |     0.71 |   58.6% |
| 10 | 1,491.69 | 1,055.16 | 1,052.14 |     0.71 |   59.7% |
| 11 | 1,475.97 | 1,040.98 | 1,043.97 |     0.71 |   59.0% |
| 12 | 1,455.54 | 1,028.87 | 1,027.52 |     0.71 |   58.2% |
| 13 | 1,430.95 | 1,010.00 | 1,011.25 |     0.71 |   57.2% |
| 14 | 1,446.76 | 1,022.87 | 1,020.11 |     0.71 |   57.9% |
| 15 | 1,472.96 | 1,049.03 | 1,030.65 |     0.71 |   58.9% |
| 16 | 1,506.40 | 1,079.69 | 1,047.19 |     0.72 |   60.3% |
| 17 | 1,482.26 | 1,063.56 | 1,029.11 |     0.72 |   59.3% |
| 18 | 1,373.88 |   970.83 |   969.03 |     0.71 |   55.0% |
| 19 | 1,349.18 |   953.44 |   951.97 |     0.71 |   54.0% |
| 20 | 1,407.92 | 1,005.07 |   983.27 |     0.71 |   56.3% |
| 21 | 1,440.29 | 1,029.11 | 1,005.51 |     0.71 |   57.6% |
| 22 | 1,455.49 | 1,032.15 | 1,024.38 |     0.71 |   58.2% |
| 23 | 1,434.20 | 1,011.67 | 1,014.61 |     0.71 |   57.4% |

---

# END OF REPORT

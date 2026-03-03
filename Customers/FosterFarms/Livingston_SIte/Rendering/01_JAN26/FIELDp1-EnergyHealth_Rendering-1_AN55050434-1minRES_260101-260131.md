# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 729,447.3 kWh (Usage per period)
- **Consumption Cost per unit:** $0.177/kWh (Cost per kWh)
- **Consumption Total Cost:** $128,893.34 (Cost per period)
- **Consumption Total Cost:** $188.03 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** Rendering-1  
**Generated:** 2026-02-26 09:45:33  
**Data Source:** AN55050434-V-1minRES_44640CLP_260101-260131c.csv  

## Time Period

- **Period:** January 01, 2026 thru January 31, 2026
- **Number of Days:** 31 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 41,129

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

- **Transformer:** Rendering-1
- **Power Factor:** 0.822
- **Total Energy (Actual):** 729,447.32 kWh (per period), 1064.14 kW (per hour)
- **Total Waste (Actual):** 157,141.14 kWh (per period), 229.24 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_Rendering-1_AN55050434-1minRES_260101-260131.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_Rendering-1_AN55050434-1minRES_260101-260131.md


## UNITY MANAGEMENT Rendering-1 SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 229.24 kW/hr
- **Blended Electricity Rate:** $0.1767/kWh (all-inclusive)
- **Rendering-1 Utility Cost Offset:** $40.51/hour
- **Annual Offset Savings:** $354841/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 877,911 BTU/hr
- **Total Cooling kW No Longer Needed:** 128.36 kW
- **Cooling Energy Cost Avoided:** $22.68/hour
- **Annual Cooling Savings:** $198695/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 357.61 kW
- **CO2e Emissions Avoided:** 1169.43 metric tons/year
- **Monthly CO2e Reduction:** 97.45 metric tons/month
- **Hourly CO2e Reduction:** 0.1335 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $45023/year

### Total Rendering-1 Unity Savings

- **Per Hour:** $68.33
- **Per Day:** $1639.89
- **Per Month:** $49196.60
- **Per Year:** $598559

### Rendering-1 Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 1,118.9 kVAR Max (Avg: 735.1 kVAR/hr ; 529,305 kVAR/mo)
- **Max Harmonic Distortion:** 31.9% Max (range: 3.0% - 31.9%)
- **Max Amperage:** 2,067A Max (range: 1125A - 2067A)

---

# Rendering-1 DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   272.75 |   263.06 |   283.77 |
| Line to Line Voltage (480v) |   472.42 |   455.63 |   491.50 |
| Current (AMPS) |  1580.60 |  1124.68 |  2066.79 |
| Phase Angle (degrees) |    34.68 |    24.36 |    45.89 |
| Total Harmonic Distortion (PCT) |    16.72 |     3.01 |    31.85 |

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
| THD Phase A (%) | 5.6% | IEEE standard per-phase calculation |
| THD Phase B (%) | 5.6% | IEEE standard per-phase calculation |
| THD Phase C (%) | 5.6% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 16.7% | Field-level stress indicator |
| Max Phase THD | 5.6% | Highest THD among all three phases |
| Min Phase THD | 5.6% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 1,320.01 kW
  - **Maximum Load:** 1,658.71 kVA
  - **Percentage of Capacity (MAX):** 66.3%
- **Average Load:** 1,293.38 kVA
  - **Percentage of Capacity (Avg):** 51.7%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 1,293.38 kVA
- **Average Power Factor (PF):** 0.822

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 1,293.34 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 472.42 V
- Average Current (Iavg_A): 1580.60 A
- Average kW (Psum_kW): 1064.14 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 0.04 kVA (0.0%)
- **Calculated PF (kW/kVA from averages):** 0.823
- **Power Factor Difference:** 0.001 (0.1%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (1293.38) and measured PF (0.822) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA | 1,293.38 |        51.7% | 886,588.46 kVA | 3,630,982.28 TOTAL-HEAT |
| kW | 1,064.14 |        42.6% | 729,447.32 kWh | 441,152,607.74 Load-Heat |
| kVAR |   735.15 |        29.4% | 503,930.25 kVARh | - |
| WASTE |   229.24 |         9.2% | 157,141.14 WASTE | 95,035,269.87 Field-Heat |

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 1 | 1,293.38 | 1,064.14 |   734.23 |     0.82 |   51.7% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 | 1,321.25 | 1,085.62 |   752.36 |     0.82 |   52.8% |
| 01 | 1,316.68 | 1,078.24 |   754.98 |     0.82 |   52.7% |
| 02 | 1,309.10 | 1,072.79 |   749.49 |     0.82 |   52.4% |
| 03 | 1,304.56 | 1,069.83 |   745.84 |     0.82 |   52.2% |
| 04 | 1,316.81 | 1,082.60 |   749.03 |     0.82 |   52.7% |
| 05 | 1,300.24 | 1,068.42 |   740.17 |     0.82 |   52.0% |
| 06 | 1,317.77 | 1,085.10 |   746.84 |     0.82 |   52.7% |
| 07 | 1,322.44 | 1,087.27 |   751.96 |     0.82 |   52.9% |
| 08 | 1,315.57 | 1,080.07 |   750.29 |     0.82 |   52.6% |
| 09 | 1,317.01 | 1,080.39 |   752.38 |     0.82 |   52.7% |
| 10 | 1,327.42 | 1,091.18 |   755.03 |     0.82 |   53.1% |
| 11 | 1,327.29 | 1,092.28 |   753.17 |     0.82 |   53.1% |
| 12 | 1,325.98 | 1,091.58 |   751.94 |     0.82 |   53.0% |
| 13 | 1,299.58 | 1,068.10 |   739.47 |     0.82 |   52.0% |
| 14 | 1,286.30 | 1,055.24 |   734.83 |     0.82 |   51.5% |
| 15 | 1,283.59 | 1,056.36 |   728.14 |     0.82 |   51.3% |
| 16 | 1,290.19 | 1,065.14 |   727.09 |     0.83 |   51.6% |
| 17 | 1,262.76 | 1,044.04 |   709.38 |     0.83 |   50.5% |
| 18 | 1,225.78 | 1,004.52 |   701.51 |     0.82 |   49.0% |
| 19 | 1,214.27 |   994.34 |   695.78 |     0.82 |   48.6% |
| 20 | 1,240.47 | 1,025.85 |   696.01 |     0.83 |   49.6% |
| 21 | 1,248.11 | 1,035.80 |   695.04 |     0.83 |   49.9% |
| 22 | 1,286.26 | 1,066.33 |   718.55 |     0.83 |   51.5% |
| 23 | 1,309.10 | 1,079.79 |   739.45 |     0.82 |   52.4% |

---

# END OF REPORT

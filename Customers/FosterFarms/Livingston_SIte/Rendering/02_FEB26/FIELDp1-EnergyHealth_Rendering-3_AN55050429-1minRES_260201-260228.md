# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 377,529.5 kWh (Usage per period)
- **Consumption Cost per unit:** $0.175/kWh (Cost per kWh)
- **Consumption Total Cost:** $65,954.40 (Cost per period)
- **Consumption Total Cost:** $100.60 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** Rendering-3  
**Generated:** 2026-03-05 11:19:44  
**Data Source:** AN55050429-V-1minRES_40320CLP_260201-260228c.csv  

## Time Period

- **Period:** February 01, 2026 thru February 28, 2026
- **Number of Days:** 28 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 39,338

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

- **Transformer:** Rendering-3
- **Power Factor:** 0.770
- **Total Energy (Actual):** 377,529.49 kWh (per period), 575.82 kW (per hour)
- **Total Waste (Actual):** 112,421.99 kWh (per period), 171.47 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_Rendering-3_AN55050429-1minRES_260201-260228.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_Rendering-3_AN55050429-1minRES_260201-260228.md


## UNITY MANAGEMENT Rendering-3 SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 171.47 kW/hr
- **Blended Electricity Rate:** $0.1747/kWh (all-inclusive)
- **Rendering-3 Utility Cost Offset:** $29.96/hour
- **Annual Offset Savings:** $262414/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 633,808 BTU/hr
- **Total Cooling kW No Longer Needed:** 55.59 kW
- **Cooling Energy Cost Avoided:** $9.71/hour
- **Annual Cooling Savings:** $85069/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 227.06 kW
- **CO2e Emissions Avoided:** 742.52 metric tons/year
- **Monthly CO2e Reduction:** 61.88 metric tons/month
- **Hourly CO2e Reduction:** 0.0848 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $28587/year

### Total Rendering-3 Unity Savings

- **Per Hour:** $42.93
- **Per Day:** $1030.33
- **Per Month:** $30909.89
- **Per Year:** $376070

### Rendering-3 Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 599.6 kVAR Max (Avg: 476.3 kVAR/hr ; 342,947 kVAR/mo)
- **Max Harmonic Distortion:** 30.1% Max (range: 3.2% - 30.1%)
- **Max Amperage:** 1,090A Max (range: 724A - 1090A)

---

# Rendering-3 DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   275.63 |   266.12 |   285.64 |
| Line to Line Voltage (480v) |   477.41 |   460.93 |   494.75 |
| Current (AMPS) |   903.78 |   724.47 |  1089.71 |
| Phase Angle (degrees) |    39.62 |    35.11 |    49.08 |
| Total Harmonic Distortion (PCT) |    16.15 |     3.18 |    30.05 |

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
| Unity THD Composite (%) | 16.1% | Field-level stress indicator |
| Max Phase THD | 5.4% | Highest THD among all three phases |
| Min Phase THD | 5.4% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 688.26 kW
  - **Maximum Load:** 894.37 kVA
  - **Percentage of Capacity (MAX):** 35.8%
- **Average Load:** 747.29 kVA
  - **Percentage of Capacity (Avg):** 29.9%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 747.29 kVA
- **Average Power Factor (PF):** 0.770

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 747.33 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 477.41 V
- Average Current (Iavg_A): 903.78 A
- Average kW (Psum_kW): 575.82 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 0.04 kVA (0.0%)
- **Calculated PF (kW/kVA from averages):** 0.771
- **Power Factor Difference:** 0.001 (0.1%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (747.29) and measured PF (0.770) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA |   747.29 |        29.9% | 489,951.48 kVA | 1,964,793.68 TOTAL-HEAT |
| kW |   575.82 |        23.0% | 377,529.49 kWh | 450,832.42 Load-Heat |
| kVAR |   476.32 |        19.1% | 312,288.22 kVARh | - |
| WASTE |   171.47 |         6.9% | 112,421.99 WASTE | 134,250.38 Field-Heat |

### Heat Unit Notes

- **TOTAL-HEAT (BTU/hr):** 1,964,793.68
- **Load-Heat (BTU/hr):** 450,832.42
- **Field-Heat (BTU/hr):** 134,250.38
- **Load-Heat (BTU, period total):** 295,580,761.85
- **Field-Heat (BTU, period total):** 88,019,022.48

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 2 |   747.29 |   575.82 |   475.58 |     0.77 |   29.9% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   737.75 |   571.47 |   466.16 |     0.77 |   29.5% |
| 01 |   735.00 |   571.16 |   462.10 |     0.78 |   29.4% |
| 02 |   745.21 |   578.46 |   469.18 |     0.78 |   29.8% |
| 03 |   737.76 |   574.62 |   461.92 |     0.78 |   29.5% |
| 04 |   751.03 |   584.46 |   471.06 |     0.78 |   30.0% |
| 05 |   752.06 |   584.28 |   472.74 |     0.78 |   30.1% |
| 06 |   758.48 |   586.30 |   480.52 |     0.77 |   30.3% |
| 07 |   752.12 |   583.62 |   473.80 |     0.78 |   30.1% |
| 08 |   760.18 |   585.97 |   483.42 |     0.77 |   30.4% |
| 09 |   747.97 |   578.73 |   473.22 |     0.77 |   29.9% |
| 10 |   757.88 |   582.32 |   484.28 |     0.77 |   30.3% |
| 11 |   747.94 |   571.74 |   481.30 |     0.76 |   29.9% |
| 12 |   741.69 |   571.55 |   471.92 |     0.77 |   29.7% |
| 13 |   739.14 |   567.36 |   472.84 |     0.77 |   29.6% |
| 14 |   755.65 |   572.23 |   492.70 |     0.76 |   30.2% |
| 15 |   742.47 |   568.54 |   476.88 |     0.77 |   29.7% |
| 16 |   750.56 |   574.67 |   481.89 |     0.77 |   30.0% |
| 17 |   742.61 |   571.27 |   473.63 |     0.77 |   29.7% |
| 18 |   746.76 |   571.84 |   479.71 |     0.77 |   29.9% |
| 19 |   739.86 |   563.71 |   478.53 |     0.76 |   29.6% |
| 20 |   755.15 |   576.88 |   486.60 |     0.76 |   30.2% |
| 21 |   744.46 |   574.98 |   472.23 |     0.77 |   29.8% |
| 22 |   750.45 |   578.93 |   477.00 |     0.77 |   30.0% |
| 23 |   743.24 |   574.60 |   470.83 |     0.77 |   29.7% |

---

# END OF REPORT

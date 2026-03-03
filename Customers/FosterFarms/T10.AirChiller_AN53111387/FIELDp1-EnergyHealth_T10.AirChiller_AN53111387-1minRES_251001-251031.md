# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 539,098.0 kWh (Usage per period)
- **Consumption Cost per unit:** $0.318/kWh (Cost per kWh)
- **Consumption Total Cost:** $171,531.18 (Cost per period)
- **Consumption Total Cost:** $231.63 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** T10.AirChiller  
**Generated:** 2026-01-06 13:46:53  
**Data Source:** AN53111387-V-1minRES_44640CLP_251001-251031zth.csv  

## Time Period

- **Period:** October 01, 2025 thru October 31, 2025
- **Number of Days:** 31 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 44,433

- **Dataset Coverage:** Partial month (0.0% of 0-day month)
- **Billing Scale Factor:** 1.000x (normalization applied for monthly comparison)

## Facility Information

- **Facility:** Foster Farms: Cherry Ave Facility
- **Location:** Fresno, CA 93706
- **Analysis Type:** Energy Field Performance Assessment
- **Technology Focus:** Unity Energy Management Solutions

---

## Executive Summary

*Brief overview of key transformer performance metrics and energy consumption.*

- **Transformer:** T10.AirChiller
- **Power Factor:** 0.890
- **Total Energy (Actual):** 539,097.98 kWh (31 days), 727.97 kW (per hour)
- **Total Energy (Monthly Equivalent):** 539,097.98 kWh
- **Total Waste (Actual):** 75,209.55 kWh (31 days), 101.56 kW (per hour)
- **Total Waste (Monthly Equivalent):** 75,209.55 kWh

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_T10.AirChiller_AN53111387-1minRES_251001-251031.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_T10.AirChiller_AN53111387-1minRES_251001-251031.md


## UNITY MANAGEMENT T10.AirChiller SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 101.56 kW/hr (actual)
- **Monthly Equivalent Waste:** 101.56 kW/hr
- **Blended Electricity Rate:** $0.3182/kWh (all-inclusive)
- **T10.AirChiller Utility Cost Offset (Monthly Equivalent):** $32.31/hour
- **Annual Offset Savings:** $283073/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 530,695 BTU/hr
- **Total Cooling kW No Longer Needed:** 108.35 kW
- **Cooling Energy Cost Avoided:** $34.48/hour
- **Annual Cooling Savings:** $302002/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 209.91 kW
- **CO2e Emissions Avoided:** 686.44 metric tons/year
- **Monthly CO2e Reduction:** 57.20 metric tons/month
- **Hourly CO2e Reduction:** 0.0784 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $26428/year

### Total T10.AirChiller Unity Savings

- **Per Hour:** $69.81
- **Per Day:** $1675.35
- **Per Month:** $50260.46
- **Per Year:** $611502

### T10.AirChiller Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 790.2 kVAR Max (Avg: 397.7 kVAR/hr ; 286,356 kVAR/mo)
- **Max Harmonic Distortion:** 156.3% Max (range: 4.3% - 156.3%)
- **Max Amperage:** 2,136A Max (range: 44A - 2136A)

---

# T10.AirChiller DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   263.60 |   251.03 |   279.58 |
| Line to Line Voltage (480v) |   456.56 |   434.79 |   484.25 |
| Current (AMPS) |  1063.72 |    43.60 |  2136.17 |
| Phase Angle (degrees) |    26.84 |    15.02 |    43.71 |
| Total Harmonic Distortion (PCT) |    32.45 |     4.29 |   156.27 |

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
| THD Phase A (%) | 10.7% | IEEE standard per-phase calculation |
| THD Phase B (%) | 11.0% | IEEE standard per-phase calculation |
| THD Phase C (%) | 10.8% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 32.4% | Field-level stress indicator |
| Max Phase THD | 11.0% | Highest THD among all three phases |
| Min Phase THD | 10.7% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 1,458.38 kW
  - **Maximum Load:** 1,651.19 kVA
  - **Percentage of Capacity (MAX):** 55.0%
- **Average Load:** 829.53 kVA
  - **Percentage of Capacity (Avg):** 27.7%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 829.53 kVA
- **Average Power Factor (PF):** 0.890

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 841.17 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 456.56 V
- Average Current (Iavg_A): 1063.72 A
- Average kW (Psum_kW): 727.97 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 11.64 kVA (1.4%)
- **Calculated PF (kW/kVA from averages):** 0.865
- **Power Factor Difference:** 0.025 (2.8%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (829.53) and measured PF (0.890) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA |   829.53 |        27.7% | 614,307.53 kVA | 2,483,936.08 TOTAL-HEAT |
| kW |   727.97 |        24.3% | 539,097.98 kWh | 225,207,043.69 Load-Heat |
| kVAR |   397.72 |        13.3% | 294,528.63 kVARh | - |
| WASTE |   101.56 |         3.4% | 75,209.55 WASTE | 31,418,632.18 Field-Heat |

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 10 |   832.85 |   730.84 |   398.23 |     0.88 |   27.8% |
| 11 |   179.31 |   165.79 |    68.24 |     0.92 |    6.0% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   493.66 |   433.74 |   233.41 |     0.88 |   16.5% |
| 01 |   867.06 |   758.99 |   417.78 |     0.88 |   28.9% |
| 02 |   907.89 |   788.91 |   448.38 |     0.87 |   30.3% |
| 03 |   909.00 |   787.27 |   453.70 |     0.87 |   30.3% |
| 04 |   915.61 |   792.08 |   458.63 |     0.87 |   30.5% |
| 05 |   939.10 |   814.80 |   466.11 |     0.87 |   31.3% |
| 06 |   992.92 |   873.66 |   471.03 |     0.88 |   33.1% |
| 07 |   982.94 |   864.39 |   467.27 |     0.88 |   32.8% |
| 08 |   973.28 |   855.57 |   463.20 |     0.88 |   32.4% |
| 09 |   965.92 |   849.66 |   458.64 |     0.88 |   32.2% |
| 10 |   964.89 |   848.90 |   457.80 |     0.88 |   32.2% |
| 11 |   963.55 |   846.72 |   459.14 |     0.88 |   32.1% |
| 12 |   956.00 |   840.67 |   454.35 |     0.88 |   31.9% |
| 13 |   950.98 |   836.95 |   450.81 |     0.88 |   31.7% |
| 14 |   958.30 |   843.27 |   454.38 |     0.88 |   31.9% |
| 15 |   957.82 |   843.61 |   452.89 |     0.88 |   31.9% |
| 16 |   949.59 |   837.92 |   446.06 |     0.88 |   31.7% |
| 17 |   949.18 |   837.60 |   445.79 |     0.88 |   31.6% |
| 18 |   910.46 |   802.44 |   429.25 |     0.88 |   30.3% |
| 19 |   785.45 |   691.38 |   371.67 |     0.88 |   26.2% |
| 20 |   582.20 |   511.89 |   275.88 |     0.88 |   19.4% |
| 21 |   367.99 |   324.49 |   171.35 |     0.88 |   12.3% |
| 22 |   296.04 |   261.61 |   136.78 |     0.88 |    9.9% |
| 23 |   350.53 |   308.79 |   163.93 |     0.88 |   11.7% |

---

# END OF REPORT

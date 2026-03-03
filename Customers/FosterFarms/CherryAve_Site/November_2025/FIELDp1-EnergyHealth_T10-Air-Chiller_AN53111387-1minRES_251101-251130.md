# BASELINE ELECTRICAL ENERGY USAGE AND COST

**Transformer Baseline :**
- **Consumption Usage:** 426,351.4 kWh (Usage per period)
- **Consumption Cost per unit:** $0.318/kWh (Cost per kWh)
- **Consumption Total Cost:** $135,657.27 (Cost per period)
- **Consumption Total Cost:** $188.67 (Cost per hour)

---

# TRANSFORMER PERFORMANCE ANALYSIS REPORT

**Transformer Name:** T10 Air Chiller  
**Generated:** 2026-02-18 15:24:51  
**Data Source:** AN53111387-V-1minRES_43260CLP_251101-251130c.csv  

## Time Period

- **Period:** November 01, 2025 thru November 30, 2025
- **Number of Days:** 30 Days
- **Data Resolution:** 1-minute
- **Total Data Points:** 43,140

- **Dataset Coverage:** Complete month (100.0% of 30-day month)
- **Billing Scale Factor:** 1.000x (no normalization needed)

## Facility Information

- **Facility:** Foster Farms
- **Location:** Cherry Ave Facility
- **Analysis Type:** Energy Field Performance Assessment
- **Technology Focus:** Unity Energy Management Solutions

---

## Executive Summary

*Brief overview of key transformer performance metrics and energy consumption.*

- **Transformer:** T10 Air Chiller
- **Power Factor:** 0.893
- **Total Energy (Actual):** 426,351.41 kWh (per period), 592.98 kW (per hour)
- **Total Waste (Actual):** 59,505.99 kWh (per period), 82.76 kW (per hour)

---

## Additional Analysis

*Detailed thermal and voltage analysis available in dedicated reports:*
- **Heat Health Analysis:** FIELDp3-HeatHealth_T10-Air-Chiller_AN53111387-1minRES_251101-251130.md
- **Voltage & Current Health:** FIELDp2-VoltAmpHealth_T10-Air-Chiller_AN53111387-1minRES_251101-251130.md


## UNITY MANAGEMENT T10 Air Chiller SAVINGS SUMMARY
*(3 Primary Elements - Energy, Cooling, CO2e)*

### Element 1: Reactive Energy Offset Savings

- **Total Electrical-Energy Waste (calc_kVA - measured_kW):** 82.76 kW/hr
- **Blended Electricity Rate:** $0.3182/kWh (all-inclusive)
- **T10 Air Chiller Utility Cost Offset:** $26.33/hour
- **Annual Offset Savings:** $230681/year

### Element 2: Cooling Elimination Savings

- **Total Heat No Longer Generated:** 416,899 BTU/hr
- **Total Cooling kW No Longer Needed:** 41.02 kW
- **Cooling Energy Cost Avoided:** $13.05/hour
- **Annual Cooling Savings:** $114346/year

### Element 3: CO2e Emissions Reduction Value

- **Total kW Waste Eliminated:** 123.79 kW
- **CO2e Emissions Avoided:** 404.80 metric tons/year
- **Monthly CO2e Reduction:** 33.73 metric tons/month
- **Hourly CO2e Reduction:** 0.0462 metric tons/hour
- **CO2e Value Rate:** $38/metric ton
- **Annual CO2e Value:** $15585/year

### Total T10 Air Chiller Unity Savings

- **Per Hour:** $41.17
- **Per Day:** $987.98
- **Per Month:** $29639.32
- **Per Year:** $360612

### T10 Air Chiller Savings Breakdown


### Unity System (MPTS) Installation Considerations

- **Max Reactive Energy:** 773.6 kVAR Max (Avg: 324.0 kVAR/hr ; 233,309 kVAR/mo)
- **Max Harmonic Distortion:** 150.8% Max (range: 0.0% - 150.8%)
- **Max Amperage:** 2,009A Max (range: 69A - 2009A)

---

# T10 Air Chiller DETAILED PERFORMANCE ANALYSIS

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
| Line to Neutral Voltage (277v) |   266.00 |   253.66 |   280.45 |
| Line to Line Voltage (480v) |   460.73 |   439.36 |   485.76 |
| Current (AMPS) |   861.49 |    69.49 |  2009.03 |
| Phase Angle (degrees) |    26.46 |    15.47 |    36.82 |
| Total Harmonic Distortion (PCT) |    39.57 |     0.00 |   150.82 |

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
| THD Phase A (%) | 13.1% | IEEE standard per-phase calculation |
| THD Phase B (%) | 13.3% | IEEE standard per-phase calculation |
| THD Phase C (%) | 13.2% | IEEE standard per-phase calculation |
| Unity THD Composite (%) | 39.6% | Field-level stress indicator |
| Max Phase THD | 13.3% | Highest THD among all three phases |
| Min Phase THD | 13.1% | Lowest THD among all three phases |

### Engineering Commentary

This composite score is useful when assessing transformer health, load imbalance, or predicting heating and harmonic clustering (G1–G8 groups). It's used in our eBehavior overlays and directly informs Unity's Voltage Health Index (VHI).

If IEEE compliance is required, individual THD values remain visible and can be cross-checked per phase.

⚠️ **Note on THD Composite**: Unity's THD Composite is not a scalar addition per IEEE. It is a field-behavior indicator that helps us track total harmonic impact across all three phases — a core component of transformer-level heat modeling.

## Capacity Utilization

- **Maximum UtilityDemand:** 1,367.69 kW
  - **Maximum Load:** 1,549.39 kVA
  - **Percentage of Capacity (MAX):** 62.0%
- **Average Load:** 675.74 kVA
  - **Percentage of Capacity (Avg):** 27.0%

## kVA and Power Factor Analysis (Measured vs Calculated)

### Measured Values (PRIMARY - Used for All Analysis)

- **Average kVA (Ssum_kVA):** 675.74 kVA
- **Average Power Factor (PF):** 0.893

**Source:** Direct meter measurements (instantaneous values averaged over time)

### Calculated Values (VERIFICATION ONLY)

- **Calculated kVA (V×I×√3/1000):** 687.47 kVA

**Calculation Inputs:**
- Average Voltage (VIavg_V): 460.73 V
- Average Current (Iavg_A): 861.49 A
- Average kW (Psum_kW): 592.98 kW

### Differences (Measured vs Calculated)
- **kVA Difference:** 11.73 kVA (1.7%)
- **Calculated PF (kW/kVA from averages):** 0.863
- **Power Factor Difference:** 0.031 (3.4%)

### Why Measured Values Are More Accurate

When voltage and current vary over time (which they always do in real systems):
- **Average(V × I) ≠ Average(V) × Average(I)** due to the non-linear multiplication
- **Time-weighted PF ≠ kW/kVA from averages** due to load variation effects

The meter's instantaneous measurements capture these variations correctly, while
calculations from averaged values systematically underestimate reactive effects.

**Analysis Method:** All heat calculations, thermal burden, and cost analysis use
the measured kVA (675.74) and measured PF (0.893) values.
Calculated values are shown above for verification and engineering transparency.

## Overall Power Metrics (FPC)

| Metric | Average | % of Capacity | Total Energy | HEAT (BTU/hr) |
| ------ | ------- | ------------- | ------------------- | ------------- |
| kVA |   675.74 |        27.0% | 485,857.40 kVA | 2,023,326.22 TOTAL-HEAT |
| kW |   592.98 |        23.7% | 426,351.41 kWh | 178,174,957.82 Load-Heat |
| kVAR |   324.04 |        13.0% | 232,984.74 kVARh | - |
| WASTE |    82.76 |         3.3% | 59,505.99 WASTE | 24,867,930.67 Field-Heat |

## Measured Monthly Averages

| Month | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ----- | ------- | ------ | -------- | ------ | ---------- |
| 11 |   675.74 |   592.98 |   322.83 |     0.88 |   27.0% |

## Measured Hourly Averages

| Hour | Avg kVA | Avg kW | Avg kVAR | Avg PF | % Capacity |
| ---- | ------- | ------ | -------- | ------ | ---------- |
| 00 |   753.99 |   653.59 |   375.00 |     0.87 |   30.2% |
| 01 |   782.33 |   679.91 |   385.90 |     0.87 |   31.3% |
| 02 |   805.71 |   708.95 |   381.88 |     0.88 |   32.2% |
| 03 |   806.49 |   709.25 |   382.87 |     0.88 |   32.3% |
| 04 |   809.05 |   712.05 |   383.07 |     0.88 |   32.4% |
| 05 |   805.33 |   708.98 |   380.92 |     0.88 |   32.2% |
| 06 |   802.09 |   705.58 |   380.51 |     0.88 |   32.1% |
| 07 |   793.97 |   698.78 |   376.11 |     0.88 |   31.8% |
| 08 |   794.16 |   698.67 |   376.73 |     0.88 |   31.8% |
| 09 |   794.60 |   698.97 |   377.19 |     0.88 |   31.8% |
| 10 |   791.66 |   696.54 |   375.57 |     0.88 |   31.7% |
| 11 |   785.27 |   690.56 |   373.25 |     0.88 |   31.4% |
| 12 |   783.62 |   688.98 |   372.74 |     0.88 |   31.3% |
| 13 |   766.65 |   673.46 |   365.66 |     0.88 |   30.7% |
| 14 |   666.90 |   587.28 |   315.22 |     0.88 |   26.7% |
| 15 |   548.18 |   483.03 |   258.02 |     0.88 |   21.9% |
| 16 |   331.69 |   293.83 |   152.09 |     0.89 |   13.3% |
| 17 |   235.10 |   209.57 |   104.46 |     0.89 |    9.4% |
| 18 |   220.57 |   197.44 |    96.92 |     0.90 |    8.8% |
| 19 |   310.02 |   273.40 |   144.42 |     0.88 |   12.4% |
| 20 |   479.35 |   419.36 |   229.88 |     0.87 |   19.2% |
| 21 |   779.85 |   681.66 |   377.35 |     0.87 |   31.2% |
| 22 |   793.83 |   689.75 |   391.98 |     0.87 |   31.8% |
| 23 |   780.93 |   674.77 |   392.34 |     0.86 |   31.2% |

---

# END OF REPORT

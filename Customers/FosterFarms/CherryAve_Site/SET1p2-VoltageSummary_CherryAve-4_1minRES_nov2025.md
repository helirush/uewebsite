# SET PAGE 2 - VOLTAGE SUMMARY FOR ENERGY FIELDS

**Generated:** 2026-01-27 14:35:10  
**Facility:** Foster Farms: Cherry Ave Facility  
**Set Report:** CherryAve-4_1minRES_nov2025  
**Period:** 2025-11-01T00:00:00 to 2025-11-30T23:59:00  
**Total Transformers in Set:** 4  
**Average Site VHI:** 92.5  

---

## VOLTAGE HEALTH DASHBOARD

This dashboard summarizes voltage behavior across all transformers in the set and links to detailed reports.

| Transformer | Capacity | Primary Voltage Group | Drop Count | Days | % Nominal | Mean V (Δ%) | Worst ΔV | Stall Amps | Est. HP | Event Tag | Cluster Time | Recovery Time | Overlay Link | VHI Score | Status | Report |
| ----------- | ---------| --------------------- | ---------- | ---- | --------- | ----------- | -------- | ---------- | ------- | --------- | ------------ | ------------- | ------------ | --------- | ------ | ------ |
| T10.AirChiller | 3,000 | 439.4–460.8V | 32892 | 26 | 53.5% | 459.5V (-4.3%) | 483.2 | - | - | - | 01:00 | 62.3min | - | 77 | ⚠️ | `FIELDp2-VoltageHealth_T10.AirChiller_unknown.md` |
| T12.Main | 2,500 | 444.8–460.8V | 41431 | 19 | 87.5% | 467.4V (-2.6%) | 491.8 | - | - | - | 10:00 | 5.1min | - | 94 | ✅ | `FIELDp2-VoltageHealth_T12.Main_unknown.md` |
| T15.Fillet | 2,500 | 463.5–477.3V | 41746 | 17 | 99.6% | 479.7V (-0.1%) | 501.8 | - | - | - | 01:00 | 2.8min | - | 100 | ✅ | `FIELDp2-VoltageHealth_T15.Fillet_unknown.md` |
| T16.Compressor | 2,500 | 456.6–476.0V | 37696 | 2 | 99.7% | 476.2V (-0.8%) | 502.1 | - | - | - | 01:00 | 30.5min | - | 100 | ✅ | `FIELDp2-VoltageHealth_T16.Compressor_unknown.md` |

### Notes
- Status icons: 🔴 Critical (VHI < 50), ⚠️ Warning (50 ≤ VHI < 80), ✅ Stable (VHI ≥ 80)
- VHI = 100 − Weighted Drop Severity − (%Time Outside Nominal × 0.5)
- Primary V Group is based on highest observed activity; if time-share data is unavailable, drop activity is used as a proxy

---

## DETAILED ACCESS 

Each transformer has its own detailed Page 2 - Voltage Behavior report with comprehensive analysis.


---

## PATTERN INSIGHTS PER TRANSFORMER

### T10.AirChiller (Date range unknown)
- Cluster detection: No strong clustering by time-of-day detected
- Recovery time average: 62.3 minutes to return within ±5% of nominal

### T12.Main (Date range unknown)
- Cluster detection: No strong clustering by time-of-day detected
- Recovery time average: 5.1 minutes to return within ±5% of nominal

### T15.Fillet (Date range unknown)
- Cluster detection: Drops cluster around 01:00 (79% of drops)
- Recovery time average: 2.8 minutes to return within ±5% of nominal

### T16.Compressor (Date range unknown)
- Cluster detection: Drops cluster around 01:00 (99% of drops)
- Recovery time average: 30.5 minutes to return within ±5% of nominal

---

**END OF SET PAGE 2 - VOLTAGE SUMMARY**

*Generated for Foster Farms: Cherry Ave Facility - CherryAve-4_1minRES_nov2025*  
*Analysis completed: 2026-01-27 14:35:13*


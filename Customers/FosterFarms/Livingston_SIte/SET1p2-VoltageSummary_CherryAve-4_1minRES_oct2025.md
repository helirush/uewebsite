# SET PAGE 2 - VOLTAGE SUMMARY FOR ENERGY FIELDS

**Generated:** 2026-01-06 13:49:18  
**Facility:** Foster Farms: Cherry Ave Facility  
**Set Report:** CherryAve-4_1minRES_oct2025  
**Period:** 2025-10-01 to 2025-11-01  
**Total Transformers in Set:** 4  
**Average Site VHI:** 89.3  

---

## VOLTAGE HEALTH DASHBOARD

This dashboard summarizes voltage behavior across all transformers in the set and links to detailed reports.

| Transformer | Capacity | Primary Voltage Group | Drop Count | Days | % Nominal | Mean V (Δ%) | Worst ΔV | Stall Amps | Est. HP | Event Tag | Cluster Time | Recovery Time | Overlay Link | VHI Score | Status | Report |
| ----------- | ---------| --------------------- | ---------- | ---- | --------- | ----------- | -------- | ---------- | ------- | --------- | ------------ | ------------- | ------------ | --------- | ------ | ------ |
| T10.AirChiller | 3,000 | 434.8–460.8V | 36535 | 28 | 38.8% | 454.4V (-5.3%) | 474.3 | - | - | - | 04:00 | 102.8min | - | 69 | ⚠️ | `FIELDp2-VoltageHealth_T10.AirChiller_251001-251101.md` |
| T12.Main | 2,500 | 444.8–460.8V | 55451 | 23 | 76.6% | 462.8V (-3.6%) | 488.5 | - | - | - | 12:00 | 9.5min | - | 88 | ✅ | `FIELDp2-VoltageHealth_T12.Main_251001-251101.md` |
| T15.Fillet | 2,500 | 458.4–460.8V | 107 | 22 | 99.5% | 475.5V (-0.9%) | 490.3 | - | - | - | 09:00 | 6.9min | - | 100 | ✅ | `FIELDp2-VoltageHealth_T15.Fillet_251001-251101.md` |
| T16.Compressor | 2,500 | 451.9–460.8V | 9385 | 8 | 99.4% | 471.6V (-1.8%) | 499.2 | - | - | - | 09:00 | 9.2min | - | 100 | ✅ | `FIELDp2-VoltageHealth_T16.Compressor_251001-251101.md` |

### Notes
- Status icons: 🔴 Critical (VHI < 50), ⚠️ Warning (50 ≤ VHI < 80), ✅ Stable (VHI ≥ 80)
- VHI = 100 − Weighted Drop Severity − (%Time Outside Nominal × 0.5)
- Primary V Group is based on highest observed activity; if time-share data is unavailable, drop activity is used as a proxy

---

## DETAILED ACCESS 

Each transformer has its own detailed Page 2 - Voltage Behavior report with comprehensive analysis.


---

## PATTERN INSIGHTS PER TRANSFORMER

### T10.AirChiller (Oct 01 - Nov 01, 2025)
- Cluster detection: No strong clustering by time-of-day detected
- Recovery time average: 102.8 minutes to return within ±5% of nominal

### T12.Main (Oct 01 - Nov 01, 2025)
- Cluster detection: No strong clustering by time-of-day detected
- Recovery time average: 9.5 minutes to return within ±5% of nominal

### T15.Fillet (Oct 01 - Nov 01, 2025)
- Cluster detection: Drops cluster around 09:00 (30% of drops)
- Recovery time average: 6.9 minutes to return within ±5% of nominal

### T16.Compressor (Oct 01 - Nov 01, 2025)
- Cluster detection: No strong clustering by time-of-day detected
- Recovery time average: 9.2 minutes to return within ±5% of nominal

---

**END OF SET PAGE 2 - VOLTAGE SUMMARY**

*Generated for Foster Farms: Cherry Ave Facility - CherryAve-4_1minRES_oct2025*  
*Analysis completed: 2026-01-06 13:49:22*


# UNITY MPTS SOLUTION ROI ANALYSIS

*Maximum Power Transfer Solution: Investment Analysis & Return on Investment*

**Facility:** Foster Farms: Cherry Ave Facility  
**Generated:** 2026-01-06  
**Analysis Period:** October 01, 2025 thru October 31, 2025  
**Solution Technology:** Unity Energy H490 MPTS Units

---

## 📊 Executive Summary

<details>
<summary><strong>Site-Level Investment & Returns</strong></summary>

**Total MPTS Investment:** $1,860,000  
**Total eStream Monitoring Investment:** $60,000  
**Combined Investment:** $1,920,000

**Annual Energy Waste (Current State):** $2,719,061  
**Simple Payback Period:** 8.2 months (average across 4 transformers)

**20-Year Net Profit:** $52,461,214  
**Internal Rate of Return (IRR):** ~147% annually

**Facility Details:**
- Total Transformers Analyzed: 4
- Combined Transformer Capacity: 10,500 kVA
- Total H490 Units Required: 9 units
- Total Monitoring Points: 4 (one per transformer)

</details>

---

## 🔬 MPTS Sizing Methodology

<details>
<summary><strong>Three-Step Validation Process</strong></summary>

Unity's H490 MPTS units are precision-sized using a rigorous 3-step validation checklist to ensure safe, effective operation:

### Step 1: Harmonic Safety Check
- **Requirement:** Total Harmonic Distortion (THD) must be < 60%
- **Purpose:** Ensures power quality is within safe operating parameters
- **Result:** If THD ≥ 60%, address power quality issues before MPTS deployment

### Step 2: kVAR Capacity Sizing
- **Formula:** Peak kVAR ÷ 400 kVAR = Number of H490 units (round up)
- **Source:** tMAX_REACTIVE from M (kVAR) analysis charts
- **Purpose:** Ensures sufficient reactive power correction capacity

### Step 3: Amperage Safety Validation
- **Formula:** (Units × 800A × 1.5 Safety Factor) must exceed tMAX_AMPERAGE
- **Purpose:** Confirms current-handling capacity with 50% safety margin
- **Result:** If margin insufficient, add additional H490 units

**H490 Unit Specifications:**
- Reactive Power Capacity: 400 kVAR per unit
- Current Capacity: 800A per unit
- Investment Cost: $200,000 per unit
- Expected Lifespan: 20+ years

</details>

---

## 🏭 Transformer-Level Analysis

### T10: AirChiller (3,000 kVA)

<details>
<summary><strong>MPTS Sizing & Validation</strong></summary>

**Transformer Specifications:**
- Capacity: 3,000 kVA
- Analysis Source: `t10m886_oct25.png`

**Step 1 - Harmonic Check:**
- THD1: 29.0%
- THD2: 36.5%
- THD3: 29.4%
- **Status:** ✅ PASS (all < 60%)

**Step 2 - kVAR Sizing:**
- Peak Reactive Power (tMAX_REACTIVE): 710.1 kVAR
- Required Units: 710.1 ÷ 400 = 1.78 → **2 H490 units**
- Total kVAR Capacity: 2 × 400 = 800 kVAR
- Coverage Margin: (800 - 710.1) ÷ 710.1 = **12.7%**

**Step 3 - Amperage Validation:**
- Peak Current (tMAX_AMPERAGE): 1241.8A
- MPTS Current Capacity: 2 units × 800A × 1.5 = 2,400A
- Amperage Margin: 2,400 - 1,241.8 = **1,158.2A (93.2%)**
- **Status:** ✅ PASS

</details>

<details>
<summary><strong>Financial Analysis</strong></summary>

**Investment:**
- H490 Units: 2 × $200,000 = $400,000
- eStream Monitoring: 1 × $15,000 = $15,000
- **Total Investment:** $415,000

**Annual Energy Waste (Current State):**
- Reactive Energy Waste: $515,256/year
- Cooling Load Waste: $117,893/year
- CO2e Emissions Waste: $11,975/year
- **Total Annual Waste:** $645,124/year

**Return on Investment:**
- Monthly Savings: $53,760
- **Payback Period:** 7.7 months
- 20-Year Savings: $12,902,489
- **20-Year Net Profit:** $12,487,489

</details>

---

### T12: Main (2,500 kVA)

<details>
<summary><strong>MPTS Sizing & Validation</strong></summary>

**Transformer Specifications:**
- Capacity: 2,500 kVA
- Analysis Source: `t12m825_oct25.png`

**Step 1 - Harmonic Check:**
- THD1: 20.4%
- THD2: 31.0%
- THD3: 30.6%
- **Status:** ✅ PASS (all < 60%)

**Step 2 - kVAR Sizing:**
- Peak Reactive Power (tMAX_REACTIVE): 900.6 kVAR
- Required Units: 900.6 ÷ 400 = 2.25 → **3 H490 units**
- Total kVAR Capacity: 3 × 400 = 1,200 kVAR
- Coverage Margin: (1,200 - 900.6) ÷ 900.6 = **33.2%**

**Step 3 - Amperage Validation:**
- Peak Current (tMAX_AMPERAGE): 2260.1A
- MPTS Current Capacity: 3 units × 800A × 1.5 = 3,600A
- Amperage Margin: 3,600 - 2,260.1 = **1,339.9A (59.3%)**
- **Status:** ✅ PASS

</details>

<details>
<summary><strong>Financial Analysis</strong></summary>

**Investment:**
- H490 Units: 3 × $200,000 = $600,000
- eStream Monitoring: 1 × $15,000 = $15,000
- **Total Investment:** $615,000

**Annual Energy Waste (Current State):**
- Reactive Energy Waste: $705,838/year
- Cooling Load Waste: $143,542/year
- CO2e Emissions Waste: $31,838/year
- **Total Annual Waste:** $881,218/year

**Return on Investment:**
- Monthly Savings: $73,435
- **Payback Period:** 8.4 months
- 20-Year Savings: $17,624,365
- **20-Year Net Profit:** $17,009,365

</details>

---

### T15: Fillet (2,500 kVA)

<details>
<summary><strong>MPTS Sizing & Validation</strong></summary>

**Transformer Specifications:**
- Capacity: 2,500 kVA
- Analysis Source: `t15m883_oct25.png`

**Step 1 - Harmonic Check:**
- THD1: 9.7%
- THD2: 38.4%
- THD3: 37.1%
- **Status:** ✅ PASS (all < 60%)

**Step 2 - kVAR Sizing:**
- Peak Reactive Power (tMAX_REACTIVE): 767.2 kVAR
- Required Units: 767.2 ÷ 400 = 1.92 → **2 H490 units**
- Total kVAR Capacity: 2 × 400 = 800 kVAR
- Coverage Margin: (800 - 767.2) ÷ 767.2 = **4.3%**

**Step 3 - Amperage Validation:**
- Peak Current (tMAX_AMPERAGE): 1861.3A
- MPTS Current Capacity: 2 units × 800A × 1.5 = 2,400A
- Amperage Margin: 2,400 - 1,861.3 = **538.7A (28.9%)**
- **Status:** ✅ PASS

</details>

<details>
<summary><strong>Financial Analysis</strong></summary>

**Investment:**
- H490 Units: 2 × $200,000 = $400,000
- eStream Monitoring: 1 × $15,000 = $15,000
- **Total Investment:** $415,000

**Annual Energy Waste (Current State):**
- Reactive Energy Waste: $574,080/year
- Cooling Load Waste: $147,283/year
- CO2e Emissions Waste: $20,472/year
- **Total Annual Waste:** $741,835/year

**Return on Investment:**
- Monthly Savings: $61,820
- **Payback Period:** 6.7 months
- 20-Year Savings: $14,836,700
- **20-Year Net Profit:** $14,421,700

</details>

---

### T16: Compressor (2,500 kVA)

<details>
<summary><strong>MPTS Sizing & Validation</strong></summary>

**Transformer Specifications:**
- Capacity: 2,500 kVA
- Analysis Source: `t16m882_oct25.png`

**Step 1 - Harmonic Check:**
- THD1: 35.1%
- THD2: 30.8%
- THD3: 33.3%
- **Status:** ✅ PASS (all < 60%)

**Step 2 - kVAR Sizing:**
- Peak Reactive Power (tMAX_REACTIVE): 660.0 kVAR
- Required Units: 660.0 ÷ 400 = 1.65 → **2 H490 units**
- Total kVAR Capacity: 2 × 400 = 800 kVAR
- Coverage Margin: (800 - 660.0) ÷ 660.0 = **21.2%**

**Step 3 - Amperage Validation:**
- Peak Current (tMAX_AMPERAGE): 1929.9A
- MPTS Current Capacity: 2 units × 800A × 1.5 = 2,400A
- Amperage Margin: 2,400 - 1,929.9 = **470.1A (24.4%)**
- **Status:** ✅ PASS

</details>

<details>
<summary><strong>Financial Analysis</strong></summary>

**Investment:**
- H490 Units: 2 × $200,000 = $400,000
- eStream Monitoring: 1 × $15,000 = $15,000
- **Total Investment:** $415,000

**Annual Energy Waste (Current State):**
- Reactive Energy Waste: $370,788/year
- Cooling Load Waste: $41,459/year
- CO2e Emissions Waste: $39,631/year
- **Total Annual Waste:** $451,878/year

**Return on Investment:**
- Monthly Savings: $37,657
- **Payback Period:** 11.0 months
- 20-Year Savings: $9,037,560
- **20-Year Net Profit:** $8,622,560

</details>

---

## 💰 Site-Level Financial Summary

<details>
<summary><strong>Consolidated Investment & Returns</strong></summary>

### Total Investment Breakdown

| Component | Quantity | Unit Cost | Total Cost |
|-----------|----------|-----------|------------|
| H490 MPTS Units | 9 | $200,000 | $1,800,000 |
| eStream Monitoring | 4 | $15,000 | $60,000 |
| **TOTAL INVESTMENT** | - | - | **$1,860,000** |

### Annual Waste by Category (Current State)

| Waste Category | T10 | T12 | T15 | T16 | **Total** |
|----------------|-----|-----|-----|-----|-----------|
| Reactive Energy | $515K | $706K | $574K | $371K | **$2,166K** |
| Cooling Load | $118K | $144K | $147K | $41K | **$450K** |
| CO2e Emissions | $12K | $32K | $20K | $40K | **$104K** |
| **Subtotal** | **$645K** | **$881K** | **$742K** | **$452K** | **$2,719K** |

### Payback Analysis by Transformer

| Transformer | Investment | Annual Waste | Monthly Savings | Payback (months) |
|-------------|------------|--------------|-----------------|------------------|
| T10.AirChiller | $415,000 | $645,124 | $53,760 | 7.7 |
| T12.Main | $615,000 | $881,218 | $73,435 | 8.4 |
| T15.Fillet | $415,000 | $741,835 | $61,820 | 6.7 |
| T16.Compressor | $415,000 | $451,878 | $37,657 | 11.0 |
| **TOTAL** | **$1,860,000** | **$2,720,055** | **$226,671** | **8.2 avg** |

### 20-Year Financial Projection

**Cumulative Savings:** $54,401,092  
**Total Investment:** $1,860,000  
**Net Profit (20 years):** $52,541,092

**Year-by-Year Savings:**
- Year 1: $2,720,055 (payback complete in month 8.2)
- Years 2-20: $2,720,055/year × 19 = $51,681,037
- **Total 20-Year Savings:** $54,401,092

</details>

<details>
<summary><strong>Environmental Impact</strong></summary>

### CO2e Emissions Reduction

**Annual CO2e Waste (Current State):** 2,698 metric tons  
**20-Year CO2e Reduction:** 53,960 metric tons

**Equivalent Environmental Impact:**
- Trees planted and grown for 10 years: ~889,000 trees
- Passenger vehicles removed from road for 1 year: ~11,728 vehicles
- Homes' energy use for 1 year: ~6,736 homes

**CO2e Value at $38.50/metric ton:**
- Annual savings: $103,873
- 20-year value: $2,077,460

</details>

---

## 📋 Implementation Recommendations

<details>
<summary><strong>Deployment Priority & Timeline</strong></summary>

### Recommended Deployment Sequence

**Priority 1: T15.Fillet (6.7 month payback)**
- 2 H490 units
- Fastest ROI
- Highest thermal cycling risk (equipment longevity)

**Priority 2: T10.AirChiller (7.7 month payback)**
- 2 H490 units
- Second-fastest ROI
- Critical cooling infrastructure

**Priority 3: T12.Main (8.4 month payback)**
- 3 H490 units
- Largest single investment
- Highest capacity utilization (48.5%)

**Priority 4: T16.Compressor (11.0 month payback)**
- 2 H490 units
- Longest payback but still <1 year
- Best current power factor (0.886)

### Phased Implementation Option

**Phase 1 (Months 1-3):** T15 + T10 = 4 units, $830K investment, $1,386K annual savings  
**Phase 2 (Months 4-6):** T12 + T16 = 5 units, $1,030K investment, $1,333K annual savings

</details>

---

## 🔍 Technical Validation Summary

<details>
<summary><strong>All Transformers Pass 3-Step Validation</strong></summary>

| Transformer | THD Pass | kVAR Units | kVAR Margin | Amperage Margin | Overall |
|-------------|----------|------------|-------------|-----------------|---------|
| T10.AirChiller | ✅ < 60% | 2 units | 12.7% | 93.2% | ✅ PASS |
| T12.Main | ✅ < 60% | 3 units | 33.2% | 59.3% | ✅ PASS |
| T15.Fillet | ✅ < 60% | 2 units | 4.3% | 28.9% | ✅ PASS |
| T16.Compressor | ✅ < 60% | 2 units | 21.2% | 24.4% | ✅ PASS |

**All transformers meet Unity's safety and performance criteria for H490 MPTS deployment.**

</details>

---

## 📞 Next Steps

1. **Review & Approval:** Present analysis to Foster Farms facility management
2. **Site Survey:** Unity technical team conducts pre-installation assessment
3. **Deployment Planning:** Finalize phased or simultaneous deployment schedule
4. **Installation:** Unity H490 units installed with eStream monitoring integration
5. **Commissioning:** System optimization and baseline validation
6. **Ongoing Monitoring:** Continuous eStream data validation and reporting

---

# END OF ROI ANALYSIS REPORT

*Generated by eStream eBehavior Analysis Platform*  
*Unity Energy Maximum Power Transfer Solution*

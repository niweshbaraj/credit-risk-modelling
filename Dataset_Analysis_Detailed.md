# Credit Risk Modeling Dataset Analysis

## Overview
The credit risk modeling project uses a comprehensive dataset split across multiple Excel files, each serving a specific purpose in the machine learning pipeline. The data represents real-world credit bureau information combined with application data for loan risk assessment.

---

## Dataset Files Breakdown

### 1. **case_study1.xlsx** - Credit Bureau Trade Line Data
**Purpose**: Contains credit bureau information focusing on trade line (account) history

**Key Statistics**:
- **Size**: 51,336 records × 26 features
- **Data Type**: Primarily numerical (int64/float64)
- **Focus**: Account management and payment history

**Feature Categories**:

#### **Account Portfolio Metrics**
- `Total_TL`: Total trade lines/accounts in credit bureau (5-30+ accounts typical)
- `Tot_Closed_TL`: Total closed accounts (indicates account closure behavior)  
- `Tot_Active_TL`: Currently active accounts (1-15 typical for active borrowers)

#### **Recent Activity (6-Month Window)**
- `Total_TL_opened_L6M`: New accounts opened in last 6 months (0-3 typical)
- `Tot_TL_closed_L6M`: Accounts closed in last 6 months
- `pct_tl_open_L6M`: Percentage of accounts opened recently (0-50%)
- `pct_tl_closed_L6M`: Percentage of accounts closed recently

#### **Extended Activity (12-Month Window)**  
- `Total_TL_opened_L12M`: New accounts in last 12 months
- `Tot_TL_closed_L12M`: Accounts closed in last 12 months
- `pct_tl_open_L12M`: Percentage opened in 12 months
- `pct_tl_closed_L12M`: Percentage closed in 12 months

#### **Payment Behavior**
- `Tot_Missed_Pmnt`: Total missed payments (0-50+ range, 0 is ideal)

#### **Account Type Distribution**
- `Auto_TL`: Automobile loan accounts (0-5 typical)
- `CC_TL`: Credit card accounts (1-10 typical) 
- `Consumer_TL`: Consumer goods financing
- `Gold_TL`: Gold loan accounts (common in Indian market)
- `Home_TL`: Housing/mortgage loans (0-2 typical)
- `PL_TL`: Personal loan accounts (0-5 typical)
- `Secured_TL`: Secured loan accounts (backed by collateral)
- `Unsecured_TL`: Unsecured loan accounts (higher risk)
- `Other_TL`: Miscellaneous account types

#### **Account Age Metrics**
- `Age_Oldest_TL`: Age of oldest account in months (2-400+ months)
- `Age_Newest_TL`: Age of newest account in months (2-200+ months)

**Business Significance**: This file captures the **credit history foundation** - how customers have managed their existing financial obligations over time.

---

### 2. **case_study2.xlsx** - Comprehensive Credit Profile + Target Variable
**Purpose**: Contains detailed credit behavior, demographics, and the target variable for model training

**Key Statistics**:
- **Size**: 51,336 records × 62 features  
- **Data Type**: Mixed (numerical, categorical, object)
- **Focus**: Complete applicant profile with risk classification

**Feature Categories**:

#### **Advanced Delinquency Metrics**
- `time_since_recent_payment`: Days since last payment (0-2000+ days)
- `time_since_first_deliquency`: Days since first missed payment
- `time_since_recent_deliquency`: Days since most recent missed payment
- `num_times_delinquent`: Total delinquency incidents (0-50+)
- `max_delinquency_level`: Highest delinquency severity reached
- `num_deliq_6mts`, `num_deliq_12mts`: Recent delinquency frequency

#### **Payment Quality Classification**
- `num_std`: Standard payments (full, on-time payments)
- `num_sub`: Sub-standard payments (partial payments)
- `num_dbt`: Doubtful payments (high risk of default)
- `num_lss`: Loss accounts (written off as uncollectable)
- `num_times_30p_dpd`: Times 30+ days past due
- `num_times_60p_dpd`: Times 60+ days past due

#### **Credit Inquiry Behavior**
- `tot_enq`: Total credit inquiries (indicates credit-seeking behavior)
- `CC_enq`, `PL_enq`: Credit card and personal loan specific inquiries
- `CC_enq_L6m`, `PL_enq_L6m`: Recent inquiry activity (0-10 typical)
- `time_since_recent_enq`: Days since last credit inquiry

#### **Demographic Information**
- `AGE`: Applicant age (18-80 years typical)
- `GENDER`: Male/Female classification
- `MARITALSTATUS`: Single/Married status
- `EDUCATION`: Education level (SSC/12TH/GRADUATE/POST-GRADUATE)
- `NETMONTHLYINCOME`: Monthly income in currency units
- `Time_With_Curr_Empr`: Employment tenure with current employer

#### **Credit Utilization & Exposure**
- `CC_utilization`: Credit card utilization ratio (0-100%+)
- `PL_utilization`: Personal loan utilization
- `pct_currentBal_all_TL`: Current balance as % of total credit
- `max_unsec_exposure_inPct`: Maximum unsecured exposure percentage

#### **Product Flags & Preferences**  
- `CC_Flag`, `PL_Flag`, `HL_Flag`, `GL_Flag`: Binary flags for product holdings
- `last_prod_enq2`: Most recent product inquiry type
- `first_prod_enq2`: First product inquiry type

#### **Credit Score & Target**
- `Credit_Score`: Applicant's credit bureau score (300-850 scale)
- **`Approved_Flag`**: **TARGET VARIABLE** - Risk classification (P1/P2/P3/P4)

**Target Distribution**:
- **P1 (Lowest Risk)**: 5,803 applicants (11.3%) - Prime customers
- **P2 (Low Risk)**: 32,199 applicants (62.7%) - Standard approval  
- **P3 (Medium Risk)**: 7,452 applicants (14.5%) - Enhanced monitoring
- **P4 (Highest Risk)**: 5,882 applicants (11.5%) - Likely rejection/high-interest

**Business Significance**: This file provides the **complete customer profile** including demographics, behavioral patterns, and the actual business decision (risk tier).

---

### 3. **Features_Target_Description.xlsx** - Data Dictionary
**Purpose**: Comprehensive documentation of all variables

**Key Statistics**:
- **Size**: 88 rows × 3 columns
- **Content**: Variable definitions and business context

**Structure**:
- **Column 1**: Source table identification
- **Column 2**: Variable name (matches dataset columns)
- **Column 3**: Business description and interpretation

**Significance**: Essential for **feature understanding** and **model interpretability** - ensures business stakeholders understand model inputs.

---

### 4. **Unseen_Dataset.xlsx** - Production Test Data  
**Purpose**: New applicant data for model prediction (no target variable)

**Key Statistics**:
- **Size**: 100 records × 42 features
- **Data Type**: Mixed (subset of training features)
- **Purpose**: Model validation and production simulation

**Missing Elements**:
- No `Approved_Flag` target variable (this is what the model predicts)
- Reduced feature set (42 vs 62+26 from training)
- Represents real-world application scenario

**Business Significance**: Simulates **production environment** where new applications need risk assessment without knowing the actual outcome.

---

## Key Relationships Between Files

### **Data Integration Strategy**
1. **case_study1.xlsx** + **case_study2.xlsx** = Complete training dataset
2. Both files share `PROSPECTID` as the common key for merging
3. Combined dataset: 51,336 records × 87 features (26+62-1 for shared ID)
4. **Unseen_Dataset.xlsx** used for final model validation

### **Feature Overlap Analysis**
- **Shared Features**: Some account-level metrics appear in both files
- **Complementary Data**: case_study1 focuses on account history, case_study2 adds behavior + demographics
- **Feature Engineering Opportunity**: Can create derived features from combinations

### **Temporal Consistency**
- All datasets represent same time period
- Consistent customer base (same `PROSPECTID` range)
- Real-world data quality issues present (missing values, outliers)

---

## Business Context & Significance

### **Industry Relevance**
This dataset structure mirrors real-world credit bureau and application processing:

1. **Credit Bureau Data** (case_study1): External data from credit reporting agencies
2. **Application Data** (case_study2): Internal bank/lender collected information
3. **Production Scoring**: New applications requiring risk assessment

### **Risk Tier System Explanation**
The four-tier classification system aligns with banking industry standards:

- **P1 (11.3%)**: Premium customers - lowest rates, highest approval
- **P2 (62.7%)**: Standard customers - regular rates and terms  
- **P3 (14.5%)**: Subprime customers - higher rates, additional conditions
- **P4 (11.5%)**: High-risk customers - likely rejection or very high rates

### **Regulatory Compliance**
- Features support fair lending practices (demographic data for bias testing)
- Credit score inclusion enables model benchmarking
- Detailed payment history supports risk-based pricing justification

---

## Data Quality Considerations

### **Strengths**
- **Large sample size**: 51,336 records provides statistical power
- **Rich feature set**: 87+ features enable comprehensive modeling
- **Real-world data**: Includes actual credit bureau information
- **Balanced target**: Reasonable distribution across risk tiers
- **Production simulation**: Unseen dataset tests real-world applicability

### **Challenges**  
- **Missing values**: Coded as -99999 in some fields
- **Feature complexity**: High dimensionality requires careful selection
- **Class imbalance**: P2 dominates (62.7%) vs other categories
- **Data encoding**: Mixed categorical/numerical formats need preprocessing
- **Temporal factors**: Point-in-time snapshot may miss seasonal patterns

---

## Machine Learning Implications

### **Modeling Opportunities**
1. **Classification Problem**: Multi-class prediction (P1/P2/P3/P4)
2. **Feature Engineering**: Rich source for derived variables
3. **Ensemble Methods**: Multiple data sources enable sophisticated modeling
4. **Interpretability**: Business-meaningful features support explainable AI

### **Technical Considerations**
- **Preprocessing Pipeline**: Handle missing values, encoding, scaling
- **Feature Selection**: Dimensionality reduction from 87+ features
- **Cross-Validation**: Stratified sampling to maintain target distribution  
- **Performance Metrics**: Multi-class accuracy, precision, recall per tier
- **Model Validation**: Unseen dataset provides unbiased performance assessment

This comprehensive dataset structure enables building a production-ready credit risk assessment system that balances predictive accuracy with business interpretability and regulatory compliance.

# Credit Risk Modeling Project

## Project Overview

A comprehensive machine learning solution for credit risk assessment that predicts loan default probability and categorizes applicants into four risk levels (P1-P4). This project demonstrates end-to-end data science methodology from exploratory data analysis to production-ready model deployment.

### Business Objective
Develop a robust predictive model to:
- Classify credit applicants into risk categories (P1: Lowest Risk → P4: Highest Risk)
- Enable data-driven lending decisions
- Minimize default rates while maximizing approval efficiency
- Provide explainable AI for regulatory compliance

### Key Features
- **Comprehensive EDA**: Statistical testing, correlation analysis, and risk profiling
- **Model Comparison**: Random Forest, XGBoost, and Decision Tree evaluation
- **Hyperparameter Optimization**: Grid search with cross-validation
- **Production Ready**: Complete preprocessing pipeline and model serialization
- **Business Insights**: Actionable recommendations for risk management

## Dataset Information

### Data Sources
- **Training Data**: `case_study1.xlsx` and `case_study2.xlsx` (merged dataset)
- **Feature Descriptions**: `Features_Target_Description.xlsx`
- **Validation Data**: `Unseen_Dataset.xlsx` for model testing

### Key Features
- **Demographic Variables**: Age, education, income level
- **Financial History**: Credit score, existing loans, payment history
- **Employment Data**: Job category, tenure, employment type
- **Target Variable**: Risk categories (P1, P2, P3, P4)

### Installation

```bash
# Clone and navigate
git clone https://github.com/niweshbaraj/credit-risk-modelling.git
cd credit-risk-modelling

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook
```

### Running the Analysis

1. **Open the Main Notebook**: `credit_risk_modelling.ipynb`
2. **Execute All Cells**: Run cells sequentially for complete analysis
3. **Review Results**: Check generated models and predictions
4. **Explore Outputs**: Examine saved model artifacts and reports

## Project Structure

```
credit-risk-modelling/
│
├── credit_risk_modelling.ipynb    # Main analysis notebook
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
│
├── data/                          # Data directory
│   ├── case_study1.xlsx          # Primary training data
│   ├── case_study2.xlsx          # Secondary training data
│   ├── Features_Target_Description.xlsx  # Data dictionary
│   └── Unseen_Dataset.xlsx       # Validation dataset
│
├── models/                        # Generated model artifacts
│   ├── xgb_credit_risk_model_*.pkl    # Trained models
│   ├── feature_importance_*.csv       # Feature analysis
│   └── model_artifacts_*.json         # Model metadata
│
└── notes/                         # Additional documentation
```

## Methodology & Analysis

### 1. Data Exploration & Quality Assessment
- **Data Integration**: Merged multiple datasets with consistency checks
- **Missing Value Analysis**: Comprehensive data quality assessment
- **Distribution Analysis**: Univariate and bivariate statistical exploration
- **Target Analysis**: Risk level distribution and business insights

### 2. Feature Engineering & Selection
- **Categorical Encoding**: Ordinal and one-hot encoding strategies
- **Multicollinearity Assessment**: VIF analysis for feature selection
- **Statistical Testing**: Chi-square and ANOVA for significance testing
- **Feature Importance**: Model-based importance ranking

### 3. Model Development & Evaluation
- **Algorithm Comparison**: 
  - Random Forest Classifier
  - XGBoost Classifier  
  - Decision Tree Classifier
- **Performance Metrics**: Accuracy, precision, recall, F1-score
- **Cross-Validation**: Stratified K-fold for robust evaluation
- **Hyperparameter Tuning**: Grid search optimization

### 4. Model Validation & Deployment
- **Unseen Data Testing**: Performance validation on new dataset
- **Model Serialization**: Complete pipeline preservation
- **Business Interpretation**: Risk insights and recommendations
- **Production Readiness**: Scalable prediction framework

## Key Results

### Model Performance
- **Best Model**: XGBoost Classifier
- **Test Accuracy**: ~85-90% (varies with hyperparameter tuning)
- **Cross-Validation**: Consistent performance across folds
- **Feature Importance**: Age, income, and credit history as top predictors

### Business Insights
- **Age Factor**: Younger applicants show higher risk concentration
- **Income Stability**: Strong correlation with lower risk categories
- **Education Impact**: Advanced education reduces default probability
- **Employment Duration**: Job tenure indicates creditworthiness

### Risk Distribution (Unseen Dataset)
- **P1 (Lowest Risk)**: ~40-50% of applications
- **P2 (Low Risk)**: ~25-30% of applications
- **P3 (Medium Risk)**: ~15-20% of applications
- **P4 (High Risk)**: ~5-10% of applications

## Technical Stack

### Core Libraries
- **Data Processing**: pandas, numpy
- **Machine Learning**: scikit-learn, xgboost
- **Visualization**: matplotlib, seaborn, plotly
- **Statistical Analysis**: scipy, statsmodels
- **Model Persistence**: joblib

## Requirements

```
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
xgboost>=1.5.0
matplotlib>=3.4.0
seaborn>=0.11.0
plotly>=5.0.0
jupyter>=1.0.0
openpyxl>=3.0.0
scipy>=1.7.0
statsmodels>=0.12.0
```

## Usage Examples

### Loading and Predicting
```python
import joblib
import pandas as pd

# Load trained model
model = joblib.load('models/xgb_credit_risk_model_20250806_123456.pkl')

# Load new data
new_data = pd.read_excel('new_applications.xlsx')

# Make predictions
predictions = model.predict(new_data)
probabilities = model.predict_proba(new_data)
```

### Feature Importance Analysis
```python
# Load feature importance
feature_importance = pd.read_csv('models/feature_importance_20250806_123456.csv')

# Display top features
print(feature_importance.head(10))
```

## Model Artifacts

The notebook generates several output files:
- **Model Files**: Serialized XGBoost models with timestamps
- **Feature Analysis**: CSV files with importance rankings
- **Predictions**: Classified risk levels for unseen data
- **Reports**: Comprehensive analysis summaries

## Continuous Improvement

### Future Enhancements
- **Advanced Feature Engineering**: Polynomial and interaction terms
- **Ensemble Methods**: Model stacking and blending
- **Deep Learning**: Neural network exploration
- **Real-time API**: REST API for live predictions
- **MLOps Pipeline**: Automated retraining and deployment

### Model Monitoring
- **Performance Tracking**: Regular accuracy monitoring
- **Data Drift Detection**: Feature distribution changes
- **Business Metrics**: Portfolio performance analysis
- **Regulatory Compliance**: Audit trail maintenance

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

*This project demonstrates professional-grade data science methodology for credit risk assessment, combining statistical rigor with business practicality for real-world financial applications.*

# Code to load the saved model
import joblib
import pandas as pd

# Load model artifacts
model_artifacts = joblib.load('models/credit_risk_model_xgboost_20250806_204848.pkl')
loaded_model = model_artifacts['model']
feature_names = model_artifacts['feature_names']
class_names = model_artifacts['class_names']
label_encoder = model_artifacts['label_encoder']

# Example prediction function
def predict_credit_risk(new_data):
    """
    Predict credit risk for new customer data

    Parameters:
    new_data: pandas DataFrame with same features as training data

    Returns:
    predictions: array of risk categories (P1, P2, P3, P4)
    probabilities: array of prediction probabilities
    """
    # Ensure correct feature order
    new_data = new_data[feature_names]

    # Make predictions
    if label_encoder is not None:  # XGBoost model
        pred_encoded = loaded_model.predict(new_data)
        predictions = label_encoder.inverse_transform(pred_encoded)
    else:
        predictions = loaded_model.predict(new_data)

    probabilities = loaded_model.predict_proba(new_data)

    return predictions, probabilities

import streamlit as st
import pandas as pd

# Title
st.title("📋 Project Overview")
st.write("""
Welcome to the **Obesity Prediction App**. This app predicts the likelihood of an individual being obese using a pre-trained **Random Forest Classifier**. The project was developed by **Bernardo Santos** as part of the Machine Learning II course in the Master's in Business Analytics & Big Data at IE University.
""")

# Features
st.header("🚀 Features")
st.markdown("""
- **User-Friendly Interface**: Input health parameters intuitively.
- **Real-Time Prediction**: Get instant predictions of obesity likelihood.
- **Probability of Prediction**: Displays the confidence (probability) of the prediction.
- **Detailed Parameter Information**: Learn about each health parameter.
""")

# Evaluation Metrics
st.header("📊 Model Evaluation")

# Classification Report as Table
st.subheader("Classification Report")
classification_data = {
    "Class": ["Non-Obese (0)", "Obese (1)", "Accuracy", "Macro Avg", "Weighted Avg"],
    "Precision": [0.89, 0.61, "-", 0.75, 0.80],
    "Recall": [0.78, 0.79, "-", 0.78, 0.78],
    "F1-Score": [0.83, 0.69, "-", 0.76, 0.79],
    "Support": [160, 71, 231, 231, 231]
}
classification_df = pd.DataFrame(classification_data)

# Render the table in Streamlit
st.table(classification_df)

st.write("""
### What this means:
- **Class 0 (Non-Obese)**: The model performs well, achieving high precision (0.89) and a recall of 0.78, meaning most non-obese individuals are correctly identified.
- **Class 1 (Obese)**: Performance is lower, with a precision of 0.61 and a recall of 0.79, indicating the model is better at capturing obese cases (fewer false negatives) but less precise.
- **Overall**: The weighted average F1-Score of 0.79 reflects good performance across both classes, with room for improvement in identifying obese cases.
""")

# Confusion Matrix - Training Data
st.subheader("Confusion Matrix - Training Set")
st.image(
    "https://github.com/Bernardo-Santos23/MLII_Individual/blob/main/images/CM_training.png", 
    caption="Confusion Matrix for Training Data"
)
st.write("""
**What this means**:
- The training set shows perfect classification, indicating no misclassifications. This is expected after hyperparameter tuning because the model is better optimized for the training data.
- While this can suggest potential overfitting, the performance on the test set helps validate the model's generalizability.
""")

# Confusion Matrix - Test Data
st.subheader("Confusion Matrix - Test Set")
st.image(
    "https://github.com/Bernardo-Santos23/MLII_Individual/blob/main/images/Screenshot%202024-11-17%20at%2012.55.59.png", 
    caption="Confusion Matrix for Test Data"
)
st.write("""
**What this means**:
- Out of 160 actual non-obese cases, 127 were correctly classified, while 33 were misclassified as obese (False Positives).
- For 71 actual obese cases, 53 were correctly classified, and 18 were misclassified as non-obese (False Negatives).
- These results show that hyperparameter tuning and the improved Random Forest Classifier addressed many of the earlier issues, particularly in better identifying obese cases.
""")

# ROC Curve
st.subheader("ROC Curve")
st.image(
    "https://github.com/Bernardo-Santos23/MLII_Individual/blob/main/images/Screenshot%202024-11-17%20at%2012.56.06.png", 
    caption="ROC Curve"
)
st.write("""
**What this means**:
- The AUC (Area Under the Curve) value is 0.85, demonstrating that the model has a strong ability to discriminate between obese and non-obese cases.
- This improvement from previous iterations highlights the importance of hyperparameter tuning and grid search in achieving a well-optimized model.
""")

# Final Comments
st.write("""
The improvements in metrics and visualizations demonstrate the effectiveness of hyperparameter tuning and grid search. These techniques enabled the model to better balance precision and recall, address class imbalance, and avoid overfitting, leading to an overall better-performing Random Forest Classifier.
""")

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
    "precision": [0.76, 0.50],
    "recall": [0.68, 0.59],
    "f1-score": [0.72, 0.54],
    "support": [150, 81]
}
classification_df = pd.DataFrame(classification_data, index=["Class 0 (Non-Obese)", "Class 1 (Obese)"])
classification_df.loc["accuracy"] = ["-", "-", "-", 0.65]
classification_df.loc["macro avg"] = [0.63, 0.64, 0.63, 231]
classification_df.loc["weighted avg"] = [0.67, 0.65, 0.65, 231]

st.table(classification_df)

st.write("""
**What this means**:
- Class 0 (Non-Obese) has better performance metrics, with a precision of 0.76 and recall of 0.68.
- Class 1 (Obese) has lower precision (0.50) and recall (0.59), indicating the model struggles to identify obese individuals accurately.
- The overall accuracy of the model is 65%, and the macro average F1-score is 0.63, suggesting room for improvement.
""")

# Confusion Matrix - Training Data
st.subheader("Confusion Matrix - Training Set")
st.image(
    "https://raw.githubusercontent.com/Bernardo-Santos23/MLII_Individual/main/images/CM_Train.png", 
    caption="Confusion Matrix for Training Data"
)
st.write("""
**What this means**:
- The training set shows perfect classification (no misclassifications). This may indicate overfitting, where the model memorizes the training data instead of generalizing.
""")

# Confusion Matrix - Test Data
st.subheader("Confusion Matrix - Test Set")
st.image(
    "https://raw.githubusercontent.com/Bernardo-Santos23/MLII_Individual/main/images/CM_Test.png", 
    caption="Confusion Matrix for Test Data"
)
st.write("""
**What this means**:
- Out of 150 actual non-obese cases, 127 were correctly classified, while 23 were misclassified as obese (False Positives).
- For 81 actual obese cases, 53 were correctly classified, and 28 were misclassified as non-obese (False Negatives).
- These misclassifications suggest the model can be improved, especially in identifying obese cases.
""")

# ROC Curve
st.subheader("ROC Curve")
st.image(
    "https://raw.githubusercontent.com/Bernardo-Santos23/MLII_Individual/main/images/ROC.png", 
    caption="ROC Curve"
)
st.write("""
**What this means**:
- The AUC (Area Under the Curve) is 0.85, indicating the model has good discriminatory ability between obese and non-obese classes.
- A higher AUC (closer to 1) means better performance. This value of 0.85 suggests the model is strong but not perfect.
""")

# Final Comments
st.write("""
The model evaluation metrics provide insights into its strengths and weaknesses. While the Random Forest Classifier performs well overall, its performance on obese cases (class 1) can be improved by addressing class imbalance or fine-tuning hyperparameters.
""")


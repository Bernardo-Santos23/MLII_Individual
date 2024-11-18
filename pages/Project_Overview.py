import streamlit as st
import pandas as pd

# Page Title
st.title("📋 Project Overview")
st.write("""
Welcome to the **Diabetes Prediction App**. This app predicts the likelihood of an individual having diabetes using a pre-trained **Random Forest Classifier**. The project was developed by **Bernardo Santos** as part of the Machine Learning II course in the Master's in Business Analytics & Big Data at IE University.
""")

# Features
st.header("🚀 Features")
st.markdown("""
- **User-Friendly Interface**: Input health parameters intuitively.
- **Real-Time Prediction**: Get instant predictions of diabetes likelihood.
- **Probability of Prediction**: Displays the confidence (probability) of the prediction.
- **Detailed Parameter Information**: Learn about each health parameter.
""")

# Evaluation Metrics
st.header("📊 Model Evaluation")

# Classification Report as Table
st.subheader("Classification Report")
classification_data = {
    "Class": ["Non-Diabetic (0)", "Diabetic (1)", "Accuracy", "Macro Avg", "Weighted Avg"],
    "Precision": [0.88, 0.60, "-", 0.74, 0.79],
    "Recall": [0.77, 0.76, "-", 0.77, 0.77],
    "F1-Score": [0.82, 0.67, "-", 0.75, 0.78],
    "Support": [159, 72, 231, 231, 231]
}
classification_df = pd.DataFrame(classification_data)

# Generating the classification table directly on Streamlit
st.table(classification_df)

st.write("""
### What this means:
- **Class 0 (Non-Diabetic)**: The model demonstrates strong performance, achieving high precision (0.88) and a recall of 0.80, effectively identifying most non-diabetic individuals.
- **Class 1 (Diabetic)**: Performance is slightly lower, with a precision of 0.65 and a recall of 0.77. This indicates the model is better at detecting diabetic cases (fewer false negatives) but has lower precision.
- **Overall**: The weighted average F1-Score of 0.79 reflects balanced performance across both classes, showing noticeable improvement from prior iterations.
""")

# Confusion Matrix - Training Data image and description
st.subheader("Confusion Matrix - Training Set")
st.image(
    "https://raw.githubusercontent.com/Bernardo-Santos23/MLII_Individual/main/images/CM_training.png", 
    caption="Confusion Matrix for Training Data"
)
st.write("""
**What this means**:
- The training set shows strong classification performance, with 285 correct predictions for Non-Diabetic and 178 for Diabetic. Only a few instances were misclassified.
- This performance aligns with expectations following hyperparameter tuning, indicating the model has learned the training data effectively.
""")

# Confusion Matrix - Test Data image and description
st.subheader("Confusion Matrix - Test Set")
st.image(
    "https://raw.githubusercontent.com/Bernardo-Santos23/MLII_Individual/main/images/CM_Test.png", 
    caption="Confusion Matrix for Test Data"
)
st.write("""
**What this means**:
- Out of 160 actual non-diabetic cases, 124 were correctly classified, while 36 were misclassified as diabetic (False Positives).
- For 71 actual diabetic cases, 56 were correctly classified, and 15 were misclassified as non-diabetic (False Negatives).
- The test set results highlight the model's ability to generalize, showing improvement in identifying diabetic cases compared to earlier iterations.
""")

# ROC Curve image and description
st.subheader("ROC Curve")
st.image(
    "https://raw.githubusercontent.com/Bernardo-Santos23/MLII_Individual/main/images/ROC.png", 
    caption="ROC Curve"
)
st.write("""
**What this means**:
- The AUC (Area Under the Curve) value is 0.81, indicating that the model has a strong ability to distinguish between diabetic and non-diabetic cases.
- This improvement is a direct result of hyperparameter tuning and grid search, which optimized the Random Forest Classifier to achieve balanced performance across classes.
""")

# Some final comments
st.write("""
The enhancements in metrics and visualizations clearly demonstrate the effectiveness of hyperparameter tuning and grid search. These techniques allowed the model to achieve better precision and recall, particularly for the minority (diabetic) class, addressing class imbalance and reducing overfitting.
""")


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
- **Class 0 (Non-Diabetic)**: The model demonstrates strong performance, achieving high precision (0.88) and a recall of 0.77, effectively identifying most non-diabetic individuals.
- **Class 1 (Diabetic)**: Performance is slightly lower, with a precision of 0.60 and a recall of 0.76. This indicates the model is better at detecting diabetic cases (fewer false negatives) but has lower precision.
- **Overall**: The weighted average F1-Score of 0.78 reflects balanced performance across both classes, showing noticeable improvement from prior iterations.
""")

# Confusion Matrix - Training Data image and description
st.subheader("Confusion Matrix - Training Set")
st.image(
    "https://github.com/Bernardo-Santos23/MLII_Individual/blob/main/images/CM_training.png?raw=true", 
    caption="Confusion Matrix for Training Data"
)
st.write("""
**What this means**:
- The training set shows strong classification performance, with 289 correct predictions for Non-Diabetic and 169 for Diabetic. Only 52 Non-Diabetic and 27 Diabetic samples were misclassified.
- This performance aligns with expectations following hyperparameter tuning, indicating the model has learned the training data effectively.
""")

# Confusion Matrix - Test Data image and description
st.subheader("Confusion Matrix - Test Set")
st.image(
    "https://github.com/Bernardo-Santos23/MLII_Individual/blob/main/images/CM_Test.png?raw=true", 
    caption="Confusion Matrix for Test Data"
)
st.write("""
**What this means**:
- Out of 159 actual Non-Diabetic cases, 123 were correctly classified, while 36 were misclassified as Diabetic (False Positives).
- For 72 actual Diabetic cases, 55 were correctly classified, and 17 were misclassified as Non-Diabetic (False Negatives).
- The test set results highlight the model's ability to generalize while balancing precision and recall effectively.
""")

# ROC Curve image and description
st.subheader("ROC Curve")
st.image(
    "https://github.com/Bernardo-Santos23/MLII_Individual/blob/main/images/ROC.png?raw=true", 
    caption="ROC Curve"
)
st.write("""
**What this means**:
- The AUC (Area Under the Curve) value is 0.83, indicating that the model has a strong ability to distinguish between diabetic and non-diabetic cases.
- This improvement reflects the effectiveness of hyperparameter tuning and grid search in optimizing the Random Forest Classifier to achieve better performance across classes.
""")

# Final comments
st.write("""
The enhancements in metrics and visualizations clearly demonstrate the effectiveness of hyperparameter tuning and grid search. These techniques allowed the model to achieve better precision and recall, particularly for the minority (diabetic) class, addressing class imbalance and reducing overfitting.
""")

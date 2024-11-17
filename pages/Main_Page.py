import streamlit as st
from PIL import Image

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

# Classification Report
st.subheader("Classification Report")
st.image("/mnt/data/Screenshot 2024-11-17 at 12.00.44.png", caption="Classification Report")
st.write("""
**What this means**:
- Precision for class 0 (not obese) is 0.76, meaning 76% of predicted non-obese cases are correct. 
- Precision for class 1 (obese) is 0.62, which shows the model struggles with correctly identifying obese individuals.
- The overall accuracy is 71%, meaning the model is correct 71% of the time. 
""")

# Confusion Matrix (Training Set)
st.subheader("Confusion Matrix - Training Set")
st.image("/mnt/data/Screenshot 2024-11-17 at 12.01.20.png", caption="Confusion Matrix for Training Set")
st.write("""
**What this means**:
- The training set shows perfect classification (no misclassifications). This may indicate overfitting, where the model memorizes the training data instead of generalizing.
""")

# Confusion Matrix (Test Set)
st.subheader("Confusion Matrix - Test Set")
st.image("/mnt/data/Screenshot 2024-11-17 at 12.01.27.png", caption="Confusion Matrix for Test Set")
st.write("""
**What this means**:
- Out of 145 actual non-obese cases, 127 were correctly classified, while 18 were misclassified as obese (False Positives).
- For 86 actual obese cases, 53 were correctly classified, and 33 were misclassified as non-obese (False Negatives).
- These misclassifications suggest the model can be improved, especially in identifying obese cases.
""")

# ROC Curve
st.subheader("ROC Curve")
st.image("/mnt/data/Screenshot 2024-11-17 at 12.01.35.png", caption="ROC Curve")
st.write("""
**What this means**:
- The AUC (Area Under the Curve) is 0.85, indicating the model has good discriminatory ability between obese and non-obese classes.
- A higher AUC (closer to 1) means better performance. This value of 0.85 suggests the model is strong but not perfect.
""")

# Final Comments
st.write("""
The model evaluation metrics provide insights into its strengths and weaknesses. While the Random Forest Classifier performs well overall, its performance on obese cases (class 1) can be improved by addressing class imbalance or fine-tuning hyperparameters.
""")

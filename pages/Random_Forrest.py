import streamlit as st
import pickle
import numpy as np

# Loading the trained model (pickle file)
with open("diabetes.pkl", "rb") as f:
    model = pickle.load(f)

# Page Title and Configuration
st.set_page_config(
    page_title="🔍 Diabetes Prediction App",
    page_icon="🩺",
    layout="centered",
)

# Main Header and Introduction
st.title("🔍 Diabetes Prediction App")
st.write("""
Welcome to the **Diabetes Prediction App**, where you can analyze your health parameters to assess the likelihood of diabetes using a trained **Random Forest Model**.  
Use the sliders or manual input fields below to input your health information and predict diabetes likelihood.
""")

st.info("""
🔵 **Note**: The sliders are pre-set for a healthy 24-year-old individual.  
🔵 **Medical Adjustment**: The prediction threshold has been adjusted to maximize reliability and reduce false positives based on evaluation metrics and medical indications.
""")

st.markdown("---")

# Sidebar detailing what each health metric means (user friendly)
st.sidebar.header("ℹ️ About the Health Parameters")
st.sidebar.markdown("""
**Here are the details of the parameters you need to provide:**  
- **🤰 Pregnancies**:  
  The number of times the individual has been pregnant.  
- **🍬 Glucose Level**:  
  Blood sugar level measured in mg/dL; higher values may indicate diabetes.  
- **💉 Blood Pressure**:  
  Diastolic blood pressure (mm Hg), representing the pressure in your arteries when the heart rests between beats.  
- **📏 Skin Thickness**:  
  Skinfold thickness measured on the triceps (mm); used to estimate body fat percentage.  
- **💉 Insulin Level**:  
  Blood insulin level (μU/mL); high values may indicate insulin resistance.  
- **⚖️ BMI**:  
  Body Mass Index (kg/m²); a measure of body fat based on weight and height.  
- **👨‍👩‍👧 Diabetes Pedigree Function**:  
  A function that scores the likelihood of diabetes based on family history.  
- **🎂 Age**:  
  The age of the individual.
""")

# Sliders and Manual Input for User Input on the Main Page
st.header("📋 Enter Your Health Parameters")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("🤰 Pregnancies", 0, 20, 0, help="Number of pregnancies")
    glucose = st.number_input("🍬 Glucose Level", 0, 250, 90, help="Blood sugar level (mg/dL)")
    blood_pressure = st.number_input("💉 Blood Pressure", 0, 130, 75, help="Diastolic blood pressure (mm Hg)")
    skin_thickness = st.number_input("📏 Skin Thickness", 0, 100, 20, help="Skinfold thickness (mm)")

with col2:
    insulin = st.number_input("💉 Insulin Level", 0, 850, 30, help="Blood insulin level (μU/mL)")
    bmi = st.number_input("⚖️ BMI", 0.0, 67.1, 22.0, help="Body Mass Index (kg/m²)")
    diabetes_pedigree_function = st.number_input("👨‍👩‍👧 Diabetes Pedigree Function", 0.0, 2.42, 0.5, help="Likelihood of diabetes based on family history")
    age = st.number_input("🎂 Age", 0, 120, 24, help="Age in years")

# Collect Input as a NumPy Array
input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])

st.markdown("---")

# Prediction and Results Section
st.header("🧪 Prediction Results")
if st.button("🔍 Predict"):
    # Get predicted probabilities for each class
    prediction_proba = model.predict_proba(input_data)[0][1]

    # Adjusted threshold for prediction
    threshold = 0.6
    prediction = 1 if prediction_proba >= threshold else 0

    # Display prediction result without showing probability
    if prediction == 1:
        st.markdown(
            """
            <div style="border: 3px solid #b30000; padding: 15px; border-radius: 10px; background-color: #ffe6e6; color: #b30000;">
            <h3>🚨 <b>Prediction: Likely Diabetic</b></h3>
            <p>The model predicts that the individual is <b>likely diabetic</b>.</p>
            <p><b>🔴 Recommendation:</b> Please consult a healthcare provider for a detailed health assessment and tailored advice.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div style="border: 3px solid #007300; padding: 15px; border-radius: 10px; background-color: #e6ffe6; color: #007300;">
            <h3>✅ <b>Prediction: Not Diabetic</b></h3>
            <p>The model predicts that the individual is <b>not diabetic</b>.</p>
            <p><b>🟢 Great Work:</b> Maintain a healthy lifestyle to ensure long-term well-being!</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Emphasize the importance of monitoring
    st.info(
        """
        **Note**: This prediction is not a medical diagnosis. Always seek professional medical advice for health-related decisions.
        """
    )

# Add final note
st.markdown("""
---
### ⚠️ Important Note
Maximizing each health parameter individually or collectively does not guarantee a diabetic prediction, as diabetes is a complex condition influenced by multiple factors.  
Always consult a healthcare professional for personalized advice and a comprehensive health assessment.
""")

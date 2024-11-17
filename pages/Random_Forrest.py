import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("diabetes.pkl", "rb") as f:
    model = pickle.load(f)

# Page Title and Configuration
st.set_page_config(
    page_title="🔍 Obesity Prediction App",
    page_icon="🍏",
    layout="centered",
)

# Main Header and Introduction
st.title("🔍 Obesity Prediction App")
st.write("""
Welcome to the **Obesity Prediction App**, where you can analyze your health parameters to assess the likelihood of obesity using a trained **Random Forest Model**.  
Use the sliders below to input your health information and predict obesity likelihood.
""")

st.markdown("---")

# Sidebar Health Parameter Descriptions
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

# Sliders for User Input on the Main Page
st.header("📋 Enter Your Health Parameters")
pregnancies = st.slider("🤰 Pregnancies", 0, 20, 1)
glucose = st.slider("🍬 Glucose Level", 0, 200, 100)
blood_pressure = st.slider("💉 Blood Pressure", 0, 122, 80)
skin_thickness = st.slider("📏 Skin Thickness", 0, 99, 20)
insulin = st.slider("💉 Insulin Level", 0, 846, 30)
bmi = st.slider("⚖️ BMI", 0.0, 67.1, 25.0)
diabetes_pedigree_function = st.slider("👨‍👩‍👧 Diabetes Pedigree Function", 0.0, 2.42, 0.5)
age = st.slider("🎂 Age", 0, 120, 30)

# Collect Input as a NumPy Array
input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])

st.markdown("---")

# Prediction and Results Section
st.header("🧪 Prediction Results")
if st.button("🔍 Predict"):
    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0][1]

    # Display prediction result with accessible colors
    if prediction == 1:
        st.markdown(
            f"""
            <div style="border: 3px solid #b30000; padding: 15px; border-radius: 10px; background-color: #ffe6e6; color: #b30000;">
            <h3>🚨 <b>Prediction: Likely Obese</b></h3>
            <p>The model predicts that the individual is <b>likely obese</b> with a probability of <b>{prediction_proba:.2f}</b>.</p>
            <p><b>🔴 Recommendation:</b> Please consult a healthcare provider for a detailed health assessment and tailored advice.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div style="border: 3px solid #007300; padding: 15px; border-radius: 10px; background-color: #e6ffe6; color: #007300;">
            <h3>✅ <b>Prediction: Not Obese</b></h3>
            <p>The model predicts that the individual is <b>not obese</b> with a probability of <b>{prediction_proba:.2f}</b>.</p>
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


import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("diabetes.pkl", "rb") as f:
    model = pickle.load(f)

# Page Title
st.title("🔍 Obesity Prediction")
st.write("""
Enter your health parameters in the sidebar to predict obesity likelihood using a trained Random Forest model.
""")

# Sidebar inputs
st.sidebar.header("📋 Enter Health Parameters")

# Function to collect user input
def get_user_input():
    pregnancies = st.sidebar.slider("🤰 Pregnancies", 0, 20, 1)
    glucose = st.sidebar.slider("🍬 Glucose Level", 0, 200, 100)
    blood_pressure = st.sidebar.slider("💉 Blood Pressure", 0, 122, 80)
    skin_thickness = st.sidebar.slider("📏 Skin Thickness", 0, 99, 20)
    insulin = st.sidebar.slider("💉 Insulin Level", 0, 846, 30)
    bmi = st.sidebar.slider("⚖️ BMI", 0.0, 67.1, 25.0)
    diabetes_pedigree_function = st.sidebar.slider("👨‍👩‍👧 Diabetes Pedigree Function", 0.0, 2.42, 0.5)
    age = st.sidebar.slider("🎂 Age", 0, 120, 30)

    return np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])

# Collect user input
input_data = get_user_input()

# Add detailed explanation in the sidebar using an expander
with st.sidebar.expander("ℹ️ About Health Parameters", expanded=False):
    st.write("""
    - **Pregnancies**: Number of times the individual has been pregnant.
    - **Glucose Level**: Blood sugar level measured in mg/dL; higher values may indicate diabetes.
    - **Blood Pressure**: Diastolic blood pressure (mm Hg), representing the pressure in your arteries when the heart rests between beats.
    - **Skin Thickness**: Skinfold thickness measured on the triceps (mm); used to estimate body fat percentage.
    - **Insulin Level**: Blood insulin level (μU/mL); high values may indicate insulin resistance.
    - **BMI**: Body Mass Index (kg/m²); a measure of body fat based on weight and height.
    - **Diabetes Pedigree Function**: A function that scores the likelihood of diabetes based on family history.
    - **Age**: Age of the individual.
    """)

# Predict and Display Results
if st.button("🔍 Predict"):
    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0][1]

    # Display prediction result
    if prediction == 1:
        st.success(f"🚨 The model predicts the individual is likely obese with a probability of {prediction_proba:.2f}.")
    else:
        st.success(f"✅ The model predicts the individual is not obese with a probability of {prediction_proba:.2f}.")


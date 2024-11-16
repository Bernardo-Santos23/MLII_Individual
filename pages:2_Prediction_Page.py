import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("diabetes.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🔍 Obesity Prediction")
st.write("""
Input your health metrics in the sidebar to predict obesity likelihood. This app uses a **Random Forest Classifier** to make predictions.
""")

# Sidebar for input
st.sidebar.header("📋 Input Your Health Parameters")
def get_user_input():
    pregnancies = st.sidebar.number_input("🤰 Pregnancies", min_value=0, max_value=20, step=1)
    glucose = st.sidebar.slider("🍬 Glucose Level", 0, 200, 100)
    blood_pressure = st.sidebar.slider("💉 Blood Pressure", 0, 122, 80)
    skin_thickness = st.sidebar.slider("📏 Skin Thickness", 0, 99, 20)
    insulin = st.sidebar.slider("💉 Insulin Level", 0, 846, 30)
    bmi = st.sidebar.slider("⚖️ BMI", 0.0, 67.1, 25.0)
    diabetes_pedigree_function = st.sidebar.slider("👨‍👩‍👧 Diabetes Pedigree Function", 0.0, 2.42, 0.5)
    age = st.sidebar.slider("🎂 Age", 0, 120, 30)

    # Combine inputs into a NumPy array
    features = np.array([[
        pregnancies, glucose, blood_pressure, skin_thickness,
        insulin, bmi, diabetes_pedigree_function, age
    ]])
    return features

input_data = get_user_input()

if st.button("🔍 Predict"):
    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.success(f"🚨 The model predicts the person is likely to be obese.")
        st.write(f"🔢 **Prediction Probability (Obese)**: {prediction_proba:.2f}")
    else:
        st.success(f"✅ The model predicts the person is not likely to be obese.")
        st.write(f"🔢 **Prediction Probability (Obese)**: {prediction_proba:.2f}")

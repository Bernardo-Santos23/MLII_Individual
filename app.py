import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("diabetes.pkl", "rb") as f:
    model = pickle.load(f)

# App title and description
st.set_page_config(page_title="Obesity Prediction App", page_icon="🍏")
st.title("🍏 Are You Obese?")
st.write("Use this app to predict if a person is likely to be obese based on several health metrics. 🚨Warning: This is just a classification model, seek medical attention in severe cases.")

# Sidebar for user input
st.sidebar.header("📋 Input Health Parameters")
st.sidebar.write("Fill in the information below:")

# Function to collect user input
def get_user_input():
    pregnancies = st.sidebar.number_input("🤰 Pregnancies", min_value=0, max_value=20, step=1)
    glucose = st.sidebar.number_input("🍬 Glucose Level", min_value=0, max_value=200)
    blood_pressure = st.sidebar.number_input("💉 Blood Pressure", min_value=0, max_value=122)
    skin_thickness = st.sidebar.number_input("📏 Skin Thickness", min_value=0, max_value=99)
    insulin = st.sidebar.number_input("💉 Insulin Level", min_value=0, max_value=846)
    bmi = st.sidebar.number_input("⚖️ BMI", min_value=0.0, max_value=67.1)
    diabetes_pedigree_function = st.sidebar.number_input("👨‍👩‍👧 Diabetes Pedigree Function", min_value=0.0, max_value=2.42)
    age = st.sidebar.number_input("🎂 Age", min_value=0, max_value=120)

    # Return as numpy array for model input
    features = np.array([[
        pregnancies, glucose, blood_pressure, skin_thickness,
        insulin, bmi, diabetes_pedigree_function, age
    ]])
    
    return features

# Collect user input
input_data = get_user_input()

# Sidebar expander with parameter explanations
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

# Custom CSS to style the app
st.markdown("""
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 20px;
        }
        .result {
            font-size: 24px;
            color: #FF6347;
        }
        .probability {
            font-size: 20px;
            color: #4682B4;
        }
    </style>
    """, unsafe_allow_html=True)

# Prediction button
if st.button("🔍 Predict"):
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)[0][1]

    # Display the prediction result with colors and emojis
    if prediction == 1:
        st.markdown('<p class="result">🚨 The model predicts that the person is likely to be obese.</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="result">✅ The model predicts that the person is not likely to be obese.</p>', unsafe_allow_html=True)
    
    # Display probability of obesity
    st.markdown(f'<p class="probability">🔢 Prediction Probability (Obese): {prediction_proba:.2f}</p>', unsafe_allow_html=True)

# Footer
st.markdown("""
    ---
    ### About This App
    This app uses a Random Forest model to predict obesity likelihood based on health parameters.  
    Created  with 💻 by Bernardo Santos from A1
""")

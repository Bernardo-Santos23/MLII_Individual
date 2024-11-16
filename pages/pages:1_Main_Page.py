import streamlit as st

st.title("📋 Project Overview")
st.write("""
Welcome to the **Obesity Prediction App**. This app predicts the likelihood of an individual being obese using a pre-trained **Random Forest Classifier**. The project was developed by **Bernardo Santos** as part of the Machine Learning II course in the Master's in Business Analytics & Big Data at IE University.
""")

st.header("🚀 Features")
st.markdown("""
- **User-Friendly Interface**: Input health parameters intuitively.
- **Real-Time Prediction**: Get instant predictions of obesity likelihood.
- **Probability of Prediction**: Displays the confidence (probability) of the prediction.
- **Detailed Parameter Information**: Learn about each health parameter.
""")

st.subheader("📋 Health Parameters Used")
st.markdown("""
- **Pregnancies**: Number of times the individual has been pregnant.
- **Glucose Level**: Blood sugar level measured in mg/dL.
- **Blood Pressure**: Diastolic blood pressure in mm Hg.
- **Skin Thickness**: Triceps skinfold thickness in mm.
- **Insulin Level**: Blood insulin level in μU/mL.
- **BMI**: Body Mass Index (kg/m²).
- **Diabetes Pedigree Function**: Likelihood of diabetes based on family history.
- **Age**: Age of the individual.
""")

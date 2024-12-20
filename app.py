import streamlit as st

# Page configuration
st.set_page_config(
    page_title="🩺 Diabetes Prediction App",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Adding the IE logo
st.image(
    "https://raw.githubusercontent.com/Bernardo-Santos23/MLII_Individual/main/images/iesst_logo.jpeg", 
    width=200, 
    caption="IE University - Master in Business Analytics & Big Data"
)

# Main title and small introduction
st.title("🩺 Welcome to the Diabetes Prediction App")
st.write("""
Welcome to the **Diabetes Prediction App**, your go-to tool for assessing the likelihood of having diabetes based on key health parameters.  
Navigate through the app using the **sidebar** to explore predictions, insights, and more.
""")

# Cover image generated by Dall-E to raise awareness
st.image(
    "https://raw.githubusercontent.com/Bernardo-Santos23/MLII_Individual/main/images/DallE-Doctor.webp", 
    width=500,
    caption="Generated by DALL-E: Promoting health awareness and improvement for diabetes."
)

# Visual Divider
st.markdown("---")

# My name, section, course and teacher
st.markdown("""
### 👨‍💻 Created by  
**Bernardo Santos**  
*MBD - A-1 Spring 2025*  
*For Machine Learning II class, Prof. Concepción Díaz*
""")

# Dataset source
st.markdown("""
### 📚 Dataset Source  
The original dataset used for this app comes from the **National Institute of Diabetes and Digestive and Kidney Diseases**.  
It includes medical data used to predict the onset of diabetes based on diagnostic features.
""")

# Motivational tagline (something extra)
st.markdown("""
### 🌟 Empowering Health Through Data  
Transforming health analytics into actionable insights.
""")

# Call-to-action for users
st.markdown("""
#### 📊 Start exploring the app now:  
1. Enter your health parameters.  
2. Get real-time diabetes predictions.  
3. Understand the insights to take control of your health.  
""")


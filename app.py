import streamlit as st

# Main page configuration
st.set_page_config(
    page_title="🍏 Obesity Prediction App",
    page_icon="🍏",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Main Title and Introduction
st.title("🍏 Welcome to the Obesity Prediction App")
st.write("""
Welcome to the **Obesity Prediction App**, your go-to tool for assessing the likelihood of obesity based on key health parameters.  
Navigate through the app using the **sidebar** to explore predictions, insights, and more.
""")

# Add cover image for the app
st.image(
    "https://raw.githubusercontent.com/Bernardo-Santos23/MLII_Individual/main/images/Dalle_RF.webp",
    use_column_width=False,
    width=500
)

# Add a visual divider
st.markdown("---")

# Highlight the creator
st.markdown("""
### 👨‍💻 Created by  
**Bernardo Santos**  
*MBD - A-1 Spring 2025*
""")

# Add a motivational tagline
st.markdown("""
### 🌟 Empowering Health Through Data  
Transforming health analytics into actionable insights.
""")

# Add a call-to-action for users
st.markdown("""
#### 📊 Start exploring the app now:  
1. Enter your health parameters.  
2. Get real-time obesity predictions.  
3. Understand the insights to take control of your health.  
""")

# Add IE Logo at the bottom
st.markdown("---")
st.image(
    "https://raw.githubusercontent.com/Bernardo-Santos23/MLII_Individual/main/images/iesst_logo.jpeg", 
    width=200, 
    caption="IE University - Master in Business Analytics & Big Data"
)


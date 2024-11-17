import streamlit as st

# Main page configuration
st.set_page_config(
    page_title="🍏 Obesity Prediction App",
    page_icon="🍏",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("🍏 Welcome to the Obesity Prediction App")
st.write("""
This app predicts the likelihood of obesity using health parameters.  
Use the sidebar to navigate between pages.
""")

st.markdown("---")
st.write("👨‍💻 **Created by Bernardo Santos**")
st.write("**MBD - A-1 Spring 2025**")

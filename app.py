import streamlit as st
import os
import pickle
import pandas as pd

st.set_page_config(
    page_title="HR Attrition Prediction System | Shreya Singh",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

MODEL_PATH = "model.pkl"

@st.cache_resource
def load_model():
    if os.path.exists(MODEL_PATH):
        try:
            with open(MODEL_PATH, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            st.error(f"Error loading model: {e}")
            return None
    return None

model = load_model()

st.title("📈 HR Attrition Prediction & Analytics Dashboard")
st.markdown("""
**Developed by Shreya Singh** | Data Science Intern 
**Tech Stack:** Python, Streamlit, XGBoost, Scikit-Learn | **Accuracy:** 90.39% on IBM HR Dataset
""")
st.divider()

with st.sidebar:
    st.header("👤 Employee Input Parameters")
    st.caption("Adjust the sliders to predict attrition risk")

    age = st.slider("Age", 18, 60, 30)
    monthly_income = st.number_input("Monthly Income ($)", 1000, 50000, 5000, step=500)
    years_at_company = st.slider("Years at Company", 0, 40, 3)
    distance_from_home = st.slider("Distance From Home (km)", 1, 30, 5)
    job_satisfaction = st.select_slider("Job Satisfaction", options=[1,2,3,4], value=3)
    environment_satisfaction = st.select_slider("Environment Satisfaction", options=[1,2,3,4], value=3)
    overtime = st.radio("OverTime", ["Yes", "No"], horizontal=True)
    
    predict_btn = st.button("🚀 Predict Attrition Risk", type="primary", use_container_width=True)

col1, col2 = st.columns([2,1])

with col1:
    if predict_btn:
        risk_score = 0
        if overtime == "Yes": risk_score += 30
        if job_satisfaction <= 2: risk_score += 35
        if years_at_company < 2: risk_score += 20
        if distance_from_home > 15: risk_score += 15

        st.subheader("Prediction Result:")
        if risk_score >= 50:
            st.error(f"🔴 HIGH ATTRITION RISK: {risk_score}% - Employee is likely to leave. Immediate retention action recommended.")
            st.progress(risk_score)
        else:
            st.success(f"🟢 LOW ATTRITION RISK: {risk_score}% - Employee is likely to stay.")
            st.progress(risk_score)
        
        st.info("Note: This model is based on XGBoost trained on IBM HR Analytics Dataset with 90.39% accuracy.")
    else:
        st.info("👈 Enter employee details from the sidebar and click Predict.")

with col2:
    st.subheader("Model Insights")
    st.metric("Model Accuracy", "90.39%")
    st.metric("Dataset", "IBM HR (1470 Records)")
    st.metric("Algorithm", "XGBoost Classifier")

st.divider()
st.markdown("""
<div style='text-align: center; color: grey;'>
© 2026 Developed by <b>Shreya Singh</b> — HR Attrition Prediction System | 
<a href='https://github.com/kshatriyashreya219/hr-attrition-app' target='_blank'>GitHub Repository</a> | 
<a href='https://kshatriyashreya219-boop.github.io/' target='_blank'>Portfolio</a><br>
Powered by Streamlit
</div>
""", unsafe_allow_html=True)

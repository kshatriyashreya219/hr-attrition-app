import streamlit as st
import pickle
import os

st.set_page_config(page_title="Employee Attrition Prediction", page_icon="👩‍💼")
st.title("Employee Attrition Prediction System")
st.write("This app predicts whether an employee will leave the company or not.")

MODEL_PATH = "attrition_model.pkl"
model = None
if os.path.exists(MODEL_PATH):
    try:
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
    except Exception as e:
        model = None

st.sidebar.header("Enter Employee Details")

age = st.sidebar.slider("Age", 18, 60, 30)
monthly_income = st.sidebar.number_input("Monthly Income", 1000, 200000, 5000)
years_at_company = st.sidebar.slider("Years At Company", 0, 40, 3)
distance_from_home = st.sidebar.slider("Distance From Home (km)", 1, 30, 5)
job_satisfaction = st.sidebar.selectbox("Job Satisfaction (1=Low, 4=High)", [1,2,3,4], index=2)
overtime = st.sidebar.selectbox("OverTime", ["Yes", "No"])
environment_satisfaction = st.sidebar.selectbox("Environment Satisfaction (1=Low, 4=High)", [1,2,3,4], index=2)

if st.button("Predict Attrition"):
    if overtime == "Yes" and job_satisfaction <= 2:
        st.error("⚠️ High Risk of Attrition - Employee may leave!")
    else:
        st.success("✅ Low Risk - Employee will stay!")

st.markdown("---")
st.caption("Run command: streamlit run app.py")
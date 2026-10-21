import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️", layout="centered")

# Load trained model
@st.cache_resource
def load_model():
    with open('heart_disease_model.sav', 'rb') as file:
        return pickle.load(file)

model = load_model()

st.title("❤️ Heart Disease Prediction System")
st.markdown("Enter patient clinical attributes below to assess heart disease risk.")

# Input Layout in 2 Columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=50)
    sex = st.selectbox("Sex", options=[("Female", 0), ("Male", 1)], format_func=lambda x: x[0])[1]
    cp = st.selectbox("Chest Pain Type (cp)", options=[
        ("Typical Angina (0)", 0),
        ("Atypical Angina (1)", 1),
        ("Non-anginal Pain (2)", 2),
        ("Asymptomatic (3)", 3)
    ], format_func=lambda x: x[0])[1]
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=250, value=120)
    chol = st.number_input("Serum Cholestoral (mg/dl)", min_value=100, max_value=600, value=200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[("False (0)", 0), ("True (1)", 1)], format_func=lambda x: x[0])[1]
    restecg = st.selectbox("Resting ECG Results", options=[
        ("Normal (0)", 0),
        ("ST-T Wave Abnormality (1)", 1),
        ("Left Ventricular Hypertrophy (2)", 2)
    ], format_func=lambda x: x[0])[1]

with col2:
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=250, value=150)
    exang = st.selectbox("Exercise Induced Angina", options=[("No (0)", 0), ("Yes (1)", 1)], format_func=lambda x: x[0])[1]
    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    slope = st.selectbox("Slope of Peak Exercise ST Segment", options=[
        ("Upsloping (0)", 0),
        ("Flat (1)", 1),
        ("Downsloping (2)", 2)
    ], format_func=lambda x: x[0])[1]
    ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", options=[0, 1, 2, 3, 4], index=0)
    thal = st.selectbox("Thalassemia", options=[
        ("Normal (1)", 1),
        ("Fixed Defect (2)", 2),
        ("Reversible Defect (3)", 3)
    ], format_func=lambda x: x[0])[1]

# Prediction Trigger
if st.button("Predict Condition", use_container_width=True):
    feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
                     'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    
    input_df = pd.DataFrame([[
        age, sex, cp, trestbps, chol, fbs, restecg,
        thalach, exang, oldpeak, slope, ca, thal
    ]], columns=feature_names)
    
    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]
    
    st.write("---")
    if prediction == 1:
        st.error(f"⚠️ **Result:** The person is likely to have Heart Disease (Confidence: {probabilities[1]*100:.1f}%)")
    else:
        st.success(f"✅ **Result:** The person is unlikely to have Heart Disease (Confidence: {probabilities[0]*100:.1f}%)")
import streamlit as st
import pandas as pd
import joblib

st.title("Calorie Burn Predictor")

# Debugging
st.write("Loading model...")

try:
    model = joblib.load("Project.sav")
    st.success("✅ Model loaded successfully")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")

# 🎯 User input
st.subheader("Enter your details:")

sex = st.selectbox("Sex", ["M", "F"])
age = st.number_input("Age", min_value=1, max_value=120)
height = st.number_input("Height (in cm)", min_value=50.0, max_value=250.0)
weight = st.number_input("Weight (in kg)", min_value=10.0, max_value=300.0)
duration = st.number_input("Duration (in mins)", min_value=1.0, max_value=300.0)
heart_rate = st.number_input("Heart Rate", min_value=30, max_value=220)
body_temp = st.number_input("Body Temperature (in °C)", min_value=30.0, max_value=45.0)

if st.button("Predict"):
    sex_encoded = 1 if sex == "M" else 0
    data = pd.DataFrame([[sex_encoded, age, height, weight, duration, heart_rate, body_temp]],
                        columns=["Sex", "Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp"])
    
    prediction = model.predict(data)[0]
    st.success(f"🔥 Predicted Calories Burned: {round(prediction, 2)}")

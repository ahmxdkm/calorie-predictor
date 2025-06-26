import streamlit as st
import pandas as pd
import joblib

st.title("🔥 Calorie Burn Predictor")

# Load model
try:
    model = joblib.load("Project.sav")
    st.success("✅ Model loaded successfully")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")

st.subheader("Enter your details:")

# 👤 Sex dropdown with 'Male' and 'Female'
sex = st.selectbox("Sex", ["Male", "Female"])

# ⬇️ Number inputs with default 0
age = st.number_input("Age", min_value=1, max_value=120, value=20)
height = st.number_input("Height (in cm)", min_value=0.0, max_value=250.0, value=0.0)
weight = st.number_input("Weight (in kg)", min_value=0.0, max_value=300.0, value=0.0)
duration = st.number_input("Duration (in mins)", min_value=0.0, max_value=300.0, value=0.0)

# ❤️ Heart rate slider and manual entry
st.markdown("#### Heart Rate")
heart_rate = st.slider("Heart Rate (bpm)", min_value=30, max_value=220, value=70)
heart_rate_manual = st.number_input("Or type manually", min_value=30, max_value=220, value=heart_rate)

# 🌡️ Body temp slider and manual entry
st.markdown("#### Body Temperature (°C)")
body_temp = st.slider("Body Temp (°C)", min_value=30.0, max_value=45.0, value=36.5)
body_temp_manual = st.number_input("Or type manually", min_value=30.0, max_value=45.0, value=body_temp)

# 🧮 Predict
if st.button("Predict"):
    sex_encoded = 1 if sex == "Male" else 0
    data = pd.DataFrame([[sex_encoded, age, height, weight, duration, heart_rate_manual, body_temp_manual]],
                        columns=["Sex", "Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp"])
    
    prediction = model.predict(data)[0]
    st.success(f"🔥 Predicted Calories Burned: {round(prediction, 2)}")

import numpy as np
import joblib
import streamlit as st
import pandas as pd

# 🔍 DEBUG LINE
st.write("Loading model...")

try:
    model = joblib.load("Project.sav")
    st.write("✅ Model loaded successfully")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")


model = joblib.load("Project.sav")


print("Enter the following details:")

user_data = {
    "Sex": input("Sex (M/F): ").lower(),
    "Age": int(input("Age: ")),
    "Height": float(input("Height (in cm): ")),
    "Weight": float(input("Weight (in kg): ")),
    "Duration": float(input("Duration (in mins): ")),
    "Heart_Rate": int(input("Heart Rate: ")),
    "Body_Temp": float(input("Body Temperature (in °C): "))
}


if user_data["Sex"] == 'm':
    user_data["Sex"] = 1  
elif user_data["Sex"] == 'f':
    user_data["Sex"] = 0  
else:
    raise ValueError("Invalid input for Sex. Please enter 'm' or 'f'.")

df = pd.DataFrame([user_data])

calories = model.predict(df)

print(f"\nPredicted Calories Burned: {calories[0]:.2f}")

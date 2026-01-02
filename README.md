# Calorie Prediction Web Application

A machine learning–based web application that predicts calorie expenditure from biometric and activity-related inputs. The model is trained on a large-scale tabular dataset and deployed as an interactive Streamlit app for real-time inference.

---

## Live Demo
👉 https://calorie-predictor-kv3k8nx6kcfyuzfbzgobbg.streamlit.app/

---

## Project Overview
This project formulates calorie estimation as a **regression problem** using labeled biometric data.  
A CatBoost Regressor was selected for its strong performance on tabular datasets and minimal preprocessing requirements.

The trained model is deployed using Streamlit, allowing users to input physiological parameters and instantly receive calorie predictions.

---

## Tech Stack
- **Language:** Python  
- **Machine Learning:** CatBoost Regressor  
- **Data Processing:** Pandas, NumPy  
- **Web Framework:** Streamlit  
- **Deployment:** Streamlit Cloud  

---

## Features
- Real-time calorie prediction from user inputs  
- Regression model trained on 750,000+ labeled records  
- Input validation for stable predictions  
- Lightweight and responsive web interface  

---

## Model Details
- **Algorithm:** CatBoost Regressor  
- **Problem Type:** Supervised regression  
- **Dataset Size:** 750K+ samples  
- **Why CatBoost:**  
  - Handles non-linear feature interactions effectively  
  - Performs well on tabular data  
  - Requires minimal feature scaling  

---

## Run Locally

```bash
git clone https://github.com/ahmxdkm/calorie-predictor.git
cd calorie-predictor
pip install -r requirements.txt
streamlit run app.py

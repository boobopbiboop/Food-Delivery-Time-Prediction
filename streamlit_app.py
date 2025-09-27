import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import PowerTransformer
import pickle

# Page config
st.set_page_config(
    page_title="Delivery Time Predictor",
    page_icon="🚚",
    layout="wide"
)

# Title
st.title("🚚 Real-Time Delivery Time Predictor")
st.markdown("Predict delivery time based on order characteristics")

# Sidebar for inputs
st.sidebar.header("📝 Order Details")

# Input fields
distance = st.sidebar.slider("Distance (km)", 0.5, 20.0, 5.0, 0.1)
prep_time = st.sidebar.slider("Preparation Time (min)", 5, 60, 15, 1)
courier_exp = st.sidebar.slider("Courier Experience (years)", 0.5, 10.0, 2.0, 0.1)

weather = st.sidebar.selectbox("Weather", ["Clear", "Cloudy", "Rainy", "Stormy"])
traffic = st.sidebar.selectbox("Traffic Level", ["Low", "Medium", "High"])
vehicle = st.sidebar.selectbox("Vehicle Type", ["Motorcycle", "Car", "Bicycle"])
time_of_day = st.sidebar.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])

# Mock model prediction (since we don't have the actual trained model)
def predict_delivery_time(distance, prep_time, courier_exp, weather, traffic, vehicle, time_of_day):
    # Simple prediction logic for demo
    base_time = distance * 2.5 + prep_time * 0.8
    
    # Weather adjustment
    weather_multiplier = {"Clear": 1.0, "Cloudy": 1.1, "Rainy": 1.3, "Stormy": 1.5}
    base_time *= weather_multiplier[weather]
    
    # Traffic adjustment
    traffic_multiplier = {"Low": 1.0, "Medium": 1.2, "High": 1.4}
    base_time *= traffic_multiplier[traffic]
    
    # Experience adjustment
    base_time *= (1 - (courier_exp - 1) * 0.05)
    
    return max(10, base_time)

# Predict button
if st.sidebar.button("🔮 Predict Delivery Time", type="primary"):
    prediction = predict_delivery_time(distance, prep_time, courier_exp, weather, traffic, vehicle, time_of_day)
    
    # Display results
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Predicted Time", f"{prediction:.1f} min")
    
    with col2:
        st.metric("Confidence Range", f"±{prediction*0.1:.1f} min")
    
    with col3:
        status = "On Time" if prediction <= 30 else "Delayed"
        st.metric("Status", status)
    
    # Additional info
    st.success(f"✅ Estimated delivery time: {prediction:.1f} minutes")
    st.info(f"📍 Distance: {distance}km | 👨‍🍳 Prep: {prep_time}min | 🏍️ Experience: {courier_exp}y")

# Instructions
st.markdown("---")
st.markdown("### 📋 How to Use")
st.markdown("1. Adjust the parameters in the sidebar")
st.markdown("2. Click 'Predict Delivery Time' button")
st.markdown("3. View the predicted delivery time and confidence interval")

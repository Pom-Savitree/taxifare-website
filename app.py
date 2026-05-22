import streamlit as st
import pandas as pd
import numpy as np
import requests

'''
# TaxiFareModel
'''

st.markdown('''
Fillin you information
''')


import datetime

d = st.date_input(
    "Date",
    datetime.date(2026, 5, 22))


t = st.time_input('Time', datetime.time(8, 45))

pickup_datetime = f"{d} {t}"

# Location and Passenger inputs
col3, col4 = st.columns(2)
with col3:
    pickup_longitude = st.number_input("Pickup Longitude", value=-73.950655, format="%.6f")
    pickup_latitude = st.number_input("Pickup Latitude", value=40.783282, format="%.6f")

with col4:
    dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.984365, format="%.6f")
    dropoff_latitude = st.number_input("Dropoff Latitude", value=40.769802, format="%.6f")
    
    


passenger_count = st.number_input('Passenger Count')


url = 'https://taxifare.lewagon.ai/predict'


params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": int(passenger_count)
}

if st.button("Get Fare Prediction 🚖"):
    response = requests.get(url, params=params)
            
    # Raise an error if the response status is bad (e.g., 400 or 500)
    response.raise_for_status()
            
    # Parse the JSON response
    prediction_data = response.json()
            
# Extract the fare prediction (adjust the key if your API uses a different name, like 'fare')
    fare = prediction_data['fare']
    
    st.info(f"### Prediction Result: {fare}")
    
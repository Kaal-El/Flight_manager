# app.py

import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Set your AviationStack API Key
API_KEY = "YOUR_API_KEY"

# Streamlit Page Setup
st.set_page_config(page_title="Airline Demand Analyzer", layout="wide")
st.title("✈️ Airline Market Demand Analyzer")

# Input: Departure Airport
dep_iata = st.text_input("Enter Departure Airport IATA Code (e.g., SYD, MEL, BNE):", value="SYD")

# Fetch Flight Data
def get_flight_data(dep_iata='SYD', limit=100):
    url = 'http://api.aviationstack.com/v1/flights'
    params = {
        'access_key': API_KEY,
        'dep_iata': dep_iata,
        'limit': limit
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get('data', [])

# Convert API Data to DataFrame
def convert_to_df(flights):
    data = []
    for flight in flights:
        try:
            data.append({
                'Airline': flight['airline']['name'],
                'Flight Number': flight['flight']['iata'],
                'Departure Airport': flight['departure']['airport'],
                'Arrival Airport': flight['arrival']['airport'],
                'Scheduled Time': flight['departure']['scheduled']
            })
        except:
            continue
    return pd.DataFrame(data)

if st.button("Fetch Data"):
    flights = get_flight_data(dep_iata.upper())
    df = convert_to_df(flights)

    if df.empty:
        st.warning("No flight data found. Please check the IATA code.")
    else:
        # Data Table
        st.subheader("📋 Flight Data Table")
        st.dataframe(df)

        # Charts
        st.subheader("📊 Arrival Airport Distribution")
        fig1, ax1 = plt.subplots()
        sns.countplot(y='Arrival Airport', data=df, order=df['Arrival Airport'].value_counts().index, ax=ax1)
        st.pyplot(fig1)

        st.subheader("🛫 Flights by Airline")
        fig2, ax2 = plt.subplots()
        sns.countplot(y='Airline', data=df, order=df['Airline'].value_counts().index, ax=ax2)
        st.pyplot(fig2)

        # Time Histogram
        st.subheader("⏰ Departure Time Distribution")
        df['Scheduled Time'] = pd.to_datetime(df['Scheduled Time'])
        df['Hour'] = df['Scheduled Time'].dt.hour
        fig3, ax3 = plt.subplots()
        sns.histplot(data=df, x='Hour', bins=24, kde=True, ax=ax3)
        ax3.set_xticks(range(0, 24))
        st.pyplot(fig3)

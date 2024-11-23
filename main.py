import streamlit as st
import requests
from datetime import datetime

# Streamlit UI
st.title("Weather and Time Viewer")
st.write("Enter your [WeatherAPI](https://www.weatherapi.com/) key and location to fetch the weather and time.")

# Input for API key
api_key = st.text_input("Enter your WeatherAPI Key:", type="password")

# Input for location (default: London)
location = st.text_input("Enter location:", "London")

if api_key and location:
    try:
        # Fetch weather data
        weather_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
        response = requests.get(weather_url)
        
        if response.status_code == 200:
            weather_data = response.json()
            
            # Extract weather details
            location_name = weather_data['location']['name']
            region = weather_data['location']['region']
            country = weather_data['location']['country']
            temperature_c = weather_data['current']['temp_c']
            condition = weather_data['current']['condition']['text']
            local_time = weather_data['location']['localtime']
            
            # Display weather
            st.subheader(f"Weather in {location_name}, {region}, {country}")
            st.write(f"**Temperature:** {temperature_c}°C")
            st.write(f"**Condition:** {condition}")
            
            # Display local time
            st.subheader("Local Time")
            st.write(f"The current time in {location_name} is: {local_time}")
        else:
            st.error("Unable to fetch weather data. Please check your API key or location.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Enter your API key and location to get started.")

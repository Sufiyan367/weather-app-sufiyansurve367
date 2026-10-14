import streamlit as st
import requests 
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('WEATHER_API_KEY')



st.set_page_config(page_title="Weather App", page_icon = '🌦️')

st.title("Weather App 🌦️ ")

st.write('Enter a name of city ')

city = st.text_input("Enter the City name")

if st.button('Fetch Weather'):
    # Added '&units=metric' to get temperature directly in Celsius
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    
    # Check if the API request was successful (Status Code 200)
    if response.status_code == 200:
        data = response.json()
        
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_condition = data['weather'][0]['description']
        name = data['name']
        country = data['sys']['country']

        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        col1.metric('Temperature 🌡️', f"{temperature}℃")
        col2.metric("Humidity 💦", f"{humidity}%")
        col3.metric('Wind Speed 🍃', f"{wind_speed} m/s")
        col4.metric("Weather Condition 🌦️", f"{weather_condition.title()}")
    else:
        st.error("City not found or invalid API key. Please check your inputs!")
import streamlit as st
import requests

# --- Title of the App ---
st.title("🌤️ Weather App")
st.write("Get current weather information for any city!")

# --- Input Field ---
city = st.text_input("Enter city name")

# --- When User Submits ---
if city:
    api_key = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        st.subheader(f"Weather in {city.title()}")
        st.write(f"**🌡️ Temperature:** {data['main']['temp']} °C")
        st.write(f"**🌥️ Weather:** {data['weather'][0]['description'].title()}")
        st.write(f"**💧 Humidity:** {data['main']['humidity']}%")
        st.write(f"**🌬️ Wind Speed:** {data['wind']['speed']} m/s")
    else:
        st.error("City not found. Please try again.")

# Optional: Add Footer
st.markdown("---")
st.caption("Made by Areeba with ❤️ using Streamlit")

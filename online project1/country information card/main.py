import streamlit as st
import requests

st.set_page_config(page_title="🌍 Country Info Card", layout="centered")

st.title("🌐 Amazing Country Information Card")
st.subheader("Get details about any country in the world!")

country = st.text_input("Enter a country name", "Pakistan")

if st.button("Show Info"):
    url = f"https://restcountries.com/v3.1/name/{country}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()[0]

        name = data['name']['common']
        capital = data['capital'][0]
        population = f"{data['population']:,}"
        region = data['region']
        subregion = data['subregion']
        area = f"{data['area']:,} km²"
        flag = data['flags']['png']
        currencies = ', '.join([val['name'] for val in data['currencies'].values()])
        languages = ', '.join(data['languages'].values())

        st.image(flag, width=200)
        st.markdown(f"### 📍 Country: {name}")
        st.markdown(f"**🏙 Capital:** {capital}")
        st.markdown(f"**👥 Population:** {population}")
        st.markdown(f"**🌍 Region:** {region}")
        st.markdown(f"**🗺 Subregion:** {subregion}")
        st.markdown(f"**📏 Area:** {area}")
        st.markdown(f"**💰 Currencies:** {currencies}")
        st.markdown(f"**🗣 Languages:** {languages}")

    except:
        st.error("⚠️ Country not found. Please check the name and try again.")

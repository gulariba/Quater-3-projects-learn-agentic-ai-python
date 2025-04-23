# portfolio_app.py

import streamlit as st

st.set_page_config(page_title="Areeba's Portfolio", page_icon="🌸", layout="centered")

# Title
st.title("👩‍💻 Areeba's Portfolio")
st.markdown("Welcome to my Streamlit-powered web portfolio!")

# Sidebar
st.sidebar.title("📌 Navigation")
nav = st.sidebar.radio("Go to:", ["Home", "About Me", "Skills", "Contact"])

# Home Section
if nav == "Home":
    st.header("🌟 Hello, I'm Areeba!")
    st.write("I'm learning Python and building awesome Streamlit apps!")
    st.image("https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif", width=150)

# About Me Section
elif nav == "About Me":
    st.header("👩‍🎓 About Me")
    st.write("""
    I am currently learning programming and working on Python projects like Mad Libs, Hangman, BMI Calculator, and more.
    
    I enjoy creating fun and functional apps using Python and Streamlit.
    """)

# Skills Section
elif nav == "Skills":
    st.header("🧠 Skills")
    st.markdown("""
    - Python Basics
    - Streamlit Web Apps
    - Google Colab Projects
    - GitHub Portfolio Management
    - Learning HTML, CSS, JavaScript & TypeScript
    """)

# Contact Section
elif nav == "Contact":
    st.header("📞 Contact Me")
    st.write("📧 Email: areeba@example.com")
    st.write("🌐 GitHub: [Areeba's GitHub](https://github.com/gulariba)")
    st.write("💼 LinkedIn: [Areeba's LinkedIn](https://www.linkedin.com/in/areeba-ahmed-khan-b8485229b/overlay/about-this-profile/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3BAcSJhYx6TWWzcQ7hmeAPHQ%3D%3D)")

    st.markdown("**Let’s build cool stuff together! 🤝**")

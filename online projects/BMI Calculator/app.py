# bmi_app.py

import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="🧮", layout="centered")

st.title("💪 BMI Calculator")
st.markdown("### Calculate your Body Mass Index (BMI)")

# Input from user
weight = st.number_input("Enter your weight (in kg):", min_value=1.0, step=0.5)
height = st.number_input("Enter your height (in meters):", min_value=0.5, step=0.01)

if st.button("Calculate BMI"):
    if weight and height:
        bmi = round(weight / (height ** 2), 2)

        st.success(f"Your BMI is: **{bmi}**")

        # Result interpretation
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.info("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Please enter valid values for both fields.")

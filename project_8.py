# Create a Python Streamlit BMI Calculator Web App

import streamlit as st

# Title of the app
st.title("BMI Calculator")

# Input fields for weight and height
height = st.number_input("Enter your height in meters (e.g., 1.75):", min_value=0.0, format="%.2f")
weight = st.number_input("Enter your weight in kilograms (e.g., 70):", min_value=0.0, format="%.2f")

# Calculator BMI 
if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.success(f"your BMI is: {bmi: .2f}")

        # BMI Category
        if bmi < 18.5:
            st.info("You are underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight") 
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight")
        else:
            st.error("You are obese")    
    else:
        st.error("please enter valid height and weight.")           
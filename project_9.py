# Python Website With Streamlit 

import streamlit as st

# Title and header 
st.title("Wellcome to My Website")
st.header("Explore Amazing Features")

# Adding Some Text
st.write("This is a simple web application built with Streamlit.")

# Adding a button
if st.button("Click Me!"):
    st.write("You clicked the button!")

# Adding User Input
name = st.text_input("What is your name?")
if st.button("streamlit"):
    st.write(f"Hello, {name}! Welcome to my Website.")    
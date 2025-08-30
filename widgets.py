
import streamlit as st

st.title("Streamlit text Input")
name=st.text_input("Enter the Name")

age=st.slider("Select your age",0,100,25)

st.write(f'Your age is {age}.')  

if name:
    st.write(f'Hello, {name}! Welcome to Streamlit.')   

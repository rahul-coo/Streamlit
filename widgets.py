
import streamlit as st

import pandas as pd

st.title("Streamlit text Input")
name=st.text_input("Enter the Name")

age=st.slider("Select your age",0,100,25)

st.write(f'Your age is {age}.')  

option=["Python", "Java", "C++","JavaScript"]

selected_option = st.selectbox("Choose a programming language", option)
st.write(f'You selected: {selected_option}')

if name:
    st.write(f'Hello, {name}! Welcome to Streamlit.')   


data={
    "Name":["John","Jane","Alice","Bob"],
    "Age":[28,34,29,42],
    "City":["New York","San Francisco","Los Angeles","Chicago"]
}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file=st.file_uploader("Choose a csv file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
import streamlit as st
import pandas as pd
import numpy as np  

# Title of the application
st.title("Hello Streamlit")

#Display a simpleTest

st.write("This is my first Streamlit application")

# Create a DataFrame
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
})

# Display the DataFrame
st.write("Here's a simple DataFrame:")
st.write(df)

##create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

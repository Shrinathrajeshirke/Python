import streamlit as st
import pandas as pd
import numpy as np

## title of the application
st.title("Hello Everyone!")


## display simple text
st.write("This is for you")

## create a datafram
df = pd.DataFrame({
    'column 1': [1,2,3,4],
    'column 2': [10,20,30,40]
})

## display the dataframe
st.write('Here is the dataframe')
st.write(df)

## line chart
data = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
st.line_chart(data)
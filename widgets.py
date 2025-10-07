import streamlit as st
import pandas as pd

st.title("Streamlit Text input")
name = st.text_input("Enter your name: ")

age = st.slider("select your age:", 0,100,25)

if name:
    st.write(f"Hello, {name}")

options = ['python', 'R', 'C','C++']
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"selected {choice}")

df = pd.DataFrame({
    "Name": ["A","B","C","D"],
    "Age":[11,21,22,12],
    "City":['X','Y','Z','W']
})

df.to_csv("data.csv")
st.write(df)

upload_file = st.file_uploader("choose a csv file", type="csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)
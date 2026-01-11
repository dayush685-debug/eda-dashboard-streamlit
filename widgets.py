import streamlit as st
import pandas as pd

st.title("Streamlit text Input")

name=st.text_input("Enter your name:")

age=st.slider("select your age:",0,100,25)

st.write(f"Your age is {age}")

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favourite language:", options)
st.write(f"You Selected {choice}")

if name:
    st.write(f"Hello, {name}")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 29, 30],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
} 

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file=st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
    
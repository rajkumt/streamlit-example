import streamlit as st
import pandas

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
st.title("my parents healthy dinner")
st.header('Breakfast Menu')
st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

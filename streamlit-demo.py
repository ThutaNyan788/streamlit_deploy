import streamlit as st


number = st.number_input("Insert a number")
st.write("The current number is ", number)
st.write(7* number)
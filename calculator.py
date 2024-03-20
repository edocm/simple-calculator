import streamlit as st

st.title("Simple Calculator")

number_one = st.number_input("Enter the first number")
operator = st.selectbox("Select operator", ["+", "-"])
number_two = st.number_input("Enter the second number")


if st.button("calculate"):
    result = None
    if operator == "+":
        result = number_one + number_two
    elif operator == "-":
        result = number_one - number_two

    st.write(f"Result of calculation: {result}")
import streamlit as st
import pandas as pd

st.title("Golden Collection")
st.header("Welcome to HomePage")
st.subheader("This is a website to showcase different Ornaments")
st.write("")

# --- Display Items in Columns ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Bangle")
    st.image("artifacts/Bangle.webp")

with col2:
    st.subheader("Ring")
    st.image("artifacts/Ring.webp")

with col3:
    st.subheader("Earring")
    st.image("artifacts/Earring.webp")

# --- Selectbox ---
selection = st.selectbox(
    "Pick one",
    ["None", "Bangle", "Ring", "Earring"],
    index=0
)

# --- Budget Slider ---
price = st.slider(
    "Enter Your Budget",
    min_value=100000,
    max_value=10000000,
    step=1000000,
    value=500000
)
st.write(f"Your Selected Budget is: ₹{price}")

# --- Input Fields ---
name = st.text_input("Enter Your Name")
contact = st.text_input("Enter Your Contact Number")
email = st.text_input("Enter Your Email ID")
address = st.text_area("Enter Your Full Address", placeholder="Mumbai")

# --- Submit Button ---
if st.button("Submit"):
    st.switch_page("pages/form_feedback.py")

import streamlit as st
import pandas as pd

st.title("Golden collection")
st.header("Welcome to HomePage")
st.subheader("This is a website to showcase different Ornaments")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

#with st.container():
#    st.subheader("Bangle")
#    st.image("artifacts\Bangle.webp")
#    st.subheader("Ring")
#    st.image("artifacts\Ring.webp")
#    st.subheader("Earring")
#    st.image("artifacts\Earring.webp")

col1, col2, col3 = st.columns([2, 2, 2],gap="medium",vertical_alignment='center',border=True)
col1.subheader("Bangle")
col1.image("artifacts\Bangle.webp")
col2.subheader("Ring")
col2.image("artifacts\Ring.webp")
col3.subheader("Earring")
col3.image("artifacts\Earring.webp")  
st.selectbox("Pick one", ["None","Bangle", "Ring","Earring"],placeholder="None")

price = st.slider("Enter Your Budget", min_value=100000, max_value=10000000,step=1000000,value=500000)
st.write(f"Your Selected Budget is :- {price}")
st.text_input("Enter Your name")
st.text_input("Enter your COntact no")
st.text_input("Enter your Email Id")
st.text_area("Enter your full address",placeholder="Mumbai")
if st.button("Submit"):
    st.switch_page('pages/form_feedback.py')
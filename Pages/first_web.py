import streamlit as st

st.header("Burger King 🍔- Thane Location")
st.subheader("Hello, This is my website")
a = st.slider("Pick a value", 10, 100,50,1)
st.write(f"The selected value is {a}")
st.selectbox('Select Item of your choice',options=['Burger','French Fries','Pizza','Moburg','Coke'])
st.image("image165449.jpg","Welcome to our fast food chain")
st.feedback(options="stars")

st.checkbox("I agree")
if st.button('Submit'):
    st.switch_page("pages\web_app.py") 

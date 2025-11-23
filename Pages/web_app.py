import streamlit as st
import pandas as pd
import numpy as np
import time

# Title
st.title("🌟 Simple Interactive Streamlit App")

# Sidebar for input
st.sidebar.header("User Input")
name = st.sidebar.text_input("Enter your name:", "Arnav")
fav_number = st.sidebar.slider("Select your favorite number:", 1, 100, 50)
color = st.sidebar.color_picker("Pick your favorite color", "#00f900")

# Main output
st.write(f"👋 Hello, **{name}**!")
st.write(f"🎨 Your favorite color is: `{color}` and your number is: **{fav_number}**")

# Dynamic chart section
st.subheader("📈 Live Updating Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
placeholder = st.empty()

for i in range(20):
    new_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["A", "B", "C"]
    )
    placeholder.line_chart(new_data)
    time.sleep(0.1)

# Expander (FAQ or Info)
with st.expander("ℹ️ What does this app do?"):
    st.write("""
        This app is a quick demo of:
        - Text input
        - Color picker
        - Slider
        - Live charts
        - Expander for extra info
    """)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")

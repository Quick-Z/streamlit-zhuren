import streamlit as st

height = st.slider("粉丝量", value=170, min_value=100, max_value=230, step=1)

st.write(f"你的粉丝量是{height}")
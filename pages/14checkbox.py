import streamlit as st

checked = st.checkbox("同意以上条款")
if checked:
  st.write("同意")
else:
  st.write("不同意")
import streamlit as st

a = 11

if a % 2 == 0:
  st.write(f'{a}是偶数')
else:
  st.write(f'{a}是奇数')
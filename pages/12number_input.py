import streamlit as st

age1 = st.number_input("年龄：")

st.write(f'你输入的年龄是{age1}岁')

age2 = st.number_input("年龄：", value=20, min_value=0, max_value=199, step=5)
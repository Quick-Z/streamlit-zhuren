import streamlit as st

# 普通输入框
name = st.text_input("请输入你的名字：")

if name:
  st.write(f'你好，{name}')

# 密码输入框
pwd = st.text_input("密码是多少？", type="password")
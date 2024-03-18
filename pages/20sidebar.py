import streamlit as st

res = ''

with st.sidebar:
  res = st.text_input('搜索：')


st.write(f'页面内容，看看搜索了啥：{res}')
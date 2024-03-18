import streamlit as st

# 多列布局（均等分成3列）
# col1, col2, col3 = st.columns(3)

# 多列布局（不同比例）
col1, col2, col3 = st.columns([1, 2, 3])

with col1:
  st.write('第1列')

with col2:
  st.write('第2列')

with col3:
  st.write('第3列')
import streamlit as st

res = st.radio(
  "给我的文章点个赞吧",
  ["点赞", "点多几篇"],
  index=1
)
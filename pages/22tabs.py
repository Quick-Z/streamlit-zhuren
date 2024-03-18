import streamlit as st

# 选项卡
tab1, tab2, tab3 = st.tabs(['点赞', '关注', '收藏'])

with tab1:
  st.write('快点赞吧')
with tab2:
  st.write('关注一下啦')
with tab3:
  st.write('收藏就是学会了')
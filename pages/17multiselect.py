import streamlit as st


article_list = st.multiselect("你喜欢哪篇文章？", 
  [
    "《『Python爬虫』极简入门》",
    "《『SD』零代码AI绘画：光影字》",
    "《『SD』Stable Diffusion WebUI 安装插件（以汉化为例）》",
    "《NumPy入个门吧》"
  ]
)

for article in article_list:
  st.write(f"你喜欢{article}")
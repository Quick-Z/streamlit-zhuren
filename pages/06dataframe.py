import streamlit as st
import pandas as pd

st.write('dict')

# 字典
st.dataframe(
  data={
    "姓名": ['雷猴', '鲨鱼辣椒'],
    "年龄": [18, 22]
  }
)

# DataFrame
df = pd.DataFrame(
  {
    "姓名": ["雷猴", "鲨鱼辣椒"],
    "年龄": [18, 22],
  }
)

st.write('DataFrame')

st.dataframe(df)
import streamlit as st
import time
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

st.title('streamlit入門')

st.write('Display Image')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

st.write('Done!')

text = st.sidebar.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', text, 'です。'


condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 0)
'コンディション：', condition

result = st.button('Click here')

if result:
    st.sidebar.write(":smile:")

left_column, right_column = st.columns(2)
left_column.write('ここは左カラム')
right_column.write('ここは右カラム')

expander_1 = st.expander('問い合わせ1')
response1 = expander_1.text_input('問い合わせ1の回答')

if response1:
    '以下の内容でお問い合わせ:'
    response1



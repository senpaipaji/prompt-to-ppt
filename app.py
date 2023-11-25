import streamlit as st
import numpy as np
import pandas as pd


st.title("PPT Generator!")
# Form -
with st.form("my_form"):
    st.subheader('Enter Your Topic - ')
    st.session_state.topic = st.text_input('')
    submit = st.form_submit_button()
# On Submit -
if submit:
    st.write('Your Topic is : ' , st.session_state)
    with open('MyText.txt','rb') as f:
        f_data = f.read()
    st.download_button(
        data=f_data,
        label = "Download PPT",
        file_name = "mytext.txt"
    )
import streamlit as st
import numpy as np
import pandas as pd
from .generate import *
import time

st.title("PPT Generator!")
# Form -
with st.form("my_form"):
    st.subheader('Enter Your Topic - ')
    st.session_state.topic = st.text_input('')
    submit = st.form_submit_button()
# On Submit -
if submit:
    st.write('Your Topic is : ' , st.session_state.topic)
    st.write('Please be patient')
    try:
        topic,completion_status = st.session_state,0
        topics = CreateTopics(topic)
        completion_status = 1
        presentation_data = CreateData(topics[2])
        presentation_data = TransformData(presentation_data)
    except:
        st.write('Server busy at the moment please try again!')
        time.sleep(3)
        st.rerun()
    try:
        CreatePPT(topic,presentation_data)
    except:
        st.write('Unable to construct PPT please try again!')
        time.sleep(3)
        st.rerun()
   
    with open(f'{topic}.pptx','rb') as f:
        f_data = f.read()
    st.download_button(
        data=f_data,
        label = "Download PPT",
        file_name = f"{topic}.pptx"
    )
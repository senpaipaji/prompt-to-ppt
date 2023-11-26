import streamlit as st
import numpy as np
import pandas as pd
from generate import *
import time

st.title("PPT Generator!")
# Form -
with st.form("my_form"):
    st.subheader('Enter Your Topic - ')
    st.session_state.topic = st.text_input('topic')
    submit = st.form_submit_button()
# On Submit -
if submit:
    st.write('Your Topic is : ' , st.session_state.topic)
    progress_bar = st.progress(0, text="Processing your request...")
    time.sleep(2)
    try:
        topic,completion_status = st.session_state.topic,0
        progress_bar.progress(20, text="Creating topics...")
        topics = CreateTopics(topic)
        st.write(topics)
        progress_bar.progress(40, text="Generating data...")
        presentation_data = CreateData(topics[:10])
        progress_bar.progress(60, text="Transforming data...")
        presentation_data = TransformData(presentation_data)
    except:
        st.write('Server busy at the moment please try again!')
        time.sleep(3)
        st.rerun()
    try:
        progress_bar.progress(80, text="Making your PPT...")
        CreatePPT(topic,presentation_data)
        completion_status = 4
    except:
        st.write('Unable to construct PPT please try again!')
        time.sleep(3)
        st.rerun()
   
    with open(f'{topic}.pptx','rb') as f:
        f_data = f.read()
    progress_bar.progress(100, text="Completed...")
    
    st.download_button(
        data=f_data,
        label = "Download PPT",
        file_name = f"{topic}.pptx"
    )
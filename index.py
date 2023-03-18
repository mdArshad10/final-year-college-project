import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(layout='wide',page_title='Home | Book Recommendation')


with st.spinner('Wait for it...'):
    st.title("Book Recommendation")

    tab1, tab2, tab3 = st.tabs(["Home", "Top-50 Books", "Recommended Books"])

    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


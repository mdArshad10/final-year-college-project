import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image


st.set_page_config(layout='wide',page_title='Home | Book Recommendation')


with st.spinner('Wait for it...'):
    st.title("Book Recommendation")

    tab1, tab2, tab3 = st.tabs(["Home", "Top-50 Books", "Recommended Books"])

    #! top - 50 Table
    with tab2:
        i = 0
        while(i<50):
            col1, col2, col3, col4 = st.columns(4)
            with col1: 
                # book - image 
                st.image("http://images.amazon.com/images/P/0439136350.01.LZZZZZZZ.jpg", width=200)
                # Book Title
                st.text(i)
                i=i+1
                st.text('Harry Potter and the Prisoner of Azkaban') 
                # Book Author
                st.text('J. K. Rowling')
                st.text("Avg. rating: 5.852804")
                
            with col2: 
                # book - image 
                st.image("http://images.amazon.com/images/P/0439136350.01.LZZZZZZZ.jpg", width=200)
                # Book Title
                st.text(i)
                i=i+1
                st.text('Harry Potter and the Prisoner of Azkaban') 
                # Book Author
                st.text('J. K. Rowling')
                st.text("Avg. rating: 5.852804")
            
            with col3: 
                # book - image 
                st.image("http://images.amazon.com/images/P/0439136350.01.LZZZZZZZ.jpg", width=200)
                # Book Title
                st.text(i)
                i=i+1
                st.text( 'Harry Potter and the Prisoner of Azkaban') 
                # Book Author
                st.text('J. K. Rowling')
                st.text("Avg. rating: 5.852804")

            with col4: 
                # book - image 
                st.image("http://images.amazon.com/images/P/0439136350.01.LZZZZZZZ.jpg", width=200)
                # Book Title
                st.text(i)
                i=i+1
                st.text('Harry Potter and the Prisoner of Azkaban') 
                # Book Author
                st.text('J. K. Rowling')
                # Avg Rating
                st.text("Avg. rating: 5.852804")
            





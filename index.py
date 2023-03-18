import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image
import time


st.set_page_config(layout='wide',page_title='Home | Book Recommendation')

st.title("Book Recommendation")

data_df = pickle.load(open("popular_movie.pkl","rb"))
book_name = list(data_df["Book-Title"].values)
book_url = list(data_df["Image-URL-M"].values)
book_author = list(data_df["Book-Author"].values)
book_rating = list(data_df["avg-rating"].values)

tab1, tab2, tab3 = st.tabs(["Home", "Top-50 Books", "Recommended Books"])

#! top - 50 Table
with tab2:
    i = 0
    while(i<50):
        col1, col2, col3, col4 = st.columns(4)
        with col1: 
            # book - image 
            st.image(book_url[i], width=200)
            st.text(book_name[i]) 
            # Book Title
            # Book Author
            st.text(book_author[i])
            st.write("Avg. rating: ", book_rating[i])
            i=i+1
            
        with col2: 
            # book - image 
            st.image(book_url[i], width=200)
            # Book Title
            st.text(book_name[i]) 

            # Book Author
            st.text(book_author[i])
            st.write("Avg. rating: ", book_rating[i])
            i=i+1
        
        with col3: 
            # book - image 
            st.image(book_url[i], width=200)
            st.text( book_name[i]) 
            # Book Title
            # Book Author
            st.text(book_author[i])
            st.write("Avg. rating: ", book_rating[i])
            i=i+1

        with col4: 
            # book - image 
            st.image(book_url[i], width=200)
            # Book Title
            st.text(book_name[i]) 
            # Book Author
            st.text(book_author[i])
            # Avg Rating
            st.write("Avg. rating: ", book_rating[i])
            i=i+1
            
with tab3:

    title = st.text_input('Movie title', placeholder="eg. A Walk to Remember")

    if st.button('Recommended Book'):
        if(title):
            with st.spinner('Wait for it...'):
                time.sleep(1)
                col1, col2, col3 = st.columns(3)
                with col1: 
                    # book - image 
                    st.image("http://images.amazon.com/images/P/0439136350.01.LZZZZZZZ.jpg", width=200)
                    # Book Title
                    st.text('Harry Potter and the Prisoner of Azkaban') 
                    # Book Author
                    st.text('J. K. Rowling')
                    st.text("Avg. rating: 5.852804")
                    
                with col2: 
                    # book - image 
                    st.image("http://images.amazon.com/images/P/0439136350.01.LZZZZZZZ.jpg", width=200)
                    # Book Title
                    st.text('Harry Potter and the Prisoner of Azkaban') 
                    # Book Author
                    st.text('J. K. Rowling')
                    st.text("Avg. rating: 5.852804")
                
                with col3: 
                    # book - image 
                    st.image("http://images.amazon.com/images/P/0439136350.01.LZZZZZZZ.jpg", width=200)
                    # Book Title
                    st.text( 'Harry Potter and the Prisoner of Azkaban') 
                    # Book Author
                    st.text('J. K. Rowling')
                    st.text("Avg. rating: 5.852804")

                col1, col2 = st.columns(2)
                with col1: 
                    # book - image 
                    st.image("http://images.amazon.com/images/P/0439136350.01.LZZZZZZZ.jpg", width=200)
                    # Book Title
                    st.text('Harry Potter and the Prisoner of Azkaban') 
                    # Book Author
                    st.text('J. K. Rowling')
                    st.text("Avg. rating: 5.852804")
                    
                with col2: 
                    # book - image 
                    st.image("http://images.amazon.com/images/P/0439136350.01.LZZZZZZZ.jpg", width=200)
                    # Book Title
                    st.text('Harry Potter and the Prisoner of Azkaban') 
                    # Book Author
                    st.text('J. K. Rowling')
                    st.text("Avg. rating: 5.852804")

        else:
            st.error('Enter the moive title', icon="🚨")
            



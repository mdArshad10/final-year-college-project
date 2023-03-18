import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import time


st.set_page_config(layout='wide',page_title='Home | Book Recommendation')

st.title("Book Recommendation")

data_df = pickle.load(open("popular_movie.pkl","rb"))
pt_df = pickle.load(open("pt_df.pkl","rb"))
books = pickle.load(open("books.pkl","rb"))

similarity_scores = cosine_similarity(pt_df)

book_name = list(data_df["Book-Title"].values)
book_url = list(data_df["Image-URL-L"].values)
book_author = list(data_df["Book-Author"].values)
book_rating = list(data_df["avg-rating"].values)

def recommend(book_name):
    # index fetch
    index = np.where(pt_df.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key= lambda x:x[1], reverse=True)[1:6]
    
    data = []
    for i in similar_items:
      item = []
      temp_df = books[books['Book-Title'] == pt_df.index[i[0]]]
      item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
      item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
      item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

      data.append(item)
    
    return data



tab1, tab2, tab3 = st.tabs(["Home", "Top-50 Books", "Recommended Books"])

#! top - 50 Table
with tab2:
    i = 0
    while(i<48):
        col1, col2, col3, col4 = st.columns(4)
        with col1: 
            # book - image 
            st.image(book_url[i], width=200)
            # Book Title
            st.text(book_name[i]) 
            # Book Author
            st.text(book_author[i])
            st.write("Avg. rating: ", book_rating[i])
            i=i+1
            
        with col2: 
            st.image(book_url[i], width=200)
            st.text(book_name[i]) 
            st.text(book_author[i])
            st.write("Avg. rating: ", book_rating[i])
            i=i+1
        
        with col3: 
            st.image(book_url[i], width=200)
            st.text( book_name[i]) 
            st.text(book_author[i])
            st.write("Avg. rating: ", book_rating[i])
            i=i+1

        with col4: 
            st.image(book_url[i], width=200)
            st.text(book_name[i]) 
            st.text(book_author[i])
            st.write("Avg. rating: ", book_rating[i])
            i=i+1
            
with tab3:

    title = st.selectbox(
    "Type or select a Book Title from the dropdown",book_name)

    if st.button('Recommended Book'):
        if(title):
            recommended_books = recommend(title)
            with st.spinner('Wait for it...'):
                time.sleep(1)
                col1, col2, col3 = st.columns(3)
                with col1: 
                    # book - image 
                    st.image(recommended_books[0][2], width=200)
                    # Book Title
                    st.text(recommended_books[0][0]) 
                    # Book Author
                    st.text(recommended_books[0][1])
                    
                    
                with col2: 
                    # book - image 
                    st.image(recommended_books[1][2], width=200)
                    # Book Title
                    st.text(recommended_books[1][0]) 
                    # Book Author
                    st.text(recommended_books[1][1])
                    
                
                with col3: 
                    # book - image 
                    st.image(recommended_books[2][2], width=200)
                    # Book Title
                    st.text( recommended_books[2][0]) 
                    # Book Author
                    st.text(recommended_books[2][1])
                    

                col1, col2 = st.columns(2)
                with col1: 
                    # book - image 
                    st.image(recommended_books[3][2], width=200)
                    # Book Title
                    st.text(recommended_books[3][0]) 
                    # Book Author
                    st.text(recommended_books[3][1])
                    
                    
                with col2: 
                    # book - image 
                    st.image(recommended_books[4][2], width=200)
                    # Book Title
                    st.text(recommended_books[4][0]) 
                    # Book Author
                    st.text(recommended_books[4][1])
                    

        else:
            st.error('Enter the moive title', icon="🚨")
            



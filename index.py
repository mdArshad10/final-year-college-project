import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import time


st.set_page_config(layout='wide',page_title='Home | Book Recommendation')

st.title("Book Recommendation v1.0.0")

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
    index2 = np.where(pt_df.index == book_name)

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

with tab1:
    # Define your introduction text
    intro = """
    ## Welcome to the Book Recommendation System!

    Do you struggle to find new books to read? Our book recommendation system is here to help! Using a sophisticated algorithm based on your reading history and preferences, we can recommend books that we think you'll love.

    To get started, simply enter the name of a book you've enjoyed in the past, and our system will generate a list of similar books that we think you'll enjoy. You can also browse our curated lists of books by genre, author, and more.

    So what are you waiting for? Start exploring our book recommendation system today and discover your next favorite read!
    """

    # Display the introduction text using Streamlit
    st.markdown(intro)

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

    # it return any things
    bk_title = st.text_input('Book title', placeholder="eg. To Kill a Mockingbird")
    if st.button('Recommended Book'):
        if(bk_title):
            recommended_books = recommend(bk_title)
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
            



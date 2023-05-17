import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import time


st.set_page_config(layout='wide',page_title='Home | Book Recommendation')

st.title("Book Recommendation v1.0.0")

data_df = pickle.load(open("popular.pkl","rb"))
pt_df = pickle.load(open("pt_df.pkl","rb"))
books = pickle.load(open("books.pkl","rb"))

similarity_scores = cosine_similarity(pt_df)

book_name = list(data_df["Book-Title"].values)
book_url = list(data_df["Image-URL-S"].values)
book_author = list(data_df["Book-Author"].values)
book_rating = list(data_df["avg-rating"].values)

isError = False
# book recommendation for new book
def recommendBook(book_name):
    # index fetch
    # print(np.where(pt.index == book_name)[0]==[])
    if np.where(pt_df.index == book_name)[0]:
      # if book recommendation is present
      index = np.where(pt_df.index == book_name)[0][0]
      similar_items = sorted(list(enumerate(similarity_scores[index])), key= lambda x:x[1], reverse=True)[1:6]  
      data = []
      for i in similar_items:
        # print(pt.index[i[0]])
        item = []
        temp_df = books[books['Book-Title'] == pt_df.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)
      
      return data
    else:
      # if book is empty then it is not return 
      # top 5 books
      global isError 
      isError = True
      st.text("the book is not found")
      return data_df.sample(5)


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
        recommended_books = recommendBook(bk_title)
        if(bk_title and (isError == False)):
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
                    
        elif isError != False:
            with st.spinner('Wait for it...'):
                time.sleep(1)
                col1, col2, col3 = st.columns(3)
                with col1: 
                    # book - image 
                    st.image(recommended_books["Image-URL-S"].values[0], width=200)
                    # Book Title
                    st.text(recommended_books["Book-Title"].values[0]) 
                    # Book Author
                    st.text(recommended_books["Book-Author"].values[0])
                     
                with col2: 
                   # book - image 
                    st.image(recommended_books["Image-URL-S"].values[1], width=200)
                    # Book Title
                    st.text(recommended_books["Book-Title"].values[1]) 
                    # Book Author
                    st.text(recommended_books["Book-Author"].values[1])
                    
                
                with col3: 
                   # book - image 
                    st.image(recommended_books["Image-URL-S"].values[2], width=200)
                    # Book Title
                    st.text(recommended_books["Book-Title"].values[2]) 
                    # Book Author
                    st.text(recommended_books["Book-Author"].values[2])

                col1, col2 = st.columns(2)
                with col1: 
                    # book - image 
                    st.image(recommended_books["Image-URL-S"].values[3], width=200)
                    # Book Title
                    st.text(recommended_books["Book-Title"].values[3]) 
                    # Book Author
                    st.text(recommended_books["Book-Author"].values[3])
                    
                    
                with col2: 
                    # book - image 
                    # book - image 
                    st.image(recommended_books["Image-URL-S"].values[4], width=200)
                    # Book Title
                    st.text(recommended_books["Book-Title"].values[4]) 
                    # Book Author
                    st.text(recommended_books["Book-Author"].values[4])


        else:
            st.error('Enter the moive title', icon="🚨")
        
        



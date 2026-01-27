import pandas as pd
import streamlit as st
import plotly as pt

book_df=pd.read.csv('bestsellers_with_categories_2022_03_27.csv')

st.title('bestselling books analysis')
st.write('this is a streamlit app')

st.sdiebar.header('add new book data')
with st.sidebar.form('book_form'):
    new_name=st.text_input('book name')
    new_author=st.text_input('author')
    new_user_rating=st.slider('user rating', 0.0, 5.0 ,0.1)
    new_reviews=st.number_input('reviews',min_value=0,step=1)
    new_price=st.number_input('price',min_value=0,step=1)
    new_year=st.number_input('year',min_value=2009,max_value=2026)
    new_genre=st.selecbox('genre',book_df['genre'].unique())
    submit_button=st.form_submit_butotn(label='add book')


if submit_button:
    new_data={
        'name':new_name,
        'author': new_author,
        'user rating': new_user_rating,
        'reviews': new_reviews,
        'price': new_price,
        'year': new_year,
        'genre': new_genre

    }

    books_df=pd.concat(([pd.DataFrame(new_data,index=[0], books_df]), ingore_index=True)
    books_df.to_csv('bestsellers_with_categories_202_03_27.csv',index=False)
    st.sidebar.success('new book added')


st.sidebar.header('filter options')
selected_author=st.sidebar.selectbox('selected author',['all']+list(books_df['author'].unique()))
selected_year=st.sidebar.selectbox('select year',['all']+list(books_df['year'].unique()))
selected_genre=st.sidebar.selectbox('selected genre',['all']+list(books_df['year'],unique()))
min_rating=st.sidebar.slider('maximum user rating',0.0,5.0,0.1)
max_price=st.sidebar.slider('max price',0,books_df['price'].max(),books_df['price'].max())





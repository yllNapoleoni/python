import pandas as pd
import streamlit as st
import plotly as pt

from module19.app import total_books, unique_titles, average_rating, average_price, top_titles

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

filtered_books_df =books_df.copy()

if selected_author !='all':
    filtered_books_df=filtered_books_df[filtered_books_df['author']==selected_author]
if selected_author != 'all':
    filtered_books_df = filtered_books_df[filtered_books_df['year'] == selected_year]
if selected_author != 'all':
    filtered_books_df = filtered_books_df[filtered_books_df['genre'] == selected_genre]

filtered_books_df=filtered_books_df[
    (filtered_books_df['user rating']>=min_rating)&(filtered_books_df['price']<= max_price)
]


st.subheader('summary statistics')
total_books=filtered_books_df.shape[0]
unique_titles=filtered_books_df['name'].nunique()
average_rating=filtered_books_df['user rating'].mean()
average_price=filtered_books_df['price'].mean()


col1,col2,col3,col4=st.columns(4)
col1.mentric('total books',total_books)
col2.mentric('unique titles',unique_titles)
col3.mentric('average rating',average_rating)
col4.mentric('average price',average_price)

st.subheader('dataset preview')
st.write(filtered_books_df.head())


col1,col2=st.columns(2)

with col1:
    st.subheader('top 10 selling books')
    top_titles=filtered_books_df['name'].value_counts().head(10)
    st.bar_chart(top_titles)
with col2:
    st.subheader('top 10 authors')
    top_authors=filtered_books_df['authors'].value_counts().head(10)
    st.bar_chart(top_authors)






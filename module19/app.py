import pandas as pd
import streamlit as st
from numpy.ma.extras import unique

iport plotly.express as px

st.header('displaying dataframes')

df= pd.DataFrame({
    'name':['vlera','andi','darisi'],
    'age':[24,25,26],
    'city':['harilaq','fushkosove','prishtine']
})

st.write(df)

st.title('bestselling books analysis')
st.write('this app analyzes the amazon top selling books from 2009 to 2022')

book_df=pd.read_csv('module19/bestsellers_with_categories_2022_02_27.csv')

st.subheader('sumamry statistics')
total_books=books_df.shape[0]
unique_titles=books_df['name'].nunique()
average_rating=books_df['user rating'].mean()
average_price=books_df['price'].mean()

col1,col2,col3,col4=st.columns(4)
col1.metric('total books',total_books)
col2.metric('unique titles',unique_titles)
col3.metric('average rating',f'{average_rating:.2f}')
col4.metric('average price',f"${average_price:.2f}")

st.subheader('dataset preview')
st.write(books_df.head())

col1,col2=st.columns(2)

with col1:
    st.subheader('top 10 book titles')
    top_titles=books_df['name'].value_counts().head(10)
    st.bar_chart(top_titles)

    with col2:
        st.subheader('top 10 authors')
        authors = books_df['author'].value_counts().head(10)
        st.bar_chart(top_authors)


st.subheader('number of fiction cs non-fiction books over the years')
size=book_df.groupby(['year','genre']).size().reset_index(name='counts')
fig=px.bar(size,x='year',y='counts',color='genre',title='nmber of fiction vs non-fiction books from 2009-2022', color_discrete_sequence=px.sequential.Plasma,barmode='group')

st.plotly_chart(fig)



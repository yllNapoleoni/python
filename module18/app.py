import streamlit as st

col1,col2,col3,col4,col5=st.columns(5,gap='small',vertical_alignment='center')

with col1:
    st.header('column 1')
    st.write("content for column 1")

with col2:
    st.header('column 2')
    st.write("content for column 2")

with col3:
    st.header('column 3')
    st.write("content for column 3")

with col4:
    st.header('column 4')
    st.write("content for column 4")

with col5:
    st.header('column 5')
    st.write("content for column 5")

with st.container():
    st.header('this is a container')
    st.write('this is inside the conatiner')

st.write('this is outside the container')

st.sidebar.header('sidebar')

st.sidebar.write('this is the sidebar')

st.sidebar.selectbox('choose option',['option 1','option2','option 3'])

st.sidebar.radio('go to',['home','data','settings'])

with st.form('my_form'):
    name=st.text_input('name')

    age=st.slider('age',min_value=0,max_value=100)

    email=st.text_input('email')

    biografy=st.text_area('shorteerr bio')

    terms=st.checkbox('i agree')

    submit_button=st.form_submit_button(label='submit')


















import streamlit as st

from modul4.loops import user_input


def main():
    st.title("hello world")

if __name__=="__main__":
    main()

if st.button("click me"):
    st.write("button clicked")

st.checkbox("check me")
if st.checkbox("check me to see some text"):
    st.write("you are seeing this becuase you checked me")

user_input=st.text_input("enter text","sample text")
st.write("you have entered: ", user_input)
age=st.number_input("enter your are",min_value=0, max_value=10)
st.write(f"your age is: {age}")

message=st.text_area("enter a message")
st.write(f"your message:{message}")

choice=st.radio("pick on", ["choice 1","choice 2","choice 3"])
st.write(f"you choose:{choice}")
if st.button("succes")
    st.succes("operation was successful")
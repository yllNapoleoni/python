import streamlit as st

def calculator(num1,num2,operation):

    if operation=='add':
        result=num1+num2

    elif operation=='sub':
        result=num1-num2

    elif operation=='multi':
        result=num1*num2

    elif operation=='div':
        try:
            result=num1/num2
        except ZeroDivisionError:
            result='cannot divide by zero'

    return result


def main():
    st.title("simple calucator")
    num1=st.number_input('enter the first number',step=1)

    num2=st.number_input('enter the second number',step=1)

    operaion=st.radio('select operation',['add','sub','multi','div'])

    result=calculator(num1,num2,operaion)

    st.write(f'result od the {operaion} of {num1} and {num2} is {result}')

if __name__=='__main__':
    main()
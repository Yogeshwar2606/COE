import streamlit as st
st.title("Percentage of spending amount")
total_salary=st.number_input("Enter the total salary")
s1=st.number_input("enter first shopping amount",min_value=1)
s2=st.number_input("enter the second shopping amount",min_value=1)
s3=st.number_input("enter the third shopping amount",min_value=1)
salaryspent=s1+s2+s3

if st.button("calculate percentage"):
    spent=(salaryspent/total_salary)*100
    st.text(f"The total amount spent in Shoppings:{salaryspent}")
    st.text(f"The total amount spent in percentage:{spent}")

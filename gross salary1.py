import streamlit as st
st.title("Calculating the gross salary")
basic_salary=int(st.text_input("Enter your salary","10000"))
if st.button("Calculate gross salary"):
    HRA=0
    DA=0
    if basic_salary < 10000:
        HRA = 0.67 * basic_salary
        DA = 0.73 * basic_salary
    elif basic_salary < 20000:
        HRA = 0.69 * basic_salary
        DA = 0.76 * basic_salary
    else:
        HRA = 0.73 * basic_salary
        DA = 0.89 * basic_salary
    gs=HRA+DA
    st.text(f"Your gross salary:{gs}")
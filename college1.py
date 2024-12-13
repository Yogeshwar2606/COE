import streamlit as st
st.title("calculating the grades of student")
project=st.number_input("Enter the marks in project")
internal=st.number_input("Enter the marks in internal")
external=st.number_input("Enter the external marks")
if st.button("calculate grade"):
    if project>=50 and internal>=50 and external>=50:
        total_marks=0.7*project+0.10*internal+0.20*external
        st.text(f"Total marks you got:{total_marks}")
        if total_marks>=90:
            st.text("A")
        elif total_marks>=80:
            st.text("B")
        else:
            st.text("c")
    else:
        if project<50:
            st.text(f"failed in project and score is:{project}")
        if external<50:
            print(f"failed in external and score is:{external}")
        if internal<50:
            print(f"failed in internal and score is:{internal}")
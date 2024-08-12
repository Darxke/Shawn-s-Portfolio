#setup_2
import streamlit as st

def setup():
    col1, col2 = st.colums(2)
    with col1:
        st.subheader("col")
    with col2:
        st.subheader("col2")
    st.header(":two: Setup")
    st.write("To install Streamlit, run this command in your terminal or command prompt:")
    st.code('pip install streamlit')
    st.write("Then create a new Python file for your project.")

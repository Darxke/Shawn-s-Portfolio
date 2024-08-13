#setup_2
import streamlit as st

def setup():
    col1, col2 = st.columns(2)
    
    st.header(":two: Setup")
    st.write("To install Streamlit, run this command in your terminal or command prompt:")
    st.code('pip install streamlit')
    st.write("Then create a new Python file for your project.")
    with col1:
        st.subheader("Step 1: Install Streamlit")
    with col2:
        st.subheader("Step 2: Verify Installation")
        st.write("streamlit hello")
    st.code('''
# Save this as 'hello_streamlit.py'
import streamlit as st
st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app!")
''')

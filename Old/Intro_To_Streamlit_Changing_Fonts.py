import streamlit as st
st.markdown('''
<style>
.big-red-text {
    color:red;
    font-size: 24px;
    }
.stButton>button {
    color:red;
    background-color: blue;
    height: 100px;
    width : 100px;
    border-radius: 100px;
    }
.stApp{
    background-color: blue;
}
</style>
''', unsafe_allow_html = True)
st.markdown('<p class = "big-red-text"> This is big red text!</p>', unsafe_allow_html= True)
st.button("clicke me")

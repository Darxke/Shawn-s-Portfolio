
# basic_3
import streamlit as st

def basicStreamlitElements():
    tab1, tab2, tab3 = st.tabs(["Text Elements", "Input Elements", "Display Images"])
    st.header(":three: Basic Streamlit Elements")
    st.write("Let's explore some basic Streamlit elements:")
    with tab1:
        st.write("Here are some examples of text elements:")
        st.code('''
    st.title("A")
    st.header("B")
    st.write("C")
    st.subheader("D")
    st.caption("E")
    ''')
        st.title("A")
        st.header("B")
        st.write("C")
        st.subheader("D")
        st.caption("E")
    with tab2:
        st.write("Streamlit provides various input elements:")
        username = st.text_input("Enter your username")
        age = st.slider("Select your age", 1, 100)
        st.write(f"Hello, {username}, you are {age} years old.")
    with tab3:
        st.write("You can display images like this:")
        st.image("https://media.discordapp.net/attachments/861294452714635274/1262567334409801769/download_1.jpg?ex=669710f5&is=6695bf75&hm=e921ecbc39564a6ad019972d83bb64980e579f5af775d941bb33142db417bad1&=&format=webp&width=395&height=259")


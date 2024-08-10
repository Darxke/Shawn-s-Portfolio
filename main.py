#Intro to streamlit day 1
import streamlit as st
from src.landing_1 import introduction
from src.setup_2 import setup
from src.basic_3 import basicStreamlitElements
from src.interative_4 import interativeApp
from src.run_5 import runApp
from src.capturing_6 import capturingVariables
from src.hands_7 import handsOnActivity
from src.wrap_8 import wrapUp
from src.todo_9 import toDoList
from src.quiz_10 import quiz
def main():
    st.title("Intro to streamlit :dark_sunglasses:")


    #add a sidebar
    st.sidebar.title("Streamlit Master Class")
    with st.sidebar.expander("Lesson Plans", expanded = True):

        streamlit_sections = [
            ":one: Introduction",
            ":two: Setup",
            ":three: Basic Streamlit Elements",
            ":four: Simple Interative App",
            ":five: Running the App",
            ":six: Capturing Variables",
            ":seven: Hands on Activity",
            ":eight: :red[Wrap up]" ,
            ":nine: ToDo List",
            ":one::zero: Quiz",
            

        ]

        selected_streamlit_section = st.radio("Go to", streamlit_sections)
    #main content
    if selected_streamlit_section:
        
        if selected_streamlit_section == ":one: Introduction":
            introduction()
        elif selected_streamlit_section == ":two: Setup":
            setup()
        elif selected_streamlit_section == ":three: Basic Streamlit Elements":
            basicStreamlitElements()
        elif selected_streamlit_section == ":four: Simple Interative App":
            interativeApp()
        elif selected_streamlit_section == ":five: Running the App":
            runApp()
        elif selected_streamlit_section == ":six: Capturing Variables":
            capturingVariables()

        elif selected_streamlit_section == ":seven: Hands on Activity":
            handsOnActivity() 
        elif selected_streamlit_section == ":eight: :red[Wrap up]":
            wrapUp()
        elif selected_streamlit_section == ":nine: ToDo List":
            toDoList()
        elif selected_streamlit_section == ":one::zero: Quiz":
            quiz()
            st.divider()
    









if __name__ == "__main__":
    main()


import streamlit as st
import openai
import time

ASSISTANT_ID = 'asst_G9g1anGONTUaOpJaBXqf81Y7'
THREAD_ID = 'thread_fRMKtlBtM7eLaCooOYlIOYaC'
ASSISTANTS_MODE = {
        'Beginner': ''' Give them the first letter of the name ''',
        'Advanced': '''Only give them three lives and only give them 5 hints max once they lose than they will have to restart'''


    }
def wait_for_run_complete(client, thread_id, run_id):
    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
        if run.completed_at:
            return run.status
        time.sleep(1)

def get_assistant_response(client, user_input):
    # Add the user's message to the thread
    client.beta.threads.messages.create(
        thread_id=THREAD_ID,
        role='user',
        content=user_input
    )
    # Create a run
    run = client.beta.threads.runs.create(
        thread_id=THREAD_ID,
        assistant_id=ASSISTANT_ID
    )
    # Wait for the run to complete
    wait_for_run_complete(client, THREAD_ID, run.id)
    # Retrieve the assistant's messages
    messages = client.beta.threads.messages.list(thread_id=THREAD_ID)

    # Return the latest assistant message
    return messages.data[0].content[0].text.value

def streamlit_assistant():
    mode = st.selectbox("Please select a gamemode", list(ASSISTANT_MODES.keys()))
    st.write("Current mode: {mode}")
    if "messages" not in st.session_state:
        st.session_state.messages = {mode: [] for mode in ASSISTANT_MODES}

    for messages in st.session_state.messages[mode]:
        with st.message(message['role']):
            st.markdown(message['content'])

    if prompt := st.chat_input(f"Ask the {mode} Assistant about Brawl Stars."):
        st.session_state.messages[mode].appened({'role': 'user', 'content': prompt})
        with st.chat_message('urser'):
            st.markdown(prompt)

    if 'open_api_key' in st.session_state and st.session_state.openai_api_key:
        client = openai.OpenAI(api_key=st.session_state.openai_api_key)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = get_assistant_response(client, prompt, mode)
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
def main():
    # Streamlit page config
    st.set_page_config(page_title="My AI Chatbot", page_icon="🤖", layout="wide")

    # Sidebar for API key input
    st.sidebar.title("Setup")
    api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

    # Main chat interface
    st.title("🤖 My AI Chatbot")
    if api_key:
        st.session_state.openai_api_key = api_key
    #Call on streamlit assistant function
    streamlit_assistant()
    
if __name__ == '__main__':
    main()

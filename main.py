import os

import openai
import streamlit as st


def show_messages(text):
    messages_str = [
        f"{_['role']}: {_['content']}" for _ in st.session_state["messages"][1:]
    ]
    text.text_area("Messages", value=str("\n\n".join(messages_str)), height=400)


BASE_PROMPT = [{"role": "system", "content": "You are a helpful assistant."}]

if 'messages' not in st.session_state:
    st.session_state['message'] = BASE_PROMPT

st.subheader("OpenAI GPT-3 Demo")

openai.api_key = os.getenv('OPENAI_API_KEY')
prompt = st.text_area("Prompt", value="Enter your message here ...")

if st.button("Send"):
    with st.spinner("generating response ..."):
        st.session_state['message'] += [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", message=st.session_state['message']
        )
        message_rsp = response["choices"][0]["message"]["content"]
        st.session_state['message'] += [{"role": "system", "content": message_rsp}]

if st.button("Clear"):
    st.session_state['message'] = BASE_PROMPT

test = st.empty()
show_messages(test)

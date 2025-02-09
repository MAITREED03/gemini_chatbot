from google import genai
import streamlit as st
import os
from dotenv import load_dotenv

#load environment variables
load_dotenv()

#get apu key from .env

api_key = os.getenv("GOOGLE_API_KEY")

#configure gemini Client with api key
client = genai.Client(api_key=api_key)

#Initialize Gemini Model
chat = client.chats.create(model="gemini-2.0-flash")

#streamlit UI
st.title("GEMINIBOT")
st.write("powered by google")


#chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#display the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


#user input

user_input = st.chat_input("Type your message........")
if user_input:
    #Display the user input
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
#get ai response
response = chat.send_message_stream(user_input)

#collect streamed response
bot_reply = ""
for chunk in response:
    if chunk.text:
        bot_reply += chunk.text + " "

#display the AI response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply.strip()})
    with st.chat_message("assistant"):
        st.markdown(bot_reply.strip())

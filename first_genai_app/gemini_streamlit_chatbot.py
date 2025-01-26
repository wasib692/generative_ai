from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
import getpass
from dotenv import load_dotenv

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",
                             api_key="your_api_key",
                             temprature=0, max_tokens=None, timeout=None,
                             max_retries=2)

messages = [
    ("system", "Translate the user sentence to French."),
    ("human", "I love programming."),
]
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI Chatbot."),
    ("human", "Question: {question}"),
])
# llm.invoke(messages)

# conversation history with system message
conversation_history = [
    ("system", "You are a helpful AI Chatbot.")
]

st.title("Langchain with Gemini!")
input_text = st.text_input("Enter Your question here...")

# output = StrOutputParser()
#
# chain = prompt | llm | output

if input_text:

    conversation_history.append(("human", input_text))
    print(f"Conversation history: {conversation_history}")

    context = ""
    for role, message in conversation_history:
        context += f"{role}: {message}\n"

    print(f"Context: {context}")

    response = llm.invoke(context)

    # print(f"Response: {response}")
    print(f"Response: {response.content}")

    st.write(response.content)
    # adding the AI's response to the conversation history
    conversation_history.append(("ai", response.content))

    # st.write(chain.invoke({'question': input_text}))

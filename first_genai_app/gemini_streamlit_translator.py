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

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that translates {input_language} to {output_language}"),
    ("human", "{input}"),
])

st.title("Langchain with Gemini!")
input_text = st.text_input("Write the sentence in English and it will be translated in French.")

output = StrOutputParser()

chain = prompt | llm | output

if input_text:
    st.write(chain.invoke({'input_language': 'English',
                           'output_language': 'French',
                           'input': input_text}))

from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

import os

lang_api_key = os.getenv("LANG_API", "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")
gem_api_key = os.getenv("GEM_API_KEY", "AIzaSyABqRZfsB8i5nU1r43ygsLXKie8D8SvqZA")

if lang_api_key is None or gem_api_key is None:
    raise ValueError("Environment variables 'LANG_API' or 'GEM_API_KEY' are not set.")

os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_API_KEY'] = lang_api_key
os.environ['GOOGLE_API_KEY'] = gem_api_key
llm = GoogleGenerativeAI(model="gemini-pro")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

st.title('Langchain Demo With GEN API')
input_text=st.text_input("Search the topic u want")

output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
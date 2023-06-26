import os
import openai
import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from PyPDF2 import PdfReader


st.set_page_config(
    page_title="Wazobia (The Nigerian Translator)",
    page_icon="🤖",
    initial_sidebar_state="collapsed"
)

load_dotenv()

langs = ["Hausa", "Igbo", "Yoruba", "English"]

# Hide Streamlit style
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            <style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown('# Wazobia (The Nigerian Translator)')

with st.sidebar:
     language = st.radio('Select language to translate to:', langs)

st.markdown('### Wazobia Translate')
prompt = st.text_input('Enter text here')

trans_template = PromptTemplate(
    input_variables=['trans'],
    template='Your task is to translate this text to ' + language + 'TEXT: {trans}'
)

# Memory
memory = ConversationBufferMemory(input_key='trans', memory_key='chat_history')

# LLMs
llm = OpenAI(model_name="text-davinci-003", temperature=0)
trans_chain = LLMChain(llm=llm, prompt=trans_template, verbose=True, output_key='translate', memory=memory)

# If there's a prompt, process it and write out response on screen
if st.button("Translate"):
    if prompt:
        response = trans_chain({'trans': prompt})
        st.info(response['translate'])

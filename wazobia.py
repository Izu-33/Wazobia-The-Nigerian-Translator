# import os
# import openai
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
    page_icon="🤖"
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


st.divider()

st.markdown('### Wazobia PDFQuery')

pdf = st.file_uploader('Upload your PDF', type='pdf')

if pdf:
    pdf_reader = PdfReader(pdf)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    # Split into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    chunks = text_splitter.split_text(text)
    
    # Create embeddings
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    # Collect user input
    user_question = st.text_input("Ask Wazobia a question about your PDF")
    if user_question:
        docs = knowledge_base.similarity_search(user_question)
        # View results of similarity search
        # st.write(docs)

        llm = OpenAI()
        chain = load_qa_chain(llm, chain_type='stuff')
        response = chain.run(input_documents=docs, question=user_question)

        st.info(response)
                

#import pacakages:
import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
import base64
import os

#imports fromm changchain:
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate


from datetime import datetime

os.environ["GOOGLE_API_KEY"] = "place your own api"

#to get text from pdfs:
def get_pdf_etext(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text

#to get chunks from text:
def get_text_chunks(text,model_name):
    if model_name=="Google AI":
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000)
    chunks=text_splitter.split_text(text)
    return chunks

#embeddings this chunks and storing them in a vectore_store:
def get_vetore_chunks(text_chunks,model_name,api_key=None):
    if model_name=="Google AI":
        embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=api_key)
    vectore_store=FAISS.from_texts(text_chunks,embedding=embeddings)
    vectore_store.save_local("faiss_index")
    return vectore_store

#create a conversational chain using langchain:
def get_conversational_chain(model_name,vectorstore=None,api_key=None):
    if model_name=="Google AI":
        prompt_template="""
        answer the question as detailed as possible from the provided context,make sure to provide all the
        details with proper structure,if the answer is not in the provided context just say ,"answer is not
        available in the context",don't provide the wrong answer"  
        context:\n{context}?\n
        Query:\n{Question}?\n

        Answer:
        """

        model=ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=0.3,api_key=api_key)
        prompt=PromptTemplate(template=prompt_template,input_variables=["context","Question"])
        chain=load_qa_chain(model,chain_type="stuff",prompt=prompt)
        return chain
    

#take the user input


def user_input(user_question,model_name,api_key,pdf_docs,conversation_history):
    if api_key is None and pdf_docs is None:
        st.warning("Please upload any pdf and provide API key")
        return 
    text_chunks=get_text_chunks(get_pdf_etext(pdf_docs),model_name)
    vectore_store=get_vetore_chunks(text_chunks,model_name,api_key)
    user_question_output=""
    response_output=""
    if model_name=="Google AI":
        embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=api_key)
        new_db=FAISS.load_local("faiss_index",embeddings,allow_dangerous_deserialization=True)
        docs=new_db.similarity_search(user_question)
        chain=get_conversational_chain("Google AI",vectorstore=new_db,api_key=api_key)
        response=chain({"input_documents":docs,"Question":user_question},return_only_outputs=True)
        user_question_output=user_question
        response_output=response['output_text']
        pdf_names=[pdf.name for pdf in pdf_docs] if pdf_docs else []
        conversation_history.append((user_question_output,response_output,model_name,datetime.now().strftime('%Y-%m-%d %H:%M:%S')," , ".join(pdf_names)))


        

from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter   
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI

def main():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        st.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        return

    st.set_page_config(
        page_title="AskPDF",
        page_icon="📝",
        layout="wide",
    )
    st.header("AskPDF")
    pdf = st.file_uploader("Upload a PDF", type="pdf")

    # Extract text from PDF
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        number_of_pages = len(pdf_reader.pages)
        text = ""
        for i in range(number_of_pages):
            page = pdf_reader.pages[i]
            text += page.extract_text()

        # Split text into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        chunks = text_splitter.split_text(text)

        # Create embeddings
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # Show user input
        user_question = st.text_input("Ask a question about this PDF:")

        if user_question:
            docs = knowledge_base.similarity_search(user_question)
            chain = load_qa_chain(ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=openai_api_key), chain_type="stuff")
            response = chain.run(input_documents=docs, question=user_question)

            st.write(response)

if __name__ == '__main__':
    main()

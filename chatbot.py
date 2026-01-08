import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

def main():
    st.set_page_config(page_title="Chat with PDF", layout="centered")
    st.title("📄 Chat with your PDF")

    pdf = st.file_uploader("Upload a PDF", type="pdf")
    use_google = st.checkbox("Use Google Gemini (LLM)")

    if pdf:
        # 1️⃣ Read PDF
        reader = PdfReader(pdf)
        text = "".join(page.extract_text() or "" for page in reader.pages)

        if not text.strip():
            st.error("Could not extract text from the PDF.")
            return

        # 2️⃣ Split text
        splitter = CharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=150
        )
        chunks = splitter.split_text(text)

        # 3️⃣ LOCAL embeddings (NO API, NO QUOTA)
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        vectorstore = FAISS.from_texts(chunks, embeddings)
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

        # 4️⃣ LLM (optional cloud usage)
        llm = (
            ChatGoogleGenerativeAI(
                model="gemini-pro",
                temperature=0
            )
            if use_google
            else ChatOpenAI(
                model="gpt-3.5-turbo",
                temperature=0
            )
        )

        # 5️⃣ Prompt
        prompt = ChatPromptTemplate.from_template(
            """
            Answer the question using only the context below.
            If the answer is not in the context, say "I don't know."

            Context:
            {context}

            Question:
            {question}
            """
        )

        # 6️⃣ Runnable chain
        chain = (
            {
                "context": retriever,
                "question": RunnablePassthrough()
            }
            | prompt
            | llm
        )

        query = st.text_input("Ask a question about your PDF")

        if query:
            response = chain.invoke(query)
            st.subheader("Answer")
            st.write(response.content)

if __name__ == "__main__":
    main()

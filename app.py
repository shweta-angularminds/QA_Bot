import streamlit as st
import tempfile
from components.sidebar import render_sidebar
from components.pdf_viewer import render_pdf_viewer
from components.chat_panel import init_chat, render_chat,chat_input


from services.pdf_loader import load_and_split_pdf
from services.vector_store import create_vector_store
from services.llm_service import ask_llm


st.set_page_config(layout="wide",page_title="Q&A Boat")

init_chat()

uploaded_files = render_sidebar()

col1,col2 = st.columns([2,1])

vector_store = None

with col1:      
     if uploaded_files:

        uploaded_file = uploaded_files[0]

        render_pdf_viewer(uploaded_file)

        # Save file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.getvalue())
            pdf_path = tmp.name

        # Create vector store only once
        if "vector_store" not in st.session_state:

            with st.spinner("Processing PDF..."):

                chunks = load_and_split_pdf(pdf_path)

                vector_store = create_vector_store(chunks)

                st.session_state.vector_store = vector_store

        else:
            vector_store = st.session_state.vector_store

with col2:
    render_chat()

    question = chat_input()

    if question and vector_store:

        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.spinner("AI is thinking..."):

            docs = vector_store.similarity_search(question, k=3)

            context = "\n".join([doc.page_content for doc in docs])

            answer = ask_llm(context, question)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        st.rerun() 
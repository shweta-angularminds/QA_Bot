import streamlit as st

def init_chat():
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
def render_chat():
    
    
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
def chat_input():
    question = st.chat_input("Ask about this PDF")
    
    return question


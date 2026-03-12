import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

def render_pdf_viewer(uploaded_file):
    
    st.subheader("Document Viewer")
    
    if uploaded_file:
        
        pdf_bytes = uploaded_file.read()
        
        pdf_viewer(
            input=pdf_bytes,
            width=700
        )
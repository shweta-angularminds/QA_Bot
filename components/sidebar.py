import streamlit as st

def render_sidebar():
    
    st.sidebar.title("📄 Documents")

    uploaded_files = st.sidebar.file_uploader(
        "Upload PDFs",
        type="pdf",
        accept_multiple_files=True
    )
    
    st.sidebar.markdown("---") 
    
    st.sidebar.subheader("Uploaded Files")
    
    if uploaded_files:
        for file in uploaded_files:
            st.sidebar.write(f"📄 {file.name}")   
            
    return uploaded_files
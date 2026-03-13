import streamlit as st

def render_welcome_page():
    st.markdown("## 🤖 Welcome to Q&A Bot")

    st.write(
            "Upload a **PDF document** and ask questions about its content. "
            "The AI will search inside the document and generate answers."
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📄 How to Use")

        st.markdown("""
            1. Upload a **PDF file** from the sidebar.
            2. Wait for the document to be processed.
            3. Ask questions in the **chat panel**.
            4. Get answers based on the document.
            """)

    with col2:
        st.markdown("### 💡 Example Questions")

        st.markdown("""
            - What is the main topic of this document?
            - Summarize the key points.
            - Explain chapter 2.
            - What conclusions are presented?
            """)

    st.divider()

    st.markdown("### 🚀 Tips for Best Results")

    st.markdown("""
        - Ask **clear and specific questions**
        - Use **short queries**
        - Ask about **specific sections**
        - Try **summary questions**
        """)

    st.info("👈 Upload a PDF from the **sidebar** to start chatting.")
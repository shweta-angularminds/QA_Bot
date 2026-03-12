import streamlit as st

from components.sidebar import render_sidebar
from components.pdf_viewer import render_pdf_viewer

st.set_page_config(layout="wide")

uploaded_files = render_sidebar()

if uploaded_files:
    render_pdf_viewer(uploaded_files[0])    
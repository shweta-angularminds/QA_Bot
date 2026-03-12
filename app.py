import streamlit as st

from components.sidebar import render_sidebar

st.set_page_config(layout="wide")

uploaded_files = render_sidebar()
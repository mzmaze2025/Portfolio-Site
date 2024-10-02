import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Márta Makhándi")
    content = """Reaching my 50th year, I decided to learn something from scratch. That is Python programming. 
                This page is the first big project on this journey."""
    st.info(content)





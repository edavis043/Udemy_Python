import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Evin Davis")
    content = "This is a repo for projects that i have done during Python Udemy Course."
    st.info(content)

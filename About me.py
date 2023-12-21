import streamlit as st
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("akash1.jpg")
with col2:
    st.title('Akash K')

    content = """
    I'm a Second year student studying in SRMIST Ramapuram, Chennai.
    An Aspiring python developer and an cybersecurity expert"""
    st.info(content)

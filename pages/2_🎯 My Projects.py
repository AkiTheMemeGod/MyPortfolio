import streamlit as st
import pandas as pd
st.set_page_config(layout="wide", page_icon="🎯", page_title="My Projects")
col1, empty_col,col2 = st.columns([1.5, 0.2, 1.5])
data = pd.read_csv("data.csv", sep=";")
with col1:
    for index, row in data[:8].iterrows():
        with st.container(border=1):
            st.title(str(index + 1) + "." + row["title"])
            st.subheader(f":rainbow[{str(row['progress'])}% Completed]")
            st.progress(int(row['progress']))
            st.subheader(row["description"])
            st.info(f"Language : {row['language']}")

            n1, n2, n3 = st.columns([0.25, 2, 0.25])
            with n2:
                st.image(f"images/{row['image']}", use_column_width="always")
                st.markdown("###")
                st.link_button(label="Source code",
                               url=row['url'],
                               use_container_width=True,
                               type="primary")
        st.markdown("###")
with col2:
    for index, row in data[8:].iterrows():
        with st.container(border=1):
            st.title(str(index + 1) + "." + row["title"])
            st.subheader(f":rainbow[{str(row['progress'])}% Completed]")
            st.progress(int(row['progress']))
            st.subheader(row["description"])
            st.info(f"Language : {row['language']}")

            n1, n2, n3 = st.columns([0.25, 2, 0.25])
            with n2:
                st.image(f"images/{row['image']}", use_column_width="always")
                st.markdown("###")
                st.link_button(label="Source code",
                               url=row['url'],
                               use_container_width=True,
                               type="primary")
        st.markdown("###")
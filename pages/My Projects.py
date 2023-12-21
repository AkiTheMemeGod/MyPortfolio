import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
col1, empty_col,col2 = st.columns([1.5, 0.5, 1.5])
data = pd.read_csv("C:\PROJECTS\MyPortfolio\data.csv", sep=";")
with col1:
    for index, row in data[:8].iterrows():
        st.title(str(index+1)+"."+row["title"])
        st.subheader(str(row['progress'])+"% Completed")
        st.progress(int(row['progress']))
        st.subheader(row["description"])
        st.info(f"Language : {row['language']}")
        st.image(f"images/{row['image']}")
        #st.write(f"[Github link]({row['url']})")
        st.link_button(label="GitHub",
                       url=row['url'],
                       use_container_width=True,
                       type="primary")
        st.write("")
        st.write("")
        st.write("")
        st.write("_______________________________")
        st.write("")
        st.write("")
with col2:
    for index, row in data[8:].iterrows():
        st.title(str(index+1)+"."+row["title"])
        st.subheader(str(row['progress'])+"% Completed")
        st.progress(int(row['progress']))
        st.subheader(row["description"])
        st.info(f"Language : {row['language']}")
        st.image(f"images/'{row['image']}")
        # st.write(f"""[Github link]({row['url']})""")
        st.link_button(label="GitHub",url=row['url'],use_container_width=True,
                       type="primary")
        st.write("")
        st.write("")
        st.write("")
        st.write("_______________________________")
        st.write("")
        st.write("")
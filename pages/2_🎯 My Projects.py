import streamlit as st
import pandas as pd
st.set_page_config(layout="wide", page_icon="🎯", page_title="My Projects")

pg_bg_img = f"""
<style>
[data-testid="stApp"] {{
background-image: url("https://i.imgur.com/FTJFIX1.jpgg");
background-size: cover;
background-repeat: no-repeat;
background-attachment: local;
background-position: top left;
}}
[data-testid="stHeader"]{{
background-color: rgba(0,0,0,0);
}}

[data-testid="stSidebar"]{{
background-color: rgba(0,0,0,0.20);
}}
</style>
"""

st.markdown(pg_bg_img,unsafe_allow_html=True)

st.markdown("""<h1 style="font-family:monospace; color:#713D0B; font-size: 100px;",
 align="center">My Projects</h1><br><br><br>""",
                unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
data = pd.read_csv("data.csv", sep=";")
with col1:
    for index, row in data[:6].iterrows():
        with st.container(border=1):
            st.markdown(f"""<h1 style="font-family:monospace; color:black; font-size: 40px;",
             align="center">{row["title"].title()}</h1><br>""",
                        unsafe_allow_html=True)

            st.subheader(f":rainbow[{str(row['progress'])}% Completed]")

            st.progress(int(row['progress']))
            st.markdown(f"""<p style="font-family:monospace; color:black; font-size: 20px;",
                         align="center">{row["description"]}</p>""",
                        unsafe_allow_html=True)
            st.success(f"Language : {row['language']}")
            st.markdown("""
                        <style>
                        .st-emotion-cache-1v0mbdj > img{\
                            margin-left: 8%;
                            width: 300px;

                            }
                        </style>

                        """, unsafe_allow_html=True)

            st.markdown("###")
            n1, n2, n3 = st.columns([0.25, 2, 0.25])
            with n2:
                st.image(f"images/{row['image']}")
                st.link_button(label="Source code",
                               url=row['url'],
                               use_container_width=True,
                               type="primary")
        st.markdown("###")
with col2:
    for index, row in data[6:12].iterrows():
        with st.container(border=1):
            st.markdown(f"""<h1 style="font-family:monospace; color:black; font-size: 40px;",
             align="center">{row["title"].title()}</h1><br>""",
                        unsafe_allow_html=True)

            st.subheader(f":rainbow[{str(row['progress'])}% Completed]")

            st.progress(int(row['progress']))
            st.markdown(f"""<p style="font-family:monospace; color:black; font-size: 20px;",
                         align="center">{row["description"]}</p>""",
                        unsafe_allow_html=True)
            st.success(f"Language : {row['language']}")
            st.markdown("""
                        <style>
                        .st-emotion-cache-1v0mbdj > img{\
                            margin-left: 8%;
                            width: 300px;

                            }
                        </style>

                        """, unsafe_allow_html=True)

            st.markdown("###")
            n1, n2, n3 = st.columns([0.25, 2, 0.25])
            with n2:
                st.image(f"images/{row['image']}")
                st.link_button(label="Source code",
                               url=row['url'],
                               use_container_width=True,
                               type="primary")
        st.markdown("###")

with col3:
    for index, row in data[12:18].iterrows():
        with st.container(border=1):
            st.markdown(f"""<h1 style="font-family:monospace; color:black; font-size: 40px;",
             align="center">{row["title"].title()}</h1><br>""",
                        unsafe_allow_html=True)

            st.subheader(f":rainbow[{str(row['progress'])}% Completed]")

            st.progress(int(row['progress']))
            st.markdown(f"""<p style="font-family:monospace; color:black; font-size: 20px;",
                         align="center">{row["description"]}</p>""",
                        unsafe_allow_html=True)
            st.success(f"Language : {row['language']}")
            st.markdown("""
                        <style>
                        .st-emotion-cache-1v0mbdj > img{\
                            margin-left: 8%;
                            width: 300px;

                            }
                        </style>

                        """, unsafe_allow_html=True)

            st.markdown("###")
            n1, n2, n3 = st.columns([0.25, 2, 0.25])
            with n2:
                st.image(f"images/{row['image']}")
                st.link_button(label="Source code",
                               url=row['url'],
                               use_container_width=True,
                               type="primary")
        st.markdown("###")
import streamlit as st


skills = ["Python",
          "Ethical Hacking",
          "Dart",
          "Web Development",
          "Game Development",
          "Pentesting"]
hobbies = ["Gaming",
           "Coding",
           "Musical Instruments",
           "Competitive Touch-Typing",
           "Cycling",
           "Art"]

st.set_page_config(layout="wide", page_title="Akash's Portfolio", page_icon="🧑‍🦱")

pg_bg_img = f"""
<style>
[data-testid="stApp"] {{
background-image: url("https://i.imgur.com/y3mZwLL.jpg");
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
education = """
    <h1 style="font-family:monospace; color:black; font-size: 60px;", align="center">📖 Education</h1>
    <br>

<h3 style="font-family:monospace; color:black; font-size: 30px;", align="center">🎓 SRMIST Ramapuram</h3>

<br>
<h5 style=font="red";>🎯 B.Tech Computer Science-Engineering: Spec in Cybersecurity</h5>

    Current Year: 2nd Year
    Year of Enrollment: 2022
    Expected Year of Graduation: 2026
<br>
<h3 style="font-family:monospace; color:black; font-size: 30px;", align="center">🏫 St.John's English School & Junior College</h3>
<br>
<h5>🎯 12th Grade (HSC):</h5>

    Year of Completion: 2022
    Percentage: 82%
<br>
<h5>🎯 10th Grade (SSLC):</h5>

    Year of Completion: 2020
    Percentage: 92%
<br>


    """
about = """
    <h1 style="font-family:monospace; color:black; font-size: 60px;", align="center">👋 Hey there, I'm Akash</h1>
    <br>
    <p style="font-family:monospace; color:black; font-size: 20px;", align="justify">
    Hey there! I'm a second-year B.Tech student diving into the world
     of Computer Science Engineering with a Cybersecurity twist at SRM University.
     Fueled by a passion for all things cybersecurity,
      I'm on a journey of constant learning and pushing boundaries in the tech scene.
       Join me as I navigate through the exciting challenges of this dynamic field and
        chase innovation wherever it leads!</p>"""


st.markdown(pg_bg_img, unsafe_allow_html=True)


st.markdown("""
            <h1 style="font-family:monospace; color:#713D0B; font-size: 100px;", align="center">My portfolio</h1>
            <br>""",
            unsafe_allow_html=True)

st.markdown("""
            <style>
            .st-emotion-cache-1v0mbdj > img{
                border-radius: 6.1%;

                }
            </style>

            """, unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown("###")
    st.markdown("###")
    st.markdown("###")
    st.image("Untitled design(2).png", use_column_width="auto")

with col2:
    st.markdown(about, unsafe_allow_html=True)

    st.markdown(education, unsafe_allow_html=True)
    st.markdown("###")
st.markdown("---")


col3, emp, col4 = st.columns([1, 0.1, 1])
with col3:
    st.markdown("""<h1 style="font-family:monospace; color:black; font-size: 80px;", align="center">💻 Skills</h1>""",
                unsafe_allow_html=True)
    for i in skills:
        st.info("🗝️ "+i)
with col4:
    st.markdown("""<h1 style="font-family:monospace; color:black; font-size: 80px;", align="center">🚴 Hobbies</h1>""",
                unsafe_allow_html=True)
    for i in hobbies:
        st.info("🎗️ "+i)


st.markdown("###")
st.markdown("""
<br>
<h1 style="font-family:monospace; color:#8420BD; font-size: 50px;", align="center">Check Out my projects</h1>
<br>""", unsafe_allow_html=True)

n1, n2, n3 = st.columns(3)
with n2:
    st.link_button("My Projects",
                   url="My_Projects",
                   use_container_width=True,
                   type="primary",
                   help="Projects that i'm currently working on!")
with st.sidebar:
    st.header("Follow-Me On")
    st.link_button("Linked-In",
                   url="https://www.linkedin.com/in/akash-k-8b2132251/",
                   use_container_width=True,
                   type="secondary",
                   help="Linked-In Profile")

    st.link_button("Twitter",
                   url="https://twitter.com/AkiTheMemeGod1",
                   use_container_width=True,
                   type="secondary",
                   help="My Twitter")
    st.link_button("GitHub",
                   url="https://github.com/AkiTheMemeGod",
                   use_container_width=True,
                   type="secondary",
                   help="My GitHub")

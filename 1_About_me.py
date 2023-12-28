import streamlit as st
skills = ["Python",
          "Ethical Hacking",
          "Flutter",
          "Web Development",
          "Game Development"]
hobbies = ["Gaming", "Coding", "Musical Instruments", "Competitive Touch-Typing", ""]

st.set_page_config(layout="wide",page_title="Akash's Portfolio", page_icon="🧑‍🦱")

st.markdown("""<h1 style="font-family:monospace; color:#8420BD; font-size: 100px;", align="center">My portfolio</h1>
<br><br><br>""",
            unsafe_allow_html=True)
col1, col2 = st.columns([1,1.5])

with col1:
    st.markdown("###")
    st.markdown("###")
    st.markdown("###")
    st.image("Untitled design(2).png",use_column_width="auto")

with col2:
    about = """
    <h1 style="font-family:monospace; color:black; font-size: 60px;", align="center">Hey there, I'm Akash</h1>
    <br>
    <p style="font-family:monospace; color:black; font-size: 20px;", align="justify">
    Hey there! I'm a second-year B.Tech student diving into the world
     of Computer Science Engineering with a Cybersecurity twist at SRM University.
     Fueled by a passion for all things cybersecurity,
      I'm on a journey of constant learning and pushing boundaries in the tech scene.
       Join me as I navigate through the exciting challenges of this dynamic field and
        chase innovation wherever it leads!</p>"""
    education = """
    <h1 style="font-family:monospace; color:black; font-size: 60px;", align="center">Education</h1>
    <br>

<h3 style="font-family:monospace; color:black; font-size: 30px;", align="center">🏫 St.John's English School & Junior College</h3>

<h5>🎯 10th Grade (SSLC):</h5>

    Year of Completion: 2020
    Percentage: 92%
<br>
<h5>🎯 12th Grade (HSC):</h5>

    Year of Completion: 2022
    Percentage: 82%
<br>
<h3 style="font-family:monospace; color:black; font-size: 30px;", align="center">🎓 SRMIST Ramapuram</h3>

<br>
<h5 style=font="red";>🎯 B.Tech Computer Science Engineering - Spec in Cybersecurity</h5>

    Current Year: 2nd Year
    Year of Enrollment: 2022
    Expected Year of Graduation: 2026
    """
    st.markdown(about,unsafe_allow_html=True)


    st.markdown(education, unsafe_allow_html=True)
    st.markdown("###")
st.markdown("---")


    # with st.expander(label="Skills"):
col3, emp, col4 = st.columns([1,0.1,1])
with col3:
    st.markdown("""<h1 style="font-family:monospace; color:black; font-size: 80px;", align="center">Skills</h1>""",
                unsafe_allow_html=True)
    for i in skills:
        st.info("⌁ "+i)
with col4:
    st.markdown("""<h1 style="font-family:monospace; color:black; font-size: 80px;", align="center">Hobbies</h1>""",
                unsafe_allow_html=True)
    for i in hobbies:
        st.info("⌁ "+i)


st.markdown("###")
st.markdown("""
<br>
<h1 style="font-family:monospace; color:#8420BD; font-size: 50px;", align="center">Check Out my projects</h1>
<br>""",unsafe_allow_html=True)

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
    st.link_button("Instagram",
                   url="https://www.instagram.com/aki_the_meme_god/",
                   use_container_width=True,
                   type="secondary",
                   help="My Instagram")
    st.link_button("Twitter",
                   url="https://twitter.com/AkiTheMemeGod1",
                   use_container_width=True,
                   type="secondary",
                   help="My Twitter")

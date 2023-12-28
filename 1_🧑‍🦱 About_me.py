import streamlit as st
skills = ["Python",
          "Ethical Hacking",
          "Flutter",
          "Web Development",
          "Game Development"]
hobbies = ["Gaming", "Coding", "Guitar", "Competitive Touch-Typing"]

st.set_page_config(layout="wide",page_title="Akash's Portfolio", page_icon="🧑‍🦱")

st.title('My Portfolio', anchor="True")

col1, col2 = st.columns(2)

with col1:
    st.image("Untitled design(2).png",use_column_width="auto")

with col2:
    st.title('Akash K')
    about = """
    I'm a Second year student studying in SRMIST Ramapuram, Chennai.
    An Aspiring python developer and an Cybersecurity Aspirant"""
    education = "II Year in B.Tech Computer-Science Engineering Specialization in Cybersecurity"
    st.info(about)
    st.markdown("###")
    st.markdown("###")
    st.subheader("Education")
    st.info(education)
    st.markdown("###")
    st.markdown("###")

    # with st.expander(label="Skills"):
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Skills")
        for i in skills:
            st.info("⌁ "+i)
    with col4:
        st.subheader("Hobbies")
        for i in hobbies:
            st.info("⌁ "+i)
        st.link_button("My Projects",
                       url="My_Projects",
                       use_container_width=True,
                       type="primary",
                       help="Projects that i'm currently working on!")

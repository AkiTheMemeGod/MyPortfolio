import streamlit as st
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


opts = ["Job inquiries", "Project idea", "Other"]

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
st.markdown(pg_bg_img, unsafe_allow_html=True)


def sendmail(From: str, To: str, mesg: str, about: str):

    msg = MIMEMultipart()
    msg['Subject'] = f'Portfolio Website : {about}'
    msg['From'] = From
    msg['To'] = To

    text = MIMEText(f"{mesg}  \nFrom : {From}\n")
    msg.attach(text)

    s = sm.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("akis.pwdchecker@gmail.com", "tjjqhaifdobuluhg")
    s.sendmail(From, To, msg.as_string())
    s.quit()



def contact_form():
    with st.form("my_form", clear_on_submit=True):
        email = st.text_input(label="Your E-mail address here:")
        what = st.selectbox(label="What do you want to talk about ?", placeholder="Select an option", options=opts, index=0)
        message = st.text_area(label="Your message: ")

        sent = st.form_submit_button("Send")# send
    if sent:
        if email and message != "":
            sendmail(email, "k.akashkumar@gmail.com", message, what)
            st.success("Email Sent Successfully !")
        else:
            st.error("The fields are empty")

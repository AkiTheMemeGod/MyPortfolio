import streamlit as st
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
st.set_page_config(layout="wide")

opts = ["Job inquiries", "Project idea", "Other"]


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


st.title("Contact Me")
with st.form("my_form",clear_on_submit=True):
    email = st.text_input(label="Your E-mail address here:")
    what = st.selectbox(label="What do you want to talk about ?",placeholder="Select an option",options=opts,index=0)
    message = st.text_area(label="Your message: ")
    if email and message != "":
        pass
    else:
        st.error("The feilds are empty")
    sent = st.form_submit_button("Send")
    if sent:
        sendmail(email, "k.akashkumar@gmail.com", message, what)
        st.info("Email Sent Successfully !")


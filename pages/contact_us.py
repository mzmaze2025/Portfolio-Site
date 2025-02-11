import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Enter your email address.")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message} 
"""
    button = st.form_submit_button()
    if button:
        try:
            send_email(message)
            st.info("Your email was sent successfully.")
        except:        st.info("I am sorry, the email cannot be sent, you can contact me on mmpythonprojects@gmail.com")

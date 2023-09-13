import streamlit as st

st.header("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Email Address:")
    text_box = st.text_area("Message:")
    submit = st.form_submit_button("Submit")
    if submit:
        st.info("Your Email has been sent successfully")

import streamlit as st

def display_info_form():
    st.write("This is a loan prediction model that uses machine learning to assess loan applications.")
    st.write("It takes into account various factors to determine the likelihood of loan approval.")
    
    email = st.text_input("Email", placeholder="Enter your email for updates")
    
    if st.button("Submit"):
        if email:
            return f"Thank you for your interest. We'll keep you updated at {email}!"
        else:
            return "Thank you for your interest in our model."
    return None

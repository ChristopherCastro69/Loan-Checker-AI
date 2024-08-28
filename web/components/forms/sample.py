import streamlit as st
import streamlit_shadcn_ui as ui



def display_form():
    st.title("User Information Form")
    
        
    with st.form("my_form"):
        
        email = st.text_input("Email", placeholder="Enter your sound check")
        family_members = st.text_input("Number of Dependent Family Members", 
                               placeholder="Enter the number of family members that are dependent on you")
        marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
        education = st.selectbox("Education", ["High School", "Graduate", "Postgraduate"])
        

        gender = st.radio("Gender", ["Male", "Female"])
        self_employed = st.radio("Are you self employed?", ["Yes", "No"])
        
        terms = st.checkbox("In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content.")

        if family_members and not family_members.isdigit():
            st.error('Please enter a valid number')
        else:
            family_members = int(family_members) if family_members else None
        
        submit_button = st.form_submit_button("Submit")
    
        
        if submit_button:
            st.write("Form submitted!")
            st.write(f"Email: {email}")
            st.write(f"Number of Family Members: {family_members}")
            st.write(f"Marital Status: {marital_status}")
            st.write(f"Education: {education}")
            st.write(f"Gender: {gender}")
            st.write(f"Self Employed: {self_employed}")
            st.write(f"Terms Accepted: {terms}")
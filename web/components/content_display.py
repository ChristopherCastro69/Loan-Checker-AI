import streamlit as st
from forms.app_form import display_app_form
from forms.info_form import display_info_form

@st.dialog("Loan Prediction by Chris")
def show_content(item):
    if item == "About the model.":
        return display_info_form()
    elif item == "Please fill up the application form.":
        return display_app_form()
        

@st.dialog("Welcome!")
def display_submission_details():
    st.write("Recent Submission Details:")
    st.markdown(f"""
    **Email:** {st.session_state.submission_details['email']}  
    **Number of Dependent Family Members:** {st.session_state.submission_details['family_members']}  
    **Education:** {st.session_state.submission_details['education']}  
    **Gender:** {st.session_state.submission_details['gender']}  
    **Self Employed:** {st.session_state.submission_details['self_employed']}  
    **Marital Status:** {st.session_state.submission_details['marital_status']}  
    **Loan Amount:** {st.session_state.submission_details['loan_amount']}  
    **Loan Amount Term:** {st.session_state.submission_details['loan_term']}  
    **Credit History:** {st.session_state.submission_details['credit']}  
    **Property Area:** {st.session_state.submission_details['property']}  
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Submit Another Application"):
            st.session_state.form_submitted = False
            st.session_state.submission_details = {}
            st.rerun()
            

    with col2:
        st.button("Get Loan")


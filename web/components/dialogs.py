import streamlit as st
import pandas as pd

import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
from forms.app_form import display_app_form
from forms.info_form import display_info_form
from predict import predict_loan
from scaler import scale_data
from hooks import load_lottiefile, load_lottieurl

#Lottie Files animation
lottie_decline = load_lottiefile(r"web\lottiefiles\decline.json") 
lottie_approved = load_lottiefile(r"web\lottiefiles\approved2.json") 


#Content Dialog
@st.dialog("Welcome to Ai Bank by Chris!")
def content_dialog(item):
    if item == "About the model.":
        return display_info_form()
    elif item == "Please fill up the application form.":
        st.session_state.open_new_application = False
        return display_app_form()
        
#Form Dialog    
@st.dialog("Welcome!")
def submitted_form_dialog():
    st.session_state.open_form_dialog = False
    st.write("Recent Submission Details:")
    st.markdown(f"""
    **Email:** {st.session_state.submission_details['email']}  
    **Number of Dependent Family Members:** {st.session_state.submission_details['family_members']}  
    **Education:** {st.session_state.submission_details['education']}  
    **Income:** {st.session_state.submission_details['income']}  
    **Additional Income:** {st.session_state.submission_details['additional_income']}  
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
            st.session_state.open_new_application = True
            st.rerun()

            
            
    with col2:
        if st.button("Get Loan"):
            st.session_state.open_result_dialog = True
            st.rerun()
            
#Results Dialog
@st.dialog("Result")
def result_dialog():
    st.session_state.open_new_application = False
    
    st.session_state.scaled_data = scale_data(st.session_state.submission_details) 
    prediction = predict_loan()
    
    if prediction is None:
        st.error("Prediction could not be made.")
        return
    
    st.subheader('Prediction Result')
    if prediction == 1:
        st.write('Loan Approved')
        st_lottie(
            lottie_approved,
            speed=1,
            reverse=False,
            loop=True,
            quality="high", # medium ; high
            height=None,
            width=None,
            key=None,
        )
    else:
        st.write('Loan Rejected')
        st_lottie(
            lottie_decline,
            speed=1,
            reverse=False,
            loop=True,
            quality="high", # medium ; high
            height=None,
            width=None,
            key=None,
        )
    
    
    if st.button("Details"):
        st.session_state.open_details_dialog = True
        st.session_state.open_result_dialog = False
        st.rerun()
        
    if st.button("Apply another loan"):
        st.session_state.form_submitted = False
        st.session_state.submission_details = {}
        st.session_state.open_new_application = True
        st.session_state.open_result_dialog = False
        st.rerun()    
    
    st.session_state.open_result_dialog = False
    

#Details Dialog
@st.dialog("Details")
def details_dialog():

    st.write("Scaled Submission Details:")
    st.dataframe(st.session_state.scaled_data)
    
    st.write("Raw Loan Dataset:")
    if 'raw_dataset' in st.session_state:
        st.dataframe(st.session_state.raw_dataset)  # Display the loan dataset
    else:
        st.error("No loan dataset available.")
        
    st.write("Before Minmax Dataset:")
    if 'before_minmax_data' in st.session_state:
        st.dataframe(st.session_state.before_minmax_data)  # Display the loan dataset
    else:
        st.error("No before minmax dataset available.")

    st.write("After Minmax Dataset:")
    if 'after_minmax_data' in st.session_state:
        st.dataframe(st.session_state.after_minmax_data)  # Display the loan dataset
    else:
        st.error("No after minmax dataset available.")
    
    st.write("Predicted Data:")
    if 'predicted_data' in st.session_state:
        st.dataframe(st.session_state.predicted_data)  # Display the loan dataset
    else:
        st.error("No data available.") 
    
    st.session_state.open_details_dialog = False
    st.session_state.open_result_dialog = False
    
    

    
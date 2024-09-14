import streamlit as st
import pandas as pd

def display_app_form():

    st.caption("Please fill up the application form")
    email = st.text_input("Email", placeholder="Enter your email")
    family_members = st.selectbox("Number of people you are providing", ["0","1", "2", "3+"])
    
    income = st.text_input("Income", placeholder="Enter your income")
    additional_income = st.text_input("Additional Income", placeholder="Enter your additional income from other sources")
    loan_amount = st.text_input("Loan Amount", placeholder="Enter the amount you want to loan")

    loan_term = st.text_input("Loan Amount Term (months)", placeholder="Enter the loan's repayment period (in months)")

    credit = st.radio("Do you have a credit history?", ["Yes", "No"])
    # Convert credit history to 1 or 0
    credit_history = 1 if credit == "Yes" else 0

    property = st.selectbox("Property Location", ["Rural", "Urban", "Semiurban"])
    terms = st.checkbox("I accept the terms and conditions.")

    # Validate inputs to ensure all fields are filled and are valid
    if st.button("Submit Application"):
        if not all([email,loan_amount, loan_term, property]):
            st.error("All fields are required.")
            return None

        if not terms:
            st.error("You must accept the terms and conditions to proceed.")
            return None

        try:
            loan_amount = round(float(loan_amount), 2) 
            income = round(float(income), 2)
            additional_income = round(float(additional_income), 2)
            loan_term = round(float(loan_term))  
            if loan_amount < 0 or loan_term < 0 or income < 0 or additional_income < 0:
                raise ValueError("Values must be positive numbers or zero.")
        except ValueError:
            st.error("Please enter valid positive numbers for either Loan Amount, Loan Term, Income, and Additional Income.")
            return None

        st.session_state.email = {
            "email": email,
        }
        
        st.session_state.df_submitted_details = pd.DataFrame({       
            "dependents": [family_members],     
            "applicant_income": [f"{income:.2f}"],
            "coapplicant_income": [f"{additional_income:.2f}"],
            "loan_amount": [f"{loan_amount:.2f}"],
            "loan_amount_term": [loan_term],
            "credit_history": [credit_history],
            "property_area": [property]
        })
        st.session_state.form_submitted = True 
        st.session_state.open_form_dialog = True  
        st.rerun()  

    # Show success dialog if form is submitted
    if st.session_state.get("form_submitted"):
        st.session_state.form_submitted = False  
    return None
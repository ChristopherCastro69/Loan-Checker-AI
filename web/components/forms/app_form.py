import streamlit as st

def display_app_form():

    st.caption("Please fill up the application form")
    email = st.text_input("Email", placeholder="Enter your email")
    family_members = st.number_input("Number of Dependent Family Members", min_value=0, max_value=69, value=0)

    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    gender = st.radio("Gender", ["Male", "Female"])
    self_employed = st.radio("Are you self employed?", ["Yes", "No"])
    marital_status = st.radio("Are you married?", ["Yes", "No"])
    loan_amount = st.text_input("Loan Amount", placeholder="Enter the amount you want to loan")

    loan_term = st.text_input("Loan Amount Term", placeholder="Enter the loan's repayment period (in days)")

    credit = st.text_input("Credit History", placeholder="Enter your recent credit history points")
    property = st.selectbox("Property Location", ["Rural", "Urban", "Semiurban"])
    terms = st.checkbox("I accept the terms and conditions.")

    # Validate inputs to ensure all fields are filled and are valid
    if st.button("Submit Application"):
        if not all([email, education, gender, self_employed, marital_status, loan_amount, loan_term, credit, property]):
            st.error("All fields are required.")
            return None

        if not terms:
            st.error("You must accept the terms and conditions to proceed.")
            return None

        try:
            loan_amount = round(float(loan_amount), 2) 
            loan_term = round(float(loan_term))  
            credit = round(float(credit))  
            if loan_amount < 0 or loan_term < 0 or credit < 0:
                raise ValueError("Values must be positive numbers or zero.")
        except ValueError:
            st.error("Please enter valid positive numbers for Loan Amount, Loan Term, and Credit History.")
            return None

        # Set session state for submission details
        st.session_state.submission_details = {
            "email": email,
            "family_members": family_members,
            "education": education,
            "gender": gender,
            "self_employed": self_employed,
            "marital_status": marital_status,
            "loan_amount": f"{loan_amount:.2f}",
            "loan_term": loan_term,
            "credit": credit,
            "property": property
        }
        st.session_state.form_submitted = True
        st.rerun()  

    # Show success dialog if form is submitted
    if st.session_state.get("form_submitted"):
        # st.dialog("Application Submitted")  # Call the dialog directly
        # st.success("Application submitted successfully!")  
       
        st.session_state.form_submitted = False  # Reset the submission flag

    return None
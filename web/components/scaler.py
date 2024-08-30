import pandas as pd
import numpy as np
import streamlit as st

def scale_data(submission_details):
    scaled_data = {}

    # Family Members
    family_members = submission_details['family_members']
    scaled_data['Dependents_0'] = 1 if family_members == 0 else 0
    scaled_data['Dependents_1'] = 1 if family_members >= 1 else 0
    scaled_data['Dependents_2'] = 1 if family_members >= 2 else 0
    scaled_data['Dependents_3+'] = 1 if family_members >= 3 else 0

    # Education
    scaled_data['Education'] = 1 if submission_details['education'] == 'Graduate' else 0

    # Income
    income = float(submission_details['income'])
    scaled_data['Income'] = np.sqrt(income)

    # Additional Income
    additional_income = float(submission_details['additional_income'])
    scaled_data['Additional_Income'] = np.sqrt(additional_income)

    # Loan Amount
    loan_amount = float(submission_details['loan_amount'])
    scaled_data['Loan_Amount'] = np.sqrt(loan_amount)

    # Gender
    scaled_data['Gender'] = 1 if submission_details['gender'] == 'Male' else 0

    # Self Employed
    scaled_data['Self_Employed'] = 1 if submission_details['self_employed'] == 'Yes' else 0

    # Marital Status
    scaled_data['Marital_Status'] = 1 if submission_details['marital_status'] == 'Married' else 0

    # Property Area
    property_area = submission_details['property']
    scaled_data['Property_Area_Rural'] = 1 if property_area == 'Rural' else 0
    scaled_data['Property_Area_Urban'] = 1 if property_area == 'Urban' else 0
    scaled_data['Property_Area_Semiurban'] = 1 if property_area == 'Semiurban' else 0

    return pd.DataFrame([scaled_data])


def display_scaled_details():
    scaled_data = scale_data(st.session_state.submission_details)
    st.write("Scaled Submission Details:")
    st.dataframe(scaled_data)

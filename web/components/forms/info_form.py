import streamlit as st
from hooks import load_lottiefile
from streamlit_lottie import st_lottie 

def display_info_form():
    lottie_welcome = load_lottiefile(r"web\lottiefiles\approved1.json") 
    st_lottie(
        lottie_welcome,
        speed=1,
        reverse=False,
        loop=True,
        quality="high", # medium ; high
        height=None,
        width=None,
        key=None,
    )
    st.write("**Overview**")
    st.write("Welcome to my Loan Prediction Application! This project leverages machine learning to predict loan approvals using Gaussian Naïve Bayes (GNB), with an impressive 85% accuracy score from the testing and training data.")
    
    st.write("**How Does the Loan Process Work?**")
    st.write("When someone applies for a loan, they fill out various details such as their income, marital status, education, credit history, and more. This information is then used by the bank to assess whether the applicant is eligible for a loan. Normally, this process can be time-consuming, requiring manual review. My project seeks to automate this loan approval process in real time, helping banks make faster and more informed decisions.")
    
    st.write("**Data Set Problems 🤔**")
    st.write("The company wants to automate the loan qualifying process. By analyzing the data provided by the applicants through an online form, we can determine if they are eligible for a loan. By using machine learning, we can accelerate the decision-making process and provide real-time results to both the customer and the bank.")
    
    st.write("**Data Set Description 🧾**")
    st.write("The dataset I used for this project contains 13 variables, including 8 categorical, 4 continuous, and 1 ID column. Here's a quick breakdown of the key variables:")
    st.write("- **Loan_ID**: Unique loan reference number")
    st.write("- **Gender**: Applicant's gender")
    st.write("- **Married**: Marital status")
    st.write("- **Dependents**: Number of dependents or family members")
    st.write("- **Education**: Whether the applicant is a graduate")
    st.write("- **Self_Employed**: Self-employment status")
    st.write("- **ApplicantIncome**: Monthly salary or income")
    st.write("- **CoapplicantIncome**: Coapplicant's monthly income")
    st.write("- **LoanAmount**: Requested loan amount")
    st.write("- **Loan_Amount_Term**: Repayment period for the loan")
    st.write("- **Credit_History**: 1 (good credit history) or 0 (bad credit history)")
    st.write("- **Property_Area**: The location of the applicant's property")
    st.write("- **Loan_Status**: Final loan status (Y: approved, N: rejected)")
    
    st.write("**What I Found in the Data**")
    st.write("During my analysis on Kaggle, I found some interesting relationships between variables. Here are the highlights:")
    st.write("- Variables like gender and marital status showed significant differences when tested with other variables like 'education' and 'dependents.'")
    st.write("- However, in many cases, there was no significant difference between variables such as education and loan status, or self-employment and loan status. This shows that not all variables are strongly associated with one another in this particular dataset.")
    
    st.write("**Key Numeric Attributes**")
    st.write("By using Z-tests, I analyzed numeric attributes such as applicant_income and loan_amount_term to detect any significant differences between groups. The most important finding was that credit history had a significant difference in determining loan approval. This insight became crucial for my model's predictions.")
    
    st.write("**Important Features for Prediction 🔑**")
    st.write("After diving into the data, I identified the following key features that impact loan approval the most:")
    st.write("| Feature               | Importance Score |")
    st.write("|-----------------------|------------------|")
    st.write("| applicant_income      | ~0.159           |")
    st.write("| coapplicant_income    | ~0.091           |")
    st.write("| loan_amount           | ~0.156           |")
    st.write("| loan_amount_term      | ~0.052           |")
    st.write("| credit_history        | ~0.337           |")
    st.write("| dependents            | ~0.045           |")
    st.write("| property_area         | ~0.055           |")
    
    st.write("The credit history feature stands out the most, indicating it plays a critical role in whether a loan is approved or not.")
    
    st.write("**The Model: Gaussian Naïve Bayes**")
    st.write("Through testing various models, I found that Gaussian Naïve Bayes performed the best, with the following results:")
    st.write("- **Train Score**: 0.852")
    st.write("- **Test Score**: 0.8182")
    st.write("Given its high performance, I chose GNB as the model for deployment on my Streamlit application. It's now being used to predict loan statuses based on user input, providing instant feedback on loan eligibility.")
    
    st.write("**Why These Features Matter in Real Life 💡**")
    st.write("In real life, when you apply for a loan, banks don't just look at one factor—they consider a variety of things to assess risk. For example:")
    st.write("- **Credit History**: If you've borrowed money in the past and repaid it responsibly, it shows the bank that you're trustworthy. A bad credit history, on the other hand, raises red flags.")
    st.write("- **Loan Amount Term**: The longer you take to repay the loan, the more risk the bank takes on. A longer loan term can mean smaller monthly payments but higher total interest.")
    st.write("- **Income**: Your monthly salary, as well as any coapplicant's income, helps banks assess if you'll be able to repay the loan. A higher income suggests better financial stability.")
    
    st.write("By feeding all these factors into the machine learning model, I can predict the likelihood of loan approval based on the patterns found in past applications.")
    
    st.write("**Conclusion**")
    st.write("In real life, loan approval isn't just about one or two factors—it's about combining multiple aspects of a person's financial history and current situation. By using Gaussian Naïve Bayes, my model predicts loan approval based on the most important factors that have been identified through analysis. It's exciting to see how these features interact and how we can use them to predict loan outcomes quickly and accurately.")
    
    # Add project links
    st.write("**Project Links**")
    st.write("- **Dataset**: [Kaggle Dataset](https://www.kaggle.com/datasets/bhavikjikadara/loan-status-prediction)")
    st.write("- **My Kaggle Model**: [Kaggle Model Link](https://www.kaggle.com/code/kaizn69/loan-status-prediction-and-model-deployment/edit)")
    st.write("- **GitHub Link**: [GitHub Repository](https://github.com/ChristopherCastro69/Loan-Prediction)")
    
  

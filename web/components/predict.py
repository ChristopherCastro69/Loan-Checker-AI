import pickle
import pandas as pd
import streamlit as st
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

def predict_loan():
    # Load the dataset
    dataset = pd.read_csv('dataset/processed_dataset.csv')
    st.session_state.raw_dataset = dataset
    
    #Combine our current submitted data to the dataset
    combined_data = pd.concat([st.session_state.df_submitted_details, dataset], ignore_index=True)
    st.session_state.before_scaling_data = combined_data
        
    # Select the features to be scaled
    scaled_features = ["applicant_income", "coapplicant_income", "loan_amount", "loan_amount_term"]
    
    #Scale the combined dataset
    scaler = StandardScaler()
    scaled_combined_data = combined_data.copy()
    scaled_combined_data[scaled_features] = scaler.fit_transform(scaled_combined_data[scaled_features])
    st.session_state.after_scaling_data = scaled_combined_data.copy()
    
    # One-hot encode categorical features in X
    categorical_features = scaled_combined_data.select_dtypes(include=['object']) # Specify your categorical feature columns

    # Encode the target variable y
    label_encoder = LabelEncoder()
    scaled_data = scaled_combined_data.copy()
    for column in categorical_features:
        scaled_data[column] = label_encoder.fit_transform(scaled_data[column].astype(str))
    st.session_state.scaled_data = scaled_data
    
    # Drop specified columns from scaled_data
    columns_to_drop = ['education', 'gender', 'married', 'self_employed']
    scaled_data.drop(columns=columns_to_drop, inplace=True, errors='ignore')
    st.session_state.selected_features_data = scaled_data.copy()
    official_features_data = st.session_state.selected_features_data
    
    # Load the model
    try:
        with open('models/gnb_model.pkl', 'rb') as gnb:
            model = pickle.load(gnb)
    except FileNotFoundError:
        st.error("Model file not found.")
        return
    
    st.session_state.predicted_data = official_features_data.iloc[0:1]
  
    # Make a prediction
    try:
        prediction = model.predict(official_features_data.iloc[0:1])
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None  # Return None in case of error
    
    return prediction[0]  # Return the prediction directly
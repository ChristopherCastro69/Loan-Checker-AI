import pickle
import pandas as pd
import streamlit as st
from sklearn.preprocessing import MinMaxScaler

def predict_loan():
    # Load the dataset
    dataset = pd.read_csv('dataset/scaled_loan_dataset.csv')
    st.session_state.raw_dataset = dataset
    
    # Get the scaled data from session state
    if 'scaled_data' not in st.session_state:
        st.error("Scaled data not found in session state.")
        return
    
    scaled_data = st.session_state.scaled_data
    
    # Combine the scaled data with the dataset
    before_minmax_data = pd.concat([scaled_data, dataset], ignore_index=True)
    st.session_state.before_minmax_data = before_minmax_data

    # Apply MinMaxScaler to combined_data
    scaler = MinMaxScaler()
    combined_data = scaler.fit_transform(before_minmax_data)  # Scale the combined data
    
    # Convert back to DataFrame for further processing
    combined_data = pd.DataFrame(combined_data, columns=dataset.columns)  # Adjust columns as needed
    st.session_state.after_minmax_data = combined_data
    
    # Load the model
    try:
        with open('models/svm_model.pkl', 'rb') as lr:
            model = pickle.load(lr)
    except FileNotFoundError:
        st.error("Model file not found.")
        return
    
    # Display prediction values
    st.session_state.predicted_data = combined_data.iloc[0:1]
    
     
    # Make a prediction
    try:
        prediction = model.predict(combined_data.iloc[0:1])
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None  # Return None in case of error
    
    return prediction[0]  # Return the prediction directly


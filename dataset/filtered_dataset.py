import pandas as pd

# Load the dataset
file_path = 'dataset/train_u6lujuX_CVtuZ9i.csv'
data = pd.read_csv(file_path)

# Remove the 'Loan_ID' column and rows with any null values
filtered_data = data.drop(columns=['Loan_ID']).dropna()

# Save the filtered dataset to a new CSV file
filtered_data.to_csv('dataset/filtered_dataset.csv', index=False)

print("Filtered dataset saved as 'filtered_dataset.csv'")
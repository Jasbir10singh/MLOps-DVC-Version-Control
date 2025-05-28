import pandas as pd
import os

#create a data

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']}

#print(data)
#creating dataframe from data
df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)  # Create the directory if it doesn't exist
# Save the DataFrame to a CSV file

file_path = os.path.join(data_dir, 'data.csv')

df.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")

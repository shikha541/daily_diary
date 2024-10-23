# Day 11[23 June 2024]
# Working with Csv Files using Pandas

import pandas as pd

# Reading a CSV file into a DataFrame
df = pd.read_csv('data.csv')
print(df.head())

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [30, 25, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Writing DataFrame to CSV
df.to_csv('data.csv', index=False)  



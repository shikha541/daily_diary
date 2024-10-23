#Day -6 [17- june 2024]

# Introduction to pandas
# Pandas is a powerful and widely used Python library for data manipulation and analysis. 
# It is especially well-suited for working with structured data, such as tabular data
#  (like spreadsheets or SQL tables), and provides high-level data structures like 
# Series and DataFrames for efficient data handling. Pandas is built on top of NumPy,
#  which allows it to operate efficiently on large datasets.

#installing pandas
 # pip install pandas

#importing pandas 
import pandas as pd

# Creating a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)

# Custom index
series = pd.Series(data, index=["a", "b", "c", "d", "e"])
print(series)



# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}

df = pd.DataFrame(data)
print(df)




# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Select columns
print("Names and Cities:")
print(df[['Name', 'City']])

# Filter data
print("\nPeople older than 30:")
print(df[df['Age'] > 30])

# Add a new column
df['Country'] = 'USA'
print("\nDataFrame with new column:")
print(df)

# Group by 'City' and get the mean age
print("\nMean age by city:")
print(df.groupby('City')['Age'].mean())

# day 7 [18 June,2024]
# Data Cleaning using pandas

# 1. handling missing data:
 #a Detecting missing data
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', None], 'Age': [25, None, 35, 40], 'Salary': [50000, 60000, None, 70000]}
df = pd.DataFrame(data)

print(df.isnull()) 
# b removing missing data

df_cleaned = df.dropna()
print(df_cleaned)

df_cleaned = df.dropna(axis=1)
print(df_cleaned)

#filling the missing data

df_filled = df.fillna(0)
print(df_filled)

df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)



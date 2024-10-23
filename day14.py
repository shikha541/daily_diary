# day14 [26 June,2024]
# Introduction to sql queries 
# Connected to MySQL
# import mysql : pip install mysql-connector-python
import mysql.connector

# Connect to MySQL database
connection = mysql.connector.connect(
    host="localhost",  # Replace with your host
    user="root",  # Replace with your MySQL username
    password="root",  # Replace with your MySQL password
    database="test"  # Replace with your MySQL database name
)

# Create a cursor object
cursor = connection.cursor()

# Execute SQL queries
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

# Fetch data
cursor.execute("SELECT * FROM your_table")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
connection.close()

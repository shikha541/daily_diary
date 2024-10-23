# day 10 [22 june 2024]
# Working with csv files 
#
#CSV (Comma Separated Values) files are a common format for storing tabular data. 
# Python provides multiple ways to work with CSV files, and the most common approaches
#  are using the built-in csv module and the powerful pandas library.

#Reading a CSV File
import csv

# Reading a CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    
    # Iterate over the rows in the file
    for row in reader:
        print(row)



# Writing to a CSV file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(["Name", "Age", "City"])
 
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])

#Reading a CSV File with Headers

with open('example.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row)  

# Writing a CSV file using headers

with open('output_with_headers.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
   
    writer.writeheader()
    writer.writerow({'Name': 'Alice', 'Age': 30, 'City': 'New York'})
    writer.writerow({'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'})
    



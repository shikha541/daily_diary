# Day 3 [13 June 2024]
# Basics of Python 
# 1. Variables : A variable in Python is a symbolic name or reference
#  that is used to store values, which can be data such as numbers, 
# strings, or complex objects. Variables are essentially a way to 
# label and store data in memory for later use, allowing programs 
# to manipulate and use the stored information.

# Rules for Naming Variables:
#1 The name must start with a letter (a-z, A-Z) or an underscore (_).
#2 The name cannot start with a number.
#3 It can contain letters, numbers, and underscores, but no spaces.
#4 Variable names are case-sensitive (e.g., age, Age, and AGE are different variables).

# 2 Data Types : Data types define the type of value a variable holds. 
# In Python, variables can store different types of data, such as numbers,
#  text, or more complex structures like lists and dictionaries. 
# Python is a dynamically typed language, which means you don’t need to 
# explicitly declare the type of a variable; the interpreter automatically assigns it based on the value assigned.

# Types :Int,float,char,boolean,string,list,tuple,dict,set

# 3 Basic Operators : Operators are used to perform operations on variables and values.
#   Arithmetic Operators : +, -, *, /, % (modulus), ** (exponent)
#   Comparison Operators : ==, !=, >, <, >=, <=
#   Logical Operators : and, or, not
#   Assignment Operators : =, +=, -=, *=, /=, %=, **=,
#   Bitwise Operators : &, |, ^, ~, <<, >>
#   Membership Operators : in, not in
#   Identity Operators : is, is not



#  Problem 1 : Write a Python program to find the area of a rectangle using the formula area = length * width

# Input: Ask the user to enter the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
print(f"The area of the rectangle is: {area}")

# Problem 2 :Write a  program to calculate the average of three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

average = (num1 + num2 + num3) / 3

print(f"The average of the three numbers is: {average}")




# data types : 
# 1. Int : integer 
# 2. Float : floating point number
# 3. Char : character
# 4. Boolean : boolean value (True or False)
# example 
age = 18
is_adult = age >= 18  # True, because 18 is considered an adult

# 5. String : sequence of characters

 # Program related to string
# Concatenation
full_name = "Alice" + " " + "Johnson"
print(full_name)  # Output: Alice Johnson

# Slicing
greeting = "Hello, world!"
print(greeting[0:5])  


# 6. List : ordered collection of items
# Example of a list
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
print(fruits[0]) 
# Output: apple

# Adding an item
fruits.append("orange")

# Changing an item
fruits[1] = "blueberry"  # Now 'banana' becomes 'blueberry'

# 7. Tuple : ordered collection of items
coordinates = (10, 20)  # Tuple
colors = ("red", "green", "blue")
# Tuples are immutable, so you can't change them after they're created.
# Accessing tuple elements
print(colors[1])  # Output: green

# 8. Dict : unordered collection of key-value pairs
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
# Accessing a value by key
print(person["name"])  # Output: Alice
person["age"] = 26
person["occupation"] = "Engineer"

# 9. Set : unordered collection of unique items
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
print(set_a | set_b)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(set_a & set_b)  # Output: {3}






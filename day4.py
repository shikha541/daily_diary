# Day 4 [14 June 2024]
# Control Statements in python (if,else-if,match,nested-if)

# Problem: Write a program to find the maximum of three numbers using if-else statement.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    maximum = num1
elif num2 >= num1 and num2 >= num3:
    maximum = num2
else:
    maximum = num3

# Output
print(f"The maximum of the three numbers is: {maximum}")

# Problem 2: Write a program to check if a number is positive, negative, or zero using elif

number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Problem 3 :Write a program to find days in week using  match statement
def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"

day = int(input("Enter a number between 1 and 7: "))
print(day_of_week(day))


# Loops in python
# 1 For loop 
# Problem  1: Write a program to print numbers from 1 to 10 using for loop

for number in range(1, 11):
    print(number)

# Problem 2:  Write a program to calculate the sum of even numbers in a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_evens = 0
for number in numbers:
    if number % 2 == 0:
        sum_of_evens += number  

# Output
print(f"The sum of even numbers is: {sum_of_evens}")


# While loop :
# Example of a while loop
count = 1

while count <= 5:
    print(f"Count is: {count}")
    count += 1  

# Break and continue statement 
for i in range(1, 6):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)

for i in range(1, 6):
    if i == 3:
        continue  # Skip when i is 3
    print(i)








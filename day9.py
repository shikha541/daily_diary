# Day 9 [20 June 2024]
# File handling in python 

# opening and closing of file
# Opening a file
file = open("example.txt", "r")

# Closing the file
file.close()

# Reading the file
# Reading the whole file
with open("example.txt", "r") as file:
    content = file.read() 
    print(content)

# reading the file line by line 
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("example.txt", "r") as file:
    line = file.readline()  # reads one line at a time
    while line:
        print(line.strip())
        line = file.readline()

with open("example.txt", "r") as file:
    lines = file.readlines()  # Returns a list of lines
    print(lines)


# Writing to a file
with open("output.txt", "w") as file:
    file.write("This is a line of text.\n")
    file.write("This is another line of text.\n")
with open("output.txt", "a") as file:
    file.write("Appending this line to the file.\n") # appending the text to the file
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)  # Writes a list of strings to the file


# Reading a binary file
with open("eg.png", "rb") as file:
    data = file.read()
    print(data)  # This will print the binary data of the file

# Writing to a binary file
with open("output.bin", "wb") as file:
    file.write(b"This is binary data.")






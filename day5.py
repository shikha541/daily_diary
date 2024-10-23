# day 5 [15 June 2024]
# Introduction to Numpy 
# Numpy is a library for the Python programming language, adding support for large, multi-dimensional arrays

# arrays in numpy :
# In NumPy, arrays are the main way to work with numerical data. You can create, manipulate, and perform a wide range of mathematical operations on arrays. 
# install numpy run command in bash - pip install numpy

#  Importing Numpy
import numpy as np
 
# creating arrays
import numpy as np
arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr)) 
# output
#[1 2 3 4 5]
#<class 'numpy.ndarray'>


# operations on arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise addition
print(arr1 + arr2)

# Element-wise multiplication
print(arr1 * arr2)

# Element-wise square
print(arr1 ** 2)


# array attributes 


arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)  # (2, 3) - 2 rows and 3 columns
print(arr.size)   # 6 - total number of elements
print(arr.ndim)   # 2 - number of dimensions


# indexing 
arr = np.array([10, 20, 30, 40, 50])

# Accessing a single element
print(arr[2])  # Output: 30


# slicing 
# Slicing elements from index 1 to 3 (excluding 4)
print(arr[1:4])
# Output: [20 30 40]

# multidimensional array 
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Access element in the first row, second column
print(arr[0, 1])  # Output: 2

# Slice the first row
print(arr[0, :])  # Output: [1 2 3]
arr = np.array([1, 2, 3, 4, 5])

# Sum and mean operation  on the array

print(arr.sum())   # Output: 15
print(arr.mean())  # Output: 3.0



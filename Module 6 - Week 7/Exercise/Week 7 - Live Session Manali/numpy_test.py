#numpy (Numerical python) is a library used for numerical operations in python. It is used for working with arrays and matrices.
# pip install numpy - to install the numpy library
import numpy as np  #importing numpy library and np is a alias name for numpy

a = np.array([1,2,3,45]) #creating an array using numpy
print(a)
print(type(a))  #type is numpy.ndarray

b = np.array([[1,2,3],[4,5,6]], dtype='float') #creating a 2D array using numpy
print(b)

zero = np.zeros((3,3)) #creating an array of zeros, rows=3, columns=3
print(zero)

ones = np.ones((4,2)) #creating an array of ones,  rows=4, columns=2
print(ones)

full = np.full((2,2), 5) #creating an array of 5, rows=2, columns=2
print(full)

range_array = np.arange(0,10,2) #creating an array of range 0 to 10 with step 2, not include the last/ending point
print(range_array)

line_space = np.linspace(0,10,5) #creating an array of 5 elements between 0 to 10
print(line_space)

print("properties of a NumPy Array")
# properties of array "b = np.array([[1,2,3],[4,5,6]]), uncomment below 2 lines to explore 3D and 4D arrays
# b = np.array([[[0,1],[2,3]],[[4,5],[6,7]]]) # this is a 3D array
# b = np.array([[[[0,1],[2,3]],[[4,5],[6,7]]],[[[8,9],[10,11]],[[12,13],[14,15]]]]) # this is a 4D array
print(f"Dimension of array b {b.ndim}") #dimension of the array
print("Shape of Array b: {0}".format(b.shape)) #shape of the array
print("size of the array b {0}".format(b.size)) #size of the array
print(f"data Type of array b {b.dtype}") #data type of the array


#reshaping the array
print(f"Array Before Reshape {b}")
print ("Array After Reshape{0}".format(b.reshape(3,2))) #reshaping the array to 3 rows and 2 column
print ("Array After Reshape{0}".format(b.reshape(2,3))) #reshaping the array to 2 rows and 2 columns

# arithmetic operations using numpy
x = np.array([1,2,3])
y = np.array([4,5,6])
print(f"Addition of x and y: {x+y}")
print(f"Subtraction of x and y: {x-y}")
print(f"Multiplication of x and y: {x*y}")
print(f"Division of x and y: {x/y}")
print(f"Square of y: {y**2}")
# square root of y
sqrt = np.sqrt(y)
print(f"Square root of y: {sqrt}")
dot_product = np.dot(x,y) #dot product of x and y
print(f"Dot Product of x and y: {dot_product}")

sin = np.sin(x) #sin of x
print(f"Sin of x: {sin}")

cos = np.cos(y) #cos of y
print(f"Cos of y: {cos}")      
import numpy as np

# Create a 1D array
print("1D array")
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print("Shape is: ", arr1.shape)
print("nDIM is: ", arr1.ndim)
print("Size is: ", arr1.size)

#create a 2D array
print("\n2D array")
arr2 = np.array([[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10]])
print(arr2)
print("Shape is: ", arr2.shape)
print("nDIM is: ", arr2.ndim)
print("Size is: ", arr2.size)

# array > array with 3 arrays
#         array with 3 arrays
print("\nMulti Dimension Array")
arr3 = np.array([[[1, 2], [3, 4], [3, 4]],
                 [[6, 7], [8, 9], [8, 9]]])
print(arr3)
print("Shape is: ", arr3.shape)
print("nDIM is: ", arr3.ndim)
print("Size is: ", arr3.size)
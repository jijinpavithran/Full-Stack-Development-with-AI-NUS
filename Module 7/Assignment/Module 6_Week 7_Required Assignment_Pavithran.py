import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 1. Introduction to NumPy and ndarray (8 Marks) 
    # a) Create a 2-dimensional NumPy array of shape (3, 3) with elements of type float64. 
    # b) Perform element-wise addition of the array with a scalar value of 10. 
    # c) Perform element-wise multiplication with another 3x3 NumPy array. 
    # d) Print the dtype, shape, and size for each of the two result arrays.

array1 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]], dtype=np.float64)
print("Original Array:")
print(array1)   

array_add = array1 + 10
print("Addition Result:")
print(array_add)

array2 = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0], [3.0, 2.0, 1.0]], dtype=np.float64)
array_mul = array1 * array2
print("Multiplication Result:")
print(array_mul)

print("Addition Result:")
print("dtype:", array_add.dtype)
print("shape:", array_add.shape)
print("size:", array_add.size)

print("\nMultiplication Result:")
print("dtype:", array_mul.dtype)
print("shape:", array_mul.shape)
print("size:", array_mul.size)



# 2. Data Cleaning and Missing Values Handling (6 Marks) 
    # a) Create a DataFrame with missing values (NaN) in several columns. 
    # b) Use Pandas functions to identify missing values using isna() or isnull() 
    # c) Use Pandas functions to drop rows with any missing data using dropna(). 
    # d) Use Pandas functions to fill missing values with a specified value (e.g., mean or 0) using fillna(). 

data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# b) Use Pandas functions to identify missing values using isna() or isnull()
missing_values = df.isna()
print("\nMissing Values:")
print(missing_values)

# c) Use Pandas functions to drop rows with any missing data using dropna()
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with any missing data:")
print(df_dropped)

# d) Use Pandas functions to fill missing values with a specified value (e.g., mean or 0) using fillna()
df_filled = df.fillna(0)
print("\nDataFrame after filling missing values with 0:")
print(df_filled)

# Alternatively, filling missing values with the mean of the column
df_filled_mean = df.apply(lambda col: col.fillna(col.mean()), axis=0)
print("\nDataFrame after filling missing values with column mean:")
print(df_filled_mean)



#  3. Matplotlib Visualisation (6 Marks) 
    # a) Create a simple line plot showing the change in the value of a variable over time (you can generate data). 
    # b) Add labels to the x-axis, y-axis, and a title. 
    # c) Customise the line plot by changing the colour, marker style, and line width. 
    # d) Create a scatter plot to show the relationship between two numerical variables (e.g., age vs. income).


    # a) Create a simple line plot showing the change in the value of a variable over time (you can generate data).
time = np.arange(0, 10, 1)
value = np.sin(time)
plt.figure(figsize=(10, 5))

    # b) Add labels to the x-axis, y-axis, and a title.
plt.plot(time, value, color='blue', marker='o', linewidth=2, label='sin(time)')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Change in Value over Time')
plt.legend()

 # c) Customise the line plot by changing the colour, marker style, and line width.
plt.grid(True)
plt.show()

 # d) Create a scatter plot to show the relationship between two numerical variables (e.g., age vs. income).
age = np.random.randint(20, 60, size=30)
income = np.random.randint(30000, 100000, size=30)

plt.figure(figsize=(10, 5))
plt.scatter(age, income, color='red', marker='x')
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Age vs. Income')
plt.grid(True)
plt.show()
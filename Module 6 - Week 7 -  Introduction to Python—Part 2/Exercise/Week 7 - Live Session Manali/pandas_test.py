import pandas as pd
# one-dimensional labeled array know as series in pandas
data = [10, 20, 30, 40, 50] 
s = pd.Series(data) # index will be 0, 1, 2, 3, 4
print(s)

s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e']) # index will be a, b, c, d, e
print(s)

s = pd.Series(data)
s.index = ['A', 'B', 'C', 'D', 'E'] # index will be A, B, C, D, E
print(s)


# multi-dimensional labeled array know as DataFrame in pandas
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'],
    'Age': [25, 26, 27, 28, 29],
    'Salary': [30000, 40000, 50000, 60000, 70000]
}
d = pd.DataFrame(data)  # index will be 0, 1, 2, 3, 4
print(d)

d = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e']) # index will be a, b, c, d, e
print(d)

d= pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'], columns=['Name', 'Age']) # index will be a, b, c, d, e
print(d)

d = pd.DataFrame(data)  
d.index = ['A', 'B', 'C', 'D', 'E'] # index will be A, B, C, D, E
print(d)

print("Information about DataFrame") 
print(d.info())     #information about DataFrame

print("Description about DataFrame")    
print(d.describe()) # description about DataFrame integer columns only/ statistics summary

print(d.columns) # column names
print(d.index)   # index names
print(d.values)  # values of DataFrame
print(d.shape)   # shape of DataFrame

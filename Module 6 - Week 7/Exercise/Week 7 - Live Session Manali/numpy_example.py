import numpy as np
# row = days , column = cities
temps= np.array([
    [31, 32, 37],
    [33, 36, 34],
    [31, 32, 32],
    [35, 32, 31],
    [31, 32, 33],
    [32, 34, 36],
    [31, 32, 33]
])
print(temps)
# max temperature of each city
print(np.max(temps, axis=0)) # axis = 0 means column

temp_mean = np.mean(temps,axis=0)
print(temp_mean)
coldest_city = np.argmin(temp_mean)
print(coldest_city)

Hottest_city = np.argmax(temp_mean)
print(Hottest_city)

# max temperature of each day  
print(np.max(temps, axis=1)) # axis = 1 means row

above35 = np.where(temps>=35)
print(above35)

sorted_array = np.sort(temps, axis=0)
print(sorted_array)

sorted_array = np.sort(temps)
print(sorted_array)
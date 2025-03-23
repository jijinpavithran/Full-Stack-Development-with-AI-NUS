import pandas as pd


calories = {"day1": 420, "day2": 380, "day3": 390}
mycalories = pd.Series(calories)
print(mycalories)

mycalories = pd.Series(calories, index=["day1", "day2"])
print(mycalories)

mydataset = {
    'calories': ["420", "380", "390"],
    'duration': [50, 40, 45]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

myvar = pd.DataFrame(mydataset, index=["day1", "day2", "day3"])
print(myvar)





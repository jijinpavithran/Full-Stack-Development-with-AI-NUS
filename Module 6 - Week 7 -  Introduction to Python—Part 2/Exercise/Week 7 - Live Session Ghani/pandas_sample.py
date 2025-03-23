import pandas as pd


file = pd.read_csv("D:\\1.Full Stack Development with AI NUS\\Module 7\\Exercise\\Week 7 - Live Session Ghani\\TestData.csv") 
pd.options.display.max_rows=99
print(file.to_string())

remove_na = file.dropna()
print(remove_na.to_string())

print(file.dropna(inplace=True))


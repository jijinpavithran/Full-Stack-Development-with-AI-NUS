import pandas as pd

# df = pd.read_csv('D:\\1. Full Stack Development with AI NUS\\Module 7\\Exercise\\Week 7 - Live Session Manali\\csv_test.csv') # Read the csv file
# print(df) # Print the dataframe

try:
    df = pd.read_csv("D:\\1.Full Stack Development with AI NUS\\Module 7\\Exercise\\Week 7 - Live Session Manali\\csv_test.csv")  
    print(df)
except FileNotFoundError:
    print("Error: csv_test.csv not found. Please check the file name.")
except Exception as e:
    print(f"An error occurred: {e}")
df_copy = df
df = df.groupby('Department')['Sales'].sum()    # Group by Department and sum the Sales
print (df)

df = df_copy
df = df.groupby('Department').agg({'Sales': 'sum', 'Project_Completed': 'sum'}) # Group by Department and sum the Sales and Project_Completed
print(df)

df = df_copy
ans = df[df['Sales'] == df['Sales'].max()]['Employee'] # Find the Employee with the highest Sales
print(ans)

df = df_copy
df = df.groupby('Department')['Hours_Worked'].mean() # Group by Department and find the mean of Hours_Worked
print(df)

df = df_copy
ans = df[df['Hours_Worked']>40]['Employee'].tolist() # Find the Employees who worked more than 40 hours
print(ans)
# 1. Variables and Data Types (5 Marks) 
# Write a Python program that: 
#     a) Declares variables for storing a user’s name, age, and height. 
#     b) Prints a greeting message using the name. 
#     c) Calculates the user’s age 10 years from now. 
#     d) Displays height in meters by converting height from centimetres.
name = "Jijin"  # variable to store name
age = 25        # variable to store age
height = 180    # variable to store height in centimeters

print("Hello {}!".format(name)) # greeting message using the name
age+=10                 # age + 10
print("{0} will be {1} years old after 10 years from now.".format(name, age)) # age 10 years from now
height = height/100     # height in meters
print(f"{name} is {height} meters tall.") 



# 2. Conditional Statements (5 Marks) 
# Write a Python program that: 
#     a) Prompts the user to enter a number. 
#     b) Checks if the number is positive, negative, or zero. 
#     c) Prints an appropriate message based on the result. 
input_number = float(input("Enter a number: ")) # prompt the user to enter a number
if(input_number>0):
    print(f"The number {input_number} is positive.")
elif(input_number<0):
    print(f"The number {input_number} is negative.")
else:
    print(f"The number {input_number} is zero.")



# 3. Loops and Iteration (5 Marks) 
# Write a program that: 
#     a) Prompts the user to input an integer nnn. 
#     b) Uses a for loop to print all even numbers from 1 up to nnn. 
#     c) Ensures only even numbers appear in the output.

int_value = int(input("Enter an integer between 1 to nnn: ")) # prompt the user to enter an integer from 1 to nnn
for i in range(1, int_value+1):
    if(i%2==0):     # condition to check the number is even
        print(i)    # print all even numbers from 1 up to nnn




# 4. Functions (5 Marks)
# Write a program that: 
    # a) Defines a function to calculate the area of a rectangle using length and width as inputs. 
    # b) Prompts the user to input values for length and width. 
    # c) Calls the function to calculate and then displays the area in a formatted message. 

def calcuate_rect_area(length, width):  # function to calculate the area of a rectangle
    return length*width

rect_length = float(input("Enter the length of the rectangle: ")) # prompt the user to enter the length 
rect_width = float(input("Enter the width of the rectangle: "))   # prompt the user to enter the width

rect_area = calcuate_rect_area(rect_length, rect_width) # function call to calculate the area
print(f"The area of a rectangle with length {rect_length} unit and width {rect_width} unit is {rect_area} unit square.") # display the area in a formatted message
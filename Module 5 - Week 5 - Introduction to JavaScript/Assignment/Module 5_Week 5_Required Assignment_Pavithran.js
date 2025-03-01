/*
    1. Variable Declaration and Data Types (5 Marks) 
        a) Declare variables to store your name (string), age (number), and isStudent (boolean). 
        b) Assign appropriate values to each variable, for example: name = "Alice", age = 22, isStudent = true. 
        c) Use console.log() to display each variable along with its data type. 
*/
let name = "Alice";
let age = 22;
let isStudent = true;

console.log("Name: " + name + " - Type:" + typeof(name));
console.log("Age: " + age + " - Type:" + typeof(age));
console.log("Is Student: "+ isStudent + " - Type:" + typeof(isStudent));


/*
    2. Conditional Statements in JavaScript (5 Marks) 
        Write a JavaScript program that uses if-else and switch statements to make decisions based on user input. 
        a) Prompt the user to enter a number and store it in a variable. 
        b) Write an if-else statement to check if the number is positive, negative, or zero. 
        c) Display the appropriate message based on the condition. 
*/
let number = prompt("Enter a Number");
let msg = "'"+ number + "' is ";
if(number == 0)
{
    console.log(msg+="ZERO");
    alert(msg);
}    
else if(number < 0)
{
    console.log(msg+="Negative Number");
    alert(msg);
}
else if(number > 0) 
{
    console.log(msg+="Positive Number");
    alert(msg);
}
else
{
    console.log(msg+="NOT a valid Number");
    alert(msg);
}


/*
    3. Loops and Arrays (5 Marks) 
    Write a JavaScript program that demonstrates the use of a for loop. 
        a) Create an array named fruits that contains four different fruit names. 
        b) Use a for loop to iterate through each element in the array. 
        c) Log each fruit name to the console. 
*/
var fruits = ["Apple", "Banana", "Orange", "Grapes"];
for(let n = 0; n<fruits.length; n++)
{
    console.log(fruits[n]);
}


/*
    4. Functions and Scope (5 Marks) 
    Write a function in JavaScript that takes two parameters (numbers), multiplies them together, and returns the result. 
        a) Create a JavaScript function called calculateArea. 
        b) This function should take two parameters: length and width. 
        c) It should return the area of a rectangle. 
        d) Call this function with sample values and display the result.
*/ 
let length = 10;
let width = 20;
console.log("Area of Rectangle with Length: "+ length + " and Width: "+ width + " is " + calculateArea(length, width));
function calculateArea(length, width)
{
    return length * width;
}
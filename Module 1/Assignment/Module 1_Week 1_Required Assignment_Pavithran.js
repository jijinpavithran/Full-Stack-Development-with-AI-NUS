/*** 1. Variables and Data Types (5 Marks): ***
        a) In JavaScript, declare a variable x and assign the value 10 to it. 
        b) Then, declare another variable y with the value "Hello" and concatenate both values, storing the result in a new variable result. 
        c) Finally, print the result to the console using console.log.
*/
let x = 10;     // Declared a variable named 'x' and assigned/initialized it with value 10

let y = "Hello";// Declared a variable named 'y' and assigned/initialized it with value "Hello".
let result = x + " " + y;   // Declared a variable named 'result', concatenates the values of variables 'x' and 'y' with a space in between and stores the resulting string in the variable 'result'

console.log(result);        // Print the result into the console


/*** 2. Control Flow (5 Marks): ***
    Write the code and explain how the if-else statement works in your program. 
    a) Write a JavaScript program that checks if a number is even or odd. 
    b) If the number is even, print "Even" to the console. 
    c) If the number is odd, print "Odd" to the console.
*/
for(let nNum = 1; nNum<5; nNum++) // Declared for loop that iterates through a sequence of numbers from 1 to 4 using variable 'nNum' 
{
    console.log("Number '" + nNum + "' is: ")  // Printing which number is checking now
    if(nNum%2 == 0)             // checks if the variable 'nNum' is even by verifying if it is divisible by 2 with no remainder
        console.log("Even");    // Print 'Even' on screen
    else                        // Else - (if the number is not Even) the number is Odd
        console.log("Odd");     // Print 'Odd' on screen
}



/*** 3. Functions (5 Marks): ***
    Write the code and explain how functions help in reusing code. 
    a) Write a function in JavaScript named greetUser that takes a parameter name. 
    b) The function should print "Hello, [name]!" to the console. Call the function three times with different names (e.g., Alice, Bob, Charlie).
*/
function greetUser(name)    // Created a function named 'greetUser' with a parameter 'name'
{
    console.log("Hello, " + name + "!");   // Print "Hello, [name]!" to the console
}
// Invoke the function 'greetUser' 3 times with different names, 1st Call with 'Alice', 2nd call with 'Bob' and final call with 'Charlie'
greetUser("Alice");
greetUser("Bob");
greetUser("Charlie");
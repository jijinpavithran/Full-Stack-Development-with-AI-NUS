// 1. Comparison Operators
var a = 5;
var b = 10;
if(a==b) 
    console.log("a and b are equal");

if(a!=b)
    console.log("a and b are not equal");

if(a>b)
    console.log("a is greater than b");

if(a>=b)
    console.log("a is greater than or equal to b ");

if(a<b)
    console.log("a is less than than b");

if(a<=b)
    console.log("a is less than or equal to b ");



// 2. Logical Operators
var x = true;
var y = true;

if(x && y)
    console.log("x AND y are TRUE");

if(x | y)
    console.log("x OR y are/is TRUE");

if(!x == false)
    console.log("NOT Operation");

if(x == y)
    console.log("x and y are equal");
else 
    console.log("x and y are NOT equal");

// Iterative Conditional Flow
var i = 0;
while (i<5)
{
    console.log(i);
    i++;
}
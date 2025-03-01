function function_name(){
    // code here defined variable with in the function
    // it can only be used in the function (function scope)
}

// const: constant variable, it stay the same value/constant declare the variable and give value to ir
// const: variable that can't be reassign, can't declare a variable the with same name as const
const x =10; 

// let: variable that can be changed, can reassign, can declare a variable with the same name as let
let a;
a=10;

const eggPrice = 5;
const breadPrice = 10;
const total = eggPrice + breadPrice;
console.log(total);

const name = "John";
const age = 20;
const address = "Jakarta";

document.getElementById("demo").innerHTML = "My Name is " + name + ", I am " + age + " years old " + "and I live in " + address;
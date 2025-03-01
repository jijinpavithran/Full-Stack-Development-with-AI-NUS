function greet(){
    console.log("Hi All");
}

function greet(name){
    console.log("Hello " + name + "!")
}

function add(a, b)
{
    return(a+b);
}

greet();

greet("Alice");
greet("Bob");
var c = "Charlie";
greet(c);

console.log(add(2,3));
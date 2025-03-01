console.log("Hello World");
let fruits=["Apple","Mango","Orange", "Banana"];
console.log(fruits);
console.log(fruits[0]);
console.log(fruits[1]);
console.log(fruits[2]);
console.log(fruits[3]); 
console.log(fruits.length);

fruits.sort();
for(let i=0;i<fruits.length;i++){
    console.log(fruits[i]);
}

fruits.push("Pineapple");
console.log(fruits);
fruits.pop();
console.log(fruits);


let count = 0;
let countEl = document.getElementById("count-el");
let saveEl = document.getElementById("save-el");
let bCountChanged = false;
function increment(){
    count++;
    countEl.innerText = count;
    console.log(count);
    bCountChanged = true;
}


function save(){
    if(!bCountChanged)
        return;
    let countStr = count + " - ";
    saveEl.innerHTML += countStr;
    bCountChanged = false;
}

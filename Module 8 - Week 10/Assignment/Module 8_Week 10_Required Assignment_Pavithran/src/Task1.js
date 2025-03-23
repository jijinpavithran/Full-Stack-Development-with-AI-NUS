// Q1. Handling Events in React (5 marks) 
// a) Create a simple component with a button labeled “Toggle Message.” 
// b) When the button is clicked, toggle a message on the screen that says “Hello, welcome to React!” 
//      This message should disappear when the button is clicked again.

import { useState } from "react";
export default function Task1() {
    const [state, setState] = useState(false);
    const toggleMessage = () => {
        setState(!state);
    };
return(
    <div>
        <button onClick={toggleMessage}>Toggle Message</button>
        {state && <h1>Hello, welcome to React!</h1>}
    </div>
);
}
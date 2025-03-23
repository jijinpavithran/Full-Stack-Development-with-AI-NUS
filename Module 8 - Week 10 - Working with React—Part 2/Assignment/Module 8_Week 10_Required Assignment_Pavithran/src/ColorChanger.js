// Q2. State Management using React Hooks (8 marks)
//      a) Build a component called ColorChanger. This component should have a text input where users can enter a colour name (e.g., “blue”). 
//      b) The component should display a box that changes colour based on the input. 
//      c) As the user types into the input, the box should automatically update to the new colour if it’s a valid colour name. 

import { useState } from "react";
import { useEffect } from "react";
import './ColorChanger.css';

export default function ColorChanger() {
const [color,setColor] = useState('');
const coloChangeHanlder = (e)=>{
    setColor(e.target.value);
}
useEffect(() => {
    document.querySelector('.Box').style.backgroundColor = color;
}, [color]);

    return(
        <div>
            <label htmlFor="color">Enter a color:</label>
            <br/>
            <input name="color" onChange={coloChangeHanlder}/>
            <div className='Box'></div>
        </div>
    );
}
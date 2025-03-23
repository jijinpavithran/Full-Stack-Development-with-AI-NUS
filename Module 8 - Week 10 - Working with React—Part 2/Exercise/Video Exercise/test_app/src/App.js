import logo from './logo.svg';
import {useState} from 'react';
import './App.css';

function App() {
  const [count, setCount] = useState(10);
 const[name, setName] = useState('');
  const onClickHandlerIn = ()=>{
    setCount(count+1);
  }

  const onClickHandlerDe = ()=>{
    setCount(count-1);
  }

  console.log('rendering');
  return (
    // <div className="App">
    //   <header className="App-header">
    //     <img src={logo} className="App-logo" alt="logo" />
    //     <p>
    //       Edit <code>src/App.js</code> and save to reload.
    //     </p>
    //     <a
    //       className="App-link"
    //       href="https://reactjs.org"
    //       target="_blank"
    //       rel="noopener noreferrer"
    //     >
    //       Learn React
    //     </a>
    //   </header>
    // </div>

    <div>
      <h1>{count}</h1>
      <br/>
      <button onClick={onClickHandlerIn}> Increment</button>
      <br/>
      <br/>
      <button onClick={onClickHandlerDe}> Decrement</button>
      <button onClick={()=>{setCount(count+1);}}> Increment++</button>

      {name!="" && <h1>Hello {name}</h1>} 
      <label id="label1" htmlFor="fname">Enter Your Name:</label>
      <input name="fname" value={name} onChange={(e)=>{setName(e.target.value);}}/> 
    </div>

  );
}

export default App;

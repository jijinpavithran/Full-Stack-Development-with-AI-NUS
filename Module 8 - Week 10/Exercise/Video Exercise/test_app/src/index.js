import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
const root = ReactDOM.createRoot(document.getElementById('root'));
const arr = ['a', 'b', 'c'];
const disable = false;
const obj = {
  backgroundColor: 'green',
  padding: '10px',
  color: 'white',
  display: 'inline-block',
}

function myClick()
{
  console.log('clicked');
}

const a = <div id ="my_hello" className='class-name' style = {obj} onClick={myClick}>HELLO</div>;
//const a =React.createElement('div', {id : "my_hello2"}, 'HELLO2');
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
// a
);

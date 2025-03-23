import Task1 from "./Task1";
import ColorChanger from "./ColorChanger";
import UserProfile from "./UserProfile";
function App() {
  const array = [1, 2, 3, 4, 5];
  return (
    <div className="App">
    <Task1 />
    <br />
    <br />
    <ColorChanger />
    <br />
    <br />
    <UserProfile id={1} />
    <UserProfile id={2} />
    <UserProfile id={3} />  
    <UserProfile id={4} />  
    </div>
  );
}

export default App;

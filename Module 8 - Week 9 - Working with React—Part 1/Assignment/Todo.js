// 4. Use JSX for Structuring Components (5 Marks) 
export default function Todo(props) {
    return (
        <div>
            <h3>My To-Do List</h3>
            <ul>
                {props.items.map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>
        </div>
    );
}
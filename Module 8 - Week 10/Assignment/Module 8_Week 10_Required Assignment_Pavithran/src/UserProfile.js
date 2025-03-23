// 3. Asynchronous Data Fetching with AJAX (7 marks)
// a) Create a UserProfile component that fetches user data from an API (for example, https://jsonplaceholder.typicode.com/users/1) and displays the user’s name, email, and address on the page. 
// b) Display a loading message while data is being fetched. 

import './UserProfile.css';

import { useState, useEffect } from 'react';

export default function UserProfile(props) {
const url = "https://jsonplaceholder.typicode.com/users/" + props.id;
const [user, setUser] = useState(null);
const [loading, setLoading] = useState(true);

useEffect(() => {
    setLoading(true);
    fetch(url).
    then(response => response.json()).
    then(data => {setUser(data); 
        console.log(data);
        setLoading(false);});
    }, 
    [url]);
    
    if (loading) {
        return <div>Loading...</div>;
    }

    if (!user) {
        return <div>No user data available.</div>;
    }

    return (
        <div className='outter-box'>
            <h1 className='user-name'>{user.name}</h1>
            <div className="user-details">
                <h3>Email: {user.email}</h3>
                {user.address && (
                <div>
                <h3>Address:</h3>
                    <p>Street: {user.address.street}</p>
                    <p>Suite: {user.address.suite}</p>
                    <p>City: {user.address.city}</p>
                    <p>Zipcode: {user.address.zipcode}</p>
                </div>
                )}

            </div>
        </div>
    );
}
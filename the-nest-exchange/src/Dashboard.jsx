import React, { useState, useEffect } from 'react';

const Dashboard = () => {
    const [user, setUser] = useState({ name: 'John Smith', offers: 0, watchers: 0 });

    useEffect(() => {
        // Simulate fetching user data from an API
        const fetchUserData = async () => {
            // Replace with your API call
            const data = await Promise.resolve({ offers: 5, watchers: 2 });
            setUser(prevState => ({ ...prevState, ...data }));
        };
        fetchUserData();
    }, []);

    return (
        <div>
            <h1>My Dashboard</h1>
            <img src="profile-pic-url" alt="Profile" />
            <h2>{user.name}</h2>
            <h3>Activity</h3>
            <div>
                <div>Offers: {user.offers}</div>
                <div>Watchers: {user.watchers}</div>
            </div>
        </div>
    );
}

export default Dashboard;
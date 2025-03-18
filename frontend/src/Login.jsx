import React, { useState } from 'react';
import './Login.css'; 

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle login logic here (e.g., API call)
    console.log('Email:', email, 'Password:', password);
  };

  return (
    <div className="login-container">
      <h2>The Nest Exchange</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="KSU Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Sign in</button>
        <button type="button">Sign up</button>
        <a href="#">Forget Password?</a>
      </form>
    </div>
  );
};

export default Login;
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Login from './Login';

function App() {
  //const [count, setCount] = useState(0)

  return (
    <div className="App">
       <header>
        The Nest Exchange
      </header>
      <div className="content">
        <Login />
      </div>
    </div>
  )
}

export default App;

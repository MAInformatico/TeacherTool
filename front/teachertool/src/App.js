import logo from './logo.svg';
import './App.css';
import React from 'react';
import Header from './components/header.js';
import Form from './components/form.js';
import './components/form.css';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Header />
        <img src={logo} className="App-logo" alt="logo" />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Teacher Tool
        </a>
        <p>Con esta herramienta puedes evaluar exámenes de inglés. Esta herramienta está en desarrollo.</p>
        <Form />
      </header>
    </div>
  );
}

export default App;

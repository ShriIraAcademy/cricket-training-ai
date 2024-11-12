// src/App.js
import React from 'react';
import './App.css';
import PredictionForm from './PredictionForm';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>Cricket Training Recommendations</h1>
            </header>
            <PredictionForm />
        </div>
    );
}

export default App;

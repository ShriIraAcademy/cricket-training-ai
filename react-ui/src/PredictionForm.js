// src/PredictionForm.js
import React, { useState } from 'react';
import axios from 'axios';

const PredictionForm = () => {
    const [inputData, setInputData] = useState("");
    const [prediction, setPrediction] = useState(null);
    const [error, setError] = useState(null);

    // Handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);  // Clear previous errors

        // Prepare data for the API request
        const data = {
            input_data: inputData.split(",").map(Number), // Convert comma-separated input to an array of numbers
        };

        try {
            // Send a POST request to the Django API
            const response = await axios.post("http://127.0.0.1:8000/api/predict/", data);
            setPrediction(response.data.prediction); // Update prediction state
        } catch (err) {
            setError("An error occurred. Please check your input and try again.");
        }
    };

    return (
        <div>
            <h2>TensorFlow Model Prediction</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Enter input data (comma-separated):
                    <input
                        type="text"
                        value={inputData}
                        onChange={(e) => setInputData(e.target.value)}
                    />
                </label>
                <button type="submit">Get Prediction</button>
            </form>

            {error && <p style={{ color: "red" }}>{error}</p>}

            {prediction && (
                <div>
                    <h3>Prediction Result:</h3>
                    <pre>{JSON.stringify(prediction, null, 2)}</pre>
                </div>
            )}
        </div>
    );
};

export default PredictionForm;

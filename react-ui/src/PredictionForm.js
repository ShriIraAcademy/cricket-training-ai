// src/PredictionForm.js
import React, { useState } from 'react';
import axios from 'axios';

const PredictionForm = () => {
    // const [inputData, setInputData] = useState("");
    const [age, setAge] = useState("");
    const [height, setHeight] = useState("");
    const [weight, setWeight] = useState("");
    const [prediction, setPrediction] = useState(null);
    const [error, setError] = useState(null);
    const [trainingSegment, setTrainingSegment] = useState("Batting");
    const [skillLevel, setSkillLevel] = useState("Beginner");
    const [bowlingType, setBowlingType] = useState("Fast Bowler");

    // Handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);  // Clear previous errors

        // Prepare data for the API request
        const data = {
            // input_data: inputData.split(",").map(Number), // Convert comma-separated input to an array of numbers
            // input_data: inputData.split(",").map((i) => [i]), // Convert comma-separated input to an array of numbers
            input_data: [[height], [weight], [Math.round(weight / ((height / 100) ** 2))], [age]],
        };

        try {
            // Send a POST request to the Django API
            const response = await axios.post("http://127.0.0.1:8000/api/predict/", data);
            // setPrediction(response.data.prediction); // Update prediction state
            setPrediction(response.data.top_shots); // Update prediction state
        } catch (err) {
            setError("An error occurred. Please check your input and try again.");
        }
    };

    const trainingSegmentOptions = [
        { value: "Batting", label: "Batting" },
        { value: "Bowling", label: "Bowling" },
    ];

    const skillLevelOptions = [
        { value: "Beginner", label: "Beginner" },
        { value: "Intermediate", label: "Intermediate" },
        { value: "Expert", label: "Expert" },
    ];

    const bowlingTypeOptions = [
        { value: "Fast Bowler", label: "Fast Bowler" },
        { value: "Off Spinner", label: "Off Spinner" },
        { value: "Leg Spinner", label: "Leg Spinner" },
    ];

    
  // Recommendations data
  const battingRecommendations = {
    "Beginner": {
        "Shots to Learn": [
            { "shot": "Front Foot Defense", "reference": "https://youtu.be/HEHggOOds1w?si=jbks8CGKhagDGzJC" },
            { "shot": "Back Foot Defense", "reference": "https://youtu.be/sKIwkvdAyJU?si=N8TPs0mfG8bj1i79" }
        ],
        "Guidance": ["Start with basic stance and grip.", "Practice hand-eye coordination drills."],
        "Fitness": ["Agility drills", "Core strengthening"]
    },
    // Add more levels...
};

const bowlingRecommendations = {
    "Fast Bowler": {
        "Beginner": {
            "Key Skills": [{ "Grip": "Basic accuracy", "Stance": "Run-up control" }],
            "Guidance": ["Practice basic delivery strides.", "Work on line and length."],
            "Fitness": ["Strengthen lower body", "Sprint intervals"]
        },
        // Add more bowler types...
    }
};

    return (
        <div>
            {/* <h2>TensorFlow Model Prediction</h2> */}
            <form onSubmit={handleSubmit}>
                {/* <label>
                    Enter input data (comma-separated):
                    <input
                        type="text"
                        value={inputData}
                        onChange={(e) => setInputData(e.target.value)}
                    />
                </label> */}
                <label>
                    Age:
                    <input
                        type="text"
                        value={age}
                        onChange={(e) => setAge(e.target.value)}
                    />
                </label>
                <label>
                Height (cm):
                    <input
                        type="text"
                        value={height}
                        onChange={(e) => setHeight(e.target.value)}
                    />
                </label>
                <label>
                Weight (kg):
                    <input
                        type="text"
                        value={weight}
                        onChange={(e) => setWeight(e.target.value)}
                    />
                </label>
                <label>
                Select Training Segment:
                    <select
                        value={trainingSegment}
                        onChange={(e) => setTrainingSegment(e.target.value)}
                    >
                        {trainingSegmentOptions.map((option) => (
                            <option key={option.value} value={option.value}>
                                {option.label}
                            </option>
                        ))}
                    </select>
                </label>
                
                <label>
                Select Skill Level:
                    <select
                        value={skillLevel}
                        onChange={(e) => setSkillLevel(e.target.value)}
                    >
                        {skillLevelOptions.map((option) => (
                            <option key={option.value} value={option.value}>
                                {option.label}
                            </option>
                        ))}
                    </select>
                </label>

                <label>
                Select Bowling Type:
                    <select
                        value={bowlingType}
                        onChange={(e) => setBowlingType(e.target.value)}
                    >
                        {bowlingTypeOptions.map((option) => (
                            <option key={option.value} value={option.value}>
                                {option.label}
                            </option>
                        ))}
                    </select>
                </label>
                <button type="submit">Get Recommendations</button>
            </form>

            {error && <p style={{ color: "red" }}>{error}</p>}

            {prediction && (
                <div>
                    <h3>Training Recommendations:</h3>
                    {/* <pre>{JSON.stringify(prediction, null, 2)}</pre> */}
                    <ul>
                    {
                        prediction.map((i) => <li key={i.name}>{i.name} : <a href={i.videolink} target="_blank">{i.videolink}</a></li>)
                    }
                    </ul>
                    
                </div>
            )}
        </div>
    );
};

export default PredictionForm;

document.getElementById("trainingForm").addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent form from submitting

  // Get user input
  const age = parseInt(document.getElementById("age").value);
  const height = parseInt(document.getElementById("height").value);
  const weight = parseInt(document.getElementById("weight").value);
  const segment = document.getElementById("segment").value;
  const skillLevel = document.getElementById("skill_level").value;
  const bowlerType = document.getElementById("bowler_type").value;

  // Assess weight (Simple BMI-like calculation)
  const minWeight = 18.5 * (height / 100) ** 2;
  const maxWeight = 24.9 * (height / 100) ** 2;

  let weightMessage = "";
  if (weight < minWeight || weight > maxWeight) {
      weightMessage = `Your weight is outside the recommended range (${Math.round(minWeight)} - ${Math.round(maxWeight)} kg). Consider a balanced fitness program.`;
  }

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

  // Determine recommendations based on the input
  let recommendations = {};
  if (segment === "Batting") {
      recommendations = battingRecommendations[skillLevel];
  } else {
      recommendations = bowlingRecommendations[bowlerType][skillLevel];
  }

  // Display recommendations
  document.getElementById("recommendations").style.display = "block";
  document.getElementById("skill_level_result").innerText = `Skill Level: ${skillLevel}`;
  document.getElementById("shots_to_learn").innerHTML = `
      <strong>Shots to Learn:</strong><br>
      ${recommendations["Shots to Learn"].map(item => `<a href="${item.reference}" target="_blank">${item.shot}</a>`).join("<br>")}
  `;
  document.getElementById("guidance").innerHTML = `
      <strong>Guidance:</strong><br>
      ${recommendations["Guidance"].join("<br>")}
  `;
  document.getElementById("fitness").innerHTML = `
      <strong>Fitness Recommendations:</strong><br>
      ${recommendations["Fitness"].join("<br>")}
  `;
  
  // Optional: Display video link for further reference
  const firstShot = recommendations["Shots to Learn"][0];
  document.getElementById("video_link").href = firstShot.reference;
  document.getElementById("video_link").style.display = "block";

  // Show weight message if applicable
  if (weightMessage) {
      alert(weightMessage);
  }
});

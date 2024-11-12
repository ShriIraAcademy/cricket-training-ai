import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Sample dataset for training the placeholder model

file_path = "/content/generated_cricket_dataset.xlsx"
data = pd.read_excel(file_path)

# Convert data to DataFrame
df = pd.DataFrame(data)
X = df[['age', 'height', 'weight']]
y_batting = df['batting_ability']
y_bowling = df['bowling_ability']

# Split data into training and testing sets
X_train, X_test, y_train_batting, y_test_batting = train_test_split(X, y_batting, test_size=0.2, random_state=42)
X_train, X_test, y_train_bowling, y_test_bowling = train_test_split(X, y_bowling, test_size=0.2, random_state=42)

# Train Random Forest models for batting and bowling skill prediction
batting_model = RandomForestClassifier(random_state=42)
bowling_model = RandomForestClassifier(random_state=42)
batting_model.fit(X_train, y_train_batting)
bowling_model.fit(X_train, y_train_bowling)

# Batting and Bowling Recommendations with References
batting_recommendations = {
    "Beginner": {
        "Shots to Learn": [
            {"shot": "Front Foot Defense", "reference": "https://youtu.be/HEHggOOds1w?si=jbks8CGKhagDGzJC"},
            {"shot": "Back Foot Defense", "reference": "https://youtu.be/sKIwkvdAyJU?si=N8TPs0mfG8bj1i79"},
            {"shot": "Straight Drive", "reference": "https://youtu.be/8eb68_qqFHM?si=L0Xa_KumkS4XUVtL"},
            {"shot": "Pull Shot", "reference": "https://youtu.be/g_Y_y4OHm1o?si=ubW4JUqPB2gCF7oP"}
        ],
        "Guidance": [
            "Start with basic stance and grip.",
            "Practice hand-eye coordination drills with slow balls.",
            "Work on simple footwork techniques to develop balance.",
            "Use lightweight bats initially to focus on control."
        ],
        "Fitness": [
            "Basic agility drills", "Core strengthening exercises", "Short sprints"
        ]
    },
    "Intermediate": {
        "Shots to Learn": [
            {"shot": "Cover Drive", "reference": "https://youtu.be/JgGf_5LY6qA?si=R7ORIuyv67rz3HlJ"},
            {"shot": "Square Cut", "reference": "https://youtu.be/eVF_m_GaT1Y?si=hvEMd0EazqR3zXkw"},
            {"shot": "On Drive", "reference": "https://youtu.be/IKz1u5H1Jik?si=3PonEX4jsNNR9Mi2"},
            {"shot": "Hook Shot", "reference": "https://youtu.be/quvpwDBViFg?si=mE8pFOkWLZ72q_d7"}
        ],
        "Guidance": [
            "Enhance footwork and body rotation for power shots.",
            "Practice timing and shot selection in the nets.",
            "Focus on finding gaps and building runs strategically.",
            "Engage in reflex training to handle faster deliveries."
        ],
        "Fitness": [
            "Stamina drills (running, cycling)", "Shoulder and arm strength training"
        ]
    },
    "Expert": {
        "Shots to Learn": [
            {"shot": "Late Cut", "reference": "https://youtu.be/uY0HkBsUaOA?si=vKMDhhKKGJww-ZS7"},
            {"shot": "Scoop Shot", "reference": "https://youtu.be/sYkw-US0tEU?si=_1WBvo9dfSnXIGM6"},
            {"shot": "Reverse Sweep", "reference": "https://youtu.be/iWOD_jqJkvA?si=Sw1g6qa8O6yQog17"},
            {"shot": "Upper Cut", "reference": "https://youtu.be/jWLdZDBFZao?si=s-XXNkB80JVqajpw"}
        ],
        "Guidance": [
            "Adapt to advanced bowlers and varying pitch conditions.",
            "Perfect shot improvisation techniques.",
            "Work on adaptability, balance, and risk assessment.",
            "Practice under simulated match conditions."
        ],
        "Fitness": [
            "Advanced endurance training", "Explosive strength exercises", "Core stability"
        ]
    }
}

bowling_recommendations = {
    "Fast Bowler": {
        "Beginner": {
            "Key Skills": [
                {"Grip": "Basic bowling accuracy", "Stance": "Run-up control"}
            ],
            "Guidance": [
                "Practice grip and release basics with tennis balls.",
                "Focus on building a consistent run-up and delivery stride.",
                "Use target practice for line and length control."
            ],
            "Fitness": ["Strengthen lower body", "Basic sprint intervals", "Core stability"],
            "reference": "https://youtu.be/TQRA8vXyShw?si=YmbEbqt9-Yez_TUM"
        },
        "Intermediate": {
            "Key Skills": [
                {"Swing": "in-swing and out-swing", "Seam positioning": "Accuracy"}
            ],
            "Guidance": [
                "Practice seam positioning for swing bowling.",
                "Focus on endurance training and faster run-ups.",
                "Develop control over line and length with regular drills."
            ],
            "Fitness": ["Sprinting for stamina", "Weight training", "Leg strength drills"],
            "reference": "https://youtube.com/shorts/9ehJf2vd-lo?si=qLX-QqZE9BwgmrNy"
        },
        "Expert": {
            "Key Skills": [
                {"Reverse swing": "Yorkers", "Variation deliveries": "Slower balls, bouncers"}
            ],
            "Guidance": [
                "Master reverse swing with appropriate wrist positioning.",
                "Practice yorkers and strategic variations.",
                "Focus on game tactics and bowling psychology."
            ],
            "Fitness": ["High-intensity cardio", "Core and upper body strength", "Explosive sprinting"],
            "reference": "https://youtube.com/shorts/HMX70moeF2g?si=fBTL8kFCiIh2pMo3"
        }
    },
    "Off Spinner": {
        "Beginner": {
            "Key Skills": [
                {"Basic spin technique": "Flight control"}
            ],
            "Guidance": [
                "Practice finger positioning for spin control.",
                "Focus on achieving a smooth and consistent action.",
                "Target line and length using small practice cones."
            ],
            "Fitness": ["Arm strengthening", "Basic shoulder mobility", "Light cardio"],
            "reference": "https://youtube.com/shorts/MSSREXGtZJ8?si=ErVzUAvD01tis5Bl"
        },
        "Intermediate": {
            "Key Skills": [
                {"Flight control": "Accuracy"}
            ],
            "Guidance": [
                "Master the basics of flight and drift.",
                "Practice using small variations like the arm ball.",
                "Work on controlling length and pace."
            ],
            "Fitness": ["Core strengthening", "Shoulder endurance training", "Agility drills"],
            "reference": "https://youtu.be/GwRgTMkmn1w?si=WSE_VywGdQFvw_LN"
        },
        "Expert": {
            "Key Skills": [
                {"Doosra": "Carrom ball", "Strategic placement": "Line and length"}
            ],
            "Guidance": [
                "Perfect complex variations like the doosra and carrom ball.",
                "Adapt bowling to different pitch and weather conditions.",
                "Focus on game strategy and understanding batter behavior."
            ],
            "Fitness": ["Advanced shoulder stability", "Core stability", "Quick footwork drills"],
            "reference": "https://youtu.be/DSmB046Nk2Q?si=6jYwrA0w6Rhd36y7"
        }
    },
    "Leg Spinner": {
        "Beginner": {
            "Key Skills": [
                {"Basic leg-spin": "Grip"}
            ],
            "Guidance": [
                "Focus on leg-spin grip and release techniques.",
                "Work on accuracy and consistency with cones.",
                "Use light balls for practicing spin control."
            ],
            "Fitness": ["Arm exercises", "Wrist strengthening", "Short cardio"],
            "reference": "https://youtu.be/NZuAwj3q-JM?si=IEV6mzreFeValaie"
        },
        "Intermediate": {
            "Key Skills": [
                {"Flipper": "Accuracy"}
            ],
            "Guidance": [
                "Practice flippers and top-spins.",
                "Refine accuracy and consistency.",
                "Improve mental focus on delivery."
            ],
            "Fitness": ["Core stability", "Shoulder mobility", "Quick steps and pivots"],
            "reference": "https://youtu.be/HdwgYTjvwXE?si=QQaK9mizhRGIeday"
        },
        "Expert": {
            "Key Skills": [
                {"Googly": "Slider"}
            ],
            "Guidance": [
                "Master complex deliveries such as googly and slider.",
                "Adapt bowling style to exploit batter weaknesses.",
                "Focus on field placement and bowler-batter strategy."
            ],
            "Fitness": ["Explosive strength", "Leg strengthening", "Agility drills"],
            "reference": "https://youtu.be/e2IJaW1InyA?si=K31jdAIPndoWIpFd"
        }
    }
}

def assess_weight(height, weight):
    # Determine approximate healthy weight range (e.g., BMI range of 18.5-24.9)
        # Approximate values here; more detailed ranges can be obtained through analysis.
    min_weight = 18.5 * (height / 100) ** 2
    max_weight = 24.9 * (height / 100) ** 2
    if weight > max_weight:
        return False, f"Your weight is above the recommended range ({int(min_weight)}-{int(max_weight)} kg). Consider a weight management program alongside skill training."
    return True, None

def get_user_input():
    age = int(input("Enter your age: "))
    height = int(input("Enter your height (in cm): "))
    weight = int(input("Enter your weight (in kg): "))

    weight_ok, weight_msg = assess_weight(height, weight)
    if not weight_ok:
        print(f"\n{weight_msg}")
        print("Recommended activities: jogging, interval training, core workouts, and balanced diet guidance.")

    print("\nChoose the training segment:")
    print("1 - Batting\n2 - Bowling")
    segment_choice = int(input("Enter 1 for Batting or 2 for Bowling: "))

    if segment_choice == 1:
        print("\nSelect your batting ability level:")
        print("1 - Beginner\n2 - Intermediate\n3 - Expert")
        skill_level_choice = int(input("Enter the number for your skill level: "))
        skill_level = {1: "Beginner", 2: "Intermediate", 3: "Expert"}.get(skill_level_choice, "Beginner")
        return age, height, weight, "Batting", skill_level, None

    elif segment_choice == 2:
        print("\nSelect the type of bowler:")
        print("1 - Fast Bowler\n2 - Off Spinner\n3 - Leg Spinner")
        bowler_type_choice = int(input("Enter the number for your bowling type: "))
        bowler_type = {1: "Fast Bowler", 2: "Off Spinner", 3: "Leg Spinner"}.get(bowler_type_choice, "Fast Bowler")

        print("\nSelect your bowling ability level:")
        print("1 - Beginner\n2 - Intermediate\n3 - Expert")
        skill_level_choice = int(input("Enter the number for your skill level: "))
        skill_level = {1: "Beginner", 2: "Intermediate", 3: "Expert"}.get(skill_level_choice, "Beginner")
        return age, height, weight, "Bowling", skill_level, bowler_type

def display_recommendations(segment, skill_level, bowler_type=None):
    if segment == "Batting":
        rec = batting_recommendations[skill_level]
        print(f"\nBatting Skill Level: {skill_level}")
        print("\nSkills to Develop:")
        for skill in rec["Shots to Learn"]:
            print(f"- {skill['shot']} (Reference: {skill['reference']})")
    else:
        rec = bowling_recommendations[bowler_type][skill_level]
        print(f"\nBowling Type: {bowler_type}\nBowling Skill Level: {skill_level}")
        print("\nSkills to Develop:")
        for skill_dict in rec["Key Skills"]:  # Iterate through the list of dictionaries
            for skill_name, skill_desc in skill_dict.items():  # Iterate through key-value pairs in each dictionary
                print(f"- {skill_name}: {skill_desc}")  # Print the skill name and description

    print("\nGuidance:")
    for guide in rec["Guidance"]:
        print(f"- {guide}")

    print("\nFitness Recommendations:")
    for fit in rec["Fitness"]:
        print(f"- {fit}")
# Run the program
age, height, weight, segment, skill_level, bowler_type = get_user_input()
display_recommendations(segment, skill_level, bowler_type)

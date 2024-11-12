import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Concatenate
from tensorflow.keras.models import Model
from sklearn.model_selection import train_test_split

# Example data
n_samples = 10000
n_shots = 10  # Number of unique cricket shots (e.g., cover drive, pull, sweep, etc.)
n_features = 4  # Height, weight, BMI, and age

# Generate synthetic data for demonstration
np.random.seed(42)
heights = np.random.uniform(150, 200, n_samples)  # Heights in cm
weights = np.random.uniform(50, 100, n_samples)   # Weights in kg
bmi = weights / ((heights / 100) ** 2)            # Calculate BMI
ages = np.random.uniform(18, 65, n_samples)       # Ages from 18 to 65

# Simulate ratings for all shots by all users
ratings = np.random.randint(1, 6, (n_samples, n_shots))  # Ratings from 1 to 5 for each cricket shot

# Split data into training and testing
train_heights, test_heights, train_weights, test_weights, train_bmi, test_bmi, train_ages, test_ages, train_ratings, test_ratings = train_test_split(
    heights, weights, bmi, ages, ratings, test_size=0.2, random_state=42
)

# Define the model
def create_model(n_shots, n_factors=50):
    # Inputs for person characteristics
    height_input = Input(shape=(1,), name="height")
    weight_input = Input(shape=(1,), name="weight")
    bmi_input = Input(shape=(1,), name="bmi")
    age_input = Input(shape=(1,), name="age")
    
    # Concatenate personal characteristics
    person_features = Concatenate()([height_input, weight_input, bmi_input, age_input])
    
    # Dense layers to process features
    dense1 = Dense(64, activation="relu")(person_features)
    dense2 = Dense(32, activation="relu")(dense1)
    
    # Output layer for predicting ratings for each cricket shot
    output = Dense(n_shots, activation="linear")(dense2)  # Predict a rating for each cricket shot
    
    # Create model
    model = Model(inputs=[height_input, weight_input, bmi_input, age_input], outputs=output)
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    return model

# Instantiate the model
model = create_model(n_shots)

# Train the model
history = model.fit(
    [train_heights, train_weights, train_bmi, train_ages],
    train_ratings,
    validation_data=([test_heights, test_weights, test_bmi, test_ages], test_ratings),
    epochs=10,
    batch_size=32,
    verbose=1
)

# Evaluate the model
test_loss, test_mae = model.evaluate([test_heights, test_weights, test_bmi, test_ages], test_ratings)
print(f"Test MSE: {test_loss:.4f}, Test MAE: {test_mae:.4f}")

# Make predictions for a new user (height, weight, bmi, age) and recommend top cricket shots
new_user = np.array([[175], [70], [22], [30]])  # Example input for a new user with age included
predicted_ratings = model.predict([new_user[0], new_user[1], new_user[2], new_user[3]])

# Get top 5 recommended cricket shots
top_shots = np.argsort(predicted_ratings[0])[::-1][:5]  # Sort by rating and get top 5 shots
print("Top recommended cricket shots indices:", top_shots)


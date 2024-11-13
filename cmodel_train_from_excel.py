import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Concatenate
from tensorflow.keras.models import Model
from sklearn.model_selection import train_test_split

# Load data from Excel file
file_path = "Extended_Cricket_Shot_Dataset.xlsx"  # Path to your Excel file
data = pd.read_excel(file_path)

# Separate features and ratings
heights = data["height"].values
weights = data["weight"].values
bmi = data["bmi"].values
ages = data["age"].values
ratings = data.iloc[:, 4:].values  # Assuming ratings start from the fifth column onward

# Define the number of unique cricket shots based on the columns in the Excel file
n_shots = ratings.shape[1]  # Number of cricket shots

# Split data into training and testing sets
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


model.save('tf_project/saved_model.keras')
# Make predictions for a new user (height, weight, bmi, age) and recommend top cricket shots
new_user = np.array([[175], [70], [22], [30]])  # Example input for a new user with age included
predicted_ratings = model.predict([new_user[0], new_user[1], new_user[2], new_user[3]])

# Get top 5 recommended cricket shots
top_shots = np.argsort(predicted_ratings[0])[::-1][:5]  # Sort by rating and get top 5 shots
print("Top recommended cricket shots indices:", top_shots)


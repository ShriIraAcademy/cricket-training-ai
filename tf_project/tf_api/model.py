# tf_api/model.py
import tensorflow as tf

# Load the pre-trained TensorFlow model
model = tf.keras.models.load_model('saved_model.keras')

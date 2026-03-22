from tensorflow.keras.models import load_model
import numpy as np
from utils import preprocess_image

# Load trained model
model = load_model("model/digit_model.h5")

# Path to image
image_path = "images/digit.png"

# Preprocess image
img = preprocess_image(image_path)

# Predict
prediction = model.predict(img)
digit = np.argmax(prediction)

print(f"🧠 Predicted Digit: {digit}")
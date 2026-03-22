import cv2
import numpy as np

def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize to 28x28
    img = cv2.resize(img, (28, 28))

    # Invert colors (white background -> black)
    img = 255 - img

    # Normalize
    img = img / 255.0

    # Reshape for model
    img = img.reshape(1, 28, 28, 1)

    return img
import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("model/digit_model.h5")

# Create main window
root = tk.Tk()
root.title("Handwritten Digit Recognition")
root.geometry("400x500")
root.configure(bg="black")

# Canvas setup
canvas_width = 300
canvas_height = 300
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack(pady=20)

# PIL image to draw on
image1 = Image.new("L", (canvas_width, canvas_height), color=255)
draw = ImageDraw.Draw(image1)

# Draw function
def paint(event):
    x1, y1 = (event.x - 8), (event.y - 8)
    x2, y2 = (event.x + 8), (event.y + 8)
    canvas.create_oval(x1, y1, x2, y2, fill="black")
    draw.ellipse([x1, y1, x2, y2], fill=0)

canvas.bind("<B1-Motion>", paint)

# Clear canvas
def clear():
    canvas.delete("all")
    draw.rectangle([0, 0, canvas_width, canvas_height], fill=255)
    label.config(text="Draw a digit")

# Predict function
def predict():
    # Resize to 28x28
    img = image1.resize((28, 28))
    img = np.array(img)

    # Normalize
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)

    # Predict
    prediction = model.predict(img)
    digit = np.argmax(prediction)

    label.config(text=f"Prediction: {digit}")

# Buttons
btn_predict = tk.Button(root, text="Predict", command=predict, bg="green", fg="white", font=("Arial", 14))
btn_predict.pack(pady=10)

btn_clear = tk.Button(root, text="Clear", command=clear, bg="red", fg="white", font=("Arial", 14))
btn_clear.pack()

# Result label
label = tk.Label(root, text="Draw a digit", bg="black", fg="white", font=("Arial", 18))
label.pack(pady=20)

# Run app
root.mainloop()
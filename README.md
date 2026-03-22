🧠 Handwritten Digit Recognition System
A high-accuracy Handwritten Digit Recognition project built using Deep Learning (CNN) and the MNIST dataset, featuring an interactive drawing canvas UI for real-time predictions.
________________________________________
🚀 Demo Features
✨ Draw digits (0–9) using mouse
🧠 Predict digit instantly using trained CNN model
🎯 Achieves ~98–99% accuracy
🧹 Clear canvas and redraw
⚡ Fast and lightweight desktop application
________________________________________
🛠️ Tech Stack
•	Python 
•	TensorFlow / Keras 
•	NumPy 
•	OpenCV 
•	Tkinter (GUI) 
•	Pillow (Image Processing)
📂 Project Structure
digit-recognition/
│
├── train.py              # Train CNN model
├── predict.py            # Predict from image
├── utils.py              # Image preprocessing
├── canvas_app.py         # Drawing canvas UI
├── requirements.txt      # Dependencies
├── README.md
├── model/                # Saved model (ignored in GitHub)
└── images/               # Sample/test images
________________________________________

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/Margisha2403/handwritten-digit-recognition.git
cd handwritten-digit-recognition
2️⃣ Install Dependencies
pip install -r requirements.txt
________________________________________
▶️ Usage
🔹 Step 1: Train Model
python train.py
🔹 Step 2: Run Drawing App
python canvas_app.py
🔹 Step 3: Draw & Predict
•	Draw any digit (0–9) 
•	Click Predict 
•	View result instantly 
________________________________________
🧠 Model Details
•	Model Type: Convolutional Neural Network (CNN) 
•	Dataset: MNIST 
•	Input Shape: 28x28 grayscale images 
•	Accuracy: ~98–99% 
________________________________________
📌 Key Highlights
✔ Real-time handwritten digit prediction
✔ User-friendly GUI using Tkinter
✔ High accuracy with optimized CNN
✔ Clean and modular code structure


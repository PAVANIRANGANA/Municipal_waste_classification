## ♻️ CleanTech: Transforming Waste Management with Transfer Learning

CleanTech is an AI-powered web application designed to classify and manage waste efficiently using image recognition. It leverages **Transfer Learning with VGG16** to predict different types of waste (like plastic, paper, organic, etc.) from uploaded images. Built with Flask, CleanTech provides a simple user interface for users to contribute toward cleaner and smarter waste disposal systems.

 🚀 Features

- 🔍 **Image-based Waste Prediction** using a trained VGG16 model.
- 💻 **User-friendly Interface** with a clean design.
- 📂 **Upload Functionality** to test predictions.
- 📊 **Result Page** showing classification outcome.
- 🖼️ Organized **static assets and templates**.
- 🧠 Transfer learning implementation using Keras.

🗂️ Project Structure
CleanTech/
│
├── static/
│ ├── assets/ # Images for UI
│ ├── css/styles.css # Styling
│ ├── forms/ # (Future use)
│ └── uploads/ # Uploaded images for prediction
│
├── templates/
│ ├── home.html
│ ├── about.html
│ ├── contact.html
│ ├── predict.html
│ ├── result.html
│ └── index.html
│
├── app.py # Main Flask application
├── create_model.py # Code to train/save VGG16 model
├── vgg16.h5 # Pretrained model file
├── ipython.html # (Optional dev/test file)
├── Readme.txt # Project notes (original)
└── README.md # This file

📸 How to Use
Go to the Predict page.

Upload an image of waste.

The model classifies it (e.g., plastic, paper).

See results on the Result page.

![Screenshot 2025-06-27 205255](https://github.com/user-attachments/assets/9ba5e293-e76c-4061-8946-9491e75eefed)

![Screenshot 2025-06-27 205355](https://github.com/user-attachments/assets/d1accfd6-7068-42ad-b17e-ee459716eb7c)

![Screenshot 2025-06-27 205441](https://github.com/user-attachments/assets/c5a870ee-e5ee-49ed-8597-458d75351585)








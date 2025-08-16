# ♻️ CleanTech: Transforming Waste Management with Transfer Learning

CleanTech is an AI-powered web application designed to classify and manage waste efficiently using image recognition. It leverages **Transfer Learning with VGG16** to predict different types of waste (like Biodegradable, Non-Biodegradable) from uploaded images. Built with Flask, CleanTech provides a simple user interface for users to contribute toward cleaner and smarter waste disposal systems.

## 📑 Table of Contents
- [🚀 Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📦 Installation](#-installation)
- [💡 Usage](#-usage)
- [🗂️ Project Structure](#️-project-structure)
- [🤝 Contributing](#-contributing)
- [🔗 Important Links](#-important-links)
- [📝 Footer](#-footer)

## 🚀 Features
- 🔍 **Image-based Waste Prediction**: Uses a trained VGG16 model to classify waste images.
- 💻 **User-friendly Interface**: Provides a clean and intuitive design for easy interaction.
- 📂 **Upload Functionality**: Allows users to upload images of waste for classification.
- 📊 **Result Page**: Displays the classification outcome with a confidence level.
- 🖼️ **Organized Assets**: Includes well-structured static assets (CSS, images) and HTML templates.
- 🧠 **Transfer Learning**: Implements transfer learning using Keras.

## 🛠️ Tech Stack
- 🐍 **Python**: The primary programming language.
- ⚙️ **Flask**: A micro web framework for building the web application.
- 🧠 **TensorFlow/Keras**: Used for building and training the VGG16 model.
- 🖼️ **HTML/CSS**: For creating the user interface.

## 📦 Installation
1.  **Clone the repository:**
   ```bash
   git clone https://github.com/PAVANIRANGANA/Municipal_waste_classification.git
   cd Municipal_waste_classification
   ```
2.  **Install dependencies:**
   ```bash
   pip install flask tensorflow pillow
   ```
3.  **Ensure the model file** `vgg16.h5` is in the root directory.
4.  **Run the app:**
   ```bash
   python app.py
   ```
5.  **Visit** `http://127.0.0.1:5000` in your browser.

## 💡 Usage
1.  **Navigate to the Predict page**: Access the `/predict` route in your browser.
2.  **Upload an image of waste**: Use the file upload form to select an image from your local machine.
3.  **View the classification result**: The application will display the predicted class (Biodegradable or Non-Biodegradable) and the confidence level on the Result page.

### Use Case Example

Imagine a recycling plant using CleanTech to automate the sorting of municipal waste. An image of the waste is captured and uploaded to the application. The VGG16 model classifies the waste as either biodegradable or non-biodegradable. This information helps the plant efficiently sort the waste, reducing manual labor and increasing the accuracy of the recycling process.

## 🗂️ Project Structure
```
CleanTech/
│
├── static/
│   ├── assets/ # Images for UI
│   ├── css/styles.css # Styling
│   ├── forms/ # (Future use)
│   └── uploads/ # Uploaded images for prediction
│
├── templates/
│   ├── home.html
│   ├── about.html
│   ├── contact.html
│   ├── predict.html
│   ├── result.html
│   └── index.html
│
├── app.py # Main Flask application
├── create_model.py # Code to train/save VGG16 model
├── vgg16.h5 # Pretrained model file
├── ipython.html # (Optional dev/test file)
├── Readme.txt # Project notes (original)
└── README.md # This file
```

## 🤝 Contributing
Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.


## 🔗 Important Links
- Demo Video : [https://drive.google.com/file/d/1mlbgCVl_DWnBuqn8M7kIv5pWr8kNHPUF/view?usp=drive_link](https://drive.google.com/file/d/1mlbgCVl_DWnBuqn8M7kIv5pWr8kNHPUF/view?usp=drive_link)

## 📝 Footer

- Repository Name: Municipal_waste_classification
- Repository URL: [https://github.com/PAVANIRANGANA/Municipal_waste_classification](https://github.com/PAVANIRANGANA/Municipal_waste_classification)
- Author: PAVANIRANGANA

⭐ Like this project? Give it a star on [GitHub](https://github.com/PAVANIRANGANA/Municipal_waste_classification)!

 Fork the Repository to start your own project !

 For issues and feature requests, raise an issue in the repository.

from flask import Flask, render_template, request, redirect, url_for
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
model = load_model("vgg16.h5")

classes = ['Biodegradable', 'Non-Biodegradable']

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        img_file = request.files["image"]
        if img_file:
            filename = img_file.filename
            image_path = f"uploads/{filename}"
            full_path = os.path.join("static", image_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            img_file.save(full_path)

            # Preprocess image
            img = image.load_img(full_path, target_size=(224, 224))
            img_tensor = image.img_to_array(img)
            img_tensor = np.expand_dims(img_tensor, axis=0)
            img_tensor = img_tensor / 255.

            prediction = model.predict(img_tensor)
            predicted_class = classes[np.argmax(prediction)]
            confidence = np.max(prediction) * 100
            result = f"{predicted_class} ({confidence:.2f}%)"

            return redirect(url_for("result", img=image_path, res=result))
    return render_template("predict.html")

@app.route("/result")
def result():
    img = request.args.get("img")
    res = request.args.get("res")
    return render_template("result.html", image_path=img, result=res)

if __name__ == '__main__':
    app.run(debug=True)

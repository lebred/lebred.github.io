import os
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import pytesseract

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"

if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    if "prescription_image" not in request.files:
        return redirect(url_for("home"))

    file = request.files["prescription_image"]
    if file.filename == "":
        return redirect(url_for("home"))

    if file:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # Use Tesseract to extract text
        image = Image.open(filepath)
        extracted_text = pytesseract.image_to_string(image)

        return render_template("index.html", text=extracted_text)


if __name__ == "__main__":
    app.run(debug=True)

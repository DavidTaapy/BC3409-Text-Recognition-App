# Import Libraries
from flask import Flask, render_template, request
from textblob import TextBlob

# Initialise Flask Application
app = Flask(__name__)

# App Route
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("Text")
        result = TextBlob(text).sentiment
        return render_template("index.html", result = result)
    else:
        return render_template("index.html", result = "Please enter text!")

# Run Application
if __name__ == "__main__":
    app.run()
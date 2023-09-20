from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(r"index.html")


if name == "main":
    app.run(debug=False, port=5000)
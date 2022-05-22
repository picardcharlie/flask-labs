from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"Welcome to Zombo.com 2.0"

@app.route("/about")
def about():
    return f"<p>For far too long has Zombo.com been away!</p><p>    <em>welcome to our new and improved</em> website, offering the latest in our services.</p>"

@app.route("/links")
def links():
    return f'<p><a href="/">Index</a></p><p><a href="/about">About</a></p>'

@app.route("/user/<name>/<age>")
def user(name,age):
    return f"Hello {name}, fellow {age} year old human."

@app.route("/numeric_dynamic/<square>")
def numeric(square):
    return f"{int(square) ** 2} is the square of {square}."

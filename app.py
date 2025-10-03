# save this as app.py
from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, World!"

@app.route("/hola")
def hola():
    return "Hola, Mundo!"

if __name__ == "__main__":
    app.run(debug=True)
    
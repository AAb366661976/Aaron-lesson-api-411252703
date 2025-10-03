# save this as app.py
from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, World!"

@app.route("/hola")
def hola():
    return "Hola, Mundo!"

@app.route("/user/<string:username>",methods=['GET'])
def show_user_profile(username):
    print('type(username)=> ',type(username))
    return 'String => {}'.format (username)

if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)

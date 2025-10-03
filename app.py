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

@app.route("/user/<int:id>",methods=['GET'])
def show_user_id(id):
    print('type(id)=> ',type(id))
    return 'Int => {}'.format (id)

@app.route("/user/<float:version>",methods=['GET'])
def show_user_version(version):
    print('type(version)=> ',type(version))
    return 'Float => {}'.format (version)

@app.route("/appinfo")
def show_appinfo():
    return "<html><body><h1>APPINFO</h1></body></html>"

@app.route("/htmlinfo")
def show_htmlinfo():
    return """
    <html>
        <head>
            <title>HTML INFO</title>
        </head>
        <body>
            <h1>HTML INFO</h1>
            <p>This is a paragraph.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)

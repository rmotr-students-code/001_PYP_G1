import os
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world(): # /
    return 'Hello World!'


@app.route('/hello/<name>/')
def hello_name(name=None):
    app.logger.info("Path requested: %s", request.path)
    app.logger.info("Client IP addr: %s", request.remote_addr)
    app.logger.info("Method used: %s", request.method)
    return 'Hello ' + name
"""
/method


GET > "Hello, you are requesting data"
POST > "Hello, you're posting data"

"""

"""
/login

<form>
<label>Username: </label><input type='text' name='username'>
<input type='submit' value='Login'>
</form>
"""


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return renderForm()
    elif request.method == "POST":
        user = request.form['username']
        return "hello %s" % user

def renderForm():
    return "<form method='post' action='/login/'><label>Username: </label><input type='text' name='username'><input type='submit' value='Login'></form>"


@app.route('/method/', methods=['POST', 'GET'])
def check_method():
    if request.method == "GET":
        return "Hello, you are requesting data"
    elif request.method == "POST":
        return "Hello, you're posting data\n"


@app.route('/hello/')
def hello_yourself():
    return 'Hello yourself!'


if __name__ == "__main__":
    app.debug = True

    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.logger.info("Starting flask app on %s:%s", host, port)

    app.run(host=host, port=port)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Azure Web App!"

@app.route('/test1')
def test1():
    return "Welcome to the test1 page"

@app.route('/test2')
def test2():
    return "Welcome to the test2 page"
    
@app.route('/test3')
def test3():
    return "Welcome to the test3 page"

@app.route('/test4')
def test4():
    return "Welcome to the test4 page"

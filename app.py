from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Azure Web App!"

@app.route('/about')
def about():
    return "Welcome to the about page"

@app.route('/index')
def third():
    return "Welcome to the index page

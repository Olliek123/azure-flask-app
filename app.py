from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Azure Web App!"

@app.route('/about')
def about():
    return "about"

@app.route('/third')
def third():
    return "third"

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Oliver's Web App... wooo"

if __name__ == '__main__':
    app.run()

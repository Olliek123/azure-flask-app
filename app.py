from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Hello from Azure Web App!</h1>
        <p>/aboutGo to About Page</a></p>
    '''

@app.route('/about')
def about():
    return '''
        <h1>About Page</h1>
        <p>This is some information about the site.</p>
        <p>/Back to Home</a></p>
    '''

if __name__ == '__main__':
    app.run()

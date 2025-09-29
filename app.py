from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Hello and welcome to my website!</h1>
        /about<button>Go to About Page</button></a>
    '''

@app.route('/about')
def about():
    return '''
        <h1>About Page</h1>
        <p>This is a second page with some extra info.</p>
        /<button>Back to Home</button></a>
    '''

if __name__ == '__main__':
    app.run()

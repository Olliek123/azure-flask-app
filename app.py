from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <h1>Hello and welcome to my website!</h1>
        <a href="/abouto to About Page</button></a>
    ''')

@app.route('/about')
def about():
    return render_template_string('''
        <h1>About Page</h1>
        <p>This is a second page with some extra info.</p>
        /<button>Back to Home</button></a>
    ''')

if __name__ == '__main__':
    app.run(debug=True)

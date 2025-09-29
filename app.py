from flask import Flask, render_template_string
app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <h1>Hello and welcome to my website!</h1>
            <form action="/        <button type="submit">Go to About Page</button>
            </form>
        </body>
        </html>
    ''')

@app.route('/about')
def about():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>About</title>
        </head>
        <body>
            <h1>About Page</h1>
            <p>This is a second page with some extra info.</p>
            /
                <button type="submit">Back to Home</button>
            </form>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)


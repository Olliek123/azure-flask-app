from flask import Flask, request, render_template_string, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)

@app.route('/')
def home():
    return "Hello from Azure Web App!"

@app.route('/initdb')
def initdb():
    db.create_all()
    return "Database initialized!"

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            new_message = Message(text=text)
            db.session.add(new_message)
            db.session.commit()
            return redirect(url_for('submit'))
    messages = Message.query.all()
    return render_template_string("""
        <form method="post">
            <input name="text" type="text" placeholder="Type something..." required>
            <input type="submit" value="Submit">
        </form>
        <h3>Messages:</h3>
        <ul>
        {% for msg in messages %}
            <li>{{ msg.text }}</li>
        {% endfor %}
        </ul>
    """, messages=messages)

if __name__ == '__main__':
    app.run()

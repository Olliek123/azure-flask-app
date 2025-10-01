from flask import Flask, request, render_template_string
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Use environment variable for security (set this in Azure App Service)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the table model
class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    message = db.Column(db.String(200))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        new_msg = Message(name=name, message=message)
        db.session.add(new_msg)
        db.session.commit()
    
    messages = Message.query.all()
    return render_template_string("""
        <h1>Leave a Message</h1>
        <form method="post">
            Name: <input name="name"><br>
            Message: <input name="message"><br>
            <input type="submit" value="Submit">
        </form>
        <h2>Messages:</h2>
        {% for msg in messages %}
            <p><strong>{{ msg.name }}</strong>: {{ msg.message }}</p>
        {% endfor %}
    """, messages=messages)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/college_chatbot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class UserQuery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(200))
    response = db.Column(db.String(200))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    response = generate_response(user_message)
    new_query = UserQuery(query=user_message, response=response)
    db.session.add(new_query)
    db.session.commit()
    return jsonify({'response': response})

def generate_response(message):
    # For demo purposes, we'll just return a static response
    return "That's a great question!"

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

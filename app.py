from flask import Flask, jsonify, request
from mongoengine import Document, StringField
from db import initialize_db
from model import User



initialize_db()
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/register', methods=['POST'])
def register():
    data = request.json

    if 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Please provide both username and password'}), 400

    username = data['username']
    password = data['password']

    new_user = User(username=username, password=password)

    try:
        new_user.save()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        print("Error during user save:")
        print(e)
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True) 
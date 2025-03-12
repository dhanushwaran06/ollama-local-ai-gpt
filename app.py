from flask import Flask, render_template, request, jsonify
import mysql.connector
import ollama
from datetime import datetime

app = Flask(__name__)

# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'ollama_chat'
}

# Function to connect to MySQL
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Route to serve the UI
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle chat requests
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # Use the Ollama library to generate a response
    bot_response = ""
    for chunk in ollama.generate(
        model='gemma3:1b',  # Replace with your Ollama model name
        prompt=user_message,
        stream=True
    ):
        bot_response += chunk['response']
    
    # Store the conversation in MySQL
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO conversations (user_message, bot_response) VALUES (%s, %s)"
    cursor.execute(query, (user_message, bot_response))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
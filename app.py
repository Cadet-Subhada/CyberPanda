from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('chat.html')  # Create chat.html inside 'templates' folder

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data.get("query", "")
    response = {"response": f"You asked: {query}"}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

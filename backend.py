from flask import Flask, jsonify
from flask_cors import CORS
from query_data import query_data

app = Flask(__name__)
CORS(app, resources={r"/get_data": {"origins": "*", "methods": ["GET"], "allow_headers": ["Content-Type", "x-api-key"]}})

@app.route('/get_data')
def get_data():
    data = query_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

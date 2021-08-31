from flask import Flask
import os
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongo:27017")

@app.route('/')
def index():
    try:
        client.admin.command('ismaster')
    except:
        return "Server not available"
    return "Shop home page, the MongoDB client is running!\n"

@app.route('/phones/', methods=['POST'])
def create_phone():
    return "Under development"

@app.route('/phones/', methods=['GET'])
def read_phone():
    return "Under development"

@app.route('/phones/', methods=['PUT'])
def update_phone():
    return "Under development"

@app.route('/phones/', methods=['DELETE'])
def delete_phone():
    return "Under development"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
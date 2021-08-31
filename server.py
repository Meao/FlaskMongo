from flask import Flask, json, jsonify, request
import os
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongo:27017")
db = client['products']
collection = db['phones']

@app.route('/')
def index():
    try:
        client.admin.command('ismaster')
    except:
        return jsonify({'message': 'Server not available'})
    return jsonify({'status': '200', 'message': 'Shop home page, the MongoDB client is running!\n'})

@app.route('/api/phones/', methods=['POST'])
def create_phone():
    try:
        # look up if I need to check for sql injections in NoSql
        data = json.dumps(request.get_json())
    except:
        return "request unavailable", 400
    # check type of data!!!
    if isinstance(data, list):
        data_created = collection.insert_many(data)
        return data_created.inserted_ids, 201
    else:
        data_created = collection.insert_one(data).inserted_id
        return data_created, 201

@app.route('/api/phones/', methods=['GET'])
def read_phone():
    return "Under development"

@app.route('/api/phones/', methods=['PUT'])
def update_phone():
    return "Under development"

@app.route('/api/phones/', methods=['DELETE'])
def delete_phone():
    return "Under development"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
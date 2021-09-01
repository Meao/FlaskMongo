from flask import Flask, json, jsonify, request
import os
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongo:27017")
# how about initialising it with a test item and a decorator that only allows a func run once?
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
        data = request.get_json(force=True)
    except:
        return jsonify({'message': 'request unavailable'}), 400
    try:
        prod = {
            'name': data['name'],
            'description': data['description'],
            'parameters': data['parameters']
        }
        #     data_created = collection.insert_many(data)
        #     return data_created.inserted_ids, 201
        # else:
        data_created = collection.insert_one(prod).inserted_id
        return jsonify({'id assigned to new phone product': data_created}), 201
    except:
        return jsonify({'message': 'db error'})

@app.route('/api/phone/<id>', methods=['GET'])
def read_phone(id):
    try:
        data_fetched = collection.find_one({"_id": id})
        return json.dumps(data_fetched)
    except:
        return "No product found", 404

@app.route('/api/phones/', methods=['GET'])
def read_phones():
    try:
        data = json.dumps(request.get_json())
        result = {}
        if data:
            for product in collection.find(data):
    except:
        return "request unavailable", 400
        data_fetched = collection.find({"_id": id})
        return json.dumps(data_fetched)
    except:
        return "No product found", 404

@app.route('/api/phones/', methods=['PUT'])
def update_phone():
    return "Under development"

@app.route('/api/phones/', methods=['DELETE'])
def delete_phone():
    return "Under development"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
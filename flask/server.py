#!/usr/bin/env python
import os

from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
# client = MongoClient(os.environ['PRODUCTS_DB_1_PORT_27017_TCP_ADDR'],27017)
client = MongoClient("mongo:27017")
# # how about initialising it with a test item and a decorator that only allows a func run once?
# db = client['products']
# collection = db['phones']
db = client.productsdb


@app.route('/testdb/')
def testdb():
    try:
        restest = client.test_database
        resdb = []
        for db_info in client.list_database_names():
            resdb.append(db_info)
    except:
        return jsonify({'message': 'Server not available'})
    return jsonify({'test_database': restest, 
    'dbs': resdb})

@app.route('/')
def todoindex():
    try:
        client.admin.command('ismaster')
    except:
        return jsonify({'message': 'Server not available'})
    return jsonify({'status': '200', 'message': 'Shop home page, the MongoDB client is running!\n'})

@app.route('/api/phone/', methods=['POST'])
def create_phone():
    try:
        # look up if I need to check for sql injections in NoSql
        data = request.get_json(force=True)
    except:
        return jsonify({'message': 'request unavailable'}), 400
    try:
        # need to create a dict structure for params
        prod = {
            'name': data['name'],
            'description': data['description'],
            'parameters': data['parameters']
        }
        # data_created = collection.insert_one(prod).inserted_id
        data_created = db.productsdb.insert_one(prod)
        return jsonify({'id assigned to new phone product': data_created.inserted_id}), 201
    except:
        return jsonify({'message': 'db error'})

@app.route('/api/phone/<id>', methods=['GET'])
def read_phone(id):
    try:
        # data_fetched = collection.find_one({"_id": id})
        data_fetched = db.productsdb.find_one({"_id": id})
        # check if jsonify or json.dumps work fine
        return jsonify(data_fetched)
    except:
        return jsonify({'message': 'No product found'}), 404

@app.route('/api/phones/', methods=['GET'])
def read_phones():
    try:
        query_params = request.get_json(force=True)
        if query_params:
            # data_fetched = collection.find(query_params)
            data_fetched = db.productsdb.find(query_params)
            if data_fetched.count() > 0:
                return jsonify(data_fetched)
            else:
                return jsonify({'message': 'No products found'}), 404
        else:
            # data_fetched = collection.find()
            data_fetched = db.productsdb.find()
            if data_fetched.count() > 0:
                return jsonify(data_fetched)
            else:
                return jsonify({'message': 'No products in db'}), 404
    except:
        return jsonify({'message': 'request unavailable'}), 400
   
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)

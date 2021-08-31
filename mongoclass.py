from flask import Flask, json, Response, request
from pymongo import MongoClient
# https://ishmeet1995.medium.com/how-to-create-restful-crud-api-with-python-flask-mongodb-and-docker-8f6ccb73c5bc
class MongoAPI:
    def __init__(self, data):
        # create a MongoClient to the running mongod instance
        self.client = MongoClient("mongodb://localhost:27017/")  
        # If database name is such that using attribute style access won’t work (like test-database), you can use dictionary style access
        database = data['database']
        # A collection is a group of documents stored in MongoDB, and can be thought of as roughly the equivalent of a table in a relational database. 
        collection = data['collection']
        # Collections and databases are created when the first document is inserted into them.
        
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data

    def read(self):
        # find() returns a Cursor instance, which allows to iterate over all matching documents
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def write(self, data):
        log.info('Writing Data')
        new_document = data['Document']
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output

    def update(self):
        filt = self.data['Filter']
        # https://docs.mongodb.com/manual/reference/operator/update-field/
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self, data):
        filt = data['Document']
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output


if __name__ == '__main__':
    data = {
        "database": "ShopDB",
        "collection": "phones",
    }
    mongo_obj = MongoAPI(data)
    print(json.dumps(mongo_obj.read(), indent=4))
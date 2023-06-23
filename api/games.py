from flask import Flask, jsonify, request
from flask_restful import   Resource, Api
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
api = Api(app)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['game_list']
collection = db['games']

class Game(Resource):

    def get(self):
        data = list(collection.find())
        serialized_data = [{**doc, '_id': str(doc['_id'])} for doc in data]
        return jsonify(serialized_data)

    def post(self):
        data = request.get_json()
        collection.insert_one(data)
        print(data)
        return {
            'message':"Data Inserted Successfully"
        }
    
    def delete(self):
        data = request.get_json()
        collection.delete_one(data)
        return {
            'message':"Data Deleted Successfully"
        }

class GameList(Resource):
    def get(self, game_id):
        try:
            data = collection.find_one({'_id': ObjectId(game_id)})
            if data:
                serialized_data = {**data, '_id': str(data['_id'])}
                return jsonify(serialized_data)
            else:
                return {'message': 'Game not found'}, 404
        except (TypeError, ValueError):
            return {'message': 'Invalid game ID'}, 400
        

    def delete(self, game_id):
        try:
            collection.delete_one({'_id': ObjectId(game_id)})
            return {'message': 'Game deleted successfully'}, 200
        except (TypeError, ValueError):
            return {'message': 'Invalid game ID'}, 400
        

    def put(self, game_id):
        data = request.get_json()
        game_id = data.get('_id')
        if game_id:
            data['_id'] = ObjectId(game_id)
            collection.update_one({'_id': data['_id']}, {'$set': data})
            return {'message': "Data Updated Successfully"}
        else:
            return {'message': 'Invalid game ID'}, 400
        
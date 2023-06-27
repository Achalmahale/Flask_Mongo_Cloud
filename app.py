from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

flaskAppInstance = Flask(__name__)
api = Api(flaskAppInstance)

username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PASSWORD')
cluster_address = os.getenv('MONGODB_CLUSTER_ADDRESS')
database = os.getenv('MONGODB_DATABASE')

# connection_string = f'mongodb+srv://{username}:{password}@{cluster_address}/{database}?retryWrites=true&w=majority'
connection_string = "mongodb+srv://achalmahale:HVTJN0JGliUuJ1uI@flask.vwnr42n.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
db = client['game_list']
collection = db['games']

#Create a class using the Resource class from flask_restful
class Game(Resource):

    def get(self):
        data = list(collection.find())
        serialized_data = [{**doc, '_id': str(doc['_id'])} for doc in data]
        return jsonify(serialized_data)

    def post(self):
        data = request.get_json()
        result = collection.insert_one(data)
        inserted_id = str(result.inserted_id)  # Convert ObjectId to string
        print(data)
        return {
            'message': "Data Inserted Successfully",
            '_id': inserted_id
        }
    
# Create another class using the Resource class from flask_restful
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
        
    def put(self, game_id):
        try:
            data = request.get_json()
            updated_data = collection.find_one_and_update(
                {'_id': ObjectId(game_id)},
                {'$set': data},
                return_document=True
            )
            if updated_data:
                serialized_data = {**updated_data, '_id': str(updated_data['_id'])}
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
        


restServerInstance = Api(flaskAppInstance)
restServerInstance.add_resource(Game,"/games")
restServerInstance.add_resource(GameList,"/games/<string:game_id>")


if __name__ == '__main__':
    flaskAppInstance.run(debug=True, host="0.0.0.0", port=5000)


from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

# Creating a Flask app instance
flaskAppInstance = Flask(__name__)
api = Api(flaskAppInstance)

# Connecting to MongoDB
username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PASSWORD')
cluster_address = os.getenv('MONGODB_CLUSTER_ADDRESS')
database = os.getenv('MONGODB_DATABASE')
connection_string = f'mongodb+srv://{username}:{password}@{database}.{cluster_address}/?retryWrites=true&w=majority'
client = MongoClient(connection_string)

# Creating a database and collection instance
db = client['game_list']
collection = db['games']

#Create a class using the Resource class from flask_restful
class Game(Resource):

    # GET
    def get(self):
        data = list(collection.find())
        serialized_data = [{**doc, '_id': str(doc['_id'])} for doc in data]
        return jsonify(serialized_data)
    
    # POST
    def post(self):
        data = request.get_json()
        result = collection.insert_one(data)
        inserted_id = str(result.inserted_id)  # Convert ObjectId to string
        print(data)
        return {
            'message': "Data Inserted Successfully",
            '_id': inserted_id
        }

class SearchGame(Resource):
    @flaskAppInstance.route("/search")
    def search_games():
        name = request.args.get("name")  # Get the name parameter from the query string
        if name:
            data = list(collection.find({"name": name}))
            serialized_data = [{**doc, "_id": str(doc["_id"])} for doc in data]
            return jsonify(serialized_data)
        else:
            return {"message": "Please provide a name parameter"}, 400


    
# Create another class using the Resource class from flask_restful
class GameList(Resource):

    # GET by ID
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
        
    # PUT by ID        
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
        
    # DELETE by ID
    def delete(self, game_id):
        try:
            collection.delete_one({'_id': ObjectId(game_id)})
            return {'message': 'Game deleted successfully'}, 200
        except (TypeError, ValueError):
            return {'message': 'Invalid game ID'}, 400
        
    # PATCH by ID
    def patch(self, game_id):
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
    

# Adding the URL endpoints to the API
restServerInstance = Api(flaskAppInstance)
restServerInstance.add_resource(Game,"/games")
restServerInstance.add_resource(GameList,"/games/<string:game_id>")
restServerInstance.add_resource(SearchGame,"/search>")



if __name__ == '__main__':
    flaskAppInstance.run(debug=True, host="0.0.0.0", port=5000)
from flask_restful import Api
from app import flaskAppInstance

from .games import Game
from .games import GameList



restServerInstance = Api(flaskAppInstance)
restServerInstance.add_resource(Game,"/api/v1.0/games")
restServerInstance.add_resource(GameList,"/api/v1.0/games/<string:game_id>")

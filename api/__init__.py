from flask_restful import Api
from app import flaskAppInstance


from .TestAPI import Test
from .TestAPI_ID import TestID
from .games import Game
from .games import GameList
# from .games import GameTitle


restServerInstance = Api(flaskAppInstance)
restServerInstance.add_resource(Test,"/api/v1.0/test")
restServerInstance.add_resource(TestID,"/api/v1.0/test/id/<string:Test_ID>")
restServerInstance.add_resource(Game,"/api/v1.0/games")
restServerInstance.add_resource(GameList,"/api/v1.0/games/<string:game_id>")
# restServerInstance.add_resource(GameTitle,"/api/v1.0/games/<string:title>")


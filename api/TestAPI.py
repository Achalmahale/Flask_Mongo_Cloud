from flask_restful import Resource
import logging as logger

class Test(Resource):

    def post(self):
        logger.debug("Post in Test")
        return {"message" : "Post worked"}, 200

    def get(self):
        logger.debug("get in Test")
        return {"message" : "get worked"}, 200

    def put(self):
        logger.debug("put in Test")
        return {"message" : "put worked"}, 200

    def delete(self):
        logger.debug("delete in Test")
        return {"message" : "delete worked"}, 200

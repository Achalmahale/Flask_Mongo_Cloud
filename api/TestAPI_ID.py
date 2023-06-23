from flask_restful import Resource
import logging as logger

class TestID(Resource):

    def post(self,Test_ID):
        logger.debug("Post in Test_ID")
        return {"message" : "Post worked, Task_ID : {}".format(Test_ID)}, 200

    def get(self,Test_ID):
        logger.debug("get in Test_ID")
        return {"message" : "get worked Task_ID : {}".format(Test_ID)}, 200

    def put(self,Test_ID):
        logger.debug("put in Test_ID")
        return {"message" : "put worked Task_ID : {}".format(Test_ID)}, 200

    def delete(self,Test_ID):
        logger.debug("delete in Test_ID")
        return {"message" : "delete worked Task_ID : {}".format(Test_ID)}, 200

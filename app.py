import logging as logger
from flask import Flask

logger.basicConfig(level="DEBUG")
flaskAppInstance = Flask(__name__)

if __name__ == '__main__':
    logger.debug("Starting Flask Server")
    from api import *
    flaskAppInstance.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)


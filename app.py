from flask import Flask

flaskAppInstance = Flask(__name__)

if __name__ == '__main__':
    from api import *
    flaskAppInstance.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
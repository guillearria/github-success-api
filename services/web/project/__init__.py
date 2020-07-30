import os

from flask import Flask, jsonify
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


# Index
class Index(Resource):
    def get(self):
        return {"message": "Server running OK."}


api.add_resource(Index, '/')


if __name__ == '__main__':
    DEBUG = bool(os.environ.get('DEBUG'))
    app.run(debug=DEBUG)

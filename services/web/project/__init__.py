import os

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from .functions import *

app = Flask(__name__)
api = Api(app)


# Index
class Index(Resource):
    def get(self):
        return {"message": "Server running OK."}


# Top 10 All-Time Contributors Data
class Top10Contributors(Resource):
    def get(self, owner, repo):
        token = request.headers['Authorization']
        data = top_contributors(token, f'{owner}/{repo}')
        return data


api.add_resource(Index, '/')
api.add_resource(Top10Contributors, '/visualization/top10contributors/<owner>/<repo>')


if __name__ == '__main__':
    DEBUG = bool(os.environ.get('DEBUG'))
    app.run(debug=DEBUG)

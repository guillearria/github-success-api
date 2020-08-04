import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource
from .functions import *

app = Flask(__name__)
CORS(app)
api = Api(app)


# Index
class Index(Resource):
    def get(self):
        return {"message": "Server running OK."}


# Repo Summary
class RepoSummary(Resource):
    def get(self, owner, repo):
        token = request.headers['Authorization']
        data = repository_summary(token, f'{owner}/{repo}')
        return data


# Top 10 All-Time Contributors Data
class Top10Contributors(Resource):
    def get(self, owner, repo):
        token = request.headers['Authorization']
        data = top_contributors(token, f'{owner}/{repo}')
        return data


# Yearly Commit Activity
class YearlyCommitActivity(Resource):
    def get(self, owner, repo):
        token = request.headers['Authorization']
        data = yearly_commit_activity(token, f'{owner}/{repo}')
        return data


api.add_resource(Index, '/')
api.add_resource(RepoSummary, '/repo-summary/<owner>/<repo>')
api.add_resource(Top10Contributors, '/visualization/top-10-contributors/<owner>/<repo>')
api.add_resource(YearlyCommitActivity, '/visualization/yearly-commit-activity/<owner>/<repo>')


if __name__ == '__main__':
    DEBUG = bool(os.environ.get('DEBUG'))
    app.run(debug=DEBUG)

import os

from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy

from playhouse.shortcuts import model_to_dict
from playhouse.db_url import connect


app = Flask(__name__)
app.config.from_object("project.config.Config")
api = Api(app)
db = SQLAlchemy(app)


class Repo(db.Model):
    __tablename__ = "repos"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    pulls = db.relationship('Pull', backref='repos', lazy=True)

    def __init__(self, name):
        self.name = name


class Pull(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repo_id = ForeignKeyField(Repo, backref='pulls')
    created_date = DateTimeField()
    is_merged = BooleanField()
    additions = IntegerField()
    deletions = IntegerField()

    def serialize(self):
        pull_dict = model_to_dict(self)
        pull_dict["created_date"] = (
            pull_dict["created_date"].strftime('%Y-%m-%d')
        )

        return pull_dict


# Index
class Index(Resource):
    def get(self):
        return {"message": "Server running OK."}


# RepoList
# shows a list of all repos
class RepoList(Resource):
    def get(self):
        query = db.Repo.select().dicts()
        return [row for row in query], 200


# PullList
# shows a list of all pulls
class PullList(Resource):
    def get(self):
        query = db.Pull.select()
        return jsonify([r.serialize() for r in query])


# PullListByRepo
# shows a list of all pulls for given repo
class PullListByRepo(Resource):
    def get(self, repo_name):
        query = db.Pull.select().join(db.Repo).where(db.Repo.name == repo_name)
        return jsonify([r.serialize() for r in query])

api.add_resource(Index, '/')
api.add_resource(RepoList, '/github/repo/')
api.add_resource(PullList, '/github/pull/')
api.add_resource(PullListByRepo, '/github/pull/<repo_name>')


if __name__ == '__main__':
    DEBUG = bool(os.environ.get('DEBUG'))
    app.run(debug=DEBUG)

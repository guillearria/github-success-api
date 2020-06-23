import os
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from peewee import *
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)

db = PostgresqlDatabase(os.environ.get("POSTGRES_DB"), user=os.environ.get("POSTGRES_USER"), password=os.environ.get(
    "POSTGRES_PASSWORD"), host=os.environ.get("SQL_HOST"), port=os.environ.get("SQL_PORT"))


class BaseModel(Model):
    class Meta:
        database = db


class Repo(BaseModel):
    name = CharField(255)

    def serialize(self):
        repo_dict = model_to_dict(self)
        return repo_dict


class Pull(BaseModel):
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


api.add_resource(RepoList, '/github/repo/')
api.add_resource(PullList, '/github/pull/')
api.add_resource(PullListByRepo, '/github/pull/<repo_name>')


if __name__ == '__main__':
    DEBUG = bool(os.environ.get('DEBUG'))
    app.run(debug=DEBUG)

import os

from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_object("project.config.Config")

api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Repo(db.Model):
    __tablename__ = "repos"

    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(128), nullable=False)
    repo = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, owner, repo):
        self.owner = owner
        self.repo = repo


class Pull(db.Model):
    __tablename__ = "pulls"

    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, nullable=False)
    is_merged = db.Column(db.Boolean, nullable=False)
    additions = db.Column(db.Integer, nullable=False)
    deletions = db.Column(db.Integer, nullable=False)
    repo_id = db.Column(db.Integer, db.ForeignKey('repos.id'), nullable=False)
    repo = db.relationship('Repo', backref='pulls')

    def __init__(self, repo_id, created_date, is_merged, additions, deletions):
        self.repo_id = repo_id
        self.created_date = created_date
        self.is_merged = is_merged
        self.additions = additions
        self.deletions = deletions


class RepoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Repo


class PullSchema(ma.SQLAlchemyAutoSchema):
    repo = ma.Nested(RepoSchema)

    class Meta:
        model = Pull
        include_fk = False


repo_schema = RepoSchema()
repos_schema = RepoSchema(many=True)
pull_schema = PullSchema()
pulls_schema = PullSchema(many=True)


# Index
class Index(Resource):
    def get(self):
        return {"message": "Server running OK."}


# RepoList
# shows a list of all repos
class RepoList(Resource):
    def get(self):
        all_repos = Repo.query.all()
        return repos_schema.dump(all_repos), 200


# PullList
# shows a list of all pulls
class PullList(Resource):
    def get(self):
        all_pulls = Pull.query.all()
        return pulls_schema.dump(all_pulls), 200


# PullListByRepo
# shows a list of all pulls for given repo
class PullListByRepo(Resource):
    def get(self, repo_name):
        pulls = Pull.query.filter(Repo.repo==repo_name).join(Repo).all()
        return pulls_schema.dump(pulls), 200


api.add_resource(Index, '/')
api.add_resource(RepoList, '/github/repo/')
api.add_resource(PullList, '/github/pull/')
api.add_resource(PullListByRepo, '/github/pull/<repo_name>')


if __name__ == '__main__':
    DEBUG = bool(os.environ.get('DEBUG'))
    app.run(debug=DEBUG)

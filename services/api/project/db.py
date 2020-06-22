import config
from peewee import *
from playhouse.shortcuts import model_to_dict

db = PostgresqlDatabase(
    os.getenv("DATABASE"),
    user=os.getenv("POSTGRES_USER"), 
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("SQL_HOST"), 
    port=os.getenv("SQL_PORT")
)

class BaseModel(Model):
    class Meta:
        database = db

# Table Description
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
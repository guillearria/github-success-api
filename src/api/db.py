import config
from peewee import *

db = PostgresqlDatabase(
    config.POSTGRES_DB,
    user=config.POSTGRES_repo, 
    password=config.POSTGRES_PASSWORD,
    host=config.POSTGRES_HOST, 
    port=config.POSTGRES_PORT
)

class BaseModel(Model):
    class Meta:
        database = db

# Table Description
class Repo(BaseModel):
    name = CharField()

    # def serialize(self):
    #     data = {
    #         'id': self.id,
    #         'name': self.name,
    #     }

    #     return data

class Pull(BaseModel):
    repo = ForeignKeyField(Repo, backref='pulls')
    created = DateTimeField()
    is_merged = BooleanField()
    additions = IntegerField()
    deletions = IntegerField()

    # def serialize(self):
    #     data = {
    #         'id': self.id,
    #         'is_merged': self.is_merged,
    #         'additions': int(self.additions),
    #         'deletions': int(self.deletions),
    #     }

    #     return data

# Connection and table creation
db.connect()
db.create_tables([Repo, Relationship, Pull])
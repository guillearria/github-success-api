from flask.cli import FlaskGroup

from project import app, db


cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    # db.connect()
    db.drop_tables([db.Repo, db.Pull])
    db.create_tables([db.Repo, db.Pull])

if __name__ == "__main__":
    cli()
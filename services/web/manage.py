from flask.cli import FlaskGroup
from github import Github
from datetime import date, timedelta

from project import app, db


cli = FlaskGroup(app)

g = Github("sapinspys", "GithubCS1!")
temp_repos = ["kubernetes/kubernetes", "apache/spark"]


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_repos_tbl")
def seed_repos_tbl():
    repo_names = [g.get_repo(repo).full_name for repo in temp_repos]
    split_repo_names = [[name.split("/")[0],name.split("/")[1]] for name in repo_names]

    repo_objects = [db.Repo(owner=names[0], repo=[1]) for names in split_repo_names]
    db.session.add_all(repo_objects)

    db.session.commit()


if __name__ == "__main__":
    cli()

from flask.cli import FlaskGroup
from github import Github
from datetime import date, timedelta

from project import *


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
    split_repo_names = [[name.split("/")[0],name.split("/")[1]] for name in temp_repos]

    repo_objects = [Repo(names[0], names[1]) for names in split_repo_names]
    db.session.add_all(repo_objects)

    db.session.commit()


@cli.command("seed_pulls_tbl")
def seed_pulls_tbl():
    repos = [g.get_repo(repo) for repo in temp_repos]
    pulls_paginatedLists = { repo.name: repo.get_pulls(state="all") for repo in repos }

    repo_names = list(pulls_paginatedLists.keys())
    date_limit = date.today() - timedelta(3)
    pulls_pls_3day = { name: [] for name in repo_names }

    for repo in repo_names:
        for pull in pulls_paginatedLists[repo]:
            pull_date = pull.created_at.date()
            if pull_date == date.today():
                continue
            elif pull_date >= date_limit:
                pulls_pls_3day[repo].append(pull)
            else:
                break

    pulls_data = []

    for repo_name in repo_names:
        pulls = pulls_pls_3day[repo_name]
        for pull in pulls:
            pulls_data.append({"repo_id": db.Repo.query.filter_by(repo=repo_name).first().id,
                                "created_date": pull.created_at.date(),
                                "is_merged": pull.merged,
                                "additions": pull.additions,
                                "deletions": pull.deletions
                                })
                            
    pull_objects = [Pull(data["repo_id"], data["created_date"], data["is_merged"], data["additions"], data["deletions"]) for data in pulls_data]
    db.session.add_all(pull_objects)

    db.session.commit()


if __name__ == "__main__":
    cli()

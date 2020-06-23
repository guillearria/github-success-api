from flask.cli import FlaskGroup
from github import Github
from datetime import date, timedelta

from project import app, db


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    # db.connect()
    if db.table_exists("Repo"):
        db.drop_tables([db.Repo])
    if db.table_exists("Pull"):
        db.drop_tables([db.Pull])
    with db.connection_context():
        db.create_tables([db.Repo, db.Pull])


@cli.command("seed_db")
def seed_db():
    temp_repos = ["kubernetes/kubernetes", "apache/spark"]
    g = Github("d38d9579d63a4781c295fc499497f5d65714c2ed")
    repos = [g.get_repo(repo) for repo in temp_repos]
    pulls_paginatedLists = dict(
        (repo.name, repo.get_pulls(state="all")) for repo in repos)

    limit = date.today() - timedelta(3)
    repo_names = list(pulls_paginatedLists.keys())
    pulls_pls_3day = dict((name, []) for name in repo_names)

    for repo in repo_names:
        for pull in pulls_paginatedLists[repo]:
            pull_date = pull.created_at.date()
            if pull_date == date.today():
                continue
            elif pull_date >= limit:
                pulls_pls_3day[repo].append(pull)
            else:
                break

    repo_data = [{"name": name} for name in repo_names]

    with db.db.atomic():
        db.Repo.insert_many(repo_data).execute()

    pulls_data = []

    for repo in repo_names:
        pulls = pulls_pls_3day[repo]
        for pull in pulls:
            pulls_data.append({"repo_id": db.Repo.get(db.Repo.name == repo),
                               "created_date": pull.created_at.date(),
                               "is_merged": pull.merged,
                               "additions": pull.additions,
                               "deletions": pull.deletions
                               })

    with db.db.atomic():
        db.Pull.insert_many(pulls_data).execute()


if __name__ == "__main__":
    cli()

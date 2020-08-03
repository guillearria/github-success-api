from github import Github
import pandas as pd


def top_contributors(token, full_name):
    """Return top 10 all-time contributors for the given repository.

    Keywork arguments:
    token -- GitHub authorization token
    full_name -- owner and name of repository in format: "owner/repo"
    """
    g = Github(token)
    repo = g.get_repo(full_name)
    stats = repo.get_stats_contributors()[90:]

    top_contributors = {
        'user': [stat.author.login for stat in stats],
        'name': [g.get_user(stat.author.login).name for stat in stats],
        'followers': [g.get_user(stat.author.login).followers for stat in stats],
        'total_commits': [stat.total for stat in stats],
    }

    return top_contributors


def repository_summary(token, full_name):
    """Returns summary of useful repository and owner data for the given repository.

    Keywork arguments:
    token -- GitHub authorization token
    full_name -- owner and name of repository in format: "owner/repo"
    """
    g = Github(token)
    owner = g.get_user(full_name.split("/")[0])
    repo = g.get_repo(full_name)

    summary = [
        {
            'avatar_url': owner.avatar_url,
            'gh_url': owner.url,
            'name': owner.name,
            'login': owner.login,
        },
        {
            "watchers": repo.subscribers_count,
            "stars": repo.watchers_count,
            "forks": repo.forks_count,
            'full_name': repo.full_name,
            'description': repo.description,
            'homepage_url': repo.homepage,
            'languages_url': repo.languages_url,
            "updated": repo.last_modified,
            "contributors": repo.get_contributors().totalCount,
            "total_commits": repo.get_commits().totalCount,
            "open_pull_requests": repo.get_pulls().totalCount,
            # "closed_pull_requests": repo.get_pulls(state="closed").totalCount,
        }
    ]

    return summary

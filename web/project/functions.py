from github import Github
import pandas as pd
import json

def repository_summary(token, full_name):
    """Returns summary of useful repository and owner data for the given repository.

    Keywork arguments:
    token -- GitHub authorization token
    full_name -- owner and name of repository in format: "owner/repo"
    """
    g = Github(token)
    repo = g.get_repo(full_name)
    owner = repo.owner

    repository_summary = [
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

    return repository_summary

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

    serialized_data = json.dumps(top_contributors, default=str)

    return serialized_data

def yearly_commit_activity(token, full_name):
    """Displays commit activity grouped by week for the last year.

    Keywork arguments:
    token -- GitHub authorization token
    full_name -- owner and name of repository in format: "owner/repo"
    """
    g = Github(token)
    repo = g.get_repo(full_name)
    stats = repo.get_stats_commit_activity()

    yearly_commit_activity = {
      'week': [stat.week for stat in stats],
      'total_commits': [stat.total for stat in stats],
    }

    serialized_data = json.dumps(yearly_commit_activity, default=str)

    return serialized_data

def yearly_code_frequency(token, full_name):
    """Displays the number of additions and deletions pushed over the last year.

    Keywork arguments:
    token -- GitHub authorization token
    full_name -- owner and name of repository in format: "owner/repo"
    """
    g = Github(token)
    repo = g.get_repo(full_name)
    stats = repo.get_stats_code_frequency()[::-1]
    months_included = []
    stats_included = []

    while len(months_included) < 12:
        for stat in stats:
            mo = stat.week.month
            if mo not in months_included:
                months_included.append(mo)
                stats_included.append(stat)

    yearly_code_frequency = {
        'week': [stat.week for stat in stats_included],
        'additions': [stat.additions for stat in stats_included],
        'deletions': [stat.deletions for stat in stats_included]
    }

    serialized_data = json.dumps(yearly_code_frequency, default=str)

    return serialized_data
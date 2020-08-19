from github import Github
from datetime import date, timedelta, datetime
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
    """Returns top 10 all-time contributors for the given repository.

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


def yearly_commit_activity(token, full_name):
    """Returns commit activity grouped by week for the last year.

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
    """Returns the number of additions and deletions pushed over the last year.

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


def daily_commits(token, full_name):
    """Returns daily commits over the last week.

    Keywork arguments:
    token -- GitHub authorization token
    full_name -- owner and name of repository in format: "owner/repo"
    """
    g = Github(token)
    repo = g.get_repo(full_name)
    stats = repo.get_stats_punch_card()
    stats = stats.raw_data

    daily_commits = {
        'day': [stat[0] for stat in stats],
        'commits': [stat[2] for stat in stats]
    }

    columns = list(daily_commits.keys())
    df = pd.DataFrame(daily_commits, columns=columns)
    df = df.groupby(["day"]).sum().reset_index()
    
    d = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6:'Saturday' } 
    df = df.replace({"day": d}) 

    daily_commits = {
        'day': df.day.tolist(),
        'commits': df.commits.tolist()
    }

    return daily_commits

def issue_activity(token, full_name):
    """Returns daily count of opened and closed issues over the last 30 days for the requested repository.

    Keywork arguments:
    token -- GitHub authorization token
    full_name -- owner and name of repository in format: "owner/repo"
    """
    g = Github(token)
    repo = g.get_repo(full_name)

    all_issues = repo.get_issues(state="all")
    issues_included = []

    end_date = datetime.now()
    start_date = end_date-timedelta(days=30)
    delta = end_date - start_date
    
    days_included = [(start_date + timedelta(days=i)).date() for i in range(delta.days)]
    final_day = days_included[0]-timedelta(days=1)

    for issue in all_issues:
        day = issue.created_at.date()
        if day == final_day:
            break
        elif day in days_included:
            issues_included.append(issue)

    data = {
        'created_at': [issue.created_at.date() for issue in issues_included],
        'status': ["closed" if issue.closed_at else "open" for issue in issues_included],
        'total_comments': [issue.comments for issue in issues_included],
    }

    columns = list(data.keys())
    df = pd.DataFrame(data, columns=columns)
    df = df.groupby(["created_at","status"]).count().reset_index()

    df_open = df[df.status == "open"]
    df_closed = df[df.status == "closed"]

    issue_activity = {
        "open_issues": {
            "created_at": df_open.created_at.tolist(),
            "issue_count": df_open.total_comments.tolist()
        },
        "closed_issues": {
            "created_at": df_closed.created_at.tolist(),
            "issue_count": df_closed.total_comments.tolist()
        }
    }

    serialized_data = json.dumps(issue_activity, default=str)

    return serialized_data

def issue_comments(token, full_name):
    """Returns all issues, their comment count, and body length for the last 7 days.

    Keywork arguments:
    token -- GitHub authorization token
    full_name -- owner and name of repository in format: "owner/repo"
    """
    g = Github(token)
    repo = g.get_repo(full_name)

    all_issues = repo.get_issues(state="all")
    issues_included = []

    end_date = datetime.now()
    start_date = end_date-timedelta(days=7)
    delta = end_date - start_date
    
    days_included = [(start_date + timedelta(days=i)).date() for i in range(delta.days)]
    final_day = days_included[0]-timedelta(days=1)

    for issue in all_issues:
        day = issue.created_at.date()
        if day == final_day:
            break
        elif day in days_included:
            issues_included.append(issue)

    issue_comments = {
        'opened_at': [issue.created_at for issue in issues_included],
        'total_comments': [issue.comments for issue in issues_included],
        'body_length': [len(issue.body) for issue in issues_included],
    }

    serialized_data = json.dumps(issue_comments, default=str)

    return serialized_data
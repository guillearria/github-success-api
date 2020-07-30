from github import Github
import pandas as pd

def top_contributors(token, full_name):
  """Displays top 10 all-time contributors for the given repository.

  Keywork arguments:
  full_name -- owner and name of repository in format: "owner/repo"
  """
  g = Github(token)
  repo = g.get_repo(full_name)
  stats = repo.get_stats_contributors()[90:]

  repo_data = {
      'user': [stat.author.login for stat in stats],
      'name': [g.get_user(stat.author.login).name for stat in stats],
      'followers': [g.get_user(stat.author.login).followers for stat in stats],
      'total_commits': [stat.total for stat in stats],
  }

#   columns = list(repo_data.keys())
#   df = pd.DataFrame(repo_data, columns=columns)
  
  return repo_data
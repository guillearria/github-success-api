# github-success-api

Development:
* git clone
* pipenv shell
* pipenv install
* python app.py
* OR gunicorn app:app --bind 0.0.0.0:5000

Endpoints:
* Index, '/'
* RepoSummary, '/repo-summary/<owner>/<repo>'
* Top10Contributors, '/visualization/top-10-contributors/<owner>/<repo>'
* YearlyCommitActivity, '/visualization/yearly-commit-activity/<owner>/<repo>'
* YearlyCodeFrequency, '/visualization/yearly-code-frequency/<owner>/<repo>'

!! MUST PASS GITHUB ACCESS TOKEN VIA AUTHORIZATION HEADER
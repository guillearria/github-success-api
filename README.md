# GitHub Success REST API

## Overview
This API serves to provide developers with statistics about specific GitHub repositories. The endpoints below provide data formatted to be used with a visualization library such as Plotly.js.

## Authentication
Each endpoint requires an authorization header for the data to be accessed. This authorization header must include a personal access token (PAT) provided by GitHub.

## HTTP Response Codes
Each response will be returned with one of the following HTTP status codes:

* `200` `OK` The request was successful
* `400` `Bad Request` There was a problem with the request (missing authorization header)
* `404` `Not found` An attempt was made to access a resource that does not exist in the API
* `405` `Method not allowed` The resource being accessed doesn't support the method specified (GET, POST, etc.).
* `500` `Server Error` An error on the server occurred (bad credentials, ie. access token)

## Development
* `git clone`
* `pipenv shell`
* `pipenv install`
* `python app.py`

## Resources

### Owner/Repo Summary

Returns a list of two dictionaries, the first contains data about the requested owner and the second contains a few statistics about the requested repository.

#### Request

    GET http://githubsuccessapi-env.eba-8utmmuhi.us-east-1.elasticbeanstalk.com/repo-summary/kubernetes/kubernetes

#### Response
```json
[
  {
    "avatar_url": "https://avatars2.githubusercontent.com/u/13629408?v=4",
    "gh_url": "https://api.github.com/users/kubernetes",
    "name": "Kubernetes",
    "login": "kubernetes"
  },
  {
    "watchers": 3233,
    "stars": 69042,
    "forks": 24888,
    "full_name": "kubernetes/kubernetes",
    "description": "Production-Grade Container Scheduling and Management",
    "homepage_url": "https://kubernetes.io",
    "languages_url": "https://api.github.com/repos/kubernetes/kubernetes/languages",
    "updated": "Sat, 15 Aug 2020 03:09:43 GMT",
    "contributors": 383,
    "total_commits": 93298,
    "open_pull_requests": 1005
  }
]
```

### Top 10 All-Time Contributors
Returns the top 10 all-time contributors along with their total commits and follower count for the requested repository.

#### Request

    GET http://githubsuccessapi-env.eba-8utmmuhi.us-east-1.elasticbeanstalk.com/visualization/top-10-contributors/kubernetes/kubernetes

#### Response
```json
{"user": ["lavalamp", "mikedanese", "thockin", "caesarxuchao", "brendandburns", "sttts", "deads2k", "wojtek-t", "smarterclayton", "liggitt"], "name": ["Daniel Smith", "Mike Danese", "Tim Hockin", "Chao Xu", "Brendan Burns", "Dr. Stefan Schimanski", "David Eads", "Wojciech Tyczynski", "Clayton Coleman", "Jordan Liggitt"], "followers": [369, 287, 1031, 382, 2007, 312, 258, 240, 1017, 537], "total_commits": [720, 853, 887, 903, 1026, 1086, 1171, 1211, 1324, 1481]}
```

### Yearly Commit Activity
Returns total commits made each week for the last 12 months for the requested repository.

#### Request

    GET http://githubsuccessapi-env.eba-8utmmuhi.us-east-1.elasticbeanstalk.com/visualization/yearly-commit-activity/kubernetes/kubernetes

#### Response
```json
{"week": ["2019-08-18 00:00:00", "2019-08-25 00:00:00", "2019-09-01 00:00:00", "2019-09-08 00:00:00", "2019-09-15 00:00:00", "2019-09-22 00:00:00", "2019-09-29 00:00:00", "2019-10-06 00:00:00", "2019-10-13 00:00:00", "2019-10-20 00:00:00", "2019-10-27 00:00:00", "2019-11-03 00:00:00", "2019-11-10 00:00:00", "2019-11-17 00:00:00", "2019-11-24 00:00:00", "2019-12-01 00:00:00", "2019-12-08 00:00:00", "2019-12-15 00:00:00", "2019-12-22 00:00:00", "2019-12-29 00:00:00", "2020-01-05 00:00:00", "2020-01-12 00:00:00", "2020-01-19 00:00:00", "2020-01-26 00:00:00", "2020-02-02 00:00:00", "2020-02-09 00:00:00", "2020-02-16 00:00:00", "2020-02-23 00:00:00", "2020-03-01 00:00:00", "2020-03-08 00:00:00", "2020-03-15 00:00:00", "2020-03-22 00:00:00", "2020-03-29 00:00:00", "2020-04-05 00:00:00", "2020-04-12 00:00:00", "2020-04-19 00:00:00", "2020-04-26 00:00:00", "2020-05-03 00:00:00", "2020-05-10 00:00:00", "2020-05-17 00:00:00", "2020-05-24 00:00:00", "2020-05-31 00:00:00", "2020-06-07 00:00:00", "2020-06-14 00:00:00", "2020-06-21 00:00:00", "2020-06-28 00:00:00", "2020-07-05 00:00:00", "2020-07-12 00:00:00", "2020-07-19 00:00:00", "2020-07-26 00:00:00", "2020-08-02 00:00:00", "2020-08-09 00:00:00"], "total_commits": [188, 231, 117, 110, 119, 124, 143, 184, 140, 167, 165, 239, 204, 85, 94, 129, 124, 120, 79, 71, 165, 158, 112, 99, 124, 133, 97, 155, 142, 63, 102, 163, 122, 94, 112, 130, 100, 97, 133, 99, 122, 114, 101, 107, 113, 115, 68, 45, 66, 50, 25, 39]}
```

### Yearly Code Frequency
Returns total additions and deletions made each month for the last 12 months for the requested repository.

#### Request

    GET http://githubsuccessapi-env.eba-8utmmuhi.us-east-1.elasticbeanstalk.com/visualization/yearly-code-frequency/kubernetes/kubernetes

#### Response
```json
{"week": ["2020-08-09 00:00:00", "2020-07-26 00:00:00", "2020-06-28 00:00:00", "2020-05-31 00:00:00", "2020-04-26 00:00:00", "2020-03-29 00:00:00", "2020-02-23 00:00:00", "2020-01-26 00:00:00", "2019-12-29 00:00:00", "2019-11-24 00:00:00", "2019-10-27 00:00:00", "2019-09-29 00:00:00"], "additions": [9950, 1652, 7544, 51401, 12142, 34646, 28899, 56881, 8420, 6969, 133671, 16423], "deletions": [-8837, -1547, -4368, -26706, -7554, -22266, -12375, -5500, -5041, -3254, -124854, -12091]}
```
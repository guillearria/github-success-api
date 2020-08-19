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
* `cd api`
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
{
  "user": ["lavalamp", "mikedanese", "thockin", "caesarxuchao", "brendandburns", "sttts", "deads2k", "wojtek-t", "smarterclayton", "liggitt"], 
  "name": ["Daniel Smith", "Mike Danese", "Tim Hockin", "Chao Xu", "Brendan Burns", "Dr. Stefan Schimanski", "David Eads", "Wojciech Tyczynski", "Clayton Coleman", "Jordan Liggitt"], 
  "followers": [369, 287, 1031, 382, 2007, 312, 258, 240, 1017, 537], 
  "total_commits": [720, 853, 887, 903, 1026, 1086, 1171, 1211, 1324, 1481]
}
```

### Yearly Commit Activity
Returns total commits made each week for the last 12 months for the requested repository. Will require `JSON.parse(response)`.

#### Request

    GET http://githubsuccessapi-env.eba-8utmmuhi.us-east-1.elasticbeanstalk.com/visualization/yearly-commit-activity/kubernetes/kubernetes

#### Response
```json
{
  "week": ["2019-08-18 00:00:00", "2019-08-25 00:00:00", "2019-09-01 00:00:00", "2019-09-08 00:00:00", "2019-09-15 00:00:00", "2019-09-22 00:00:00", "2019-09-29 00:00:00", "2019-10-06 00:00:00", "2019-10-13 00:00:00", "2019-10-20 00:00:00", "2019-10-27 00:00:00", "2019-11-03 00:00:00", "2019-11-10 00:00:00", "2019-11-17 00:00:00", "2019-11-24 00:00:00", "2019-12-01 00:00:00", "2019-12-08 00:00:00", "2019-12-15 00:00:00", "2019-12-22 00:00:00", "2019-12-29 00:00:00", "2020-01-05 00:00:00", "2020-01-12 00:00:00", "2020-01-19 00:00:00", "2020-01-26 00:00:00", "2020-02-02 00:00:00", "2020-02-09 00:00:00", "2020-02-16 00:00:00", "2020-02-23 00:00:00", "2020-03-01 00:00:00", "2020-03-08 00:00:00", "2020-03-15 00:00:00", "2020-03-22 00:00:00", "2020-03-29 00:00:00", "2020-04-05 00:00:00", "2020-04-12 00:00:00", "2020-04-19 00:00:00", "2020-04-26 00:00:00", "2020-05-03 00:00:00", "2020-05-10 00:00:00", "2020-05-17 00:00:00", "2020-05-24 00:00:00", "2020-05-31 00:00:00", "2020-06-07 00:00:00", "2020-06-14 00:00:00", "2020-06-21 00:00:00", "2020-06-28 00:00:00", "2020-07-05 00:00:00", "2020-07-12 00:00:00", "2020-07-19 00:00:00", "2020-07-26 00:00:00", "2020-08-02 00:00:00", "2020-08-09 00:00:00"], 
  "total_commits": [188, 231, 117, 110, 119, 124, 143, 184, 140, 167, 165, 239, 204, 85, 94, 129, 124, 120, 79, 71, 165, 158, 112, 99, 124, 133, 97, 155, 142, 63, 102, 163, 122, 94, 112, 130, 100, 97, 133, 99, 122, 114, 101, 107, 113, 115, 68, 45, 66, 50, 25, 39]
}
```

### Yearly Code Frequency
Returns total additions and deletions made each month for the last 12 months for the requested repository. Will require `JSON.parse(response)`.

#### Request

    GET http://githubsuccessapi-env.eba-8utmmuhi.us-east-1.elasticbeanstalk.com/visualization/yearly-code-frequency/kubernetes/kubernetes

#### Response
```json
{
  "week": ["2020-08-09 00:00:00", "2020-07-26 00:00:00", "2020-06-28 00:00:00", "2020-05-31 00:00:00", "2020-04-26 00:00:00", "2020-03-29 00:00:00", "2020-02-23 00:00:00", "2020-01-26 00:00:00", "2019-12-29 00:00:00", "2019-11-24 00:00:00", "2019-10-27 00:00:00", "2019-09-29 00:00:00"], 
  "additions": [9950, 1652, 7544, 51401, 12142, 34646, 28899, 56881, 8420, 6969, 133671, 16423], 
  "deletions": [-8837, -1547, -4368, -26706, -7554, -22266, -12375, -5500, -5041, -3254, -124854, -12091]
}
```

### Daily Commits
Returns daily commits over the last week for the requested repository.

#### Request

    GET http://githubsuccessapi-env.eba-8utmmuhi.us-east-1.elasticbeanstalk.com/visualization/daily-commits/kubernetes/kubernetes

#### Response
```json
{
  "day": [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
  ],
  "commits": [
    825,
    3275,
    3672,
    3871,
    3840,
    3495,
    1022
  ]
}
```

### Issue Activity
Returns daily count of opened and closed issues over the last 30 days for the requested repository.

#### Request

    GET http://githubsuccessapi-env.eba-8utmmuhi.us-east-1.elasticbeanstalk.com/visualization/issue-activity/kubernetes/kubernetes

#### Response
```json
{
    "open_issues": {
        "created_at": ["2020-07-19", "2020-07-20", "2020-07-21", "2020-07-22", "2020-07-23", "2020-07-24", "2020-07-25", "2020-07-26", "2020-07-27", "2020-07-28", "2020-07-29", "2020-07-30", "2020-07-31", "2020-08-01", "2020-08-02", "2020-08-03", "2020-08-04", "2020-08-05", "2020-08-06", "2020-08-07", "2020-08-08", "2020-08-09", "2020-08-10", "2020-08-11", "2020-08-12", "2020-08-13", "2020-08-14", "2020-08-15", "2020-08-16", "2020-08-17"], 
        "issue_count": [8, 16, 20, 26, 13, 17, 4, 2, 15, 12, 15, 21, 12, 7, 3, 12, 22, 23, 15, 27, 9, 7, 20, 25, 26, 17, 21, 9, 6, 22]
    }, 
    "closed_issues": {
        "created_at": ["2020-07-19", "2020-07-20", "2020-07-21", "2020-07-22", "2020-07-23", "2020-07-24", "2020-07-25", "2020-07-26", "2020-07-27", "2020-07-28", "2020-07-29", "2020-07-30", "2020-07-31", "2020-08-01", "2020-08-02", "2020-08-03", "2020-08-04", "2020-08-05", "2020-08-06", "2020-08-07", "2020-08-08", "2020-08-09", "2020-08-10", "2020-08-11", "2020-08-12", "2020-08-13", "2020-08-14", "2020-08-15", "2020-08-16", "2020-08-17"], 
        "issue_count": [15, 18, 21, 31, 21, 20, 5, 4, 18, 16, 17, 21, 16, 7, 2, 14, 14, 16, 12, 10, 10, 10, 10, 14, 18, 15, 13, 4, 1, 4]
    }
}
```
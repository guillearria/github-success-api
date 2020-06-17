# gh-analysis

Interactive visualizations for 5 popular GitHub repositories.

Built using:
Python + PyGitHub + Flask + Dash + Flask-Restful + Postgres + AWS 

Routes:
* Refresh DB (last 3 days): POST /api/refresh
* Visualization 1: GET /api/visualization1
* .....

## Notes:
Steps to reproduce:
* file structure (dash/ui, flask/api, postgres/db)
* create necessary application scripts
* create config.py script for db
* pin required dependencies to requirement.txt files (pip-tools using requirements.in)
* Compose necessary Dockerfiles (creates custom images)
* create docker-compose.yml (runs of multiple containers, ie.container instructions)

Docker cmds:
* All images: docker images
* All containers: docker container ls -la

Docker Installation https://docs.docker.com/engine/install/ubuntu/

Ubuntu Docker Permissions Error: https://stackoverflow.com/questions/47854463/docker-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socke

Useful Tutorial: https://medium.com/datadriveninvestor/end-to-end-machine-learning-from-data-collection-to-deployment-ce74f51ca203
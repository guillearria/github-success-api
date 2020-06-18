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
* add req dependencies to requirement.in (temporary)
* pin req dependencies to requirement.txt files (pip-tools using requirements.in)
* compose necessary Dockerfiles (creates custom images)
* create docker-compose.yml (runs of multiple containers, ie.container instructions)

Docker cmds:
* All images: docker images
* All containers: docker container ls -la

Docker Installation https://docs.docker.com/engine/install/ubuntu/

Ubuntu Docker Permissions Error: https://stackoverflow.com/questions/47854463/docker-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socke

Useful Tutorial: https://medium.com/datadriveninvestor/end-to-end-machine-learning-from-data-collection-to-deployment-ce74f51ca203

'''
Indeed, Flask's built-in server is a development only server, and should not be used in production.

From the official deployment documentation:

When running publicly rather than in development, you should not use the built-in development server (flask run). The development server is provided by Werkzeug for convenience but is not designed to be particularly efficient, stable, or secure.

You can use any python production web server (tornado, gunicorn, …) instead.
'''
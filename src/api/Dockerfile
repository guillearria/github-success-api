# Dockerfile

# Python version
FROM python:3.8-slim-buster

ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

ADD . /app

EXPOSE  5000

CMD ["python", "-b", "0.0.0.0:8050", "app:app"]
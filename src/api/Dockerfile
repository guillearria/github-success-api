FROM python:3.8-slim-buster

ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

ADD . /app

EXPOSE  5000

CMD ["gunicorn", "-b", "0.0.0.0:8050", "app:app"]
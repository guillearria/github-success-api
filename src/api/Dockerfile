# Dockerfile

# Python version
FROM python:3.8-slim-buster

# Set work dir
WORKDIR /app

# Install dependencies
ADD requirements.txt /app/
RUN pip install -r requirements.txt

ADD . /app
EXPOSE  5000
CMD ["gunicorn", "--timeout", "1200", "-b", "0.0.0.0:5000", "app:app"]
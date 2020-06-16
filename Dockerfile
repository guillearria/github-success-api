FROM python:3.8-slim-buster
LABEL maintainer="guillermo.arriadevoe@gmail.com"
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["python", "app.py"]
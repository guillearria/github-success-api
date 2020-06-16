FROM python:3.8-slim-buster
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt
ADD . /src
EXPOSE  5000
CMD ["python", "/src/app.py"]
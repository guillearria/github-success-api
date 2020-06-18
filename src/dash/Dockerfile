# Dockerfile

# Python version
FROM python:3.8-slim-buster

# Set work dir
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project:
# means any code changes locally will be copied over
COPY . /app

# EXPOSE  8050

# CMD ["python", "-b", "0.0.0.0:5000", "app:app"]
CMD ["python", "app.py"]
FROM python:3.6-slim-stretch

# Requirements
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Copy app
COPY . /app
WORKDIR /app

# Run app
CMD ["python", "/app/app/__init__.py"]

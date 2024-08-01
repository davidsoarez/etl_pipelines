FROM python:3.11-slim-buster AS build-stage

# Set work directory
WORKDIR /app

# Set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y netcat && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Copy the entrypoint script
COPY entrypoint.sh .

# Set the entrypoint
ENTRYPOINT ["./entrypoint.sh"]
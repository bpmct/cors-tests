# Dockerfile
FROM python:3.9-slim-buster

# Install Node.js
RUN apt-get update && apt-get install -y curl \
    && curl -sL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs git

# Upgrade pip
RUN pip install --upgrade pip

# Create a working directory
WORKDIR /app

# Install Python dependencies
COPY backend/requirements.txt .
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5000

CMD [ "bash" ]

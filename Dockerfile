# Base Image
FROM python:3.7

# Set default enviroment variables
ENV PYTHONUNBUFFERED 1

# run this before copying requirements for cache efficiency
RUN pip install --upgrade pip

# Create and set working directory
RUN mkdir /CSE312
WORKDIR /CSE312

# Add requirements.txt file to "CSE312" directory
COPY requirements.txt .

# Install project dependencies
RUN pip install -r requirements.txt

# Add current directory to "CSE312" directory
COPY . .

#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Run the command line below to build a Docker image:
# docker build -t cse312 .
# Run the command line below to run a Docker container:
# docker run --publish 8500:8000 --detach cse312
# Run the command line below to get into the Docker terminal:
# docker exec -ti "container id" /bin/bash
# Run the command line below to list Docker containers:
# docker ps
# Run the command line below to list Docker containers:
# docker kill "container id" to kill a Docker container
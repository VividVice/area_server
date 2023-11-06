# Use an official Python runtime as a parent image
FROM python:3.11.5-alpine

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Run app.py when the container launches
CMD ["python", "main.py"]


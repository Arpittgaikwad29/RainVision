# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies, including pytest for testing
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir pytest

# Make port 5000 available to the outside world
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

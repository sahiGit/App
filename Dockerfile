FROM python:3.8-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Install any dependencies
RUN pip install --no-cache-dir flask

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]

FROM python:3.9.13-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir websockets

# Expose the port the app runs on
EXPOSE 8989

# Run the server when the container launches
CMD ["python3", "server.py"]

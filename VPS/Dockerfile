# Stage 1: Build stage
FROM python3.9

# Set the working directory
WORKDIR /app

# Install ffmpeg in the container
RUN apt-get update && apt-get install -y ffmpeg

# Copy requirements.txt
COPY requirements.txt ./

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy app source inside the docker image
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define the command to be run when launching the container
CMD ["python3", "src/app.py"]
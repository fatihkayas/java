# Use Python 3.9 image as the base
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy project files into container
COPY . /app

# Install the necessary dependencies
RUN apt-get update && apt-get install -y \
    libsdl1.2debian \
    libsndfile1 \
    libsm6 \
    libxrender1 \
    libfontconfig1 \
    && pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]

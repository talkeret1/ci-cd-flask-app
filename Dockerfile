# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /flask-app

# Copy files
COPY requirements.txt .
COPY app ./app
COPY README.md .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "-m", "app"]
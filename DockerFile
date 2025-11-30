# Base image with common known vulnerabilities (good for testing scanners)
FROM python:3.9-slim

WORKDIR /app

# Copy dependency file (if you don’t have one, create minimal)
COPY requirements.txt .

# Install Python dependencies
# Using --no-cache-dir so final image is smaller
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Default run command (modify as needed)
CMD ["python", "main.py"]

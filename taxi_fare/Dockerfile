# Use an official Python runtime as the base image
FROM python:3.8-slim

WORKDIR /app

# Copy and install API dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the API code
COPY app.py .

# Expose port 8000 for the API service
EXPOSE 8000

# Start the API with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

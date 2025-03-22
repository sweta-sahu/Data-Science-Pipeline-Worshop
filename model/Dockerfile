# Use an official Python runtime as the base image
FROM python:3.8-slim

# Install system dependencies required by LightGBM (libgomp)
RUN apt-get update && apt-get install -y libgomp1 && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy and install model dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the model file and service code
COPY taxi_fare_model.pkl .
COPY model_service.py .

# Expose port 8501 for the model service
EXPOSE 8501

# Start the model service with uvicorn
CMD ["uvicorn", "model_service:app", "--host", "0.0.0.0", "--port", "8501"]

# Taxi Fare Prediction

Welcome to the Taxi Fare Prediction project! This repository demonstrates a complete end-to-end machine learning pipeline—from data ingestion and preprocessing, feature engineering, model building using an ensemble stacking approach, evaluation, and finally, deployment as microservices with business logic overlays.

## Table of Contents

- [Overview](#overview)
- [Project Components](#project-components)
  - [Data Ingestion & Preprocessing](#data-ingestion--preprocessing)
  - [Feature Engineering](#feature-engineering)
  - [Model Building & Evaluation](#model-building--evaluation)
  - [Model Deployment](#model-deployment)
  - [Business Logic Microservice](#business-logic-microservice)
- [Usage](#usage)
- [Installation & Setup](#installation--setup)

## Overview

This project builds a regression model to predict taxi fares based on various inputs such as:
- Trip distance and duration
- Traffic conditions
- Weather conditions

We use an ensemble stacking approach that combines models like XGBRegressor, RandomForestRegressor, GradientBoostingRegressor, and LGBMRegressor for robust predictions. 

Two microservices are deployed:
1. **Model Inference Service:** Preprocesses the input data and returns the base taxi fare prediction.
2. **Business Logic Service:** Applies additional logic to adjust the fare based on time of day and weather conditions.

## Project Components

### Data Ingestion & Preprocessing
- **Dataset:** [Taxi Fare Dataset on Kaggle](https://www.kaggle.com/datasets/denkuznetz/taxi-price-prediction/data)
- **Preprocessing Steps:**  
  - Data cleaning and handling missing values  
  - Encoding categorical features (e.g., Traffic Conditions)  
  - Feature scaling and transformation
  - Computing derived features such as "Average_Speed_km_h"

### Feature Engineering
- Creating new features (e.g., Average Speed from trip distance and duration)
- Feature selection to improve model performance

### Model Building & Evaluation
- **Ensemble Stacking Approach:**  
  Combines predictions from multiple regressors:
  - XGBRegressor  
  - RandomForestRegressor  
  - GradientBoostingRegressor  
  - LGBMRegressor
- **Evaluation Metrics:**  
  - Mean Squared Error (MSE)  
  - Mean Absolute Error (MAE)  
  - R² Score

### Model Deployment
- **Inference Service:**  
  - Implemented using FastAPI  
  - Preprocesses input data, runs inference, and returns predictions
- **Containerization:**  
  - Docker is used to package the microservices for consistent deployment across environments

### Business Logic Microservice
- Applies additional rules (e.g., surge pricing based on time of day and weather conditions) on top of the base prediction.
- Exposes endpoints via FastAPI and integrates with the Inference Service

## Usage

To run the services locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/taxi-fare-mlops-demo.git
   cd taxi-fare-mlops-demo
   ```

2. **Docker:**
   ```bash
   docker-compose build
   docker-compose up -d
   docker-compose down 
    ```
   
3. **Access the API Endpoints:**

- Model Inference Service: http://localhost:8501/docs

- Business Logic Service: http://localhost:8502/docs

## Installation & Setup
Prerequisites:

- Python 3.8+

- Docker

- Git

Python Dependencies: Install the required packages using pip:
```bash
pip install -r requirements.txt
```
Running Locally: You can also run the services locally without Docker:
```bash
uvicorn model_service:app --port 8501
uvicorn app:app --port 8000
```


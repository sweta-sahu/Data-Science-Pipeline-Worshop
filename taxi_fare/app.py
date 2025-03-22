from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class TaxiFareRequest(BaseModel):
    Trip_Distance_km: float
    Passenger_Count: int
    Base_Fare: float
    Per_Km_Rate: float
    Per_Minute_Rate: float
    Trip_Duration_Minutes: float
    Time_of_Day: str
    Day_of_Week: str
    Traffic_Conditions: str
    Weather: str

MODEL_SERVICE_URL = "http://model:8501/predict"

@app.post("/predict")
def predict_taxi_fare(request: TaxiFareRequest):
    try:
        response = requests.post(MODEL_SERVICE_URL, json=request.dict())
        response.raise_for_status()
        data = response.json()
        
        base_fare = data.get("predicted_taxi_fare", 0.0)
        
        surge_multiplier = 1.0
        weather_multiplier = 1.0
        
        if request.Time_of_Day.lower() in ["morning", "evening"]:
            surge_multiplier = 1.10  # 10% increase during peak hours
        
        if request.Weather.lower() == "rain":
            weather_multiplier = 1.05  # 5% increase in rainy conditions
        
        # Calculate the adjusted fare
        adjusted_fare = base_fare * surge_multiplier * weather_multiplier
        adjusted_fare = round(adjusted_fare, 2)
        
        return {
            "base_predicted_taxi_fare": base_fare,
            "adjusted_predicted_taxi_fare": adjusted_fare,
            "currency": "USD",
            "business_logic_details": {
                "surge_multiplier": surge_multiplier,
                "weather_multiplier": weather_multiplier
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

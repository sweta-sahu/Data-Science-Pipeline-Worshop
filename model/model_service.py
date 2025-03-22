from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib

app = FastAPI()

# Load the saved model
model = joblib.load('taxi_fare_model.pkl')

class ModelInput(BaseModel):
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

@app.post("/predict")
def predict(input_data: ModelInput):
    df = pd.DataFrame([input_data.dict()])
    
    df["Average_Speed_km_h"] = df.apply(
        lambda row: row["Trip_Distance_km"] / (row["Trip_Duration_Minutes"] / 60.0) 
                    if row["Trip_Duration_Minutes"] > 0 else 0.0,
        axis=1
    )
    
    traffic_mapping = {"Low": 1, "Medium": 2, "High": 3}
    df["Traffic_Conditions"] = df["Traffic_Conditions"].map(traffic_mapping)
    
    log_pred = model.predict(df)
    fare = float(np.expm1(log_pred[0]))
    
    return {"predicted_taxi_fare": round(fare, 2), "currency": "USD"}

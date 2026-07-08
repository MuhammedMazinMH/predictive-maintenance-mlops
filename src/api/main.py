import pickle
import numpy as np
from fastapi import FastAPI
from schemas import PredictionRequest, PredictionResponse

app = FastAPI(title="Predictive Maintenance API")

# Load model and features at startup
with open("../models/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("../models/features.pkl", "rb") as f:
    feature_names = pickle.load(f)

@app.get("/")
def home():
    return {"message": "API is running", "model": "RandomForest RUL predictor"}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    input_data = np.array([[getattr(request, f) for f in feature_names]])
    rul = float(model.predict(input_data)[0])
    
    if rul < 20:
        risk = "critical"
    elif rul < 50:
        risk = "high"
    else:
        risk = "normal"
    
    return {"rul": round(rul, 2), "risk_level": risk}

@app.get("/health")
def health():
    return {"status": "ok"}
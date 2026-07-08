from pydantic import BaseModel

class PredictionRequest(BaseModel):
    sensor_1: float
    sensor_2: float
    sensor_5: float
    sensor_6: float
    sensor_7: float
    sensor_9: float
    sensor_10: float
    sensor_11: float
    sensor_12: float
    sensor_14: float
    sensor_15: float
    sensor_16: float
    sensor_17: float
    sensor_18: float
    sensor_20: float
    setting_2: float
    setting_3: float

class PredictionResponse(BaseModel):
    rul: float
    risk_level: str
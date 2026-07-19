from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import joblib

# ----------------------------
# Load Model
# ----------------------------
try:
    model = joblib.load("linear_regression.pkl")
except Exception as e:
    raise RuntimeError(f"Unable to load model: {e}")

# ----------------------------
# FastAPI App
# ----------------------------
app = FastAPI(
    title="Manufacturing Equipment Output Prediction API",
    description="Predict hourly production output of injection molding machines using Linear Regression.",
    version="1.0.0"
)

# ----------------------------
# Input Schema
# ----------------------------

class MachineInput(BaseModel):

    Injection_Temperature: float = Field(..., example=220)
    Injection_Pressure: float = Field(..., example=150)
    Cycle_Time: float = Field(..., example=25)
    Cooling_Time: float = Field(..., example=15)
    Material_Viscosity: float = Field(..., example=120)
    Ambient_Temperature: float = Field(..., example=30)
    Machine_Age: int = Field(..., example=5)
    Operator_Experience: float = Field(..., example=4)
    Maintenance_Hours: float = Field(..., example=12)

    Shift: str = Field(..., example="Day")
    Machine_Type: str = Field(..., example="Type_A")
    Material_Grade: str = Field(..., example="Standard")
    Day_of_Week: str = Field(..., example="Monday")

    Temperature_Pressure_Ratio: float = Field(..., example=1.47)
    Total_Cycle_Time: float = Field(..., example=40)
    Efficiency_Score: float = Field(..., example=85)
    Machine_Utilization: float = Field(..., example=90)


# ----------------------------
# Home
# ----------------------------

@app.get("/")
def home():
    return {
        "message": "Manufacturing Equipment Output Prediction API is Running",
        "model": "Linear Regression",
        "status": "Healthy"
    }


# ----------------------------
# Health Check
# ----------------------------

@app.get("/health")
def health():
    return {
        "status": "OK",
        "model_loaded": True
    }


# ----------------------------
# Prediction Endpoint
# ----------------------------

@app.post("/predict")
def predict(data: MachineInput):

    try:

        input_df = pd.DataFrame([data.dict()])

        prediction = model.predict(input_df)[0]

        return {
            "Predicted_Parts_Per_Hour": round(float(prediction),2)
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
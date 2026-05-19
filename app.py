"""
app.py
------
FastAPI application that serves weather predictions using the
trained Decision Tree model (5 features, 4 weather classes).
Serves a static HTML frontend at the root URL.
"""

import pickle

import pandas as pd
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# ── Load the trained model and label encoder ────────────────────────
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# ── FastAPI app instance ────────────────────────────────────────────
app = FastAPI(
    title="Weather Prediction API",
    description="Predict weather conditions (Sunny / Cloudy / Rainy / Stormy) "
                "based on Temperature, Humidity, Wind Speed, Pressure, "
                "and Cloud Cover values.",
    version="2.0.0",
)

# ── Serve static assets (CSS / JS / images if needed later) ─────────
app.mount("/static", StaticFiles(directory="static"), name="static")


# ── Request schema ──────────────────────────────────────────────────
class WeatherInput(BaseModel):
    temperature: float
    humidity: float
    wind_speed: float
    pressure: float
    cloud_cover: float


# ── Endpoints ───────────────────────────────────────────────────────
@app.get("/")
def home():
    """Serve the frontend UI."""
    return FileResponse("static/index.html")


@app.post("/predict")
def predict(data: WeatherInput):
    """Predict the weather condition from 5 input features."""
    input_data = pd.DataFrame(
        [[data.temperature, data.humidity, data.wind_speed,
          data.pressure, data.cloud_cover]],
        columns=["Temperature", "Humidity", "Wind_Speed",
                 "Pressure", "Cloud_Cover"],
    )
    prediction = model.predict(input_data)
    predicted_label = label_encoder.inverse_transform(prediction)[0]
    return {"predicted_weather": predicted_label}

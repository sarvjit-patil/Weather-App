# Weather Prediction API using FastAPI and MLFlow

A simple Machine Learning based web API that predicts weather conditions
(Sunny / Cloudy / Rainy / Stormy) based on five weather parameters.

## Tech Stack

| Tool            | Purpose                          |
|-----------------|----------------------------------|
| **Python**      | Programming language             |
| **FastAPI**     | REST API framework               |
| **scikit-learn**| Decision Tree Classifier         |
| **MLFlow**      | Experiment tracking & model logging |
| **Docker**      | Application containerization     |
| **GitHub**      | Version control                  |

## Project Structure

```
weatherapp/
├── app.py                # FastAPI application
├── train_model.py        # Model training script with MLFlow
├── generate_dataset.py   # Dataset generation script
├── weather.csv           # Training dataset (1000 rows, 6 columns)
├── model.pkl             # Trained model (generated)
├── label_encoder.pkl     # Label encoder (generated)
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

## Dataset

The dataset (`weather.csv`) contains **1000 rows** and **6 columns**:

| Column       | Type    | Description                         |
|--------------|---------|-------------------------------------|
| Temperature  | float   | Temperature in °C (10–40)           |
| Humidity     | float   | Humidity percentage (20–100)        |
| Wind_Speed   | float   | Wind speed in km/h (0–60)          |
| Pressure     | float   | Atmospheric pressure in hPa (970–1030) |
| Cloud_Cover  | float   | Cloud cover percentage (0–100)      |
| Weather      | string  | Target: Sunny, Cloudy, Rainy, Stormy |

## Setup & Run (Local)

### 1. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate the Dataset (optional — already included)

```bash
python generate_dataset.py
```

### 4. Train the Model

```bash
python train_model.py
```

This creates `model.pkl` and `label_encoder.pkl`, and logs the experiment to MLFlow.

### 5. Run the FastAPI Server

```bash
uvicorn app:app --reload
```

Open your browser at **http://127.0.0.1:8000** to see the welcome message.  
Interactive API docs are available at **http://127.0.0.1:8000/docs**.

### 6. View MLFlow Dashboard

```bash
mlflow ui
```

Open **http://127.0.0.1:5000** to view experiment runs, parameters, and metrics.

## Docker

### Build the Image

```bash
docker build -t weather-api .
```

### Run the Container

```bash
docker run -p 8000:8000 weather-api
```

## API Endpoints

### `GET /`

Returns a welcome message.

**Response:**
```json
{
  "message": "Welcome to the Weather Prediction API!",
  "usage": "Send a POST request to /predict with temperature, humidity, wind_speed, pressure, and cloud_cover."
}
```

### `POST /predict`

Predicts weather condition from five input parameters.

**Request Body:**
```json
{
  "temperature": 35,
  "humidity": 30,
  "wind_speed": 5,
  "pressure": 1025,
  "cloud_cover": 10
}
```

**Response:**
```json
{
  "predicted_weather": "Sunny"
}
```

## GitHub Commands

```bash
git init
git add .
git commit -m "Initial Commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

## Application Workflow

1. User sends temperature, humidity, wind speed, pressure, and cloud cover via POST `/predict`.
2. FastAPI receives and validates the request.
3. The trained Decision Tree model processes the input.
4. The API returns the predicted weather condition.
5. MLFlow logs model parameters and accuracy during training.
6. Docker runs the entire application inside a container.

## Author

Weather Prediction API — ISE Practical Submission

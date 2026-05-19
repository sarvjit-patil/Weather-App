"""
train_model.py
--------------
Trains a Decision Tree Classifier on weather.csv (1000 rows, 5 features)
and logs the experiment to MLFlow.  The trained model is saved as model.pkl.
"""

import pickle

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# ── 1. Load the dataset ────────────────────────────────────────────
df = pd.read_csv("weather.csv")
print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print(df.head())
print(f"\nClass distribution:\n{df['Weather'].value_counts()}\n")

# ── 2. Prepare features and labels ─────────────────────────────────
FEATURES = ["Temperature", "Humidity", "Wind_Speed", "Pressure", "Cloud_Cover"]

X = df[FEATURES]
y = df["Weather"]

# Encode the target labels (Sunny, Cloudy, Rainy, Stormy) → integers
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# ── 3. Split into train / test sets ────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# ── 4. Train with MLFlow tracking ──────────────────────────────────
mlflow.set_experiment("Weather_Prediction_Experiment")

with mlflow.start_run():
    # Hyperparameters
    max_depth = 10
    random_state = 42

    # Train the Decision Tree Classifier
    model = DecisionTreeClassifier(
        max_depth=max_depth, random_state=random_state
    )
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Log parameters and metrics to MLFlow
    mlflow.log_param("model_type", "DecisionTreeClassifier")
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_param("random_state", random_state)
    mlflow.log_param("test_size", 0.2)
    mlflow.log_param("num_features", len(FEATURES))
    mlflow.log_param("features", ", ".join(FEATURES))
    mlflow.log_param("dataset_rows", df.shape[0])
    mlflow.log_metric("accuracy", accuracy)

    # Log the sklearn model artifact to MLFlow
    mlflow.sklearn.log_model(model, "weather_model")

    print(f"Model trained successfully!")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(f"MLFlow Run ID: {mlflow.active_run().info.run_id}")
    print(f"\nClassification Report:\n")
    print(classification_report(
        y_test, y_pred,
        target_names=label_encoder.classes_,
    ))

# ── 5. Save model and label-encoder locally ────────────────────────
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)

print("model.pkl and label_encoder.pkl saved to disk.")

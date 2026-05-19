"""
generate_dataset.py
-------------------
Generates a realistic 1000-row weather dataset with 5 feature columns
and 1 target column.  The data has logical correlations between
features and weather conditions.
"""

import csv
import random

random.seed(42)

ROWS = 1000

# Weather rules (approximate real-world correlations):
#   Sunny  → high temp, low humidity, low wind, high pressure, low cloud
#   Cloudy → moderate temp, moderate humidity, moderate wind, mid pressure, mid-high cloud
#   Rainy  → warm temp, high humidity, moderate wind, low pressure, high cloud
#   Stormy → any temp, very high humidity, high wind, very low pressure, very high cloud

def generate_row(weather):
    if weather == "Sunny":
        temp       = round(random.uniform(25, 40), 1)
        humidity   = round(random.uniform(20, 50), 1)
        wind_speed = round(random.uniform(0, 15), 1)
        pressure   = round(random.uniform(1010, 1030), 1)
        cloud_cover= round(random.uniform(0, 25), 1)
    elif weather == "Cloudy":
        temp       = round(random.uniform(18, 32), 1)
        humidity   = round(random.uniform(45, 75), 1)
        wind_speed = round(random.uniform(5, 25), 1)
        pressure   = round(random.uniform(1000, 1018), 1)
        cloud_cover= round(random.uniform(40, 80), 1)
    elif weather == "Rainy":
        temp       = round(random.uniform(15, 30), 1)
        humidity   = round(random.uniform(70, 95), 1)
        wind_speed = round(random.uniform(10, 35), 1)
        pressure   = round(random.uniform(990, 1010), 1)
        cloud_cover= round(random.uniform(70, 100), 1)
    else:  # Stormy
        temp       = round(random.uniform(10, 35), 1)
        humidity   = round(random.uniform(80, 100), 1)
        wind_speed = round(random.uniform(30, 60), 1)
        pressure   = round(random.uniform(970, 1000), 1)
        cloud_cover= round(random.uniform(85, 100), 1)
    return [temp, humidity, wind_speed, pressure, cloud_cover, weather]


# Distribution: 30% Sunny, 30% Cloudy, 25% Rainy, 15% Stormy
weights = ["Sunny"] * 300 + ["Cloudy"] * 300 + ["Rainy"] * 250 + ["Stormy"] * 150

random.shuffle(weights)

rows = [generate_row(w) for w in weights]

with open("weather.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Temperature", "Humidity", "Wind_Speed", "Pressure", "Cloud_Cover", "Weather"])
    writer.writerows(rows)

print(f"Generated weather.csv with {len(rows)} rows and 6 columns.")

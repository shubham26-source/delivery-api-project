import kagglehub
import pandas as pd
import os
import numpy as np

# Download dataset
path = kagglehub.dataset_download("bhanupratapbiswas/food-delivery-time-prediction-case-study")

files = os.listdir(path)

# Load Excel
df = pd.read_excel(os.path.join(path, files[0]))

# ---------------- STEP 1: Create distance ----------------
def calculate_distance(lat1, lon1, lat2, lon2):
    return np.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

df['distance'] = calculate_distance(
    df['Restaurant_latitude'],
    df['Restaurant_longitude'],
    df['Delivery_location_latitude'],
    df['Delivery_location_longitude']
)

# ---------------- STEP 2: Encode categorical ----------------
df = pd.get_dummies(df, columns=['Type_of_order', 'Type_of_vehicle'], drop_first=True)

# ---------------- STEP 3: Drop unnecessary columns ----------------
df = df.drop(['ID', 'Delivery_person_ID'], axis=1)

# ---------------- SAVE ----------------
df.to_csv("processed_data.csv", index=False)

print("Processed data saved!")
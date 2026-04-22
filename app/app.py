from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
import os

model_path = os.path.join(os.path.dirname(__file__), '..', 'model.pkl')
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return "Delivery Time Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Extract inputs
    features = [
        data['Delivery_person_Age'],
        data['Delivery_person_Ratings'],
        data['distance']
    ]

    # Convert to array
    final_features = np.array([features])

    prediction = model.predict(final_features)

    return jsonify({
        "predicted_delivery_time": float(prediction[0])
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
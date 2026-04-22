from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load trained model
model_path = os.path.join(os.path.dirname(__file__), '..', 'model.pkl')
model = pickle.load(open(model_path, 'rb'))

# Home route (UI)
@app.route('/')
def home():
    return render_template('index.html')

# Prediction API
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        # Extract inputs
        features = [
            data['Delivery_person_Age'],
            data['Delivery_person_Ratings'],
            data['distance']
        ]

        # Convert to numpy array
        final_features = np.array([features])

        # Predict
        prediction = model.predict(final_features)

        return jsonify({
            "predicted_delivery_time": float(prediction[0])
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

# 🚚 Delivery Time Prediction System

## 📌 Project Overview

This project predicts food delivery time using a Machine Learning model and provides a complete end-to-end system including a web interface, API, Docker containerization, and CI/CD pipeline using Jenkins.

---

## 🎯 Features

* 📊 Machine Learning model for delivery time prediction
* 🌐 Interactive web UI for user input
* ⚙️ Flask API for predictions
* 🐳 Dockerized application
* 🔁 CI/CD pipeline using Jenkins

---

## 🧠 How It Works

1. User enters:

   * Delivery Person Age
   * Delivery Person Rating
   * Distance
2. Data is sent to Flask API
3. ML model predicts delivery time
4. Result is displayed on UI

---

## 🏗️ Tech Stack

* Python
* Flask
* Scikit-learn
* HTML, CSS, JavaScript
* Docker
* Jenkins

---

## 🚀 Running the Project

### 🔹 Option 1: Run Locally

```bash
pip install -r requirements.txt
python app/app.py
```

Open:

```
http://localhost:5000
```

---

### 🔹 Option 2: Run with Docker

```bash
docker build -t delivery-api .
docker run -p 5000:5000 delivery-api
```

---

## 🔁 CI/CD Pipeline (Jenkins)

* Pulls code from GitHub
* Builds Docker image
* Stops old container
* Runs updated container automatically

---

## ⚠️ Limitations

* Does not include real-time traffic or weather data
* Uses simplified features for prediction

---

## 🔮 Future Improvements

* Integrate real-time traffic APIs (Google Maps)
* Add weather data
* Include time-of-day and order type features
* Improve model accuracy with advanced algorithms

---

## 👨‍💻 Author

Shubham Sharma

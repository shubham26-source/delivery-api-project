import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load processed data
df = pd.read_csv("processed_data.csv")

X = df[['Delivery_person_Age', 'Delivery_person_Ratings', 'distance']]
y = df['Time_taken(min)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

print("Model trained!")

pickle.dump(model, open('model.pkl', 'wb'))
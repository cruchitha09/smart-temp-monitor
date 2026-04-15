import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")
temps = data['temperature'].values

# Prepare data (3 inputs → 1 output)
X = []
y = []

window_size = 3

for i in range(len(temps) - window_size):
    X.append(temps[i:i+window_size])
    y.append(temps[i+window_size])

X = np.array(X)
y = np.array(y)

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

# Check accuracy
from sklearn.metrics import mean_absolute_error
y_pred = model.predict(X)
mae = mean_absolute_error(y, y_pred)

print("Model trained successfully")
print("MAE:", mae)
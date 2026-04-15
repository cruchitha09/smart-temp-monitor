import sys
import json
import pickle
import numpy as np
import os

try:
    # Get current file directory
    base_dir = os.path.dirname(__file__)

    # Correct path to model.pkl
    model_path = os.path.join(base_dir, "model.pkl")

    # Load model
    model = pickle.load(open(model_path, "rb"))

    # Get input from Node.js
    data = json.loads(sys.argv[1])

    # Validate input
    if not isinstance(data, list) or len(data) < 3:
        print("Error: Need at least 3 numeric values")
        sys.exit()

    # Convert to numpy array
    input_data = np.array(data[-3:], dtype=float).reshape(1, -1)

    # Predict
    prediction = model.predict(input_data)

    # Print ONLY number (important for Node.js)
    print(float(prediction[0]))

except Exception as e:
    print("Error:", str(e))
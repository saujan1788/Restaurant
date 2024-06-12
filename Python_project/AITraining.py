import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# Load the cleaned data
file_path = "Python_project/DataLake/CleanFileByScript.xlsx"
df = pd.read_excel(file_path)

# Ensure the necessary columns are treated as the correct types
df['TIME_NUMERIC'] = df['TIME_NUMERIC'].astype(float)
df['PAX_CLEANED'] = df['PAX_CLEANED'].astype(int)

# Features and target
X = df[['TIME_NUMERIC']].values
y = df['PAX_CLEANED'].values

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the model
model = Sequential([
    Input(shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1)  # Output layer for regression
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=50, validation_split=0.2)

# Evaluate on the test set
test_loss = model.evaluate(X_test, y_test)
print(f'Test Loss: {test_loss}')

# Make predictions
y_pred = model.predict(X_test)

# Compare predictions with actual values
print("First 10 Predictions vs Actual Values:")
for i in range(10):  # Print the first 10 predictions
    print(f'Actual: {y_test[i]}, Predicted: {y_pred[i][0]}')

# Save the model
model.save('Python_project/DataLake/TrainedModel.h5')

print("Model training complete and model saved to TrainedModel.h5")

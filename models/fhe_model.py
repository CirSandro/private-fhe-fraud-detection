"""
Module for training and deploying an FHE-enabled
Random Forest model using Concrete ML.

This module trains a Random Forest model on a balanced dataset of credit card
fraud transactions, applies homomorphic encryption to the trained model using
Concrete ML, and saves the necessary files for later deployment.

The following steps are performed:
1. Data loading and preprocessing
2. Balancing the dataset
3. Feature scaling
4. Model training
5. Homomorphic encryption and model deployment
"""

import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from concrete.ml.sklearn.rf import RandomForestClassifier
from concrete.ml.deployment import FHEModelDev

# Load the data (100,000 rows only)
DATA_PATH = os.path.join(os.path.abspath(os.getcwd()), "dataset", "card_transdata.csv")
df = pd.read_csv(DATA_PATH, nrows=100000)  # Limit to 100,000 rows

# Check for missing values
if df.isnull().sum().any():
    df = df.dropna()

# Handle class imbalance
fraud = df[df["fraud"] == 1]
non_fraud = df[df["fraud"] == 0].sample(n=len(fraud), random_state=42)
balanced_df = pd.concat([fraud, non_fraud])

# Separate features and target
X = balanced_df.drop(columns=["fraud"])
y = balanced_df["fraud"].astype(int)

# Split into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Preprocessing: scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

# Save the scaler for later use
SCALER_PATH = os.path.join(os.path.abspath(os.getcwd()), "models", "scaler.pkl")
joblib.dump(scaler, SCALER_PATH)

# Train the Random Forest model with Concrete ML
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Compile the model for homomorphic encryption
model.compile(X_train_scaled)

# Save the model and necessary files for client and server
FHE_DIRECTORY = os.path.join(os.path.abspath(os.getcwd()), "models", "fhe_files")
dev = FHEModelDev(path_dir=FHE_DIRECTORY, model=model)
dev.save()

print("Model trained, compiled, and saved.")

##############################################################################
##############################################################################
##############################################################################

"""
Generate new data using synthezizer using XGBoost.
"""

# Load packages
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import xgboost as xgb

from sklearn.preprocessing import LabelEncoder

# Load data

## Remove "Modules" from the string
path_folder = script_dir.replace("\\Modules", "")
path_file = '\\data\\data_v2.parquet'

df = pd.read_parquet(path_folder + path_file)

# XGBoost synthetizer --------------------------------------------------------

n_size = df.shape[0] # size to generate

## Prepare data for XGBoost ..................................................

# Encode categorical variables
encoded_data = df.copy()
label_encoders = {}

# Identify categorical columns and encode them
for col in encoded_data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    encoded_data[col] = le.fit_transform(encoded_data[col])
    label_encoders[col] = le

# Display the first few rows of the encoded data
encoded_data.head()

# Step 1: Simulate a target variable using clustering ........................
# Use KMeans to group similar rows and assign cluster labels as synthetic targets
n_clusters = 5  # Define the number of clusters
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
synthetic_targets = kmeans.fit_predict(encoded_data)

# Add the synthetic target to the data
encoded_data_with_target = encoded_data.copy()
encoded_data_with_target['synthetic_target'] = synthetic_targets

# Step 2: Train XGBoost using synthetic targets ..............................
X = encoded_data_with_target.drop(columns=['synthetic_target'])
y = encoded_data_with_target['synthetic_target']

# Convert to DMatrix for XGBoost
dtrain = xgb.DMatrix(X, label=y)

# Train the model
params = {
    "objective": "multi:softprob",  # Multi-class classification
    "num_class": n_clusters,       # Number of clusters
    "max_depth": 6,
    "eta": 0.1,
    "seed": 42,
}
model = xgb.train(params, dtrain, num_boost_round=100)

# Step 3: Generate synthetic data ............................................
def generate_synthetic_data_XGBoost(model, original_data, n_samples=500):
    """
    Generate synthetic data based on the trained XGBoost model.
    """
    sampled_data = original_data.sample(n=n_samples, replace=True, random_state=42)
    dmatrix = xgb.DMatrix(sampled_data)
    synthetic_targets = model.predict(dmatrix).argmax(axis=1)  # Predicted cluster labels
    synthetic_data = sampled_data.copy()
    synthetic_data['synthetic_target'] = synthetic_targets
    return synthetic_data

# Generate synthetic data
synth_data = generate_synthetic_data_XGBoost(model, X, 
                                             n_samples = n_size)

# Save ----------------------------------------------------------------------

# Save to csv
path_save = '\\synth\\synth_XGBoost.csv'
synth_data.to_csv(path_folder + path_save, 
                  index=False)

# Save to parquet 
path_save = '\\synth\\synth_XGBoost.parquet'
synth_data.to_parquet(path_folder + path_save)

##############################################################################
##############################################################################
##############################################################################
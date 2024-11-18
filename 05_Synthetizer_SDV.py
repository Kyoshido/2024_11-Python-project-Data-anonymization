##############################################################################
##############################################################################
##############################################################################

# Load packages
import pandas as pd
from DataSynthesizer.DataDescriber import DataDescriber
from DataSynthesizer.DataGenerator import DataGenerator
from DataSynthesizer.ModelInspector import ModelInspector

# Load data
path = 'data/data_v2.parquet'
df = pd.read_parquet(path)

# DataSynthesizer ------------------------------------------------------------

# Step 1: Describe the original dataset
input_data = 'data/data_v2.csv'  # Path to your original CSV file
description_file = 'description.json'  # File to save the dataset description
n = df.shape[0]  # Number of rows for the synthetic data

# Describe the dataset
describer = DataDescriber()
describer.describe_dataset_in_correlated_attribute_mode(dataset_file=input_data)
describer.save_dataset_description_to_file(description_file)

# Step 2: Generate synthetic data
generator = DataGenerator()
generator.generate_dataset_in_correlated_attribute_mode(n=n, description_file=description_file)

# Save the synthetic data to a CSV file
synthetic_data = 'synthetic_data.csv'
generator.save_synthetic_data(synthetic_data)

# Load and display the synthetic data
synthetic_df = pd.read_csv(synthetic_data)
print(synthetic_df.head())





##############################################################################
##############################################################################
##############################################################################
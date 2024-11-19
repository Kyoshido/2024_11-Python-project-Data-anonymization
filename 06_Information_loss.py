##############################################################################
##############################################################################
##############################################################################

"""
Evaluate information loss in the data.
"""

# Load packages
import pandas as pd
import matplotlib.pyplot as plt

# Load data
path = 'data/data_v2.parquet'
original_df  = pd.read_parquet(path)

path = 'synth/synth_MostlyAI.parquet'
synthetic_df  = pd.read_parquet(path)

# Information loss -----------------------------------------------------------

# Compare means of each numerical column in original and synthetic datasets
mean_comparison = pd.DataFrame({
    'Original Mean': original_df.mean(numeric_only=True),
    'Synthetic Mean': synthetic_df.mean(numeric_only=True)
})

# Compare quantiles (0.25, 0.5, 0.75) of each numerical column in original and synthetic datasets
quantiles_to_compare = [0.25, 0.5, 0.75]
quantile_comparison = pd.DataFrame()

for quantile in quantiles_to_compare:
    quantile_comparison[f'Original Quantile {quantile}'] = original_df.quantile(quantile, numeric_only=True)
    quantile_comparison[f'Synthetic Quantile {quantile}'] = synthetic_df.quantile(quantile, numeric_only=True)

mean_comparison, quantile_comparison

# Plotting each numerical column comparison between original and synthetic datasets
numeric_columns = original_df.select_dtypes(include=['number']).columns

for column in numeric_columns:
    plt.figure(figsize=(10, 5))
    
    # Plot histogram of the original dataset for the current column
    plt.hist(original_df[column], bins=20, alpha=0.5, label='Original', color='blue', edgecolor='black')

    # Plot histogram of the synthetic dataset for the current column
    plt.hist(synthetic_df[column], bins=20, alpha=0.5, label='Synthetic', color='red', edgecolor='black')
    
    # Add title and labels
    plt.title(f'Comparison of {column} Between Original and Synthetic Data')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.legend()
    
    # Display the plot
    plt.show()

##############################################################################
##############################################################################
##############################################################################
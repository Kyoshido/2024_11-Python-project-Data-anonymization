##############################################################################
##############################################################################
##############################################################################

"""
Evaluate information loss in the data visually.
"""

# Load packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data

## Remove "Modules" from the string
path_folder = script_dir.replace("\\Modules", "")
## Original
path_file = '\\data\\data_v2.parquet'
df_orig = pd.read_parquet(path_folder + path_file)
## MostlyAI
path_file = '\\synth\\synth_MostlyAI.parquet'
df_MostlyAI = pd.read_parquet(path_folder + path_file)
## XGBoost
path_file = '\\synth\\synth_XGBoost_v2.parquet'
df_XGBoost = pd.read_parquet(path_folder + path_file)

# Information loss - Visual comparison ---------------------------------------

# Step 1: Save Numerical Variable Comparisons
def save_numerical_comparisons(orig, mostlyai, xgboost, numerical_columns, output_dir):
    for col in numerical_columns:
        # Boxplot for distributions
        plt.figure(figsize=(10, 6))
        data_to_plot = [orig[col], mostlyai[col], xgboost[col]]
        plt.boxplot(data_to_plot, labels=["Original", "MOSTLY AI", "XGBoost"])
        plt.title(f"Box Plot for {col}")
        plt.ylabel(col)
        plt.savefig(os.path.join(output_dir, f"boxplot_{col}.png"))
        plt.close()

        # Bar plot for means
        means = [orig[col].mean(), mostlyai[col].mean(), xgboost[col].mean()]
        plt.figure(figsize=(8, 5))
        plt.bar(["Original", "MOSTLY AI", "XGBoost"], means)
        plt.title(f"Mean Comparison for {col}")
        plt.ylabel("Mean")
        plt.savefig(os.path.join(output_dir, f"mean_comparison_{col}.png"))
        plt.close()

# Step 2: Save Categorical Variable Comparisons
def save_categorical_comparisons(orig, mostlyai, xgboost, categorical_columns, output_dir):
    for col in categorical_columns:
        # Calculate normalized frequencies
        orig_freq = orig[col].value_counts(normalize=True)
        mostlyai_freq = mostlyai[col].value_counts(normalize=True)
        xgboost_freq = xgboost[col].value_counts(normalize=True)

        # Create a combined DataFrame
        freq_df = pd.DataFrame({
            "Original": orig_freq,
            "MOSTLY AI": mostlyai_freq,
            "XGBoost": xgboost_freq
        }).fillna(0)

        # Plot side-by-side bar charts
        freq_df.plot(kind="bar", figsize=(12, 6))
        plt.title(f"Frequency Distribution Comparison for {col}")
        plt.ylabel("Proportion")
        plt.xlabel(col)
        plt.legend(loc="upper right")
        plt.xticks(rotation=45)
        plt.savefig(os.path.join(output_dir, f"categorical_comparison_{col}.png"))
        plt.close()

# Identify numerical and categorical columns
numerical_columns = df_orig.select_dtypes(include=["int64", "float64"]).columns
categorical_columns = df_orig.select_dtypes(include=["object"]).columns

# Save plots
path_save = '\\utility'
save_numerical_comparisons(
    df_orig, df_MostlyAI, df_XGBoost, 
    numerical_columns, 
    path_folder + path_save)
save_categorical_comparisons(
    df_orig, df_MostlyAI, df_XGBoost, 
    categorical_columns, 
    path_folder + path_save)

##############################################################################
##############################################################################
##############################################################################
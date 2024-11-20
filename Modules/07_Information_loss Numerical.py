##############################################################################
##############################################################################
##############################################################################

"""
Evaluate information loss in the data.
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

# Information loss - Numerical comparison ------------------------------------


# Function to create comparison table for numerical variables
def create_numerical_comparison_table(orig, mostlyai, xgboost, numerical_columns):
    comparison_table = []
    for col in numerical_columns:
        row = {
            "Variable": col,
            "Original Mean": orig[col].mean(),
            "MOSTLY AI Mean": mostlyai[col].mean(),
            "XGBoost Mean": xgboost[col].mean(),
            "Original 25th Percentile": orig[col].quantile(0.25),
            "MOSTLY AI 25th Percentile": mostlyai[col].quantile(0.25),
            "XGBoost 25th Percentile": xgboost[col].quantile(0.25),
            "Original Median": orig[col].median(),
            "MOSTLY AI Median": mostlyai[col].median(),
            "XGBoost Median": xgboost[col].median(),
            "Original 75th Percentile": orig[col].quantile(0.75),
            "MOSTLY AI 75th Percentile": mostlyai[col].quantile(0.75),
            "XGBoost 75th Percentile": xgboost[col].quantile(0.75),
        }
        comparison_table.append(row)
    return pd.DataFrame(comparison_table).T

# Function to create comparison table for categorical variables
def create_categorical_comparison_table(orig, mostlyai, xgboost, categorical_columns):
    comparison_table = []
    for col in categorical_columns:
        row = {
            "Variable": col,
            "Original Distribution": orig[col].value_counts(normalize=True).to_dict(),
            "MOSTLY AI Distribution": mostlyai[col].value_counts(normalize=True).to_dict(),
            "XGBoost Distribution": xgboost[col].value_counts(normalize=True).to_dict(),
        }
        comparison_table.append(row)
    return pd.DataFrame(comparison_table)

# Reformat the categorical comparison table for better readability
def reformat_categorical_comparison_table(categorical_comparison_table):
    reformatted_rows = []
    for _, row in categorical_comparison_table.iterrows():
        variable = row["Variable"]
        for category, original_val in row["Original Distribution"].items():
            reformatted_row = {
                "Variable": variable,
                "Category": category,
                "Original": original_val,
                "MOSTLY AI": row["MOSTLY AI Distribution"].get(category, 0),
                "XGBoost": row["XGBoost Distribution"].get(category, 0),
            }
            reformatted_rows.append(reformatted_row)
    return pd.DataFrame(reformatted_rows)

# Identify numerical and categorical columns
numerical_columns = df_orig.select_dtypes(include=["int64", "float64"]).columns
categorical_columns = df_orig.select_dtypes(include=["object"]).columns

# Create comparison tables
numerical_comparison_table = create_numerical_comparison_table(
    df_orig, df_MostlyAI, df_XGBoost, numerical_columns)
categorical_comparison_table = create_categorical_comparison_table(
    df_orig, df_MostlyAI, df_XGBoost, categorical_columns)

# Reformat the table
reformatted_categorical_comparison = reformat_categorical_comparison_table(
    categorical_comparison_table)

# Print comparison tables
print(numerical_comparison_table)
print(reformatted_categorical_comparison)

# Save ----------------------------------------------------------------------

# Save to csv
path_save = '\\utility\\numerical_comparison.csv'
numerical_comparison_table.to_csv(
                  path_folder + path_save, 
                  index=False)

path_save = '\\utility\\categorical_comparison.csv'
reformatted_categorical_comparison.to_csv(
                  path_folder + path_save, 
                  index=False)

##############################################################################
##############################################################################
##############################################################################
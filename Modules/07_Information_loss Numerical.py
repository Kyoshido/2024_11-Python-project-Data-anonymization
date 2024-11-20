##############################################################################
##############################################################################
##############################################################################

"""
Evaluate information loss in the data numerically.
"""

# Load packages
import pandas as pd
import numpy as np
from utils import create_numerical_comparison_table
from utils import create_categorical_comparison_table
from utils import reformat_categorical_comparison_table

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
                  path_folder + path_save)

path_save = '\\utility\\categorical_comparison.csv'
reformatted_categorical_comparison.to_csv(
                  path_folder + path_save)

##############################################################################
##############################################################################
##############################################################################
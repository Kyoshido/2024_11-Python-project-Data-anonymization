##############################################################################
##############################################################################
##############################################################################

"""
Evaluate information loss in the data visually.
"""

# Load packages
import pandas as pd
import numpy as np
from utils import save_numerical_comparisons
from utils import save_categorical_comparisons

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
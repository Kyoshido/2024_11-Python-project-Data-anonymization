##############################################################################
##############################################################################
##############################################################################

"""
Label data and set back the categories after XGBoost.
After that it is saved with label "_v2".
"""

# Load packages
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load data

## Remove "Modules" from the string
path_folder = script_dir.replace("\\Modules", "")
path_file = '\\synth\\synth_XGBoost.parquet'
df_synt = pd.read_parquet(path_folder + path_file)

path_file = '\\data\\data_v2.parquet'
df_orig = pd.read_parquet(path_folder + path_file)

# Label data -----------------------------------------------------------------

# Rebuild Label Encoders from the original file
label_encoders = {}
for col in df_orig.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    le.fit(df_orig[col])  # Fit to original data
    label_encoders[col] = le

# Decode the synthetic data
def decode_synthetic_data(synthetic_data, label_encoders):
    decoded_data = synthetic_data.copy()
    for col, encoder in label_encoders.items():
        if col in decoded_data.columns:  # Ensure the column exists in synthetic data
            decoded_data[col] = encoder.inverse_transform(decoded_data[col].astype(int))
    return decoded_data

# Decode the synthetic data
decoded_synthetic_data = decode_synthetic_data(df_synt, label_encoders)

# Drop the synthetic target column (if present) before decoding
synth_data = decoded_synthetic_data.drop(
    columns=["synthetic_target"], errors="ignore")

# Save ----------------------------------------------------------------------

# Save to csv
path_save = '\\synth\\synth_XGBoost_v2.csv'
synth_data.to_csv(path_folder + path_save, 
                  index=False)

# Save to parquet 
path_save = '\\synth\\synth_XGBoost_v2.parquet'
synth_data.to_parquet(path_folder + path_save)

##############################################################################
##############################################################################
##############################################################################
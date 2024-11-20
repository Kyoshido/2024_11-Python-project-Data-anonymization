##############################################################################
##############################################################################
##############################################################################

"""
Calculate risk measuremet to evaluate amount of risk in the data.
Metric of k-anonimity is used.

k-Anonymity is a privacy model that ensures that each individual in a dataset 
is indistinguishable from at least k-1 others, thus protecting individuals by 
grouping them into clusters where each group has at least k members with 
similar attributes.
"""

# Load packages
import pandas as pd
from utils import evaluate_k_anonymity

# Load data

## Remove "Modules" from the string
path_folder = script_dir.replace("\\Modules", "")
path_file = '\\data\\data_v2.parquet'

df = pd.read_parquet(path_folder + path_file)

##############################################################################

# Evaluate k-anonymity -------------------------------------------------------

# Initialize the Tool:
anonymizer = evaluate_k_anonymity(path_folder + path_file)

# Set Quasi-Identifiers:
anonymizer.set_quasi_identifiers(["age", "gender", "married", "education"])

# Calculate k-Anonymity:
k_anonymity = anonymizer.calculate_k_anonymity()

# Evaluate Risk:
risk_ok = anonymizer.evaluate_risk(threshold=5)

# Display Grouped Counts:
grouped_counts = anonymizer.display_grouped_counts()

##############################################################################
##############################################################################
##############################################################################
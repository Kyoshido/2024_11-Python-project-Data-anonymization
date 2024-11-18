##############################################################################
##############################################################################
##############################################################################

# Load packages
import pandas as pd

# Load data
path = 'data/data_v2.parquet'
df = pd.read_parquet(path)

# k-anonymity ----------------------------------------------------------------

# Define the columns to use for k-anonymity
quasi_identifiers = ["age", "married"]
quasi_identifiers = ["age", "gender", "married"]
quasi_identifiers = ["age", "gender", "married", "education"]

# Group by the selected quasi-identifiers and calculate the size of each group
grouped = df.groupby(quasi_identifiers
           ).size(
           ).reset_index(name='count'
           ).sort_values(by='count', ascending=True)

# Display the grouping with counts
print(grouped)

# Calculate k-anonymity
k_anonymity = grouped['count'].min()

print(f'k-Anonymity for the given combination of variables ({quasi_identifiers}): {k_anonymity}')

##############################################################################
##############################################################################
##############################################################################
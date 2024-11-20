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

# Load data

## Remove "Modules" from the string
path_folder = script_dir.replace("\\Modules", "")
path_file = '\\data\\data_v2.parquet'

df = pd.read_parquet(path_folder + path_file)

# k-anonymity ----------------------------------------------------------------

class AnonymizationTool:
    def __init__(self, data_path):
        """
        Initialize the tool with the dataset path.
        """
        self.data = pd.read_parquet(data_path)
        self.quasi_identifiers = []

    def set_quasi_identifiers(self, identifiers):
        """
        Set the quasi-identifiers to be used for anonymization.
        """
        self.quasi_identifiers = identifiers

    def calculate_k_anonymity(self):
        """
        Calculate k-anonymity based on the current quasi-identifiers.
        """
        if not self.quasi_identifiers:
            raise ValueError("Quasi-identifiers must be set before calculating k-anonymity.")
        
        grouped = (
            self.data.groupby(self.quasi_identifiers)
                .size()
                .reset_index(name='count')
                .sort_values(by='count', ascending=True)
        )
        
        k_anonymity = grouped['count'].min()
        print(f'K-anonymity for the given combination of quasi-identifiers ({self.quasi_identifiers}): {k_anonymity}')
        return k_anonymity

    def evaluate_risk(self, threshold):
        """
        Evaluate the re-identification risk based on k-anonymity.
        """
        k_anonymity = self.calculate_k_anonymity()
        if k_anonymity < threshold:
            print(f"Warning: The dataset does not meet the k-anonymity threshold ({threshold}).")
        else:
            print(f"The dataset meets the k-anonymity threshold ({threshold}).")
        return k_anonymity >= threshold

    def display_grouped_counts(self):
        """
        Display the grouped counts for the current quasi-identifiers.
        """
        if not self.quasi_identifiers:
            raise ValueError("Quasi-identifiers must be set before displaying grouped counts.")
        
        grouped = (
            self.data.groupby(self.quasi_identifiers)
            .size()
            .reset_index(name='count')
            .sort_values(by='count', ascending=True)
        )
        print("Grouped Counts:")
        print(grouped)
        return grouped



# Usage Example --------------------------------------------------------------

# Initialize the Tool:
anonymizer = AnonymizationTool(path_folder + path_file)

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
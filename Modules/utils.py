###############################################################################
###############################################################################
###############################################################################

"""
Additional custom functions.
"""

###############################################################################

# Helper function to create table ---------------------------------------------

# Package
import pandas as pd

# Show all rows by setting the display options:
pd.set_option('display.max_rows', None)  # Show all rows

# Function
def table(dataframe, column_name):
    """
    Creates a frequency table for the specified column in the given DataFrame.
    
    Parameters:
        dataframe (pd.DataFrame): A DataFrame that contains the data.
        column_name (str): The name of the column to create the table for.
    
    Return value:
        pd.DataFrame: Frequency table with a column of values ​​and their frequency.
    """
    table = pd.DataFrame(dataframe[column_name].value_counts(
                                              ).sort_index()
                        ).reset_index()
    table.columns = [column_name, 'Frequency']
    # ---
    return table

###############################################################################

# Custom function to describe variable ----------------------------------------

# Package
import matplotlib.pyplot as plt

# Function
def overview(df, column_name, description, chart_type, hist_bins = 10):
    """
    Analyzes the specified column in a DataFrame by displaying descriptive statistics
    and generating a bar chart.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the column.
        column_name (str): The name of the column to analyze (default: 'engnat').

    Returns:
        pandas.Series: Descriptive statistics of the column.
    """
    # Descriptive statistics
    stats = df[column_name].describe()
    print("Descriptive Statistics:")
    # print(stats)
    
    # Visualization

    if chart_type == 'hist':
        # Plot histogram
        df[column_name].plot.hist(color='skyblue', 
                                  bins=hist_bins)
        plt.title(f'Histogram for {description}')
        plt.xlabel(column_name)
        plt.ylabel('Frequency')
        plt.show()
    elif chart_type == 'bar':
        # Plot bar chart
        df[column_name].value_counts(
                      ).plot(kind='bar', 
                             color='skyblue')
        plt.title(f'Bar Chart for {description}')
        plt.xlabel(column_name)
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        plt.show()
    else:
        raise ValueError("Invalid chart_type. Use 'bar' or 'hist'.")
    # ---
    return stats

###############################################################################

# Evaluate k-anonymity --------------------------------------------------------

class evaluate_k_anonymity:
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

###############################################################################

# Generate synthetic data -----------------------------------------------------
def generate_synthetic_data_XGBoost(model, original_data, n_samples=500):
    """
    Generate synthetic data based on the trained XGBoost model.
    """
    sampled_data = original_data.sample(n=n_samples, replace=True, random_state=42)
    dmatrix = xgb.DMatrix(sampled_data)
    synthetic_targets = model.predict(dmatrix).argmax(axis=1)  # Predicted cluster labels
    synthetic_data = sampled_data.copy()
    synthetic_data['synthetic_target'] = synthetic_targets
    return synthetic_data

###############################################################################

# Decode the synthetic data ---------------------------------------------------

# Package
from sklearn.preprocessing import LabelEncoder

# Function
def decode_synthetic_data(synthetic_data, label_encoders):
    decoded_data = synthetic_data.copy()
    for col, encoder in label_encoders.items():
        if col in decoded_data.columns:  # Ensure the column exists in synthetic data
            decoded_data[col] = encoder.inverse_transform(decoded_data[col].astype(int))
    return decoded_data

###############################################################################

# Function to create comparison table for numerical variables -----------------
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

###############################################################################

# Function to create comparison table for categorical variables ---------------
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

###############################################################################

# Reformat the categorical comparison table for better readability ------------
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

###############################################################################
###############################################################################
###############################################################################
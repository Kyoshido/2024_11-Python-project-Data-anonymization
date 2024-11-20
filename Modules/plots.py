###############################################################################
###############################################################################
###############################################################################

"""
Additional custom functions. 
Here are specified visual functions.
"""

###############################################################################

# Save Numerical Variable Comparisons ----------------------------------------

# Package
import matplotlib.pyplot as plt

# Function
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

###############################################################################

# Save Categorical Variable Comparisons --------------------------------------

# Package
import matplotlib.pyplot as plt

# Function
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

###############################################################################
###############################################################################
###############################################################################
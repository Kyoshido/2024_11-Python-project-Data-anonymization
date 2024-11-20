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
###############################################################################
###############################################################################
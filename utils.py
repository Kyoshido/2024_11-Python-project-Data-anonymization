# Helper function to create table ---------------------------------------------
import pandas as pd

# Show all rows by setting the display options:
pd.set_option('display.max_rows', None)  # Show all rows

def table(dataframe, column_name):
    """
    Creates a frequency table for the specified column in the given DataFrame.
    
    Parameters:
        dataframe (pd.DataFrame): A DataFrame that contains the data.
        column_name (str): The name of the column to create the table for.
    
    Return value:
        pd.DataFrame: Frequency table with a column of values ​​and their frequency.
    """
    table = pd.DataFrame(dataframe[column_name].value_counts().sort_index()).reset_index()
    table.columns = [column_name, 'Frequency']
    return table
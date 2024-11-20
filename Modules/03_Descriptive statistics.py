##############################################################################
##############################################################################
##############################################################################

"""
Calculate some descriptive statistics to see weaknesses of the data.
For each variable we calculate frequency table and plot a histogram.
"""

# Load packages
import pandas as pd
import matplotlib.pyplot as plt
from utils import overview

# Load data

## Remove "Modules" from the string
path_folder = script_dir.replace("\\Modules", "")
path_file = '\\data\\data_v2.parquet'

df = pd.read_parquet(path_folder + path_file)

##############################################################################

# Descriptive statistics ------------------------------------------------------

# Age .....................................................
overview(df, "age", "Age", "hist", 50)

# Gender ..................................................
overview(df, "gender", "Gender", "bar")

# Married .................................................
overview(df, "married", "Marital Status", "bar")

# Religion ................................................
overview(df, "religion", "Religion", "bar")

# Education ...............................................
overview(df, "education", "Education", "bar")

# Urban ...................................................
overview(df, "urban", "Urban Residence", "bar")

# English Native ..........................................
overview(df, "engnat", "English Native", "bar")

# Handedness ..............................................
overview(df, "hand", "Handedness", "bar")

# Sexual Orientation ......................................
overview(df, "orientation", "Sexual Orientation", "bar")

# Race ....................................................
overview(df, "race", "Race", "bar")

# Voted  ..................................................
overview(df, "voted", "Voting", "bar")

# Family size .............................................
overview(df, "familysize", "Family Size", "bar")

##############################################################################
##############################################################################
##############################################################################
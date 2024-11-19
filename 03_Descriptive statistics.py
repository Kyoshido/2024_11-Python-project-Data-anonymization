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
path = 'data/data_v2.parquet'
df = pd.read_parquet(path)

# Descriptive statistics ------------------------------------------------------

# Age .....................................................
overview(df, "age", "Age")

# Gender ..................................................
overview(df, "gender", "Gender")

# Married .................................................
overview(df, "married", "Marital Status")

# Religion ................................................
overview(df, "religion", "Religion")

# Education ...............................................
overview(df, "education", "Education")

# Urban ...................................................
overview(df, "urban", "Urban Residence")

# English Native ..........................................
overview(df, "engnat", "English Native")

# Handedness ..............................................
overview(df, "hand", "Handedness")

# Sexual Orientation ......................................
overview(df, "orientation", "Sexual Orientation")

# Race ....................................................
overview(df, "race", "Race")

# Voted  ..................................................
overview(df, "voted", "Voting")

# Family size .............................................
overview(df, "familysize", "Family Size")

##############################################################################
##############################################################################
##############################################################################
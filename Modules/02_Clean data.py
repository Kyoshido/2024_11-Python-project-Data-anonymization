##############################################################################
##############################################################################
##############################################################################

"""
Clean dataset.
First we select only specific columns.
Then we check variables one by one and adjust them properly.
At the end, it is save as data_v2.
"""

# Load packages
import pandas as pd
from utils import table

# Load data

## Remove "Modules" from the string
path_folder = script_dir.replace("\\Modules", "")
path_file = '\\data\\data.csv'

df = pd.read_csv(path_folder + path_file, 
                 delimiter='\t'
                 )

# Clean data -----------------------------------------------------------------

# Select specific columns
var_select = [
    "age", "gender", "married", "religion", "education", "urban",
    "engnat", "hand", "orientation", "race", "voted", "familysize"
]
df = df[var_select]

# Age .....................................................
## table
table_var = table(df, 'age')
print(table_var)

## Filter invalid records
df = df[df['age'] < 111] # max is 110
table_filter = table(df, 'age')
print(table_filter)

# Gender ..................................................
# 1=Male, 2=Female, 3=Other
## table
table_var = table(df, 'gender')
print(table_var)

## Filter invalid records
len(df[~df['gender'].isin([1, 2])]) # ~ is negation
df['gender'] = df['gender'].map({
    1: "Male", 
    2: "Female"
})
table_filter = table(df, 'gender')
print(table_filter)

# Married .................................................
## table
table_var = table(df, 'married')
print(table_var)

## Filter invalid records
df = df[df['married'].isin([1, 2, 3])]
df['married'] = df['married'].map({
    1: "Never married",
    2: "Currently married",
    3: "Previously married"
})
table_filter = table(df, 'married')
print(table_filter)

# Religion ................................................
## table
table_var = table(df, 'religion')
print(table_var)

## Filter invalid records
df = df[df['religion'].isin(range(1, 11))]
df['religion'] = df['religion'].map({
    1: "Agnostic", 
    2: "Atheist", 
    3: "Buddhist", 
    4: "Catholic",
    5: "Mormon", 
    6: "Protestant", 
    7: "Other Christian",
    8: "Hindu", 
    9: "Jewish", 
    10: "Muslim", 
    11: "Sikh"
})
table_filter = table(df, 'religion')
print(table_filter)

# Education ...............................................
## table
table_var = table(df, 'education')
print(table_var)

## Filter invalid records
df = df[df['education'].isin([1, 2, 3, 4])]
df['education'] = df['education'].map({
    1: "Lesser", 
    2: "High school", 
    3: "University", 
    4: "Graduate"
})
table_filter = table(df, 'education')
print(table_filter)

# Urban ...................................................
## table
table_var = table(df, 'urban')
print(table_var)

## Filter invalid records
df = df[df['urban'].isin([1, 2, 3])]
df['urban'] = df['urban'].map({
    1: "Rural", 
    2: "Suburban", 
    3: "Urban"
})
table_filter = table(df, 'urban')
print(table_filter)

# English Native ..........................................
## table
table_var = table(df, 'engnat')
print(table_var)

## Filter invalid records
df = df[df['engnat'].isin([1, 2])]
df['engnat'] = df['engnat'].map({
    1: "Yes", 
    2: "No"
    })
table_filter = table(df, 'engnat')
print(table_filter)

# Handedness ..............................................
## table
table_var = table(df, 'hand')
print(table_var)

## Filter invalid records
df = df[df['hand'].isin([1, 2, 3])]
df['hand'] = df['hand'].map({
    1: "Right", 
    2: "Left", 
    3: "Both"
})
table_filter = table(df, 'hand')
print(table_filter)

# Sexual Orientation ......................................
## table
table_var = table(df, 'orientation')
print(table_var)

## Filter invalid records
df = df[df['orientation'].isin(range(1, 6))]
df['orientation'] = df['orientation'].map({
    1: "Heterosexual", 
    2: "Bisexual", 
    3: "Homosexual",
    4: "Asexual", 
    5: "Other"
})
table_filter = table(df, 'orientation')
print(table_filter)

# Race ....................................................
## table
table_var = table(df, 'race')
print(table_var)

## Filter invalid records
df = df[df['race'].isin([10, 20, 30, 50, 60, 70])]
df['race'] = df['race'].map({
    10: "Asian", 
    20: "Arab", 
    30: "Black",
    50: "Native American", 
    60: "White", 
    70: "Other"
})
table_filter = table(df, 'race')
print(table_filter)

# Voted  ..................................................
## table
table_var = table(df, 'voted')
print(table_var)

## Filter invalid records
df = df[df['voted'].isin([1, 2])]
df['voted'] = df['voted'].map({
    1: "Yes", 
    2: "No"
})
table_filter = table(df, 'voted')
print(table_filter)

# Family size .............................................
## table
table_var = table(df, 'familysize')
print(table_var)

## Filter invalid records
df = df[(df['familysize'] > 0) & (df['familysize'] < 20)]
table_filter = table(df, 'familysize')
print(table_filter)

# Save data ------------------------------------------------------------------
# https://arrow.apache.org/docs/python/parquet.html

## Saving the DataFrame to a Parquet file
path_save = '\\data\\data_v2.parquet'
df.to_parquet(path_folder + path_save)

# Save to csv
path_save = '\\data\\data_v2.csv'
df.to_csv(path_folder + path_save, 
          index=False)

##############################################################################
##############################################################################
##############################################################################
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

# Load data
path = 'data/data_v2.parquet'
df = pd.read_parquet(path)

# Descriptive statistics ------------------------------------------------------

# Age .....................................................
df["age"].describe()

plt.figure(figsize=(10, 5))
df['age'].plot(kind = 'hist', 
               bins = 30, 
               edgecolor = 'black')
plt.title('Histogram for Age')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Gender ..................................................
df["gender"].describe()

plt.figure(figsize=(10, 5))
df['gender'].value_counts().plot(kind='bar')
plt.title('Bar Chart for Gender')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

# Married .................................................
df["married"].describe()

plt.figure(figsize=(10, 5))
df['married'].value_counts().plot(kind='bar')
plt.title('Bar Chart for Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

# Religion ................................................
df["religion"].describe()

plt.figure(figsize=(10, 5))
df['religion'].value_counts().plot(kind='bar')
plt.title('Bar Chart for Religion')
plt.xlabel('Religion')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

# Education ...............................................
df["education"].describe()

plt.figure(figsize=(10, 5))
df['education'].value_counts().plot(kind='bar')
plt.title('Bar Chart for Education')
plt.xlabel('Education')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

# Urban ...................................................
df["urban"].describe()

plt.figure(figsize=(10, 5))
df['urban'].value_counts().plot(kind='bar')
plt.title('Bar Chart for Urban Residence')
plt.xlabel('Urban Residence')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

# English Native ..........................................
df["engnat"].describe()

plt.figure(figsize=(10, 5))
df['engnat'].value_counts().plot(kind='bar')
plt.title('Bar Chart for English Native')
plt.xlabel('English Native')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

# Handedness ..............................................
df["hand"].describe()

plt.figure(figsize=(10, 5))
df['hand'].value_counts().plot(kind='bar')
plt.title('Bar Chart for Handedness')
plt.xlabel('Handedness')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

# Sexual Orientation ......................................
df["orientation"].describe()

plt.figure(figsize=(10, 5))
df['orientation'].value_counts().plot(kind='bar')
plt.title('Bar Chart for Sexual Orientation')
plt.xlabel('Sexual Orientation')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

# Race ....................................................
df["race"].describe()

plt.figure(figsize=(10, 5))
df['race'].value_counts().plot(kind='bar')
plt.title('Bar Chart for Race')
plt.xlabel('Race')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

# Voted  ..................................................
df["voted"].describe()

plt.figure(figsize=(10, 5))
df['voted'].value_counts().plot(kind='bar')
plt.title('Bar Chart for Voting')
plt.xlabel('Voted')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

# Family size .............................................
df["familysize"].describe()

plt.figure(figsize=(10, 5))
df['familysize'].plot(kind = 'hist', 
                      bins = 20, 
                      edgecolor = 'black')
plt.title('Histogram for Family Size')
plt.xlabel('Family Size')
plt.ylabel('Frequency')

##############################################################################
##############################################################################
##############################################################################
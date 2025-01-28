# Andres Garcia Gomez
# ITP 259
# HW1
# Question 1

# Pre-Step: Import necessary modules
import numpy as np
import pandas as pd

# Part 1

# Creating a dictionary based off of the DataFrame given in the assignment sheet
initialDict = {'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
              'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
                       'Matthew', 'Laura', 'Kevin', 'Jonas'],
              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no',
                          'no', 'yes'], 'score': [12.5, 9.0, 16.5, np.nan, 9.0, 20.0, 14.5, np.nan, 8.0, 19.0]}

# Converting the newly created dictionary into a DataFrame
Q1_DF = pd.DataFrame.from_dict(initialDict)
print(Q1_DF)

# Part 2

# Printing the name and attempts of students who qualified!
print()
print(Q1_DF[Q1_DF['qualify'] == 'yes'].loc[:, ['name', 'attempts']])

# Part 3

# Printing the name and score of contestants who qualified in ONE attempt.
print()
print(Q1_DF[(Q1_DF['qualify'] == 'yes') & (Q1_DF['attempts'] == 1)].loc[:, ['name', 'score']])


# Part 4

# Printing the DataFrame that replaces the NaN values with 0s in the 'score' column
print()
Q1_DF = Q1_DF.fillna(0)

# Printing out the DataFrame to verify that we filled the NaN values with 0s
print()
print(Q1_DF)

# Part 5

# Printing the DataFrame, sorted with attempts in ascending order and scores in descending order, in that hierarchy.
print()
print(Q1_DF.sort_values(by = ['attempts', 'score'], ascending = [True, False]))

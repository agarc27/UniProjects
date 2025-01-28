# Andres Garcia Gomez
# ITP 259
# HW1
# Question 2

# Pre-Step: Import necessary modules
import pandas as pd

# Part 1

# Reading the csv file and converting it into a DataFrame
DF = pd.read_csv('Trojans_roster.csv')
print(DF)

# Part 2

# Replacing the index of the DataFrame with the existing "#'
print()
DF = DF.set_index('#')
print(DF)

# Part 3

# Removing certain columns from the DataFrame
print()
DF = DF.drop(columns=['LAST SCHOOL', 'MAJOR'])
print(DF)

# Part 4


print()
print(DF[DF['POS.'] == 'QB'].loc[:, 'NAME'])

# Part 5

# Printing the name, position, height, and weight of the tallest team player(s).
print()
print(DF[DF['HT.'] == DF['HT.'].max()].loc[:, ['NAME', 'POS.', 'HT.', 'WT.']])

# Part 6

# Printing the number of players that are local (from Los Angeles)
print()
print(DF['HOMETOWN'].value_counts()['Los Angeles, Calif.'])

# Part 7

# Printing out the information of the top 3 heaviest players
print()
print(DF.nlargest(3, ['WT.']))

# Part 8

# Adding a new column, 'BMI', to the existing dataframe; BMI being defined by the formula in the assignment sheet.
print()
DF['BMI'] = round(703 * DF['WT.']/(DF['WT.']**2), 2)
print(DF)

# Part 9

# Printing the means and medians of the players' heights, weights, and BMI
print()
print('Means')
print(round(DF[['HT.', 'WT.', 'BMI']].mean(), 2))
print()
print('Median')
print(round(DF[['HT.', 'WT.', 'BMI']].median(), 2))

# Part 10

print()
print('Means by Position')
print(round(DF.groupby('POS.')[['HT.', 'WT.', 'BMI']].mean(), 2))
print()
print('Medians by Position')
print(round(DF.groupby('POS.')[['HT.', 'WT.', 'BMI']].median(), 2))

# Part 11
print()
print(DF.groupby('POS.')['POS.'].count())

# Part 12
print()
print(DF[DF['BMI'] < DF['BMI'].mean()].loc[:, ['NAME']])

# Part 13
print()
print(DF.index.unique())

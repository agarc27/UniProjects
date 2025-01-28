""" Andres Garcia Gomez
    ITP-449
    Assignment #8
    A program which aims to create a line of best fit for 
    quantitative diabetes progression.
"""

# Packages and modules needed for the program to run.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Outlier caluclator created by Kristof which he said
# we could use for wrangling purposes on assignments. 
def calc_nonoutlier_range(data):
	Q3 = data.quantile(0.75)
	Q1 = data.quantile(0.25)
	IQR = Q3 - Q1
	lower_value = Q1 - 1.5 * IQR
	upper_value = Q3 + 1.5 * IQR
	return [lower_value, upper_value]

# The main function where we write all that is needed to create 
# our figure and regression. 
def main():
    # Wrangle Step 1: Gather the data in one place
    file_path = 'diabetes.csv'
    df_diabetes = pd.read_csv(file_path, skiprows=1)
    
    # Wrangle Step 2: Identify the target attribute and extract both
    # the target and the most statistically correlated attribute by
    # using a correlation matrix. I gave my best attempt at extracting
    # the most correlated attribute in a programmatic fashion.
    correlation_matrix = df_diabetes.corr(numeric_only = True)
    df_corr = correlation_matrix['Y'].sort_values(ascending=False)
    corr_att = df_corr.index[1]
    print(corr_att)

    df_diabetes = df_diabetes[['Y',corr_att]]

    # Wrangle Step 3: Dealing with missing or duplicated values
    df_diabetes.dropna(inplace=True)
    df_diabetes.drop_duplicates(inplace=True)

    # Wrangle Step 4: Removing outliars from the data
    lower, upper = calc_nonoutlier_range(df_diabetes[corr_att])
    filt_lower = df_diabetes[corr_att] >= lower
    filt_upper = df_diabetes[corr_att] <= upper
    df_no_outliers = df_diabetes[ filt_lower ]
    df_no_outliers = df_no_outliers[ filt_upper ]

    # Wrangle Step 5: Seperating the data into target and feature vector
    y = df_no_outliers['Y'] # Target
    x = df_no_outliers[corr_att] # Feature vector
    # print(x.shape)
    X = pd.DataFrame(x.values.reshape(-1, 1), columns=[x.name])

    # Running a linear regression using the new variables above
    model_linreg = LinearRegression()
    model_linreg.fit(X, y)

    # Creating the line of best fit using the LinReg we ran above.
    X_lobf = np.linspace(df_no_outliers[corr_att].min(), df_no_outliers[corr_att].max(), 2)
    y_lobf = model_linreg.intercept_ + model_linreg.coef_*X_lobf

    # Creating the figure in which we'll have the scatterplot 
    # and linear regression line displayed.
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.scatter(X, y, label='Diabetes data')
    ax.plot(X_lobf, y_lobf, color='orange', label='Line of best fit')
    ax.set(xlabel=f'{corr_att}', ylabel='Progression', title=f'Diabetes data: Progression vs {corr_att} (Linear Regression')
    ax.legend()
    #fig.tight_layout()
    plt.savefig('Diabetes Regression.png')

if __name__ == '__main__':
    main()

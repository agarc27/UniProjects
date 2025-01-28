""" Andres Garcia Gomez
    ITP-449
    Assignment #6
    We are going to train and test a Logistic Refression model based
    on the diabetes data. From this, we will produce a Confusion Matrix
    to visualize the relationship between all attributes.
"""

# Packages and modules needed for the program to run.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay

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
    df_diabetes = pd.read_csv(file_path)
    #print(df_diabetes)

    # Note: we are doing this a little out of order
    df_diabetes.drop_duplicates(inplace=True)

    # Wrangle Step 2: Select attributes - both target and
    # most correlated numeric attributes. Must be done programatically.
    correlation_matrix = df_diabetes.corr(numeric_only = True)
    # print(correlation_matrix)
    
    # We are looking at the likelihood of getting diabetes, so
    # 'Outcome' is the target. Let's isolate that column to help
    # us find the other attributes.
    df_corr = correlation_matrix['Outcome'].sort_values(ascending=False)
    #print(df_corr)
    
    # Sorting in descending order, the most correlated variable will always
    # be equal to 1, being correlated to itself. So to find the three most
    # correlated attributes, we look at the names of indicies 1-3.
    slimmed_index_list = list(df_corr.index[[0,1,2,3]])

    df_diabetes = df_diabetes[slimmed_index_list]
    print(df_diabetes.info())

    # Wrangle Step 3: Dealing with missing values
    df_diabetes.dropna(inplace=True)

    # Wrangle Step 4: Deal with outliers.
    df_no_outliers = df_diabetes
    for i in range(1,4,1): # Can do this programatically
        lower, upper = calc_nonoutlier_range(df_diabetes.iloc[:,i])
        filt_lower = df_diabetes.iloc[:,i] >= lower
        filt_upper = df_diabetes.iloc[:,i] <= upper
        df_no_outliers = df_no_outliers[ filt_lower ]
        df_no_outliers = df_no_outliers[ filt_upper ]
    print(df_no_outliers)

    # Wrangle Step 5: Seperating the data into target and 
    # feature vector
    y = df_no_outliers['Outcome']
    X = df_no_outliers.drop(columns='Outcome')

    # Wrangle Step 6: Encoding
    # Not needed

    # Wrangle Step 7: Transforming
    # Not needed

    # Wrangle Step 8: Partition the data into testing and
    # training sets.
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=42, stratify=y)

    # Create an empty model and then train it
    model_logreg = LogisticRegression()
    model_logreg.fit(X_train, y_train)
    
    # Calculate the accuracy of the Logistic Regression
    accuracy = model_logreg.score(X_test, y_test)
    print(f'accuracy: {accuracy:.2f}%')

    # Make predictions on test data
    y_pred = model_logreg.predict(X_test)

    # Use the actual and predicted values to create
    # a confusion matrix
    conf_matrix = confusion_matrix(y_test, y_pred)
    print(conf_matrix)

    # Create a confusion matrix display object
    display = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=['No', 'Yes'])

    # Plot the confusion matrix display object 
    fig, axes = plt.subplots()
    display.plot(ax=axes)
    axes.set(title=f'Diabetes Classification Confusion Matrix \n Accuracy = {accuracy:.2f}')
    fig.tight_layout()

    # Save the figure
    plt.savefig('Diabetes Logistic Regression Confusion Matrix.png')

if __name__ == '__main__':
    main()

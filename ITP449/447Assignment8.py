""" Andres Garcia Gomez
    ITP-449
    Assignment #11
    With this assignment, we want to train and optimize a KNN
    Classifcation model using diabetes data, while also producing
    visualizations of the model.
"""

# Packages and modules needed for the program to run.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler

# Outlier caluclator created by Kristof which he said
# we could use for wrangling purposes on assignments. 
def calc_nonoutlier_range(data):
	Q3 = data.quantile(0.75)
	Q1 = data.quantile(0.25)
	IQR = Q3 - Q1
	lower_value = Q1 - 1.5 * IQR
	upper_value = Q3 + 1.5 * IQR
	return [lower_value, upper_value]

def main():    
# The main function where we write all that is needed to create 
# our figure and model.

#Step 1: Data Wrangling Process 

    # Wrangle Step 1: Gather the data in one place
    file_path = 'diabetes.csv'
    df_diabetes = pd.read_csv(file_path)
    #print(df_diabetes)

    # Note: we are doing this a little out of order; dropping dupes at the proper 
    # step results in the loss of one data point however it is not dropped in this step,
    # thus it may be a processing error.
    df_diabetes.drop_duplicates(inplace=True)

    # Wrangle Step 2: Select attributes - both target and
    # most correlated numeric attributes. Must be done programatically.
    correlation_matrix = df_diabetes.corr(numeric_only = True)
    #print(correlation_matrix)
    
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
    #print(df_diabetes.info())

    # Wrangle Step 3: Dealing with missing values
    df_diabetes.dropna(inplace=True)

    # Wrangle Step 4: Deal with outliers.
    df_no_outliers = df_diabetes
    for i in range(1,len(slimmed_index_list)):
        lower, upper = calc_nonoutlier_range(df_diabetes.iloc[:,i])
        filt_lower = df_diabetes.iloc[:,i] >= lower
        filt_upper = df_diabetes.iloc[:,i] <= upper
        df_no_outliers = df_no_outliers[ filt_lower ]
        df_no_outliers = df_no_outliers[ filt_upper ]

    # print(df_no_outliers)

    # # Wrangle Step 5: Seperating the data into target and 
    # # feature vector
    y = df_no_outliers['Outcome']
    X = df_no_outliers.drop(columns='Outcome')

    # Wrangle Step 6: Encoding
    # Not needed

    # Wrangle Step 7: Transforming
    # For KNN, transforming is necessary; I used the standard scalar.
    X_ss = pd.DataFrame(StandardScaler().fit_transform(X), columns = X.columns)

    # Wrangle Step 8: Partition the data into testing and
    # training sets.
    X_train, X_test, y_train, y_test = train_test_split(X_ss, y, train_size=0.7, random_state=42, stratify=y)

# Step 2: 

# Cross-Validation Step: Finding an optimal hyperparameter
    ks = range(1, round(1.5*((X_train.shape[0])**0.5))+1)
    p_grid = {
        'n_neighbors': ks
    }
    model_knn = KNeighborsClassifier()
    gscv = GridSearchCV(estimator=model_knn, param_grid = p_grid)
    gscv.fit(X_train, y_train)
    print('best params:\n',gscv.best_params_) #Gives optimal hyperparam
    print('scores:\n',gscv.cv_results_['mean_test_score'])#Shows us scores of all possible k's

#Step 3:
    # KNN Classifier using the hyperparameter found 
    # through the cross-validation step

    k = gscv.best_params_['n_neighbors']
    model_knn_class = KNeighborsClassifier(n_neighbors=k)
    model_knn_class.fit(X_train, y_train)
    
    # Calculate the accuracy of the KNN Classifier
    accuracy = model_knn_class.score(X_test, y_test)
    print(f'accuracy: {accuracy:.2f}')


#Step 4:
    # Visualizing a plot of the validation score 
    # and its corresponding k
 
    fig, axes = plt.subplots(1,2, figsize=(16,9))
    axes[0].plot(ks, gscv.cv_results_['mean_test_score'])
    axes[0].set(title = f'Accuracy Score vs k \n Best k={k}')
    
#Step 5:
    # Creating a confusion matrix based on the predictions of 
    # the testing data.

    # Predictions on test data to be used for the confusion matrix
    y_pred = model_knn_class.predict(X_test)

    # Use the actual and predicted values to create
    # a confusion matrix
    conf_matrix = confusion_matrix(y_test, y_pred)
    #print(conf_matrix)

    # Create a confusion matrix display object
    display = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=['No', 'Yes'])

#Step 6:    
    # Visualizing the confusion matrix. 

    display.plot(ax = axes[1])
    axes[1].set(title=f'Diabetes Classification Confusion Matrix \n Accuracy = {accuracy:.2f}')

    # Finishing touches on the fig
    fig.suptitle('Diabetes KNN Classification Results')
    fig.tight_layout()
    plt.savefig('diabetes_knn_classification_results.png')

if __name__ == '__main__':
    main()

""" Andres Garcia Gomez
    ITP-449
    Final Project
    The goal of this program is to create an optimized SVm classification
    model with the 'winequality_white.csv' dataset. Afterwards, we will create a line
    plot of accruacy vs hyperparam setup and a confusion matrix.
"""

# Packages to be used
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

# Program to be used for outliers
def calc_nonoutlier_range(data):
	Q3 = data.quantile(0.75)
	Q1 = data.quantile(0.25)
	IQR = Q3 - Q1
	lower_value = Q1 - 1.5 * IQR
	upper_value = Q3 + 1.5 * IQR
	return [lower_value, upper_value]

# The main function to be used for the program.
def main():
    # Data Wrangle Step 1: Store the data into a location.
    file_path = 'winequality-white.csv'
    df_winequality = pd.read_csv(file_path, skiprows = 1, sep = ';')
    print(df_winequality.info())

    # Doing this a little out of order, we're dropping dupes early
    # before limiting the attributes.
    df_winequality.drop_duplicates(inplace=True)

    # Data Wrangle Step 2: Analyze and select desired attributes.  
    correlation_matrix = df_winequality.corr(numeric_only = True)
    # print(correlation_matrix)

    # To find the traits most closely associated to quality, we look at 
    # the absolute values in order.  
    df_corr = abs(correlation_matrix['quality']).sort_values(ascending=False)

    # To get the four most statistically correlated numeric attributes, we 
    # simply grab the first five attributes once ordered. 

    corr_att = df_corr.index[range(0,5)]
    # print(corr_att)

    df_winequality = df_winequality[corr_att]
    # print(df_winequality)

    # Data Wrangle Step 3: Remove any missing or duplicated data.  
    df_winequality.dropna(inplace=True)
    # print(df_winequality)

    # Data Wrangle Step 4: Remove any outliers.  
    for attr in df_winequality.columns[:-1]:
        if attr != 'quality':
            range_low, range_high = calc_nonoutlier_range(df_winequality[attr])
            df_winequality = df_winequality[ (df_winequality[attr] > range_low) & (df_winequality[attr] < range_high) ]

    # Data Wrangle Step 5: Separate into target and feature vectors.  
    y = df_winequality['quality']
    X = df_winequality.drop(columns = 'quality')

    # Data Wrangle Step 6: Encoding
    # Not needed since all data is numeric

    # Data Wrangle Step 7: Transforming
    X_ss = pd.DataFrame(StandardScaler().fit_transform(X), columns = X.columns)

    # Data Wrangle Step 8: Splie the data into testing and training sets.
    X_train, X_test, y_train, y_test = train_test_split(X_ss, y, train_size=0.75, random_state=42, stratify=y)

    # Cross Validation 

    model_svc1 = SVC()
    param_dict_svc1 = {
        'C': [0.1, 1, 10, 100],
        'kernel':['linear']
    }
    gscv_svc1 = GridSearchCV(
        model_svc1,
        param_grid=param_dict_svc1
    )
    gscv_svc1.fit(X_train, y_train)
    test_params1 = gscv_svc1.best_params_

    test_model1 = SVC(kernel = test_params1['kernel'], C = test_params1['C'])
    test_model1.fit(X_train, y_train)
    accuracy1 = test_model1.score(X_test, y_test)
    print(f'accuracy: {accuracy1:.2f}')

    model_svc2 = SVC()
    param_dict_svc2 = {
        'C': [0.1, 1, 10, 100],
        'kernel':['rbf'],
        'gamma': [0.1, 1, 10, 100]
    }
    gscv_svc2 = GridSearchCV(
        model_svc2,
        param_grid=param_dict_svc2
    )
    gscv_svc2.fit(X_train, y_train)
    test_params2 = gscv_svc2.best_params_
    
    test_model2 = SVC(kernel = test_params2['kernel'], C = test_params2['C'], gamma=test_params2['gamma'])
    test_model2.fit(X_train, y_train)
    accuracy2 = test_model2.score(X_test, y_test)
    print(f'accuracy: {accuracy2:.2f}')

    final_SVC_model = test_model2
    final_SVC_model.fit(X_train, y_train)
    y_pred = final_SVC_model.predict(X_test)

    # List of all accuracy scores for the plot
    list1 = gscv_svc1.cv_results_['mean_test_score']
    list2 = gscv_svc2.cv_results_['mean_test_score']
    accuracy_scores = np.concatenate((list1,list2))
    
    # Visualize
    fig, axes = plt.subplots(1, 2, figsize=(20,9))
    conf_matrix = confusion_matrix(y_test, y_pred)
    cm_disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix)
    cm_disp.plot(ax=axes[0])
    axes[0].set(title='Confusion Matrix')
    axes[1].plot(range(len(accuracy_scores)), accuracy_scores)
    axes[1].set(title='Accuracy Score vs. Hyperparam Setup', xlabel = 'Hyperparam Setup',
    ylabel = 'Accuracy Score')
    fig.suptitle('Wine Quality SVM Classification Results')
    fig.tight_layout()
    plt.savefig('Wine Quality SVM Classification Results.png')


if __name__ == '__main__':
    main()

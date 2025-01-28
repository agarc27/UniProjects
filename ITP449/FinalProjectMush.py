""" Andres Garcia Gomez
    ITP-449
    Final Project
    The goal of this program is to train and optimize a 
    decision tree classifier model for the mushroom.csv dataset.
"""
# Packages to be used
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Would be used if we were to remove outliers
def calc_nonoutlier_range(data):
	Q3 = data.quantile(0.75)
	Q1 = data.quantile(0.25)
	IQR = Q3 - Q1
	lower_value = Q1 - 1.5 * IQR
	upper_value = Q3 + 1.5 * IQR
	return [lower_value, upper_value]

# The main function from which everything will run
def main():
    # Data Wrangle Step 1: Store the data into a location.
    file_path = "mushrooms.csv"
    df_mushrooms = pd.read_csv(file_path)
    print(df_mushrooms)

    # Data Wrangle Step 2&3: Select attributes and deal 
    # with missing data.
    df_mushrooms.drop_duplicates(inplace=True)
    df_mushrooms.dropna(inplace=True)

    # Data Wrangle Step 4: Remove outliers.
    # NOT NEEDED since all features in the feature vector are categorical.

    # Data Wrangle Step 5: Seperate data into target and feature vectors.
    y = df_mushrooms['class']
    X = df_mushrooms.drop(columns = 'class')
    X_test_data = X

    # Data Wrangle Step 6: Encode 
    # print(X.info())
    X = pd.get_dummies(X)
    print(X.columns)

    # Data Wrangle Step 7: Transform
    # Not needed for decision trees 

    # Data Wrangle Step 8: Split the data into training and testing sets.
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=42, stratify=y)

    # Cross-Validation
    # Note that due to having numerous possible hyperparamter combos,
    # we are using a RandomizedSearchCV to expedite the process and get close
    # to optimal
    model_dt = DecisionTreeClassifier()
    hyperparam_dict = {
        'criterion': ['entropy', 'gini'],
        'max_depth': np.arange(2, round((X_train.shape[0])**0.5) + 1),
        'min_samples_leaf': np.arange(2, 11)
    }

    rscv = RandomizedSearchCV(estimator=model_dt, param_distributions=hyperparam_dict)
    rscv.fit(X_train, y_train)
    best_params = rscv.best_params_
    print(best_params)

    # Create and train final model with optimal hyperparams
    model_dt = DecisionTreeClassifier(criterion=best_params['criterion'], max_depth=best_params['max_depth'], min_samples_leaf=best_params['min_samples_leaf'])
    
    # Train and test final model
    model_dt.fit(X_train, y_train)
    y_pred = model_dt.predict(X_test)
    
    # Visualize
    fig, axes = plt.subplots(1, 2, figsize=(20,9))
    conf_matrix = confusion_matrix(y_test, y_pred)
    cm_disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix)
    cm_disp.plot(ax=axes[0])
    axes[0].set(title='Confusion Matrix')
    plot_tree(model_dt, ax=axes[1], feature_names=X.columns, class_names=y.unique(), filled=True)
    axes[1].set(title='Decision Tree Visualization')
    fig.suptitle('Mushroom Decision Tree Results')
    fig.tight_layout()
    plt.savefig('Mushroom Edibility Decision Tree Results.png')

    # Final prediction on the mushroom attributes provided in #3
    final_data = {'test_data': ['x', 's', 'n', 't','y','f','c','n','k','e','e', 
's', 's','w','w','p','w','o','p','r','s','u']}

    # Transforming the data into a DataFrame
    mushroom_test_data = pd.DataFrame.from_dict(final_data, orient = 'index',
columns = ['cap-shape','cap-surface','cap-color','bruises','odor','gill-attachment',
'gill-spacing', 'gill-size','gill-color','stalk-shape','stalk-root', 'stalk-surface-above-ring',
'stalk-surface-below-ring', 'stalk-color-above-ring','stalk-color-below-ring','veil-type',
'veil-color', 'ring-number', 'ring-type','spore-print-color', 'population', 'habitat'])

    # Combining the dataframe into a copy of the original data, so we can 
    # easily use getdummies on it.
    frames = [X_test_data, mushroom_test_data]
    modified_df = pd.concat(frames)
    # print(modified_df)
    modified_df = pd.get_dummies(modified_df)
    print(modified_df)

    # Running the data into the model to predict.
    test_data_row = modified_df.loc['test_data']
    final_pred = model_dt.predict([test_data_row])
    
    # The final prediction for the mushroom
    print(final_pred)

if __name__ == '__main__':
    main()

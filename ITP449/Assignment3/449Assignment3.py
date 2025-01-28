""" Andres Garcia Gomez
    ITP-449
    Assignment #3
    We are producing visualizations from the data within
    the Palmer Penguins dataset. The first visualization 
    is a scatterplot matrix of all numeric attributes. The
    second visualization is a scatterplot comparing bill 
    length and flipper length.
"""
# Packages requires for the assignment.
import pandas as pd
import matplotlib.pyplot as plt

# The main function; in this case, it just runs all the code to create
# the two visualizations.
def main():
    # List that houses all the releveant column names we'll need from the dataframe
    variable_names = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 
    'body_mass_g','species'] 

    # Data Wrangling/Cleaning the data
    # First, we create a dataframe from the data in the file. Then, we slim it down
    # to the releveant data using the list of column names. Finally, we remove all the
    # missing data points and can now use the data.
    df_penguins = pd.read_csv('penguins.csv')
    df_slimmed = df_penguins[variable_names]
    df_no_nulls = df_slimmed.dropna()

    # For figure 2, we further splice the data, each into a dataframe that 
    # correlates to one of the three species.
    df_adelie = df_no_nulls.loc[df_no_nulls['species'] == 'Adelie']
    df_chinstrap = df_no_nulls.loc[df_no_nulls['species'] == 'Chinstrap']
    df_gentoo = df_no_nulls.loc[df_no_nulls['species'] == 'Gentoo']

    # Figure 1
    fig, ax = plt.subplots(4,4, figsize = (16,9))
    # Nested for loop that allows us to format all sixteen plots in an efficient matter
    for x in range(4):
        for y in range(4):
            # Conditional statement that allows us to create a histogram if the 
            # columns are the same.
            if x == y:
                ax[x,y].hist(df_no_nulls[variable_names[x]])
                ax[x,y].set(xlabel = variable_names[x])
            else:
            # Otherwise, we get a normal scatterplot of the two variables.
                ax[x,y].scatter(df_no_nulls[variable_names[x]],df_no_nulls[variable_names[y]])
    # Extra parts of the figure: tightness, title, and saving it.
    fig.suptitle('Palmer Penguins Attributes Scatterplot Matrix')
    fig.tight_layout()
    plt.savefig('penguins_attributes_scatterplot_matrix.png')
    
    #Figure 2
    plt.clf() # Clears the current figure.
    fig, ax = plt.subplots(figsize = (10, 7)) 

    # Graphing three different scatterplots on the same figure: one for each species.
    ax.scatter(df_adelie['bill_length_mm'], df_adelie['flipper_length_mm'], label = 'Adelie')
    ax.scatter(df_chinstrap['bill_length_mm'], df_chinstrap['flipper_length_mm'], label = 'Chinstrap')
    ax.scatter(df_gentoo['bill_length_mm'], df_gentoo['flipper_length_mm'], label = 'Gentoo')
    
    # Extra parts of the figure: axis labels, title, and saving it.
    fig.legend()
    ax.set(xlabel = 'bill_length_mm')
    ax.set(ylabel = 'flipper_length_mm')
    fig.suptitle('bill_length_mm vs flipper_length_mm')
    plt.savefig('penguins_bill_flipper_by_species.png')

# Runs the function.
if __name__ == '__Assignment__':
    main()

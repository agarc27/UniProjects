""" Andres Garcia Gomez
    ITP-449
    Assignment #5
    The goal of this program is to create six visualizations 
    about the prices and quantities of avocados.
"""
# Packages required for the assignment
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# The main function; in this case, it'll run all the code to create
# the six subplots that show Avocado Prices and Volume over time.
def main():
    # Data Wrangling/Cleaning the data
    # First, we create a dataframe from the data in the file. Then, we slim it down
    # to the releveant data. Then, we sort the data by date. This will be our
    # first dataframe used for two visualizations: the leftmost ones.
    df_avocados = pd.read_csv('avocado.csv')
    df_slimmed = df_avocados[['Date', 'AveragePrice', 'Total Volume']]
    df_slimmed['Date'] = pd.to_datetime(df_slimmed['Date'])
    df_sorted = df_slimmed.sort_values('Date')
    # Here, we create a second dataframe; we add a column for TotalRevenue, group
    # by date and aggregate with sum, and then retool the AveragePrice column.
    df_sorted['TotalRevenue'] = df_sorted['AveragePrice'] * df_sorted['Total Volume']
    df_grouped = df_sorted.groupby('Date').sum()
    df_grouped['AveragePrice'] = df_grouped['TotalRevenue']/df_grouped['Total Volume']

    # Creating the subplots figure
    fig, ax = plt.subplots(2,3)

    # The leftmost visualizations for the 'Raw' data; we use the first dataframe
    # to visualize here as it contains the raw values for the AveragePrice.
    ax[0,0].scatter(df_sorted['Date'], df_sorted['AveragePrice'], s=10)
    ax[1,0].scatter(df_sorted['Date'], df_sorted['Total Volume'], s=10)
    ax[0,0].set(title = 'Raw')

    # The center visualizations for the 'Aggregated' data; we use the second dataframe
    # to visualize here as it contains the aggreagted values for the AveragePrice.
    ax[0,1].plot(df_grouped.index, df_grouped['AveragePrice'], marker = 'o', 
    linestyle = 'solid', markersize = 3)
    ax[1,1].plot(df_grouped.index, df_grouped['Total Volume'], marker = 'o', 
    linestyle = 'solid', markersize = 3)
    ax[0,1].set(title = 'Aggregated')

    # The rightmost visualizations for the 'Smoothed' data; we use the second dataframe
    # to visualize here as it contains the aggreagted values for the AveragePrice,
    # which we then smooth using rolling windows with value = 20.
    ax[0,2].plot(df_grouped.index, df_grouped['AveragePrice'].rolling(20).mean(), 
    marker = 'o', linestyle = 'solid', markersize = 3)
    ax[1,2].plot(df_grouped.index, df_grouped['Total Volume'].rolling(20).mean(), 
    marker = 'o', linestyle = 'solid', markersize = 3)
    ax[0,2].set(title = 'Smoothed')

    # A loop here used to beautify the subplots; this includes removing tick labels,
    # rotating tick labels, and setting axis labels
    for h in range(3):
        ax[0,h].xaxis.set_ticklabels([])
        ax[1,h].tick_params(axis='x', rotation=90)
        ax[1,h].set(xlabel = 'Time')

    # Y-axis labels for all of the subplots
    ax[0,0].set(ylabel = 'Average Price (USD)')
    ax[1,0].set(ylabel = 'Total Volume (millions)')

    # Finshing touches on the figure before saving; title and layout.
    fig.suptitle('Avocado Prices and Volume Time Series')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('avocados.png')

# Needed to run the function
if __name__ == '__main__':
    main()

# I apologize if the subplots could be optimized with loops. For the life of me
# I could not figure out a way to do so without it being more cumbersome than
# the way I did it.

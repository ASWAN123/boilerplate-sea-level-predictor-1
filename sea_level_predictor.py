import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(x, y)

    # Create first line of best fit
    # Import scipy and draw the line of Linear Regression:
    slope, intercept, r, p, std_err = linregress(x, y)

    def my_func(n):
        return slope * n + intercept

    # Adding the sea level in 2050 on the plot
    x1 = list(range(1880, 2051))
    y1 = list(map(my_func, x1))

    plt.plot(x1, y1)

    # Create second line of best fit
    index_year = x.index[x == 2000][0]  # 2000 to 2013
    x2 = x[index_year:]
    y2 = y[index_year:]

    slope, intercept, r, p, std_err = linregress(x2, y2)

    # Adding the sea level in 2050 on the plot
    x2 = list(range(2000, 2051))
    y2 = list(map(my_func, x2))

    plt.plot(x2, y2)

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    plt.savefig('sea_level_plot.png')
    return plt.gca()
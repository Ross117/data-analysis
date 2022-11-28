import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (9, 9))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    def generate_yrs(orig):
    
        yrs_to_add = []

        start = 2014
        end = 2050
        i = start

        while i <= end:
            yrs_to_add.append(i)
            i += 1

        yrs = pd.concat([orig, pd.Series(yrs_to_add)])

        return yrs

    # Create first line of best fit
    lr_result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope, intercept, *other = lr_result
    yrs = generate_yrs(df['Year'])

    ax.plot(yrs, intercept + slope * yrs)

    # Create second line of best fit
    df_2000s = df[df.Year >= 2000]

    lr_result_2000s = linregress(df_2000s['Year'], df_2000s['CSIRO Adjusted Sea Level'])
    slope_2000s, intercept_2000s, *other = lr_result_2000s
    yrs_2000s = generate_yrs(df_2000s['Year'])

    ax.plot(yrs_2000s, intercept_2000s + slope_2000s * yrs_2000s)

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    fig.savefig('scatterplot.png')
    return plt.gca()

## DYNAMIC DASHBOARD EXAMPLE - Functionality
#    Last update: April 2016


## INDEX
#    + Function definition
#    + Data creation
##


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



## Function definition ---------------------------------------------------------------

def generate_random_column(column_name):
    ''' Adds a new column in the dataframe (or recalculates existing) '''
    data[column_name] = np.random.rand(50)

def remove_column(column_name):
    ''' Removes the specified column, returns False if column is not found (True otherwise) '''
    try:
        data.drop(column_name, axis=1, inplace=True)
    except ValueError:
        print 'No such column'
        return False
    else:
        return True

def filter_dataframe(values):
    ''' Returns the data filtered by the 'size' column '''
    return data[ data['size'].isin(values) ]
    

def make_plot(df, style, plot_kind, colors):
    ''' Plotter: plots the data with the specified specifications '''
    # Use styling template
    plt.style.use(style)
    
    if len(colors) == 1: # correction for Series plotting
        colors = colors[0]
    
    if plot_kind == '':
        df.plot(figsize=(18,5), color=colors)
    
    else:
        df.plot(kind=plot_kind, figsize=(18,5), color=colors)    


## Data creation ---------------------------------------------------------------------

data = pd.DataFrame()

generate_random_column('Apples')
generate_random_column('Bananas')

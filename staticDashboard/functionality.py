
## STATIC DASHBOARD EXAMPLE - Functionality
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

    
def make_plot(style, plot_kind):
    ''' Plotter: plots the data with the specified specifications '''
    # Use styling template
    plt.style.use(style)
    
    if plot_kind == '':
        data.plot(figsize=(15,5))
    
    else:
        data.plot(kind=plot_kind, figsize=(10,5))    


## Data creation ---------------------------------------------------------------------

data = pd.DataFrame()

generate_random_column('Apples')
generate_random_column('Bananas')

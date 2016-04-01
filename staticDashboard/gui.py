
## STATIC DASHBOARD EXAMPLE - GUI dashboard creation
#    MRG - March 2016
#    Contact: Guillermo Monge (r559042)


## INDEX
#    + Dashboard creation
#    + Event handling
##


from ipywidgets import widgets
from IPython.display import display, clear_output

from functionality import *


## DASHBOARD CREATION ----------------------------------------------------------------

dashboard = widgets.VBox()

# Title and spacers
header = widgets.HTML("<h3 style='color: darkblue; width: 900px; text-align: center;'>Static Example</h3>")
vspace = widgets.HTML("<br>")
hspace = widgets.HTML("<h2 style='color: white;'>--</h2>")

# Style selection
selector = widgets.widget_selection.SelectMultiple(
    description='Select series to plot:',
    options=list(data.columns),)

styler = widgets.Dropdown(
    options={'default': 'classic','ggplot': 'ggplot', 'fivethirtyeight': 'fivethirtyeight',
             'deep': 'seaborn-deep','gray': 'grayscale', 'dark-palette': 'seaborn-dark-palette',
             'bright': 'seaborn-bright', 'dark': 'dark_background', 'nice': 'bmh'},
    default_value=2,
    help='Plotting style:',)
kinder = widgets.widget_selection.ToggleButtons(
    options={'Line': '', 'Bar': 'bar', 'Area': 'area', 'Density': 'kde'},
    default_value=2,
    help='Figure selection:',)
style_subpanel = widgets.HBox(children = [kinder, hspace, styler])

# New column generation
new_col_name = widgets.Text(
    description='Column:',
    value='Random',)
new_col_button = widgets.Button(description="Generate!")

go_button = widgets.Button(description="REPLOT",)

# Final Layout
lower_subpanel = widgets.HBox(children = [new_col_name, new_col_button, hspace, go_button])
body_panel = widgets.HBox(children=[style_subpanel, hspace, hspace, lower_subpanel])

dashboard.children = [header, vspace, body_panel]


## EVENT HANDLING --------------------------------------------------------------------

## New column generation

def new_column_wrapper(_):
    _name = '_'.join( new_col_name.value.split() )
    generate_random_column(_name)
    print '--> New column {} generated'.format(_name)

    # On button click
new_col_button.on_click(new_column_wrapper)

    # On form submition
new_col_name.on_submit(new_column_wrapper) 


## Ploting
def plot_wrapper(_):
    clear_output()
    _style = styler.value
    _kind = kinder.value
    make_plot(_style, _kind)

go_button.on_click(plot_wrapper)

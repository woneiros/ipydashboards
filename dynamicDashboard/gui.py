
## DYNAMIC DASHBOARD EXAMPLE - GUI dashboard creation
#    MRG - March 2016
#    Contact: Guillermo Monge (r559042)


## INDEX
#    + Presets
#    + Dashboard creation
#    + Event handling
##


from ipywidgets import widgets
from IPython.display import display, clear_output

from functionality import *


## PRESETS ---------------------------------------------------------------------------

COLORS = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white']


## DASHBOARD CREATION ----------------------------------------------------------------

dashboard = widgets.VBox()

# Title and spacers
header = widgets.HTML("<h3 style='color: darkblue; width: 900px; text-align: center;'>Dynamic Example</h3>")
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
del_col_button = widgets.Button(description="Remove")

# Column select-color-er
cols_hd = widgets.HTML("<h4><b>Column selection</b></h4>")
num_cols = widgets.Dropdown(options=['1','2'], description='How many columns to plot:')
cols_grp = []
for i in range( int(num_cols.value) ):
    _column = widgets.Dropdown(description='Show', options=['Apples','Bananas'])
    _color = widgets.ToggleButtons(options=COLORS, description='Color: ')
    cols_grp.append( widgets.HBox(children = [_column, _color]) )
    cols_grp.append(vspace)
grp_cols_panel = widgets.VBox(children = cols_grp )
    
# Replot button
go_button = widgets.Button(description="REPLOT",)

# Final Layout
mid_subpanel = widgets.HBox(children = [new_col_name, new_col_button, del_col_button])
footer_subpanel = widgets.VBox(children = [cols_hd, num_cols, vspace, grp_cols_panel])
body_panel = widgets.HBox(children=[style_subpanel, hspace, hspace, mid_subpanel])

dashboard.children = [header, vspace, body_panel, vspace, footer_subpanel, vspace, go_button]


## EVENT HANDLING --------------------------------------------------------------------

## Number of columns to plot
def update_num_cols(_, old, new):
    new_cols = []
    _avail_cols = list(data.columns)
    for i in range( int(num_cols.value) ):
        _column = widgets.Dropdown(description='Show', options=_avail_cols)
        _color = widgets.ToggleButtons(options=COLORS, description='Color: ')
        new_cols.append( widgets.HBox(children = [_column, _color]) )
        new_cols.append(vspace)
    grp_cols_panel.children = new_cols 

num_cols.on_trait_change(update_num_cols, 'value')


## Update columns available
def update_columns():
    # update the number of columns available dropdown
    num_cols.options = map( str, range(1, data.columns.shape[0] + 1) )
    
    _avail_cols = list(data.columns)
    
    # update column selectors
    for hbox in grp_cols_panel.children:
        if isinstance(hbox, widgets.widget_box.FlexBox):
            # update columns available
            hbox.children[0].options = _avail_cols


## New column generation
def new_column_wrapper(_):
    # generate column and notify
    _name = '_'.join( new_col_name.value.split() )
    generate_random_column(_name)
    print '--> New column "{}" generated'.format(_name)
    update_columns()
    
# On button click
new_col_button.on_click(new_column_wrapper)

# On form submition
new_col_name.on_submit(new_column_wrapper) 


## Remove column wrapper
def remove_column_wrapper(_):
    # generate column and notify
    _name = '_'.join( new_col_name.value.split() )
    remove_column(_name)
    print '--> Column "{}" was removed'.format(_name)
    update_columns()

# On button click
del_col_button.on_click(remove_column_wrapper)
    
    
## Ploting
def plot_wrapper(_):
    clear_output()
    
    _style = styler.value
    _kind = kinder.value
    
    _columns = []
    _colors = []
    
    for hbox in grp_cols_panel.children:
        if isinstance(hbox, widgets.widget_box.FlexBox):
            # Get columns & colors to plot
            _columns.append(hbox.children[0].value)
            _colors.append(hbox.children[1].value)

    make_plot(data[_columns], _style, _kind, _colors)

go_button.on_click(plot_wrapper)

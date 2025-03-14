#############################################
#IMPORT PACKAGES#

from dash import Dash, dcc, html, Input, Output #dash core components
import dash_bootstrap_components as dbc
#############################################
## Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server=app.server ##declare the server for deployment
#############################################
##Create app components

markdown= dcc.Markdown(id='our-markdown',children='title1', style={'fontSize':12,'textAlign': 'center', 'color':'red'} ) ##add id property to distinguish different components
button=html.Button(children="Button")
checklist=dcc.Checklist(options=['NYC', 'Munich', 'Frankfurt'])
radio=dcc.RadioItems(id='our-radio', options=['red', 'orange', 'green'])
dropdown=dcc.Dropdown(id='our-dropdown',options=['title1', 'title2', 'title3'], value='title2')
slider=dcc.Slider(id='our_slider', min=0, max=10, step=1,value=0)
## one component added here: mark down
## components can have properties: ids, children and styles. children: allow adding of text content. 
##style: defines the look of the component
#############################################

## App Layout
# app.layout = dbc.Container([
#     markdown, button, checklist, radio, dropdown, slider
# ])


app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([markdown], width=8)]),
        dbc.Row([dbc.Col([radio], width=8)]),
        dbc.Row(
            [
                dbc.Col([dropdown], width=3),
                dbc.Col([slider], width=9),
            ]
        ),
    ]
)
##NEVER ASSIGN MORE THAN 12 COLUMNS!!
#############################################
##CONFIGURE CALL BACKS
##CALL BACK DECORATOR: specify components and correspodning properties I want to link together
##Output: specifies component pf property that will be modified. 
##Input: specifies the property of the component that will activate the callback. Value of property of dropdown
@app.callback(
    Output(component_id='our-markdown', component_property='children'),
    Input(component_id='our-dropdown', component_property='value')
)

def update_markdown(value_dropdown):
    title = value_dropdown
    return title


@app.callback(
    Output(component_id='our-markdown', component_property='style'),
    Input(component_id='our_slider', component_property='value'),
    Input(component_id='our-radio', component_property='value')
)

def update_markdown(value_slider,value_radio):
    title_size = {'fontSize': 12+2*value_slider,'color': value_radio}
    return title_size

 
#############################################

## Run the app##
if __name__ == '__main__':
    app.run_server(debug=False)
    
    
 #### Useful components: Button, checklist, radioitems, dropdown, slide
 ###
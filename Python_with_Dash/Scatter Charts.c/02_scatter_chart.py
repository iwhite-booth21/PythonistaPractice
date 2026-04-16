import json

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

df = pd.read_csv('datasets/cars_data.csv')

df = df[df['mileage'] < 200000]

fig = px.scatter(df, 
                 x="price", 
                 y="mileage", 
                 color="year", 
                 hover_data=["brand", "model"])

fig.update_layout(clickmode='event+select')

fig.update_traces(marker_size=6)

app.layout = html.Div([
    dcc.Graph(
        id='basic-interactions',
        figure=fig
    ),

    html.Div([html.H4(children='Hover Data'),
              html.Pre(id='hover-data', style=styles['pre'])
              ], className='three columns'),
    html.Div([html.H4(children='Click Data'),
              html.Pre(id='click-data', style=styles['pre']),
             ], className='three columns'),
    html.Div([html.H4(children='Selected Data'),
              html.Pre(id='selected-data', style=styles['pre']),
             ], className='three columns'),
    html.Div([html.H4(children='Relayout Data'),
              html.Pre(id='relayout-data', style=styles['pre']),
             ], className='three columns')
    ])


@app.callback(
    Output('hover-data', 'children'),
    [Input('basic-interactions', 'hoverData')])
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)


@app.callback(
    Output('click-data', 'children'),
    [Input('basic-interactions', 'clickData')])
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)

### Accessing the selected data
### When the page first loads, the variable selectedData is empty, so we handle that situation
### When a selection is made, we can access the data like a dictionary
### There is a variable called points which contains all the points data

@app.callback(
    Output('selected-data', 'children'),
    [Input('basic-interactions', 'selectedData')])
def display_selected_data(selectedData):

    if(selectedData):

      selected_df = pd.DataFrame(selectedData['points'])
      summary_text = "Avg. Price: ${:,}".format(int(selected_df['x'].mean())), "\n"\
                     "Avg. Mileage: {:,}".format(int(selected_df['y'].mean()))

      return summary_text

    else:

      return str(selectedData)


@app.callback(
    Output('relayout-data', 'children'),
    [Input('basic-interactions', 'relayoutData')])
def display_relayout_data(relayoutData):
    return json.dumps(relayoutData, indent=2)




if __name__ == '__main__':
    app.run_server(debug=True)
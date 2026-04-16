import json

import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

### These styles will be applied to some preformatted text which we will use to
### render information about points in a plot which will be selected/clicked/hovered on etc.

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

df = pd.read_csv('datasets/cars_data.csv')

### Filter out outliers in the dataset which can skew the chart
df = df[df['mileage'] < 200000]

fig = px.scatter(df, 
                 x="price", 
                 y="mileage", 
                 color="year", 
                 hover_data=["brand", "model"])

### setting clickmode to event+select ensures clicks and point selections are
### recognized as events
fig.update_layout(clickmode='event+select')

fig.update_traces(marker_size=6)     

### The layout includes a graph, and also preformatted text fields (html.Pre) 
### whose contents change based on interactions with the graph
### The three columns class is for the arrangement of the text fields based on 
### what is defined in external_stylesheets

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


@app.callback(
    Output('selected-data', 'children'),
    [Input('basic-interactions', 'selectedData')])
def display_selected_data(selectedData):
    return json.dumps(selectedData, indent=2)


@app.callback(
    Output('relayout-data', 'children'),
    [Input('basic-interactions', 'relayoutData')])
def display_relayout_data(relayoutData):
    return json.dumps(relayoutData, indent=2)


if __name__ == '__main__':
    app.run(debug=True)
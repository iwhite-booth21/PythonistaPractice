#### We generate a basic line chart, and then make it interactive
#### The time period covered in the chart can be modified based on user input

import dash
import plotly.express as px
import pandas as pd
from dash import html
from dash import dcc


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

stocks_data = pd.read_csv('GSPC_Data.csv')

### Converting the Date field to datetime is not required for this demo
### But will be needed later on when we add an interactive slider

stocks_data['Date'] = pd.to_datetime(stocks_data['Date'])

fig = px.line(stocks_data, 
			  x="Date", 
			  y="Adj Close")

app.layout = html.Div([
    dcc.Graph(
        id='close-over-time',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
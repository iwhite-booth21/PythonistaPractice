import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


cars_data = pd.DataFrame({
    "Company": ["Tesla", "Tesla", "Tesla", "Ford", "Ford", "Ford"],
    "State": ["California", "Washington", "Oregon", "California", "Washington", "Oregon"],
    "Sales": [6, 3, 6, 4, 8, 10]
})

### Change the barmode from "stack" to "group"
 
fig = px.bar(cars_data, 
			 x="Company", 
			 y="Sales", 
			 color="State", 
			 barmode="group")

app.layout = html.Div(children=[
    html.H2(children='Car Sales in CA, OR, and WA'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
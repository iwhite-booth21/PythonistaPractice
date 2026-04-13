import dash
import plotly.express as px
import pandas as pd
from dash import html
from dash import dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


cars_data = pd.DataFrame({
    "Company": ["Tesla", "Tesla", "Tesla", "Ford", "Ford", "Ford"],
    "State": ["California", "Washington", "Oregon", "California", "Washington", "Oregon"],
    "Sales": [6, 3, 6, 4, 8, 10]
})

### Re-configure the figure to plot bars for each state in different colors.
### Then stack the bars for each company on top of one another. 
### By default, this is done based on the category plotted on the X axis.

fig = px.bar(cars_data, 
			 x="Company", 
			 y="Sales", 
			 color="State", 
			 barmode="stack")

app.layout = html.Div(children=[
    html.H2(children='Car Sales in CA, OR, and WA'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)





    
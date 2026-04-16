import dash
import plotly.express as px
import pandas as pd
from dash import html
from dash import dcc


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

stocks_data = pd.read_csv('datasets/GSPC_Data.csv')

stocks_data['Date'] = pd.to_datetime(stocks_data['Date'])

### We define Graph and a RangeSlider instances which will be added to the layout right here
### The Graph points to an interactive graph which gets updated with a callback (defined below)
### For now, the callback only defines a figure whose title gets updated by the slider selection
###		- we will use the slider to update the line chart later on 

graph = dcc.Graph(id='interactive-chart')

date_slider = dcc.RangeSlider(
				 id='year-slider',
				 min=stocks_data['Date'].min().year,
		         max=stocks_data['Date'].max().year,
		         value= [stocks_data['Date'].min().year, stocks_data['Date'].max().year],
		         marks = {str(year): str(year) for year in stocks_data['Year'].unique()},
		         step=None
		      )

### The layout includes the graph and date_slider

app.layout = html.Div([graph, date_slider])

### Dash callbacks: https://dash.plotly.com/basic-callbacks
### Any update to the Input (our RangeSlider) triggers this callback
###		- the values represented by the RangeSlider are accessed from the 'value' parameter
### The Output of the callback has two parameters:
###		- the ID of an element which it will update
###		- a property in that compent which will get updated
###		- in this case, the 'figure' of the dcc.Graph object with the ID 'interactive-chart'
### In this case, we don't modify the line chart based on the slider - just the title text

@app.callback(
    dash.dependencies.Output('interactive-chart', 'figure'),
    [dash.dependencies.Input('year-slider', 'value')])
def update_figure(value):
    
    fig = px.line(stocks_data, 
			  x="Date", 
			  y="Adj Close")

    fig_title = 'Slider selection: ' + str(value[0]) + ' to ' + str(value[1])

    fig.update_layout(title_text = fig_title)

    return fig



if __name__ == '__main__':
    app.run(debug=True)



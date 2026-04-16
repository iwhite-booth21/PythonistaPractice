import dash
import plotly.express as px
import pandas as pd
from dash import html
from dash import dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

stocks_data = pd.read_csv('datasets/GSPC_Data.csv')

stocks_data['Date'] = pd.to_datetime(stocks_data['Date'])

graph = dcc.Graph(id='interactive-chart')

date_slider = dcc.RangeSlider(
				 id='year-slider',
				 min=stocks_data['Date'].min().year,
		         max=stocks_data['Date'].max().year,
		         value= [stocks_data['Date'].min().year, stocks_data['Date'].max().year],
		         marks = {str(year): str(year) for year in stocks_data['Year'].unique()},
		         step=None
		      )

app.layout = html.Div([graph, date_slider])

### Within update_figure, create a filtered dataset using the range set by the RangeSlider
### The fig now uses the filtered dataset
### The fig_title is also updated
### Sliding the RangeSlider causes the chart to be updated with the filtered dataset

@app.callback(
    dash.dependencies.Output('interactive-chart', 'figure'),
    [dash.dependencies.Input('year-slider', 'value')])
def update_figure(value):

	filtered_data = stocks_data[(stocks_data['Year'] >= value[0]) \
								& (stocks_data['Year'] <= value[1])]
    
	fig = px.line(filtered_data,
    			  x="Date", 
    			  y="Adj Close")

	fig_title = 'S&P 500 from ' + str(value[0]) + ' to ' + str(value[1])

	fig.update_layout(title_text = fig_title)

	return fig



if __name__ == '__main__':
    app.run(debug=True)



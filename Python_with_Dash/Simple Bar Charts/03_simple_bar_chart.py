import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


cars_data = pd.DataFrame({
    "Company": ["Tesla", "Tesla", "Tesla", "Ford", "Ford", "Ford"],
    "State": ["California", "Washington", "Oregon", "California", "Washington", "Oregon"],
    "Sales": [6, 3, 6, 4, 8, 10]
})
 
fig = px.bar(cars_data, 
			 x="Company", 
			 y="Sales", 
			 color="State", 
			 barmode="group")

#### Configure the figure using update_layout
## The full list of properties which can be set is available here:
## https://plotly.com/python/reference/layout/

## Navigate to the above URL and view the elements

## Layout elements in the docs are arranged in a hierarchical manner
## When defining a particular element, use '_' to go down the hierarcy
## e.g. font --> color can be set with the property font_color
##      legend --> font --> size set with legend_font_size

## There is a hierarchy of elements for each layout
## e.g. the font_size is the global font size which is inherited by child elements such as:
##    - title, legend, axes
## Inherited properties can be overridden by child elements
## e.g. legend_font_family overrides font_family
## The default font size for each element ()

fig.update_layout(
    title_text='Sales of Tesla and Ford',
    plot_bgcolor='ivory',
    paper_bgcolor='linen',
    font_color='darkslategray',
    font_family='Arial',
    font_size=20,
    legend_font_family='Georgia',
    legend_font_size=15
)

app.layout = html.Div(children=[
    html.H2(children='Car Sales in CA, OR, and WA'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
import dash
from dash import html
# Use this to get the html capability

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

text = ('Dash is a Web Application Framework for Python. '
        'It is a free and open source option for developers to build '
        'with limited knowledge of HTML, and no knowledge of CSS')

app.layout = html.Div(children=[
    html.H1(children='Welcome to Dash'),
    html.Div(children=text)
])

if __name__ == '__main__':
    app.run(debug=True)
# app.server is depracated use app.run
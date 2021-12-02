import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('test 1.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="graph"),
    html.Button("Switch Axis", id='btn', n_clicks=0)
])

@app.callback(
    Output("graph", "figure"), 
    [Input("btn", "n_clicks")])
def display_graph(n_clicks):
    if n_clicks % 2 == 0:
        x, y = 'Time', 'Force Sensor Value'
    else:
        x, y = 'Force Sensor Value', 'Time'

    fig = px.line(df, x=x, y=y)    
    return fig

app.run_server(debug=True)

df = pd.read_csv('test 2.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="graph"),
    html.Button("Switch Axis", id='btn', n_clicks=0)
])

@app.callback(
    Output("graph", "figure"), 
    [Input("btn", "n_clicks")])
def display_graph(n_clicks):
    if n_clicks % 2 == 0:
        x, y = 'Time', 'EMG Sensor Value'
    else:
        x, y = 'EMG Sensor Value', 'Time'

    fig = px.line(df, x=x, y=y)    
    return fig

app.run_server(debug=True)
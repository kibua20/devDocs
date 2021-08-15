#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from flask import Flask

#define dataframe
df = px.data.iris()

#before
#app = dash.Dash(__name__)

#after - flask app
server = Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
  # url_base_pathname='/yourpath'
  # external_stylesheets = 'your css'
)
# end

# dash app layout
app.layout = html.Div([
    dcc.Graph(id="scatter-plot"),
    html.P("Petal Width:"),
    dcc.RangeSlider(
        id='range-slider',
        min=0, max=2.5, step=0.1,
        marks={0: '0', 2.5: '2.5'},
        value=[0.5, 2]
    ),
])

# callback - feed data
@app.callback(
    Output("scatter-plot", "figure"), 
    [Input("range-slider", "value")])
def update_bar_chart(slider_range):
    low, high = slider_range
    mask = (df['petal_width'] > low) & (df['petal_width'] < high)
    fig = px.scatter(
        df[mask], x="sepal_width", y="sepal_length", 
        color="species", size='petal_length', 
        hover_data=['petal_width'])
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)





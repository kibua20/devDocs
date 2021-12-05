# -*- coding: utf-8 -*-

from dash_html_components.Br import Br
import flask

import dash
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import dash_table

# flask server
application = flask.Flask(__name__)

# dash app with flask server
dash_app1 = Dash(__name__, server=application, url_base_pathname='/dashapp1/')
dash_app2 = Dash(__name__, server=application, url_base_pathname='/dashapp2/')
dash_app3 = Dash(__name__, server=application, url_base_pathname='/dashapp3/')
dash_app4 = Dash(__name__, server=application, url_base_pathname='/dashapp4/')
dash_app5 = Dash(__name__, server=application, url_base_pathname='/dashapp5/')

# flask app
@application.route('/')
def index():
    #print('flask app index()')
    return 'OK'


# --------------------------------------------------------------------------------------------------------
# dash app with simple component -  https://dash.plotly.com/dash-html-components
dash_app1.layout = html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ])
])


# --------------------------------------------------------------------------------------------------------
# dash 2 app with graph
import plotly.express as px

fig = px.scatter(x=[0, 1, 2, 3, 4, 5], y=[0, 1, 4, 9, 16, 17])
dash_app2.layout = html.Div([dcc.Graph(figure=fig)])


# --------------------------------------------------------------------------------------------------------
# dash app 3
dash_app3.layout = html.Div(id='my_id', 
                            className='my_class',
                            children=[
                                html.H1(children='Hello Dash'),
                                html.Div(children='''Dash: A web application framework for Python.'''),
                                dcc.Graph(
                                    id='example-graph',
                                    figure={
                                        'data': [
                                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                                        ],
                                        'layout': {'title': 'Dash Data Visualization'}
                                    }
                                )
                            ])

# --------------------------------------------------------------------------------------------------------
# dash app 4 https://dash.plotly.com/urls
dash_app4.layout = html.Div([
    # display link and html
    dcc.Link('Navigate to "/dashapp4"',  href='/dashapp4'),
    html.Br(),
    dcc.Link('Navigate to "/dashapp4/page1"',href='/dashapp4/page1'),

    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),

    # content will be rendered in this element
    html.Div(id='page-content'),
])

@dash_app4.callback(Output('page-content', 'children'), 
                    [Input('url', 'href'), 
                     Input('url', 'pathname'),
                     Input('url', 'search'),
                     Input('url', 'hash')])
def display_page(href, pathname, search, hash):
    return html.Div([
        html.H2('Displayed by callback:'),
        html.H4('href = {}'.format(href)),
        html.H4('pathname = {}'.format(pathname)),
        html.H4('search = {}'.format(search)),
        html.H4('hash = {}'.format(hash)),
    ])



# --------------------------------------------------------------------------------------------------------
# dash app 5 width pandas
df = px.data.stocks()

dash_app5.layout = html.Div([
    html.Br(),
    html.H2('Time series graph with Dash'),
    html.Br(),
    dcc.Dropdown(
        id="ticker",
        options=[{"label": x, "value": x} for x in df.columns[1:]],
        value=df.columns[1],
        clearable=False,
    ),
    dcc.Graph(id="time-series-chart"),
    html.Br(),
    dash_table.DataTable(
        id='df-stack-table',
        columns=[{"name": i, "id": i} for i in df.head().columns],
        data=df.head(15).to_dict('records'),)
])


@dash_app5.callback(Output("time-series-chart", "figure"), [Input("ticker", "value")])
def display_time_series(ticker):
    fig = px.line(df, x='date', y=ticker)
    return fig


# --------------------------------------------------------------------------------------------------------
# run the app.
if __name__ == "__main__":
    application.debug = True
    application.run()

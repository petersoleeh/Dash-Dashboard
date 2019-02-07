import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Output
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
from app import flask_app


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



dashapp = dash.Dash(__name__, server=flask_app, sharing=True, external_stylesheets=external_stylesheets, url_base_pathname='/dashboard/', csrf_protect=False)


dashapp.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])


dashapp = dash.Dash(__name__, server=flask_app, sharing=True, external_stylesheets=external_stylesheets, url_base_pathname='/dashboard1/', csrf_protect=False)


dashapp.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python2.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 4, 3], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 1, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

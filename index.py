import os
import pandas as pd
from data import *
from dash import html, dcc

# Dash Bootstrap components
import dash_bootstrap_components as dbc
from layouts import *

# Import app
from app import app
from navbar import Navbar



nav = Navbar()

header = dbc.Row(
    dbc.Col(
        html.Div(
            [
                html.H2(children="Bitcoin Dashboard"),
                html.H3(children="A Visualization of Historical Data"),
            ]
        )
    ),
    className="banner",
)


def index():
    layout = html.Div(children=[
        nav, header, timechainLayout
    ])

    return layout

app.layout = index()

if __name__ == '__main__':
    app.run_server(debug=True)
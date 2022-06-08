import os
import pandas as pd
from data import *
from dash import html, dcc
import dash_bootstrap_components as dbc
from layouts import *
from app import app

# import navbar & call function
from navbar import Navbar

nav = Navbar()


# Initialize Header
header = dbc.Row(
    dbc.Col(
        html.Div(
            [
            ]
        )
    ),
    className="banner",
)


# Index function calls layouts
def index():
    layout = html.Div(children=[
        nav, header, mempoolLayout
    ])

    return layout

app.layout = index()

if __name__ == '__main__':
    app.run_server(debug=True)
# Import Bootstrap from Dash
import os
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc


# Navigation Bar fucntion
def Navbar():
    navbar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src="assets/bitcoin-symbol.png", height="30px")),
                            dbc.Col(dbc.NavbarBrand("Bitcoin Dashboard", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",

                    ),
                    href="https://plotly.com",
                    style={"textDecoration": "none"},
                ),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            ]
        ),
        color="",
        dark=True,
        style={"padding": "25px 25px 25px 25px"}
    )
    return navbar
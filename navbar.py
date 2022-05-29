# Import Bootstrap from Dash
import os

import dash_bootstrap_components as dbc


# Navigation Bar fucntion
def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Mempool")),
            dbc.NavItem(dbc.NavLink("Timechain")),
            dbc.NavItem(dbc.NavLink("Mining")),
        ],
        brand="Home",
        sticky="top",
        color="light",
        dark=False,
        expand="lg",
    )
    return navbar
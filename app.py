# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_bootstrap_components as dbc

# Initialize Dash App
# Add external bootstrap style sheet
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SUPERHERO]
)

app.title = "Bitcoin Data Visualization"
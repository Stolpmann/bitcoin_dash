from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
from data import clean_block_data, supply_t
import plotly.express as px


fig = px.bar(clean_block_data, x="height", y="txs", barmode="group")


timechainLayout = html.Div(children=[
    dbc.Row(
        [
            dbc.Col(html.Div(dcc.Graph(id='example-graph',
                                       figure=fig
                                        ),), width=9),
            dbc.Col(html.Div(dash_table.DataTable(supply_t.to_dict('records'),
                                                  [{"name": i, "id": i} for i in supply_t.columns],
                                                  id='tbl'),
                             ), width=3),
        ]
    ),
    dbc.Row(
        [
            dbc.Col(html.Div("An automatically sized column"), width=6),
            dbc.Col(html.Div("An automatically sized column"), width=6),
        ],
    ),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
])
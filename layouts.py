from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
from data import clean_block_data, supply_clean, hash
import plotly.express as px



supply = px.bar(hash, x=hash.index, y="0", barmode="group")

supply.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

timechainLayout = html.Div(children=[
    dbc.Row(
        [
            dbc.Col(html.Div(dcc.Graph(id='example-graph',
                                       figure=supply
                                        ),),
                    width=9,
                    style={"padding-left": "50px"},

                    ),

            dbc.Col(html.Div(dash_table.DataTable(supply_clean.to_dict('records'),
                                  [{"name": i, "id": i} for i in supply_clean.columns],
                                  id='tbl',
                                  style_data={
                                      'color': 'white',
                                      'backgroundColor': 'rgb(0, 0, 0, 0)',
                                      'fontWeight': 'bold'
                                  },
                                  style_header={
                                      'color': 'white',
                                      'backgroundColor': 'rgb(0, 0, 0, 0)',
                                      'fontWeight': 'bold'
                                  },
                                  ),
                             ),
                    width=3,
                    style={"padding": "120px 50px 20px 0", }
                    ),
        ]
    ),
    dbc.Row(
        [
            dbc.Col(html.Div("An automatically sized column"),
                    width=6,
                    style={"padding-left": "50px"},
                    ),
            dbc.Col(html.Div("An automatically sized column"),
                    width=6,
                    style={"padding-left": "50px"},
),
        ],
    ),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
])
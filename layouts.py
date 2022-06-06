from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
from data import *
import plotly.express as px
import plotly.graph_objects as go


# Initialize colours
colors = {
    'background': '#15202b',
    'text': '#FF9900'
}
colors2 = ['#4D4D4D', '#FF9900']


# hashrate chart
hashrate = px.bar(hash, x=hash.index, y="0", barmode="group", title="Hsshrate Average per Block")

hashrate.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='white',
)

hashrate.update_traces(marker_color='orange')


# difficulty chart
difficulty = px.line(header, x="height", y="difficulty", title='Difficuly in TH/s')

difficulty.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='white',
)

difficulty.update_traces(line=dict(color='orange'))


# supply pie chart
supply = go.Figure(data=[go.Pie(labels=bitcoin_supply_titles, values=bitcoin_supply, title='Supply')])

supply.update_traces(marker=dict(colors=colors2,line=dict(color='#FFFFFF', width=1)), title=dict(position='top left'))

supply.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='white',
)


# Projected halvings Chart

halvings = px.line(halving, x="Year", y="Start BTC", title="Projected Supply", log_y=True)

halvings.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='white',
)

halvings.update_traces(line=dict(color='orange'))

# Average THroughput per difficulty adjustment

throughput = px.line(clean_block_data, x="height", y="totalfee", title="Total Fee per Block", log_x=True)

throughput.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='white'
)

throughput.update_traces(line=dict(color='orange'))

# Initialize Mining Layout

miningLayout = html.Div(children=[
    dbc.Row(
        [
            dbc.Col(html.Div(dcc.Graph(id='example-graph',
                                       figure=hashrate
                                        ),),
                    width=7,
                    style={"padding-left": "10px", "border-style": "solid"},

                    ),

            dbc.Col(html.Div(dash_table.DataTable(supply_clean.to_dict('records'),
                                  [{"name": i, "id": i} for i in supply_clean.columns],
                                  id='tbl',
                                  style_data={
                                      'color': 'orange',
                                      'backgroundColor': 'rgb(0, 0, 0, 0)',
                                      'fontWeight': 'bold'
                                  },
                                  style_header={
                                      'color': 'orange',
                                      'backgroundColor': 'rgb(0, 0, 0, 0)',
                                      'fontWeight': 'bold'
                                  },
                                  ),
                             ),
                    width=5,
                    style={"padding": "120px 50px 30px 30px", "border-style": "solid"}
                    ),
        ]
    ),
    dbc.Row(
        [
            dbc.Col(html.Div(dcc.Graph(id='example-graph2',
                                       figure=difficulty
                                        ),),
                    width=7,
                    style={"padding-left": "20px", "border-style": "solid"},

                    ),
            dbc.Col(html.Div(dcc.Graph(id='example-graph3',
                                       figure=supply
                                        ),),
                    width=5,
                    style={"padding-left": "5px", "border-style": "solid"},

                    ),
        ],
    ),
    dbc.Row(
        [
            dbc.Col(html.Div(dcc.Graph(id='example-graph4',
                                       figure=halvings
                                       ), ),
                    width=6,
                    style={"padding-left": "20px", "border-style": "solid"},

                    ),
            dbc.Col(html.Div(dcc.Graph(id='example-graph5',
                                       figure=throughput
                                       ), ),
                    width=6,
                    style={"padding-left": "5px", "border-style": "solid"},

                    ),
        ],
    )
])


# UTXO increase Line Chart

utxo = px.line(utxo, x=utxo.index, y="utxo_increase", title="UTXO Increae by Block",)

utxo.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='white'
)

utxo.update_traces(line=dict(color='orange'))


# UTXO output type Pie CHart

supply = go.Figure(data=[go.Pie(labels=bitcoin_supply_titles, values=bitcoin_supply, title='Supply')])

supply.update_traces(marker=dict(colors=colors2,line=dict(color='#FFFFFF', width=1)), title=dict(position='top left'))

supply.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='white',
)



# Initialize Timechain Layout

timechainLayout = html.Div(children=[
    dbc.Row(
        [
            dbc.Col(html.Div(dcc.Graph(id='example-graph',
                                       figure=utxo
                                        ),),
                    width=7,
                    style={"padding-left": "10px", "border-style": "solid"},

                    ),

            dbc.Col(html.Div(dash_table.DataTable(supply_clean.to_dict('records'),
                                  [{"name": i, "id": i} for i in supply_clean.columns],
                                  id='tbl',
                                  style_data={
                                      'color': 'orange',
                                      'backgroundColor': 'rgb(0, 0, 0, 0)',
                                      'fontWeight': 'bold'
                                  },
                                  style_header={
                                      'color': 'orange',
                                      'backgroundColor': 'rgb(0, 0, 0, 0)',
                                      'fontWeight': 'bold'
                                  },
                                  ),
                             ),
                    width=5,
                    style={"padding": "120px 50px 30px 30px", "border-style": "solid"}
                    ),
        ]
    ),
    dbc.Row(
        [
            dbc.Col(html.Div(dcc.Graph(id='example-graph2',
                                       figure=difficulty
                                        ),),
                    width=7,
                    style={"padding-left": "20px", "border-style": "solid"},

                    ),
            dbc.Col(html.Div(dcc.Graph(id='example-graph3',
                                       figure=supply
                                        ),),
                    width=5,
                    style={"padding-left": "5px", "border-style": "solid"},

                    ),
        ],
    ),
    dbc.Row(
        [
            dbc.Col(html.Div(dcc.Graph(id='example-graph4',
                                       figure=halvings
                                       ), ),
                    width=6,
                    style={"padding-left": "20px", "border-style": "solid"},

                    ),
            dbc.Col(html.Div(dcc.Graph(id='example-graph5',
                                       figure=throughput
                                       ), ),
                    width=6,
                    style={"padding-left": "5px", "border-style": "solid"},

                    ),
        ],
    )
])
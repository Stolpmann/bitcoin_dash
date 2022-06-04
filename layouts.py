from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
from data import clean_block_data,supply_clean,hash,bitcoin_supply_titles,bitcoin_supply,header
import plotly.express as px
import plotly.graph_objects as go


# Initialize colours
colors = {
    'background': '#15202b',
    'text': '#FF9900'
}
colors2 = ['#4D4D4D', '#FF9900']


# hashrate chart
hashrate = px.bar(hash, x=hash.index, y="0", barmode="group", title="Hsshrate Average per Block ")

hashrate.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='white'
)


# difficulty chart
difficulty = px.line(header, x="height", y="difficulty", title='Difficuly in TH/s')

difficulty.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='white',
)


# supply chart
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
                                       figure=hashrate
                                        ),),
                    width=8,
                    style={"padding-left": "10px"},

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
                    width=4,
                    style={"padding": "120px 50px 0px 0", }
                    ),
        ]
    ),
    dbc.Row(
        [
            dbc.Col(html.Div(dcc.Graph(id='example-graph2',
                                       figure=difficulty
                                        ),),
                    width=8,
                    style={"padding-left": "20px"},

                    ),
            dbc.Col(html.Div(dcc.Graph(id='example-graph3',
                                       figure=supply
                                        ),),
                    width=4,
                    style={"padding-left": "5px"},

                    ),
        ],
    ),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
])
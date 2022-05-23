# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#15202b',
    'text': '#FF9900'
}

df = pd.read_csv ('clean_block_data.csv')
supply = pd.read_csv('supply.csv')
halving = pd.read_csv('halvings.csv')
print(df)

bitcoin_supply =[supply['issuance_remaining'][0], int(supply['total_amount'][0])]

bitcoin_supply_titles = ['Issuance Remaining', 'Circulating Supply']

colors2 = ['#4D4D4D', '#FF9900']

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


fig1 = px.line(df, x="height", y="txs", title='Bitcoin Transactions')

fig1.update_traces(line_color='#FF9900', line_width=3, )

fig2 = px.line(halving, x="Year", y="Start BTC", title='Projected Halvings',log_x=True)

fig2.update_traces(line_color='#FF9900', line_width=3)

fig3 = go.Figure(data=[go.Pie(labels=bitcoin_supply_titles, values=bitcoin_supply)])

fig3.update_traces(marker=dict(colors=colors2,line=dict(color='#FFFFFF', width=1)))



fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    title=dict(font_size=20)
)
fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    title = dict(font_size=20)

)

fig3.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    title=dict(text='Bitcoin Supply', font_size=20)
)

app.layout = html.Div(style={'backgroundColor': colors['background'], 'marginLeft': -10, 'marginRight': -10, 'marginTop': -25}, children=[
    html.H1(
        children='Bitcoin Dashboard',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'paddingTop': 15
        }
    ),

    html.Div(children='', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig1
    ),
    html.H1(
        children='Supply',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'paddingTop': 15
        }
    ),

    html.Div(children='', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-3',
        figure=fig2
    ),


    html.Div(
        children='',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'paddingTop': -30
    }),

    dcc.Graph(
        id='example-graph-4',
        figure=fig3,
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
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
print(df)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


fig1 = px.line(df, x="height", y="txs", title='Bitcoin Transactions')

fig1.update_traces(line_color='#FF9900', line_width=3)

fig2 = px.line(df, x="height", y="txs", title='Bitcoin Transactions')

fig2.update_traces(line_color='#FF9900', line_width=3)

fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Bitcoin Dashboard',
        style={
            'textAlign': 'center',
            'color': colors['text']
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
        children='Bitcoin Dashboard',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-3',
        figure=fig2
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
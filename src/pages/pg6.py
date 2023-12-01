import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   path='/vehicle-energy-efficiency',  # represents the url text
                   name='Vehicle energy efficiency',  # name of page, commonly used as name of link
                   title='Vehicle energy efficiency'  # epresents the title of browser's tab
)


# df = px.data.tips()

# layout = html.Div()

df = px.data.tips()

layout = html.Div(
    [
        dbc.Row([
            dbc.Col(
                [
                    # html.Img(src='assets/smoking2.jpg')
                ], width=4
            ),
            dbc.Col(
                [
                    dcc.RadioItems(df.day.unique(), id='day-choice2', value='Sat')
                ], width=6
            )
        ]),
        dbc.Row([
            dbc.Col(
                [
                    dcc.Graph(id='bar-fig4',
                              figure=px.bar(df, x='smoker', y='total_bill'))
                ], width=12
            )
        ])
    ]
)


@callback(
    Output('bar-fig4', 'figure'),
    Input('day-choice2', 'value')
)
def update_graph(value):
    dff = df[df.day==value]
    fig = px.bar(dff, x='smoker', y='total_bill')
    return fig

import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   path='/data-collection-overview',  # represents the url text
                   name='Data collection overview',  # name of page, commonly used as name of link
                   title='Data collection overview'  # epresents the title of browser's tab
)

# page 2 data
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
                    dcc.RadioItems(df.day.unique(), id='day-choice', value='Sat')
                ], width=6
            )
        ]),
        dbc.Row([
            dbc.Col(
                [
                    dcc.Graph(id='bar-fig',
                              figure=px.bar(df, x='smoker', y='total_bill'))
                ], width=12
            )
        ])
    ]
)


@callback(
    Output('bar-fig', 'figure'),
    Input('day-choice', 'value')
)
def update_graph(value):
    dff = df[df.day==value]
    fig = px.bar(dff, x='smoker', y='total_bill')
    return fig

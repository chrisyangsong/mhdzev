import dash
from dash import dcc, html
import plotly.express as px

dash.register_page(__name__,
                   path='/vehicle-attributes',
                   name='Vehicle attributes',
                   title='Vehicle attributes',
                   image='pg3.png',
                   description='This section will cover the key attributes of the vehicles in each organization, including weight class, nominal range (mile), rated energy (kWh), max charge rate (kW), peak power (kW), peak torque (Nm), towing capacity (lbs), fuel-fired heater (1 yes, 0 no), capital cost (USD), and count of vehicles.'
)

layout = html.Div(
    [
        dcc.Markdown('## This is the newest heatmap design', style={'textAlign':'center'}),
        dcc.Graph(figure= px.imshow([[1, 20, 30],
                                     [20, 1, 60],
                                     [30, 60, 1]]))
    ]
)

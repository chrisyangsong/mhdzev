import dash
from dash import dcc, html, callback, Output, Input, dash_table
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from datetime import datetime as dt
from dash_table import DataTable
# import geopandas as gpd

# To create meta tag for each page, define the title, image, and description.
dash.register_page(__name__,
                   path='/',  # '/' is home page and it represents the url
                   name='Home',  # name of page, commonly used as name of link
                   title='Index',  # title that appears on browser's tab
                #    image='pg1.png',  # image in the assets folder
                   description='Histograms are the new bar charts.'
)

# page 1 data
# df_1 = px.data.gapminder()
# read the csv file using pandas
# df = pd.read_csv('data/a/1/2023/10/1/truck_trajectory.csv')

px.set_mapbox_access_token("pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A")
initial_columns = []
initial_data = []
layout = html.Div(
    [
        # dbc.Row(
        #     [
        #         dbc.Col(
        #             [
        #                 # dcc.Dropdown(options=df_1.continent.unique(),
        #                             #  id='cont-choice')
        #             ], xs=10, sm=10, md=8, lg=4, xl=4, xxl=4
        #         )
        #     ]
        # ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        
                        html.H1('Select Company:',style={'font-size': '1em'}),
                        dcc.Dropdown(id="company-choice",
                                     options=[
                                        {"label": "a", "value": "a"},
                                        {"label": "b", "value": "b"},
                                        {"label": "c", "value": "c"},
                                        {"label": "d", "value": "d"}],
                                        multi=False,
                                        value='a',
                                        style={'width': "50%"}
                                    ),
                        html.Br(),
                        html.H1('Select Vehicle:',style={'font-size': '1em'}),
                        dcc.Dropdown(id="vehicle-choice",
                                     options=[
                                        {"label": "1", "value": "1"},
                                        {"label": "2", "value": "2"}],
                                        multi=False,
                                        value='1',
                                        style={'width': "50%"}
                                    ),
                        html.Br(),
                        html.H1('Select Date:',style={'font-size': '1em'}),
                        dcc.DatePickerSingle(
                                    id="date-picker",
                                    min_date_allowed=dt(2023, 10, 1),
                                    max_date_allowed=dt(2025, 12, 31),
                                    initial_visible_month=dt(2023, 10, 1),
                                    date=dt(2023, 10, 1).date(),
                                    display_format="MM/DD/YYYY",
                                    style={"border": "0px solid black",'width': '100%'},
                                )
                    ], xs=10, sm=10, md=8, lg=4, xl=4, xxl=4
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(id='output_container', children=[]),
                        dcc.Graph(id='my_bee_map', figure={}),
                        # dcc.Graph(
                        #     id='scatter-map',
                        #     figure=px.scatter_mapbox(
                        #         df,
                        #         lat=df['Latitude'],
                        #         lon=df['Longitude'],
                        #         hover_name="Timestamp",
                        #         zoom=8,
                        #         mapbox_style="open-street-map",
                        #     )
                        # )
                    ], width=12
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        # dash_table.DataTable(data=df.to_dict('records'), page_size=10)
                        dash_table.DataTable(
                            id='my_dash_table',
                            columns=initial_columns,
                            data=initial_data
                            ),


                    ], width=12
                )
            ]
        )
    ]
)


@callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure'),
     Output('my_dash_table', 'columns'),
     Output('my_dash_table', 'data')],
    [Input(component_id='date-picker', component_property='date'),
     Input(component_id='company-choice', component_property='value'),
     Input(component_id='vehicle-choice', component_property='value')]
)
def update_graph(option_date, option_company, option_vehicle):
    # print(option_date)


    # container = "The company chosen by user was: {}<br>. ".format(option_company)+\
    #             "The vehicle chosen by user was: {}<br>. ".format(option_vehicle)+\
    #             "The date chosen by user was: {}. ".format(option_date)
    company_text = "The company chosen by user was: {}".format(option_company)
    vehicle_text = "The vehicle chosen by user was: {}".format(option_vehicle)
    date_text = "The date chosen by user was: {}".format(option_date)
    
    # df = pd.read_csv('data/a/1/2023/10/1/truck_trajectory.csv')
    # x = 'data/'+option_company+'/'+option_vehicle+'/' + option_date[0:4]+'/'+option_date[5:7]+'/'+option_date[8:10]+'/truck_trajectory.csv'

    df = pd.read_csv('data/'+option_company+'/'+option_vehicle+'/' + option_date[0:4]+'/'+option_date[5:7]+'/'+option_date[8:10]+'/truck_trajectory.csv')
    fig=px.scatter_mapbox(
                                df,
                                lat=df['Latitude'],
                                lon=df['Longitude'],
                                hover_name="Timestamp",
                                zoom=8,
                                mapbox_style="open-street-map",
                            )
    columns = [{'name': col, 'id': col} for col in df.columns]
    # columns = [{'name': f'Column_{i}', 'id': f'col_{i}'} for i in range(3)]
    
    # table = dash_table.DataTable(data=df.to_dict('records'), page_size=10)
    

    return  [
        html.P(company_text),
        html.P(vehicle_text),
        html.P(date_text),
        # html.P(x),
    ], fig,columns, df.to_dict('records')

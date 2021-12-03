from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from app import app
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

# Load CSV file from datasets folder
df1 = pd.read_csv('datasets/nc_raw_data.csv')

# Layout
layout = html.Div([
    html.Br(),
    html.H1(children='Refugees Re-Settled in Major NC Cities Over Time',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('North Carolina Refugee Population -  2010 to 2018', style={'textAlign': 'center'}),
    html.Br(),
    dcc.Graph(id='graph2'),
    html.Div('Please select a city', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-city',
        options=[

            {'label': 'Charlotte', 'value': 'Charlotte'},
            {'label': 'Raleigh', 'value': 'Raleigh'},
            {'label': 'Greensboro', 'value': 'Greensboro'},
            {'label': 'High Point', 'value': 'High Point'},
            {'label': 'Durham', 'value': 'Durham'},
            {'label': 'New Bern', 'value': 'New Bern'},
            {'label': 'Wilmington', 'value': 'Wilmington'},
            {'label': 'Asheville', 'value': 'Asheville'},
            {'label': 'Carrboro', 'value': 'Carrboro'}
        ],
        value='Charlotte'
    )
])


@app.callback(Output('graph2', 'figure'),
              [Input('select-city', 'value')])
def update_figure(selected_city):
    line_df = df1[(df1['city'] == selected_city)]
    line_df = line_df.groupby(['year'])['people'].sum().reset_index()
    data_linechart = [go.Scatter(x=line_df['year'], y=line_df['people'], mode='lines', name='refugees by city')]

    return{'data': data_linechart, 'layout': go.Layout(title='Total Refugees in ' + selected_city + ', NC from 2010 to 2018',
                                      xaxis={'title': 'Year'}, yaxis={'title': 'Number of Refugees'})}


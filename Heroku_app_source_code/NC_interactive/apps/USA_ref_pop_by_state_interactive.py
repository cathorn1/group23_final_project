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
df1 = pd.read_csv('datasets/annual_refugee_data.csv')

# Layout
layout = html.Div(children=[
    html.Br(),
    html.H1(children='US State Refugee Populations Year-Over-Year',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('US State Refugee Population -  2010 to 2018', style={'textAlign': 'center'}),
    html.Br(),
    dcc.Graph(id='graph4'),
    html.Div('Please select a state', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-state',
        options=[

            {'label': 'Alabama', 'value': 'Alabama'},
            {'label': 'Alaska', 'value': 'Alaska'},
            {'label': 'Arizona', 'value': 'Arizona'},
            {'label': 'Arkansas', 'value': 'Arkansas'},
            {'label': 'California', 'value': 'California'},
            {'label': 'Colorado', 'value': 'Colorado'},
            {'label': 'Connecticut', 'value': 'Connecticut'},
            {'label': 'Delaware ', 'value': 'Delaware '},
            {'label': 'District of Columbia', 'value': 'District of Columbia'},
            {'label': 'Florida', 'value': 'Florida'},
            {'label': 'Georgia', 'value': 'Georgia'},
            {'label': 'Idaho', 'value': 'Idaho'},
            {'label': 'Illinois', 'value': 'Illinois'},
            {'label': 'Indiana', 'value': 'Indiana'},
            {'label': 'Iowa', 'value': 'Iowa'},
            {'label': 'Kansas', 'value': 'Kansas'},
            {'label': 'Kentucky', 'value': 'Kentucky'},
            {'label': 'Louisiana', 'value': 'Louisiana'},
            {'label': 'Maine', 'value': 'Maine'},
            {'label': 'Maryland', 'value': 'Maryland'},
            {'label': 'Massachusetts', 'value': 'Massachusetts'},
            {'label': 'North Carolina', 'value': 'North Carolina'},
            {'label': 'Michigan', 'value': 'Michigan'},
            {'label': 'Minnesota', 'value': 'Minnesota'},
            {'label': 'Mississippi', 'value': 'Mississippi'},
            {'label': 'Missouri', 'value': 'Missouri'},
            {'label': 'Nebraska', 'value': 'Nebraska'},
            {'label': 'Nevada', 'value': 'Nevada'},
            {'label': 'New Hampshire', 'value': 'New Hampshire'},
            {'label': 'New Jersey', 'value': 'New Jersey'},
            {'label': 'New Mexico', 'value': 'New Mexico'},
            {'label': 'New York', 'value': 'New York'},
            {'label': 'North Dakota', 'value': 'North Dakota'},
            {'label': 'Ohio', 'value': 'Ohio'},
            {'label': 'Oklahoma', 'value': 'Oklahoma'},
            {'label': 'Oregon', 'value': 'Oregon'},
            {'label': 'Pennsylvania', 'value': 'Pennsylvania'},
            {'label': 'Rhode Island', 'value': 'Rhode Island'},
            {'label': 'South Carolina', 'value': 'South Carolina'},
            {'label': 'Tennessee', 'value': 'Tennessee'},
            {'label': 'Texas', 'value': 'Texas'},
            {'label': 'Utah', 'value': 'Utah'},
            {'label': 'Vermont', 'value': 'Vermont'},
            {'label': 'Virginia', 'value': 'Virginia'},
            {'label': 'Washington', 'value': 'Washington'},
            {'label': 'West Virginia', 'value': 'West Virginia'},
            {'label': 'Wisconsin', 'value': 'Wisconsin'},
            {'label': 'Wyoming', 'value': 'Wyoming'},

        ],
        value='North Carolina'
    )
])


@app.callback(Output('graph4', 'figure'),
              [Input('select-state', 'value')])
def update_figure(selected_state):
    line_df = df1[(df1['state'] == selected_state)]
    line_df = line_df.groupby(['year'])['people'].sum().reset_index()
    data_linechart = [go.Scatter(x=line_df['year'], y=line_df['people'], mode='lines', name='refugees by state')]

    return{'data': data_linechart, 'layout': go.Layout(title='Total Refugees in ' + selected_state + ' from 2010 to 2018',
                                      xaxis={'title': 'Year'}, yaxis={'title': 'Number of Refugees'})}


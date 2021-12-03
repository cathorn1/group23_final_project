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
df1 = pd.read_csv(DATA_PATH.joinpath("nc_raw_data.csv"))

# Layout
layout = html.Div([
    html.Br(),
    html.H1(children='Annual Refugees Re-Settled in NC Cities ',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('North Carolina Refugee Population -  2010 to 2018', style={'textAlign': 'center'}),
    html.Br(),
    dcc.Graph(id='graph1', figure={}),
    html.Div('Please select a year', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-year',
        options=[

            {'label': '2010', 'value': 2010},
            {'label': '2011', 'value': 2011},
            {'label': '2012', 'value': 2012},
            {'label': '2013', 'value': 2013},
            {'label': '2014', 'value': 2014},
            {'label': '2015', 'value': 2015},
            {'label': '2016', 'value': 2016},
            {'label': '2017', 'value': 2017},
            {'label': '2018', 'value': 2018}
        ],
        value=2018
    )
])


@app.callback(Output(component_id='graph1', component_property='figure'),
              [Input(component_id='select-year', component_property='value')])
def update_figure(selected_year):
    filtered_df = df1[(df1['year'] == selected_year)]
    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    new_df = filtered_df.groupby(['city'])['people'].sum().reset_index()
    new_df = new_df.sort_values(by=['people'], ascending=[False]).head(15)
    data_interactive_barchart = [go.Bar(x=new_df['city'], y=new_df['people'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Refugee Population in North Carolina in '
                                                                         + str(selected_year),
                                                                   xaxis={'title': 'NC City'},
                                                                   yaxis={'title': 'Total Refugee Population'})}

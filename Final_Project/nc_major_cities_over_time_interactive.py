import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('Datasets/nc_raw_data.csv')

app = dash.Dash()

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('North Carolina Refugee Population -  2010 to 2018', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Interactive Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represent the number of refugees in major cities in NC over the years.'),
    dcc.Graph(id='graph1'),
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


@app.callback(Output('graph1', 'figure'),
              [Input('select-city', 'value')])
def update_figure(selected_city):
    line_df = df1[(df1['city'] == selected_city)]
    line_df = line_df.groupby(['year'])['people'].sum().reset_index()
    data_linechart = [go.Scatter(x=line_df['year'], y=line_df['people'], mode='lines', name='refugees by city')]

    return{'data': data_linechart, 'layout': go.Layout(title='Total Refugees in ' + selected_city + ', NC from 2010 to 2018',
                                      xaxis={'title': 'Year'}, yaxis={'title': 'Number of Refugees'})}

if __name__ == '__main__':
    app.run_server()
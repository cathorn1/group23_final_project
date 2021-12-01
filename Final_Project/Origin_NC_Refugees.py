import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

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
    html.Div('Origins of Refugees in North Carolina - 2010 to 2018', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Interactive Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represent the number of refugees from the top 15 countries by selected year.'),
    dcc.Graph(id='graph1'),
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
@app.callback(Output('graph1', 'figure'),
              [Input('select-year', 'value')])
def update_figure(selected_year):

    filtered_df = df1[(df1['year'] == selected_year)]

    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    filtered_df = filtered_df.groupby(['origin'])['stateorigin'].reset_index()

    #new_df = new_df.sort(by=['stateorigin'], ascending=[False]).head(15)
    filtered_df = filtered_df.sort_values(by=['stateorigin'], ascending=[False])
    data_interactive_barchart = [go.Bar(x=filtered_df['origin'], y=filtered_df['stateorigin'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Refugees in NC by Country of Origin'
                                                                         + str(selected_year),
                                                                   xaxis={'title': 'Country of Origin'},
                                                                   yaxis={'title': 'Population'})}


if __name__ == '__main__':
    app.run_server()
# data = [go.Bar(x=df['origin'], y=df['people'])]
# # Preparing data ---- create traces for male and female total
# trace3 = go.Scatter(x=df['Country of Origin Code'], y=df['Total'], mode='markers+lines', name='Total')
# data = [ trace3]
#
#
# # Preparing layout
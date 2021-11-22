import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('Datasets/demographics_residing_usa.csv')

app = dash.Dash()

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Origin of Refugees by Country', style={'textAlign': 'center'}),
    html.Div('United State Refugee Population -  2010 to 2020', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Interactive Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represents the number of refugees in the top 15 states in the USA by selected year.'),
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
            {'label': '2018', 'value': 2018},
            {'label': '2019', 'value': 2019},
            {'label': '2020', 'value': 2020},

        ],
        value=2020
    )
])


@app.callback(Output('graph1', 'figure'),
              [Input('select-year', 'value')])
def update_figure(selected_year):

    filtered_df = df1[(df1['year'] == selected_year)]

    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    filtered_df = filtered_df[(filtered_df['Population Type'] == "REF")]

    new_df = filtered_df.groupby(['Country of Origin Name'])['people'].sum().reset_index()

    new_df = new_df.sort_values(by=['people'], ascending=[False]).head(15)
    data_interactive_barchart = [go.Bar(x=new_df['Country of Origin Name'], y=new_df['people'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Top Refugee Populations in USA in '
                                                                         + str(selected_year),
                                                                   xaxis={'title': ' Country'},
                                                                   yaxis={'title': 'Total Refugee Population'})}


if __name__ == '__main__':
    app.run_server()
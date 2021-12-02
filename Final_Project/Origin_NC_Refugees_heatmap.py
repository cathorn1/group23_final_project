import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


df = pd.read_csv('Datasets/nc_raw_data.csv')
fig = px.choropleth(df, locations = 'origin', locationmode= 'country names', color='stateorigin', hover_name='origin')

app = dash.Dash(__name__)

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
    html.H3('Interactive Choropleth Map', style={'color': '#df1e56'}),
    html.Div('This map colors the origin countries of refugees in North Carolina based on how many came from there.'),

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
    ),
    dcc.Graph(id='chloropleth'),
    ])
@app.callback(Output('chloropleth', 'figure'),
              [Input('select-year', 'value')])
def update_figure(selected_year):

    filtered_df = df[(df['year'] == selected_year)]

    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)


    new_df = filtered_df.groupby(['origin'])['stateorigin'].first().reset_index()
    new_df = new_df[(new_df['stateorigin'] > 0)]
    #new_df = new_df.sort(by=['stateorigin'], ascending=[False]).head(15)
    #new_df = new_df.sort_values(by=['stateorigin'], ascending=[False])
    fig = px.choropleth(
        new_df,
        locations = 'origin',
        locationmode= 'country names',
        color='stateorigin',
        hover_name='origin',
        hover_data={'origin' : False},
        range_color=(1, filtered_df['stateorigin'].max()),
        labels={'stateorigin': 'Refugees'},
        title= 'Origins of Refugees in North Carolina in ' + str(selected_year))
    fig.update_geos(visible = False, resolution = 110,
                    showland = True, landcolor= "lightgray"
                    )
    #fig.update_layout(title_text = , height = 300, margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


if __name__ == '__main__':
    app.run_server()

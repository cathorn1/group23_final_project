from dash import dcc
from dash import html
from dash.dependencies import Input, Output


# Connect to main app.py file
from app import app
from app import server

server = app.server
# Connect to your app pages
from apps import NC_heatmap_interactive, NC_major_cities_over_time_interactive, NC_annual_refs_by_city_interactive

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div('Please Select a Graph to View:', style={'textAlign': 'center', 'fontSize': 'large'}),
    html.Br(),
    html.Div(children=[
        dcc.Link('North Carolina Refugee Heatmap | ', href='/apps/NC_heatmap_interactive'),
        dcc.Link('NC Refugee Pop. In Major Cities | ', href='/apps/NC_major_cities_over_time_interactive'),
        dcc.Link('NC Annual Refugee Pop. By City', href='/apps/NC_annual_refs_by_city_interactive'),
    ], className="row", style={'textAlign': 'center', 'fontSize': 'large'}),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/NC_heatmap_interactive':
        return NC_heatmap_interactive.layout
    if pathname == '/apps/NC_major_cities_over_time_interactive':
        return NC_major_cities_over_time_interactive.layout
    if pathname == '/apps/NC_annual_refs_by_city_interactive':
        return NC_annual_refs_by_city_interactive.layout
    else:
        return NC_heatmap_interactive.layout


if __name__ == '__main__':
    app.run_server(debug=False)

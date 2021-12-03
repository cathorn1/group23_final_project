from dash import dcc
from dash import html
from dash.dependencies import Input, Output


# Connect to main app.py file
from app import app
from app import server

server = app.server
# Connect to your app pages
from apps import USA_annual_ref_origin_pop_interactive, USA_ref_pop_by_state_interactive

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div('Please Select a Graph to View:', style={'textAlign': 'center', 'fontSize': 'large'}),
    html.Br(),
    html.Div(children=[
        dcc.Link('USA Refugee Pop. Year-Over-Year | ', href='/apps/USA_ref_pop_by_state_interactive'),
        dcc.Link('USA Refugee Top Countries Of Origin', href='/apps/USA_annual_ref_origin_pop_interactive'),
    ], className="row", style={'textAlign': 'center', 'fontSize': 'large'}),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/USA_ref_pop_by_state_interactive':
        return USA_ref_pop_by_state_interactive.layout
    if pathname == '/apps/USA_annual_ref_origin_pop_interactive':
        return USA_annual_ref_origin_pop_interactive.layout
    else:
        return USA_ref_pop_by_state_interactive.layout


if __name__ == '__main__':
    app.run_server(debug=False)

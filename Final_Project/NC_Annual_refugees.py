import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('Datasets/annual_refugee_data.csv')

df = df[(df['state'] == 'North Carolina')]

trace1 = [go.Bar(x=df['year'], y=df['people'])]

# Preparing layout
layout = go.Layout(title='Annual Total of Refugees Resettled in North Carolina', xaxis_title="Year",
                   yaxis_title="Total Refugees")

# Plot the figure and saving in a html file
fig = go.Figure(data=trace1, layout=layout)
pyo.plot(fig, filename='nc_barchart.html')
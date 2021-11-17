import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('Datasets/annual_refugee_data.csv')

# Removing empty spaces from State column to avoid errors
# df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating unrecovered column
# df['Unrecovered'] = df['Confirmed'] - df['Deaths'] - df['Recovered']

# Creating sum of number of cases group by Country Column
# new_df = df.groupby(['Country']).agg(
#     {'Confirmed': 'sum', 'Deaths': 'sum', 'Recovered': 'sum', 'Unrecovered': 'sum'}).reset_index()

df = df[(df['state'] == 'North Carolina')]

df = df.groupby(['state'])['annualtotal'].sum().reset_index()

# Preparing data
trace1 = [go.Bar(x=df['year'], y=df['people'])]

# Preparing layout
layout = go.Layout(title='Annual Total of Refugees Resettled in North Carolina', xaxis_title="Year",
                   yaxis_title="Total Refugees")

# Plot the figure and saving in a html file
fig = go.Figure(data=trace1, layout=layout)
pyo.plot(fig, filename='nc_barchart.html')
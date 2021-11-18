import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# Load CSV file from Datasets folder
df = pd.read_csv('Datasets/annual_refugee_data.csv')

#df['statetotal'] = pd.to_datetime(df['statetotal'])

# convert year column to datetime format for filtering
#df['year'] = pd.to_datetime(df['year'], format = '%Y') # %Y filters only the year
# filter df to the year 2020 so each country only has a single point for population
#df = df[(df['year'] >= 2014)]

df = df[(df['state'] == 'North Carolina') & (df['year'] >= 2010)]
df = df.sort_values('year')

# Preparing data
data = [go.Scatter(x=df['year'], y=df['annualtotal'], mode='lines', name='annualtotal')]

# Preparing layout
layout = go.Layout(title='Annual Amount of Refugees Resettled in the USA', xaxis_title="Year",
                   yaxis_title="Number of Refugees")


# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='annual_ref_usa.html')

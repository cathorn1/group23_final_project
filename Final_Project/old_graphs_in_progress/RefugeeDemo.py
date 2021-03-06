import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/annual_refugee_data.csv')

#df['statetotal'] = pd.to_datetime(df['statetotal'])

# convert year column to datetime format for filtering
#df['year'] = pd.to_datetime(df['year'], format = '%Y') # %Y filters only the year
# filter df to the year 2020 so each country only has a single point for population
#df = df[(df['year'] >= 2014)]

df = df[(df['state'] == 'North Carolina') & (df['year'] >= 2010)]
df = df.sort_values('year')
# Preparing data
#data = [go.Scatter(x=df['Date'], y=df['Confirmed'], mode='lines', name='Death')]

# Sorting values and select 20 first value
#new_df = new_df.sort_values(by=['statetotal'], ascending=[False]).head(20).reset_index()

# Preparing data
data = [go.Scatter(x=df['year'], y=df['annualtotal'], mode='lines', name='annualtotal')]

# Preparing layout
layout = go.Layout(title='annual_refugee_data.numbers', xaxis_title="annual_refugee_data.numbers",
                   yaxis_title="Number of People")


# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('annual_refugee_data.csv')

df['statetotal'] = pd.to_datetime(df['statetotal'])

# convert year column to datetime format for filtering
df['year'] = pd.to_datetime(df['year'], format = '%Y') # %Y filters only the year
# filter df to the year 2020 so each country only has a single point for population
df = df[(df['year'] >= "2018")]


# Sorting values and select 20 first value
#new_df = new_df.sort_values(by=['statetotal'], ascending=[False]).head(20).reset_index()

# Preparing data

trace1 = go.Scatter(x=df['statetotal'], y=df['year'], mode='lines', name='year')
trace2 = go.Scatter(x=df['statetotal'], y=df['stateorigin'], mode='lines', name='stateorigin')
trace3 = go.Scatter(x=df['statetotal'], y=df['state'], mode='lines', name='state')
trace4 = go.Scatter(x=df['statetotal'], y=df['city'], mode='lines', name='city')

data = [trace1,trace2,trace3, trace4]





# Preparing layout
layout = go.Layout(title='annual_refugee_data.numbers', xaxis_title="annual_refugee_data.numbers",
                   yaxis_title="Number of People", barmode='stack')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stackbarchart.html')

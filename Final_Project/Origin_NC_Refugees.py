import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('Datasets/annual_refugee_data.csv')
print(type(df))
#df1 = pd.read_csv('annual_refugee_data.csv')

# filter df to the year 2020 so each country only has a single point for population
df = df[(df['state'] == "North Carolina")]
print(df)
# filter df further to only contain refugee data instead of both refugee and asylum
df = df.groupby(['origin'])['people'].sum().reset_index()
df = df.sort_values(by=['people'], ascending = False).head(20)


data = [go.Bar(x=df['origin'], y=df['people'])]
# # Preparing data ---- create traces for male and female total
# trace3 = go.Scatter(x=df['Country of Origin Code'], y=df['Total'], mode='markers+lines', name='Total')
# data = [ trace3]
#
#
# # Preparing layout
layout = go.Layout(title='Population of Refugees in NC by Country of Origin', xaxis_title="Country of Origin",
                   yaxis_title="Population")
# # # Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='static/ncrefugeeorigin.html')

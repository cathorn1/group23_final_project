import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/demographics_residing_usa.csv')

#df1 = pd.read_csv('annual_refugee_data.csv')
# convert year column to datetime format for filtering
df['Year'] = pd.to_datetime(df['Year'], format = '%Y') # %Y filters only the year
# filter df to the year 2020 so each country only has a single point for population
df = df[(df['Year'] == "2020")]
# filter df further to only contain refugee data instead of both refugee and asylum
df = df[(df['Population Type'] == "REF")]

# Preparing data ---- create traces for male and female total
trace3 = go.Scatter(x=df['Country of Origin Code'], y=df['Total'], mode='markers+lines', name='Total')
data = [ trace3]


# Preparing layout
layout = go.Layout(title='Population of Refugees and Asylum Seekers in the United States', xaxis_title="Country of Origin",
                   yaxis_title="Total population")
# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='static/multilinechart.html')

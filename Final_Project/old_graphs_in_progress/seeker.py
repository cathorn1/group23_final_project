import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('asylum_applications_residing_usa (1).csv')

# Removing empty spaces from State column to avoid errors
#df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

#df1 = pd.read_csv('annu al_refugee_data.csv')
# convert year column to datetime format for filtering
#f['Year'] = pd.to_datetime(df['Year'], format = '%Y') # %Y filters only the year
# filter df to the year 2020 so each country only has a single point for population
df = df[(df['Year'] == "2020")]
# filter df further to only contain refugee data instead of both refugee and asylum
df = df[(df['Application Type'] == "New")]




# Creating unrecovered column
#df['Country of Origin Name'] = df['Country of Asylum Name'] - df['Application Average Persons Per Case'] - df['Application Data']


#
# Preparing data
trace1 = go.Bar(x=df['Country of Origin Name'], y=df['Country of Asylum Name'], name='Country of Asylum Name', marker={'color': '#CD7F32'})
trace2 = go.Bar(x=df['Country of Origin Name'], y=df['Application Average Persons Per Case'], name='Application Average Persons Per Case', marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=df['Country of Origin Name'], y=df['Application Data'], name='Application Data', marker={'color': '#FFD700'})
data = [trace1, trace2, trace3]

# Preparing layout
layout = go.Layout(title=' The number of applications for asylum residing in United States of America.', xaxis_title="Country",
                  yaxis_title="Number of cases", barmode='stack')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stackbarchart.html')



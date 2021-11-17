import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('annual_refugee_data.csv')

# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating unrecovered column
# df['Unrecovered'] = df['Confirmed'] - df['Deaths'] - df['Recovered']

# Creating sum of number of cases group by Country Column
# new_df = df.groupby(['Country']).agg(
#     {'Confirmed': 'sum', 'Deaths': 'sum', 'Recovered': 'sum', 'Unrecovered': 'sum'}).reset_index()


df = df.groupby(['state']).agg({'annualtotal': 'sum'}).reset_index()

nc_data = df[(df['state'] == 'North Carolina')]

# nc_data = df[(df['year'] > 2000)]


# Sorting values and select 20 first value
# new_df = new_df.sort_values(by=['Confirmed'], ascending=[False]).head(20).reset_index()

# Preparing data
trace1 = go.Bar(x=nc_data['year'], y=nc_data['annualtotal'], name='annual total', marker={'color': '#CD7F32'})


# Preparing layout
layout = go.Layout(title='Annual Total of Refugees Resettled in North Carolina', xaxis_title="Year",
                   yaxis_title="Total Refugees", barmode='stack')

# Plot the figure and saving in a html file
fig = go.Figure(data=trace1, layout=layout)
pyo.plot(fig, filename='nc_barchart.html')
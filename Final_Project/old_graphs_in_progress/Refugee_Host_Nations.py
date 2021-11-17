import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/annual_refugee_data.csv')


#


i = -3
r = range(2011,2016)
#for i in range(5):
 #   cdf.loc['US'].loc[r[i]].head(10).plot(x='Origin', y='Refugees',
 #                                         color=c[i])
    # Creating sum of number of cases group by Country Column
new_df=df.groupby(['people']).agg(
      {'stateorigin': 'sum', 'state': 'sum', 'annualtotal': 'sum'}).reset_index()

trace1 = go.Bar(x=new_df['state'], y=new_df['annualtotal'], name='annualtotal', marker={'color': '#CD7F32'})
trace1 = go.Scatter(x=df['statetotal'], y=df['city'], mode='lines', name='city')
trace2 = go.Scatter(x=df['statetotal'], y=df['year'], mode='lines', name='year')
trace3 = go.Scatter(x=df['statetotal'], y=df['state'], mode='lines', name='state')
data = [trace1,trace2,trace3]

data = [trace1]
plt.title(label='United States Refugees Accepted by Origin Country')
plt.xticks(rotation=60)
plt.subplots_adjust(bottom=.2)
plt.ylabel("Number of Immigrants Accepted")
plt.xlabel("Origin Country")
plt.show()


df[(df.people.notnull()) & (df.year == 2015)].sort_values(by='people',
                                                           ascending=False).head(10)



data = df[(df.statetotal.notnull()) & (df.annualtotal == r[i])]
data = data.sort_values(by='people', ascending=False).head(15)
bar = sns.barplot(y="state", x="people", orient="h", data=data,
                  palette="dark", estimator=sum)

bar.set_title(label=
              "Nations Accepting Highest Numbers of Refugees\n%s" % r[i])
bar.set_xlabel(xlabel="Refugees")
bar.set_ylabel(ylabel="Host State")
plt.subplots_adjust(left=.2)
plt.show()



layout = go.Layout(title='annual_refugee_data.numbers', xaxis_title="annual_refugee_data.numbers",
                    yaxis_title="Number of People", barmode='stack')

#Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stackbarchart.html')

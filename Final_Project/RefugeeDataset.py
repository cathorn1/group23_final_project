import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('refugees_per_capita.csv')


#


i = -3
r = range(2011,2016)

#for i in range(5):
#  cdf.loc['US'].loc[r[i]].head(10).plot(x='Origin', y='Refugees',
       #                                   color=c[i])
    # Creating sum of number of cases group by Country Column
new_df=df.groupby(['Country']).agg(
        {'Population': 'sum', 'Refugees': 'sum', 'RefPerCap': 'sum'}).reset_index()


trace1 = go.Bar(x=new_df['Refugees'], y=new_df['RefPerCap'], name='RefPerCap', marker={'color': '#CD7F32'})
trace2 = go.Bar(x=new_df['Population'], y=new_df['Population'], name='Population', marker={'color': '#9EA0A1'})

data = [trace1, trace2]

plt.title(label='United States Refugees Accepted by Origin Country\n%d' % r[i])
plt.xticks(rotation=60)
plt.subplots_adjust(bottom=.2)
plt.ylabel("Number of Immigrants Accepted")
plt.xlabel("Origin Country")
# plt.show()


df[(df.Refugees.notnull()) & (df.Year == 2015)].sort_values(by='Refugees',
                                                            ascending=False).head(10)



data = df[(df.Refugees.notnull()) & (df.Year == r[i])]
data = data.sort_values(by='Refugees', ascending=False).head(1)
bar = sns.barplot(y="Country", x="Refugees", orient="h", data=data,
                  palette="dark", estimator=sum)

bar.set_title(label=
              "Nations Accepting Highest Numbers of Refugees")
bar.set_xlabel(xlabel="Refugees")
bar.set_ylabel(ylabel="Host Country")
plt.subplots_adjust(left=.2)
plt.show()



layout = go.Layout(title='annual_refugee_data.numbers', xaxis_title="annual_refugee_data.numbers",
                    yaxis_title="Number of People", barmode='stack')

#Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stackbarchart.html')

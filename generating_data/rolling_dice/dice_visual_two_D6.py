from plotly.graph_objs import Bar, Layout
from plotly import offline

from die_class import Die

##Creating dice.
die_1 = Die()
die_2 = Die()

##Making rolls and storing the results.
results = []
for num_roll in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

##Visualize the results.
x_values = list(range(2,max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Result', 'dtick':1}       ##To label all the bars(since, plotly labels only some bars if there are more bars).
y_axis_config = {'title':'Frequency of Result'}
layout = Layout(title='Results of rolling two D6 1000 times', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data':data, 'layout':layout}, filename='generating_data/rolling_dice/two_d6.html')


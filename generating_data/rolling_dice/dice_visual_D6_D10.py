# from project_die import Die
# 
#Create a D6
# die = Die()
# 
#Make some rolls and store the results
# results = []
# for num_roll in range(100):
    # result = die.roll()
    # results.append(result)
# print(results)
# 
#Analyzing the results
# 
# die = Die()
# results = []
# for num_roll in range(1000):
    # result = die.roll()
    # results.append(result)

#Analyze the results.
# frequencies = []
# for value in range(1, die.num_sides+1):
    # frequency = results.count(value)
    # frequencies.append(frequency)
# print(frequencies)

##Making a Histogram

# from plotly.graph_objs import Bar, Layout
# from plotly import offline

# from project_die import Die

# die = Die()
# results = []
# for num_roll in range(1000):
    # result = die.roll()
    # results.append(result)

# frequencies = []
# for value in range(1, die.num_sides+1):
    # frequency = results.count(value)
    # frequencies.append(frequency)

#Visualize the results.
# x_values = list(range(1,die.num_sides+1))
# data = [Bar(x=x_values, y=frequencies)]

# x_axis_config = {'title':'Result'}
# y_axis_config = {'title':'Frequency of Result'}
# layout = Layout(title='Results of rolling one D6 1000 times', xaxis = x_axis_config, yaxis = y_axis_config)
# offline.plot({'data':data, 'layout':layout}, filename='d6.html')

##Rolling dice of different sizes

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die_class import Die

##Create a D6 and a D10
die_1 = Die()
die_2 = Die(10)

##Make some rolls and store the results
results = []
for num_roll in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

##Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

##Visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Result', 'dtick':1}
y_axis_config = {'title':'Frequency of Result'}
layout = Layout(title='Results of rolling a D6 and a D10 50000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':layout}, filename='d6_d10.html')
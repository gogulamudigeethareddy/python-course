#Cube of a number
# 
# import matplotlib.pyplot as plt
# 
# x_values = [1,2,3,4,5]
# y_values = [1,8,27,64,125]
# 
# fig,ax = plt.subplots()
# ax.scatter(x_values, y_values, s=100)
# 
# ax.set_title("Cube Numbers", fontsize=24)
# ax.set_xlabel("Values", fontsize=14)
# ax.set_ylabel("Cube of Value", fontsize=14)
# 
# plt.show()
# 
#Cubes in a range
# 
# import matplotlib.pyplot as plt
# 
# x_values = range(1, 5000)
# y_values = [x**3 for x in x_values]
# 
# fig,ax = plt.subplots()
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)
# 
# ax.set_title("Cube Numbers", fontsize=24)
# ax.set_xlabel("Values", fontsize=14)
# ax.set_ylabel("Cube of Value", fontsize=14)
# 
# plt.show()

##Molecular Motion

# import matplotlib.pyplot as plt
# from random import choice
# from project_random_walk import RandomWalk 

# while True:
   #Make a random walk
#    rw = RandomWalk(5000)  #To increase the num_points, adding plot points
#    rw.fill_walk()

   #Plot the points in the walk
#    plt.style.use('classic')
#    fig, ax = plt.subplots(figsize=(15,9))  #To fit the plot in the screen
#    point_numbers = range(rw.num_points)
#    ax.plot(rw.x_values, rw.y_values, c='', linewidth=4)
   
   #Emphasize the first and last points
#    ax.plot(0, 0, c='green', linewidth=10)
#    ax.plot(rw.x_values[-1], rw.y_values[-1], c='red', linewidth=2)
   
   #Remove the axes
#    ax.get_xaxis().set_visible(False)
#    ax.get_yaxis().set_visible(False)
   
#    plt.show()
   
#    keep_running = input("Make another walk?(y/n): ")
#    if keep_running == 'n':
    #    break
   
##Modified Random Walks
# import matplotlib.pyplot as plt
# from random import choice
# from project_tiy_rw import RandomWalk 

# while True:
  #Make a random walk
#   rw = RandomWalk(5000)  #To increase the num_points, adding plot points
#   rw.fill_walk()

  #Plot the points in the walk
#   plt.style.use('classic')
#   fig, ax = plt.subplots(figsize=(15,9))  #To fit the plot in the screen
#   point_numbers = range(rw.num_points)
#   ax.plot(rw.x_values, rw.y_values, c='blue', linewidth=4)
  
  #Emphasize the first and last points
#   ax.plot(0, 0, c='green', linewidth=10)
#   ax.plot(rw.x_values[-1], rw.y_values[-1], c='red', linewidth=2)
  
  #Remove the axes
#   ax.get_xaxis().set_visible(False)
#   ax.get_yaxis().set_visible(False)
  
#   plt.show()
  
#   keep_running = input("Make another walk?(y/n): ")
#   if keep_running == 'n':
      # break
  
##Rolling Dice

# from plotly.graph_objs import Bar, Layout
# from plotly import offline

# from rolling_dice.die_class import Die

##Creating dice.
# die_1 = Die(8)
# die_2 = Die(8)

#Making rolls and storing the results.
# results = []
# for num_roll in range(10000):
   #  result = die_1.roll() + die_2.roll()
   #  results.append(result)

##Analyze the results.
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result+1):
   #  frequency = results.count(value)
   #  frequencies.append(frequency)

#Visualize the results.
# x_values = list(range(2,max_result+1))
# data = [Bar(x=x_values, y=frequencies)]

# x_axis_config = {'title':'Result', 'dtick':1}       ##To label all the bars(since, plotly labels only some bars if there are more bars).
# y_axis_config = {'title':'Frequency of Result'}
# layout = Layout(title='Results of rolling two D8 10000 times', xaxis = x_axis_config, yaxis = y_axis_config)
# offline.plot({'data':data, 'layout':layout}, filename='two_d8.html')

##Rolling three dice

# from plotly.graph_objs import Bar, Layout
# from plotly import offline
 
# from rolling_dice.die_class import Die
# 
#Creating dice.
# die_1 = Die()
# die_2 = Die()
# die_3 = Die()
# 
#Making rolls and storing the results.
# results = []
# for num_roll in range(1000):
   #  result = die_1.roll() + die_2.roll() + die_3.roll()
   #  results.append(result)
# 
#Analyze the results.
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
# for value in range(3, max_result+1):
   #  frequency = results.count(value)
   #  frequencies.append(frequency)
# 
#Visualize the results.
# x_values = list(range(3,max_result+1))
# data = [Bar(x=x_values, y=frequencies)]
# 
# x_axis_config = {'title':'Result', 'dtick':1}       
# y_axis_config = {'title':'Frequency of Result'}
# layout = Layout(title='Results of rolling three D6 1000 times', xaxis = x_axis_config, yaxis = y_axis_config)
# offline.plot({'data':data, 'layout':layout}, filename='three_d6.html')

#Multiplication
# 
# from plotly.graph_objs import Bar, Layout
# from plotly import offline
#  
# from rolling_dice.die_class import Die
# 
#Creating dice.
# die_1 = Die()
# die_2 = Die()
# 
#Making rolls and storing the results.
# results = []
# for num_roll in range(1000):
   #  result = die_1.roll() * die_2.roll()
   #  results.append(result)
# 
#Analyze the results.
# frequencies = []
# max_result = die_1.num_sides * die_2.num_sides
# for value in range(1, max_result+1):
   #  frequency = results.count(value)
   #  frequencies.append(frequency)
# 
#Visualize the results.
# x_values = list(range(1,max_result+1))
# data = [Bar(x=x_values, y=frequencies)]
# 
# x_axis_config = {'title':'Result', 'dtick':1}       
# y_axis_config = {'title':'Frequency of Result'}
# layout = Layout(title='Results of rolling two D6 1000 times', xaxis = x_axis_config, yaxis = y_axis_config)
# offline.plot({'data':data, 'layout':layout}, filename='multiply_d6.html')
# 
##Die Comprehension(List comprehension)
# 
from plotly.graph_objs import Bar, Layout
from plotly import offline
#  
from rolling_dice.die_class import Die
# 
##Creating dice.
die_1 = Die()
die_2 = Die()

##Making rolls and storing the results.
results = []
results = [(die_1.roll()+die_2.roll()) for _ in range(1000)]
  
##Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

##Visualize the results.
x_values = list(range(2,max_result+1))
data = [Bar(x=x_values, y=frequencies)]
# 
x_axis_config = {'title':'Result', 'dtick':1}       
y_axis_config = {'title':'Frequency of Result'}
layout = Layout(title='Results of rolling two D6 1000 times', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data':data, 'layout':layout}, filename='generating_data/rolling_dice/comprehension_d6.html')



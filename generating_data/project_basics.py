import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

figure, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
plt.show()

##Built-in styles

plt.style.use('seaborn')
figure, ax = plt.subplots()

ax.plot(input_values, squares, linewidth=3)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis='both',labelsize=14)

plt.show()

##scatter plot

import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')  #replaced 'seaborn' with 'seaborn-v0_8'
fig, ax = plt.subplots()
ax.scatter(2,4, s=200)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

##scatter plot with a series of points

import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='red', s=100)  #'c' means color

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

##Data getting automatically using a loop

import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=(0,0.5,0), s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.axis([0, 1100, 0, 1100000])

plt.show()

##Colormap - Series of colors in a gradient

import matplotlib.pyplot as plt
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.axis([0, 1100, 0, 1100000])

plt.savefig('generating_data/squares_plot.png', bbox_inches='tight')  #To save the plots automatically and removing extra white spaces(2nd argument)

##Random Walk

from random import choice

class RandomWalk:
    """A class to generate random walks."""
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        #All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        """Calculate all the points in the walk."""
        while len(self.x_values) < self.num_points:
            
            #Decide which direction to go and how far to go in that direction.
            
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            
            #Reject moves that go nowhere
            
            if x_step == 0 and y_step == 0:
                continue
            
            #Calculate the new position.
            
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)
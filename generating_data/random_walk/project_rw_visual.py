import matplotlib.pyplot as plt
from project_random_walk import RandomWalk  # type: ignore

##Make a random walk and Plot the points in the walk

rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()

##Keep making new walks, as long as the program is active.

while True:
    ##Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    ##Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()
    
    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break

##Coloring the points in the walk

while True:
    ##Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    ##Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.show()
    
    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break

##Starting and Ending points

while True:
    ##Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    ##Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    
    ##Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    plt.show()
    
    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break

##Removing the axes and Adding the plot points

while True:
    ##Make a random walk
    rw = RandomWalk(50_000)  #To increase the num_points, adding plot points
    rw.fill_walk()

    ##Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))  #To fit the plot in the screen
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    
    ##Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    ##Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break

    
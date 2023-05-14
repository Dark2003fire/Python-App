from socket import SO_PRIORITY
from turtle import width
from typing import Literal
import matplotlib.pyplot as plt
import numpy as np

x = np.array([23,45,8,79,65,58,45,78 ,48 ,95])
y = [10,20,30,40,50,60,70,80,90,100]
plt.bar(x , y, edgecolor = 'black' , color='Lightblue'  )  #This is bar chart


#plt.hist(x , y, edgecolor = 'black' , color='Lightgreen'  ) #This is Histogram

plt.scatter(x , y, edgecolor = 'black' , color='Lightyellow' , marker='o',
            label='Company' )  # this is Scatterplot

#plt.fill_between(x ,y , color="azure") # this is Area chart

#plt.plot(x , y , linewidth=2 ,color='springgreen') #This is line chart or plot also you can say 


#plt.stackplot(x, y ,color ="ivory") # this is stacked chart




plt.title("Simple Examples")
plt.xlabel("Profit")
plt.ylabel("Sales pickups")
plt.legend(loc='upper left')
plt.show()



























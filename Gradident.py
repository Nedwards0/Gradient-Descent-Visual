import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np 
import math

y_data=[]
x_data=[]
fig = plt.figure('c2') 
ax = plt.axes() 
line, = ax.plot([], [], lw=4) 
def derivative(x):#Change to function deriavitve
    x=2*x
    return(x)
def function(x):#Change to function
    x=x**2
    return(x)
error=5#any value over 1 will work
starting_point=700#Starting guess
increment=.1
last=500#This is just setting for the first loop
up_looper=starting_point*
lw_loower=0-(starting_point*3)
range=up_looper-lw_loower
point=100
increment=range/point
plot_x=[]
plot_y=[]
x=0

while (x<point):#Generating F(x)
  x=x+1
  plot_x.append(lw_loower)
  plot_y.append(function(lw_loower))
  lw_loower=lw_loower+increment
plt.plot(plot_x,plot_y,'--')
increment=starting_point*2
y_data.append(function(starting_point))
x_data.append((starting_point))
counter=0
#Graident descent
while(abs(error)>.00000005):#This is the tolerance of the function if you want absoulte change to while true
    if(abs(derivative(starting_point+increment))<abs(derivative(starting_point-increment))):
        starting_point=starting_point+increment
        error= abs(derivative(starting_point))
        last=starting_point
    
    else:
        starting_point=starting_point-increment#Steping to left
        error= last-starting_point
        last=starting_point
    y_data.append(function(starting_point))
    x_data.append((starting_point))
    if starting_point==0:
      break
    counter=counter+1
    increment=increment*(.75)#This is how step size change change it to a larger decimal 
                             #if you want smaller increment decrease.
print(starting_point)#This is the location found that is near local min
print(len(x_data))#This is the amount of steps taken for the min
# initialization function 
def init(): 
    # creating an empty plot/frame 
    line.set_data([], []) 
    return line, 
  
# lists to store x and y axis points 
xdata, ydata = [], [] 
  
# animation function 
def animate(i): 
      
    # x, y values to be plotted 
    x = x_data[i]
    y = y_data[i]
      
    # appending new points to x, y axes points list 
    xdata.append(x) 
    ydata.append(y) 
      
    # set/update the x and y axes data 
    line.set_data(xdata, ydata) 
      
    # return line object 
    return line, 
      
plt.title('Gradient Descent!') 
#Generating the   
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=int(len(y_data)), interval=1, blit=True) 
  
# save the animation as mp4 video file 
writergif=animation.PillowWriter(fps=30)
anim.save('Visual.gif', writer =animation.PillowWriter(fps=1) ) 

#plt.plot(t**3) 
plt.show() 

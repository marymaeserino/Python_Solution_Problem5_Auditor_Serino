import numpy as np
import matplotlib.pyplot as plt

n=np.arange(200) #creates array from 0 to 199
eq=input("Input equation x(n) in numpy notation: ")  #User input equation
x=eval(eq) #evaluates the user input equation with respect to n array

y=[] #creates empty list of y
for i in range (0,200): #loop ranging from 0,200
    if i==0:
        y1=-1.5*x[i]+2*x[i+1]-0.5*x[i+2] #condition if i=0. It calls out index of array x using i
        y.append(y1) #adds the value per loop in y list
    elif i>0 and i<=198:
        y2=0.5*x[i+1]-0.5*x[i-1] #condition if i is >0 and <=198. It calls out index of array x using i
        y.append(y2)    #adds the value per loop in y list
    elif i==199:
        y3=1.5*x[i]-2*x[i-1]+0.5*x[i-2] #condition if i is 199 It calls out index of array x using i
        y.append(y3)    #adds the value per loop in y list
   
plt.plot(n,x,'-r',linewidth=3,label="x(n)") #plots x(n)
plt.plot(n,y,'-k',linewidth=3,label="y(n)") #plots y(n)
plt.title('Graphs of x(n) and y(n)')
plt.xlabel('n')
plt.ylabel('x and y')
plt.grid()    
plt.legend(loc="best")
        
    
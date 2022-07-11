#Write by adolfhitlor

try:
    import matplotlib
except ModuleNotFoundError:
    import os
    os.system('pip install matplotlib')
matplotlib.use("TkAgg")
from matplotlib.pyplot import *
ax=gca()

#Setup the graph like descartes graph

#No line in top
ax.spines['top'].set_color('none')

#Set the left axis to zero value
ax.spines['left'].set_position('zero')

#No line in right
ax.spines['right'].set_color('none')

#Set the bottom axis to zero value
ax.spines['bottom'].set_position('zero')

#epsilon is created for limited calculation
epsilon=1e-7


#Set the graph size
def setsize(width=10,height=10):
    xlim(-width/2,width/2)
    ylim(-height/2,height/2)

#Set the graph to 20x20
setsize(20,20)





#!/usr/bin/env python
# coding: utf-8

# In[56]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math


# In[57]:


ARC = 0.24 #air resistance coefficient
AM = 0.1 #arrow mass
TD = 30 #target distance
g = 9.81
vt = AM*g/ARC #terminal velocity# inputs


# In[58]:


def program():
    IVM = int(input("initial velocity magnitude: "))
    IVA = int(input('initial velocity angle(above the horizontal): '))
    TS = float(input('time step: '))
    v0 = [IVM*math.cos(IVA*math.pi/180),IVM*math.sin(IVA*math.pi/180)] #[vx,vy] initial
    tf = (2*v0[1]*math.sin(IVA*math.pi/180))/g #max possible time
    xmax = (v0[1]*v0[1]*math.cos(IVA*math.pi/180))/g #max x displacement
    times = np.arange(0,tf,TS)
    print('your arrow travelled', xmax,'meters')
    if abs(xmax-TD)<=0.5:
        print('you hit the target!, you were ', abs(xmax-TD), ' meters away from the center')
    else:
        print('you missed!, you were ', abs(xmax-TD), ' meters away from the center')
    print('rerun this cell if you want to try again!')


# In[59]:


program() #run this cell to start


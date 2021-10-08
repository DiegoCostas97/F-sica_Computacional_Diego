#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:53:01 2021

@author: RAI\diego.costas
"""

import matplotlib.pyplot as plt
from scipy import integrate as sci
import numpy as np

#def ex_1(u):
#    f = np.piecewise(u, [0<= u <= 2, u > 2], [0,5])
#    return f

def f(t):
    return 2*t+4

def escalon_(t):
    if -1<= t <2:
        return 2*t+4
    if t <=2:
        return escalon_(t-3)
    if t <-1:
        return escalon_(t+3)
    
def fa1(t):
    f = escalon_(t)
    return f*np.cos(2*np.pi*t/T)

def fb1(t):
    f = escalon_(t)
    return f*np.sin(2*np.pi*t/T)


T=3
t0 = -1

#a0
sol = sci.quad(escalon_, t0, t0+T, limit=1000)
a0 = sol[0]/T

#a1
sol = sci.quad(fa1, t0, t0+T, limit=1000)
a1 = 2*sol[0]/T

#b1
sol = sci.quad(fb1, t0, t0+T, limit=1000)
b1 = 2*sol[0]/T

t = np.arange(-5, 5, 0.01)

ff = np.zeros(len(t))
for i in range(len(t)):
    ff[i]=escalon_(t[i])
    
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(t,ff,"r-")
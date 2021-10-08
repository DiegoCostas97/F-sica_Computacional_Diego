#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 20:17:08 2021

@author: RAI\diego.costas
"""

import matplotlib.pyplot as plt
import numpy as np

def escalon(u):
    f = np.piecewise(u, [u<=2, u>2], [0,5])
    return f

def escalon_(t, a):
    m = np.zeros(a)
    for i in range(a):
        if t[i]<=0:
            m[i] = 0
        else:
            m[i] = 5
    return m

t1 = -2
tf = 5

dt = 0.001
t = np.arange(t1, tf, dt)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(t, escalon(t), "-r")


 

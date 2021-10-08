#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 19:51:44 2021

@author: RAI\diego.costas
"""

import scipy.integrate as si
import numpy as np
import matplotlib.pyplot as plt

def d3x_dt3(var, t):
    x, z, k = var #z = dx/dt k = d²x/dt²
    d3x_dt3 = -np.exp(-t) -60*t*np.sin(t**2) - 40*t**3*np.cos(t**2)
    return [z, k, d3x_dt3]

z0 = -1.
k0 = 11.
x0 = 0

tempos = np.linspace(0, 10, 200)
sol = si.odeint(d3x_dt3, [x0, z0, k0], tempos)
x = sol[:,0] #IGUAL QUE x = [i[0] for i in sol]
z = sol[:,1] 
k = sol[:,2]


fig = plt.figure(figsize=(8, 10))
#plt.title("$d³x/dt³ + e^{-t} - 60t \cdot sen(t²) -40t³ \cdot cos(t²)$")

ax1 = fig.add_subplot(311)
ax1.plot(tempos, x, c="purple")
ax1.set_xlabel("t")
ax1.set_ylabel("x")
ax1.grid()


ax2 = fig.add_subplot(312)
ax2.plot(tempos, z,  c="green")
ax2.set_xlabel("t")
ax2.set_ylabel("$dx/dt$")
plt.grid()

ax3 = fig.add_subplot(313)
ax3.plot(tempos, k,  c="blue")
ax3.set_xlabel("t")
ax3.set_ylabel("$d²x/dt²$")
plt.grid()
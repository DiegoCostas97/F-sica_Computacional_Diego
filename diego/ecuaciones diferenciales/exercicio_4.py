#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 19:21:55 2021

@author: RAI\diego.costas
"""

import scipy.integrate as si
import numpy as np
import matplotlib.pyplot as plt

def sistema(var, t):
    x, y = var
    dx_dt = -0.1*x
    dy_dt = 0.1*x - 0.2*y
    return [dx_dt, dy_dt]

t_inic = 0
t_fin = 20

tiempos = np.linspace(t_inic, t_fin, 300)

x0 = 100
y0 = 0

sol = si.odeint(sistema, [x0, y0], tiempos)

x = [i[0] for i in sol]
y = [i[1] for i in sol]

fig = plt.figure(figsize=(15,6))

ax1 = fig.add_subplot(131)
ax1.plot(tiempos, x, c="purple", label="Solución de: \n $dx/dt=x - x*y - 0.1*x²$ para $0 \leq t \leq 30$")
ax1.set_xlabel("t")
ax1.set_ylabel("x")
plt.grid()
#plt.legend(loc="upper right");

ax2 = fig.add_subplot(132)
ax2.plot(tiempos, y,  c="yellow", label="Solución de: \n $dx/dt= x*y - y - 0.05*y² $ para $0 \leq t \leq 30$")
ax2.set_xlabel("t")
ax2.set_ylabel("y")
plt.grid()
#plt.legend(loc="upper right");


ax3 = fig.add_subplot(133)
ax3.plot(x, y, c="blue")
ax3.set_xlabel("x")
ax3.set_ylabel("y")
plt.grid()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 19:33:12 2021

@author: RAI\diego.costas
"""

import scipy.integrate as si
import numpy as np
import matplotlib.pyplot as plt

def d2x_dt2(var, t):
    x, z = var #z = dx/dt
    d2x_d2t = -0.6*z - 20.6*x
    return [z, d2x_d2t]

z0 = 0
x0 = 5
tempos = np.linspace(0, 10, 200)
sol = si.odeint(d2x_dt2, [x0, z0], tempos)
x = sol[:,0]
z = sol[:,1] # IGUAL QUE x = [i[0] for i in sol]


fig = plt.figure(figsize=(15,6))
plt.title("$d²x/dt² + 0.6\cdot dx/dt + 20.6x$")

ax1 = fig.add_subplot(121)
ax1.plot(tempos, x, c="purple", label="Solución de: \n $dx/dt=x - x*y - 0.1*x²$ para $0 \leq t \leq 30$")
ax1.set_xlabel("t")
ax1.set_ylabel("x")
ax1.grid()


ax2 = fig.add_subplot(122)
ax2.plot(tempos, z,  c="green", label="Solución de: \n $dx/dt= x*y - y - 0.05*y² $ para $0 \leq t \leq 30$")
ax2.set_xlabel("t")
ax2.set_ylabel("$dx/dt$")
plt.grid()



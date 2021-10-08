#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 20:02:52 2021

@author: RAI\diego.costas
"""

import scipy.integrate as si
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lorentz(var, t):
    x, y, z = var 
    dx_dt = 10*(y - x)
    dy_dt = 28*x - y -x*z
    dz_dt = x*y - (8/3)*z
    return [dx_dt, dy_dt, dz_dt]

x0 = y0 = z0 = 5.
tempos = np.linspace(0, 12, 1000)

sol = si.odeint(lorentz, [x0, y0, z0], tempos)

x = sol[:,0]
y = sol[:,1]
z = sol[:,2]


fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(221, projection='3d')

p = ax.scatter3D(x, y, z, c=z, cmap="plasma")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

fig.colorbar(p, pad=0.15)

ax1 = fig.add_subplot(222)
ax1.plot(x, y, c="orange")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")

ax2 = fig.add_subplot(223)
ax2.plot(x, z, c="purple")
ax2.set_xlabel("X")
ax2.set_ylabel("Z")

ax3 = fig.add_subplot(224)
ax3.plot(y, z, c="r")
ax3.set_xlabel("Y")
ax3.set_ylabel("Z")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:58:26 2021

@author: RAI\diego.costas
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.optimize as sco

def fund_7(v):
    x, y = v #IMPORTANTE, NON SE PODE CHAMAR AOS DOUS ARGUMENTOS Á VEZ
    z = x * np.exp(-x**2 - y**2)
    return z

def fund_7_(v):
    x, y = v #IMPORTANTE, NON SE PODE CHAMAR AOS DOUS ARGUMENTOS Á VEZ
    z = 1/(x * np.exp(-x**2 - y**2))
    return z

fig = plt.figure(figsize=(6,6))

ax = Axes3D(fig)
# ax = fig.add_subplot(111, projection="3d") OUTRO XEITO

Xmin, Xmax = -1.0, 1.0
Ymin, Ymax = -1, 1

x = np.linspace(Xmin, Xmax, 100)
y = np.linspace(Ymin, Ymax, 100)
X, Y = np.meshgrid(x, y) #MESHGRID DEVOLVE UNHA MATRIZ DE COORDENADAS A PARTIR DOS ANTERIORES DOUS VECTORES x, y

Z = fund_7([X, Y])

sol_min = sco.fmin(fund_7, (0,0))
sol_max = sco.fmin(fund_7_, (0,0))
minimo = fund_7(sol_min)
maximo = fund_7(sol_max)


#ax.plot_wireframe(X, Y, Z, color="y", rstride=3, cstride=250, label="$f(x,y)=xe^{-(x² + y²)}$")
ax.plot_surface(X, Y, Z, rstride=5, cstride=230, label="$f(x,y)=xe^{-(x² + y²)}$")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.scatter(sol_min[0], sol_min[1], fund_7(sol_min), marker=".", color="r", s=30, label="Mínimo da función")
ax.scatter(sol_max[0], sol_max[1], fund_7(sol_max), marker=".", color="b", s=30, label="Máximo da función")

ax.legend()

plt.show()


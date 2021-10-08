#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:12:35 2021

@author: RAI\diego.costas
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.optimize as sco

def fund_pizarra(v):
    x, y = v #IMPORTANTE, NON SE PODE CHAMAR AOS DOUS ARGUMENTOS Á VEZ
    z = x**3 + 3*x*y**2 - 15*x - 12*y
    return z

fig = plt.figure(figsize=(6,6))

ax = Axes3D(fig)
# ax = fig.add_subplot(111, projection="3d") OUTRO XEITO

Xmin, Xmax = 0, 5
Ymin, Ymax = 0, 5
#
x = np.linspace(Xmin, Xmax, 100)
y = np.linspace(Ymin, Ymax, 100)
X, Y = np.meshgrid(x, y) #MESHGRID DEVOLVE UNHA MATRIZ DE COORDENADAS A PARTIR DOS ANTERIORES DOUS VECTORES x, y

Z = fund_pizarra([X, Y])
#
#sol = sco.fmin(fund_pizarra, (3,3))
#minimo = fund_pizarra(sol)
#
#ax.plot_wireframe(X, Y, Z, color="y", rstride=3, cstride=250, label="$f(x,y)=x³ + 3xy²-15x-12y$")
#ax.set_xlabel("X")
#ax.set_ylabel("Y")
#ax.set_zlabel("Z")
#
#ax.scatter(sol[0], sol[1], fund_pizarra(sol), marker=".", color="k", s=40, label="Mínimo da función")
#
#plt.legend();

res = sco.minimize(fund_pizarra, (0,0), bounds=((0,5),(0,5)))
xmin = res.x[0]
ymin = res.x[1]
fmin = res.fun

ax.plot_wireframe(X, Y, Z, color="y", rstride=3, cstride=250, label="$f(x,y)=x³ + 3xy²-15x-12y$")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.scatter(xmin, ymin, fmin, marker=".", color="k", s=40, label="Mínimo da función")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:55:54 2021

@author: RAI\diego.costas
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.optimize as sco

def fund_6(v):
    x, y = v #IMPORTANTE, NON SE PODE CHAMAR AOS DOUS ARGUMENTOS Á VEZ
    z = x**2 + y**2 + 8
    return z

fig = plt.figure(figsize=(6,6))

ax = Axes3D(fig)
# ax = fig.add_subplot(111, projection="3d") OUTRO XEITO

Xmin, Xmax = -10, 10
Ymin, Ymax = -10, 10

x = np.linspace(Xmin, Xmax, 100)
y = np.linspace(Ymin, Ymax, 100)
X, Y = np.meshgrid(x, y) #MESHGRID DEVOLVE UNHA MATRIZ DE COORDENADAS A PARTIR DOS ANTERIORES DOUS VECTORES x, y

Z = fund_6([X, Y])

sol = sco.fmin(fund_6, (0,0))
minimo = fund_6(sol)

ax.plot_wireframe(X, Y, Z, color="y", rstride=3, cstride=250, label="$f(x,y)=x²+y²+8$")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.scatter(sol[0], sol[1], fund_6(sol), marker=".", color="k", label="Mínimo da función")

plt.legend();

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 20:08:39 2021

@author: RAI\diego.costas
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.optimize as sco

def fund_5(v):
    x, y = v #IMPORTANTE, NON SE PODE CHAMAR AOS DOUS ARGUMENTOS Á VEZ
    z = x**2 + y**4 + x + y
    return z

fig = plt.figure(figsize=(6,6))

ax = Axes3D(fig)
# ax = fig.add_subplot(111, projection="3d") OUTRO XEITO

Xmin, Xmax = -5.0, 5.0
Ymin, Ymax = -5, 5

x = np.linspace(Xmin, Xmax, 100)
y = np.linspace(Ymin, Ymax, 100)
X, Y = np.meshgrid(x, y) #MESHGRID DEVOLVE UNHA MATRIZ DE COORDENADAS A PARTIR DOS ANTERIORES DOUS VECTORES x, y

Z = fund_5([X, Y])

sol = sco.fmin(fund_2, (0,0))
minimo = fund_5(sol)

ax.plot_wireframe(X, Y, Z, color="y", rstride=3, cstride=250, label="$f(x,y)=x²+y⁴+x+y$")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.scatter(sol[0], sol[1], fund_5(sol), marker=".", color="k", label="Mínimo da función")

plt.legend();

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:39:57 2021

@author: RAI\diego.costas
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.optimize as sco

def fund_pizarra(v):
    x, y, z = v #IMPORTANTE, NON SE PODE CHAMAR AOS DOUS ARGUMENTOS Á VEZ
    f = x * (y**2/4*x) + z**2/y + 2/z
    return f

#fig = plt.figure(figsize=(6,6))
#
#ax = Axes3D(fig)
## ax = fig.add_subplot(111, projection="3d") OUTRO XEITO
#
#Xmin, Xmax = 0, 5
#Ymin, Ymax = 0, 5
#Zmin, Zmax = 0, 5
#
#x = np.linspace(Xmin, Xmax, 100)
#y = np.linspace(Ymin, Ymax, 100)
#y = np.linspace(Zmin, Zmax, 100)
#X, Y, Z = np.meshgrid(x, y, z) #MESHGRID DEVOLVE UNHA MATRIZ DE COORDENADAS A PARTIR DOS ANTERIORES DOUS VECTORES x, y
#
#Z = fund_pizarra([X, Y])

res = sco.minimize(fund_pizarra, (1,2,3), bounds=((0,10),(0,10), (0, 10)))
xmin = res.x[0]
ymin = res.x[1]
zmin = res.x[2]
fmin = res.fun

#ax.plot_wireframe(X, Y, Z, color="y", rstride=3, cstride=250, label="$f(x,y)=x³ + 3xy²-15x-12y$")
#ax.set_xlabel("X")
#ax.set_ylabel("Y")
#ax.set_zlabel("Z")
#
#ax.scatter(xmin, ymin, fmin, marker=".", color="k", s=40, label="Mínimo da función")
#
#plt.legend()
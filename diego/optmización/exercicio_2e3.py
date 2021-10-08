#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 19:17:33 2021

@author: RAI\diego.costas
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco


def curva(x):
    y = - np.sin(x)/x - 5    
    return y


def minimo(a, b):
    for (i,j) in zip(a, b):
        if j == np.min(minimos):
            return round(i), round(j)
        
        

sols = np.zeros(5)
estimacions = np.linspace(-15, 15, 5)

for i in range(5):
    sols[i] = sco.fmin(curva, estimacions[i])

minimos = curva(sols)
print("Os mínimos da función son: ", minimos)
print("")

minimo_global = minimo(sols, minimos)
print("O mínimo global da función está en: ", minimo_global)

x1 = np.linspace(-15, 15, 200)
plt.plot(x1, curva(x1))
plt.scatter(sols, curva(sols))

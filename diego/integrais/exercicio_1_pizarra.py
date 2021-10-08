#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 20:02:20 2021

@author: RAI\diego.costas
"""

from scipy import integrate
import numpy as np

#%%
def f(x):
    if x<0:
        return 0.0
    else:
        return 1.0
    
sol = integrate.quad(f, 0, 6)

integ, err = sol

print("integral:\n", integ)
print("err:\n", err, "\n")

print("solución exacta: {}".format(8))
#%%

x2 = lambda x: x**2

sol = integrate.quad(x2, 0, 4)
integ, err = sol

print("integral:\n", integ)
print("err:\n", err, "\n")
#%%

x3 = lambda x: np.exp(x)

sol = integrate.quad(x3, 0, np.inf)
integ, err = sol

print("integral:\n", integ)
print("err:\n", err, "\n")
#%%
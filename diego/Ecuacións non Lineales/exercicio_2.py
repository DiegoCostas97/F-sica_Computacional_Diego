#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 19:33:36 2021

@author: RAI\diego.costas
"""

import numpy as np
import scipy.optimize as sco
import matplotlib.pyplot as plt

#def func(m, T):
#    f1 = m - np.tanh(m/T)
#    return f1
#
#T = np.linspace(1e-6,2,50)
#
#m = [0]*len(T)
#    
#for i in range(len(T)):
#    m[i] = sco.fsolve(func, 0.5, args=(T[i]))
#
#
#plt.plot(T, m)

def ffnolineal(x):
    x1, x2 = x
    f1 = 1.4*x1 - x2 - 0.6
    f2 = x1**2 -1.6*x1 -x2 - 4.6
    
    return [f1, f2]

x1, x2 = sco.fsolve(ffnolineal, [-1, -2.])
sol1 = sco.fsolve(ffnolineal, [-2., -5.])
sol2 = sco.fsolve(ffnolineal, [2., 5.])



x1 = np.linspace(-10, 10, 50)
plt.plot(x1, 1.4*x1 - 0.6)
plt.plot(x1, x1**2 -1.6*x1 - 4.6)






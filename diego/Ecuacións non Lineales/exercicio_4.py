#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 19:03:03 2021

@author: RAI\diego.costas
"""

import numpy as np
import scipy.optimize as sco
import matplotlib.pyplot as plt

def f_nolineal(x):
    x1, x2 = x
    f1 = 1.2*x1**3 - x1**2 + x2
    f2 = 3*x1 + x2 -1 
    
    return [f1, f2]

sol1 = sco.fsolve(f_nolineal, [-2., -1.])
sol2 = sco.fsolve(f_nolineal, [0., 0.6])
sol3 = sco.fsolve(f_nolineal, [1.8, 2.2])

#
#
x1 = np.linspace(-4, 4, 50)
plt.plot(x1, x1**2 - 1.2*x1**3)
plt.plot(x1, 1 - 3*x1)
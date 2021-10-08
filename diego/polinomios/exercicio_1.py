#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 19:13:28 2021

@author: RAI\diego.costas
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco

def polinomio(x):
    y = x**5 - 11*x + 49*x**3 - 121*x**2 + 178*x - 120
    
    return y

x = np.linspace(-10, 10, 50)
plt.plot(x, x**5 - 11*x + 49*x**3 - 121*x**2 + 178*x - 120)
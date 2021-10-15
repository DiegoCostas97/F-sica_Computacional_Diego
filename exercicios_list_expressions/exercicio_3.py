#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 19:33:20 2021

@author: RAI\diego.costas
"""


import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt

# 3. Generate random $n$ 2D $(x, y)$ points in a $[-L, L]$ square. Order them respect the $y$ coordinate. 
#  
#     a) Reorder them with the distance to $(L, L)$ vertex. 

x = np.random.uniform(-5, 5, 1000)
y = np.random.uniform(-5, 5, 1000)

plt.scatter(x, y)

# A distancia con respecto ao eixo y é simplemente x

def dis2(x, x0 = 0.):
    """ return the absolute distance of x with respect x0
    """
    return abs(x-x0)

aa = sorted(list(zip(x,y)), key=dis2)

    
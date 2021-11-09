#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 21:32:55 2021

@author: diegocostasrodriguez
"""

import numpy as np
import matplotlib.pyplot as plt
import random

x = np.linspace(0, 1, 100)
plt.plot(x, x, linestyle="-.", c="k")

rd = np.random.uniform(0, 1, 10000)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

rd = np.random.uniform(0, 1, 50000)
coordinates = list(chunks(rd, 2))

above = [i for i in coordinates if i[1] >= i[0]]
below = [i for i in coordinates if i[1] < i[0]]

rd_x_above = [i[0] for i in above]
rd_y_above = [i[1] for i in above] 

rd_x_below = [i[0] for i in below]
rd_y_below = [i[1] for i in below] 
        
plt.scatter(rd_x_above, rd_y_above, c="mediumseagreen", s=3, alpha=0.2)
plt.scatter(rd_x_below, rd_y_below, c="orange", s=3, alpha=0.2)

solution = 1*(1-0)*len(below)/len(coordinates)


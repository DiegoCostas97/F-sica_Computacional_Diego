#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 21:32:55 2021

@author: diegocostasrodriguez
"""

import numpy as np
import matplotlib.pyplot as plt
import random

fig = plt.figure(figsize=(15,6))
ax1 = fig.add_subplot(121)

x = np.linspace(0, 1, 100)
ax1.plot(x, x, linestyle="-.", c="k", label="$f(x) = x$")

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
        
ax1.scatter(rd_x_above, rd_y_above, c="mediumseagreen", s=3, alpha=0.2)
ax1.scatter(rd_x_below, rd_y_below, c="orange", s=3, alpha=0.2, label="Area solution")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
leg = plt.legend(loc="upper right")
for lh in leg.legendHandles: 
    lh.set_alpha(1)

solution = 1*(1-0)*len(below)/len(coordinates)
print(solution)


ax2 = fig.add_subplot(122)

x = np.linspace(0, 1, 100)
ax2.plot(x, x**2, linestyle="-.", c="k", label="$f(x)=x^2$")

rd = np.random.uniform(0, 1, 10000)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

rd = np.random.uniform(0, 1, 50000)
coordinates = list(chunks(rd, 2))

above = [i for i in coordinates if i[1] >= i[0]**2]
below = [i for i in coordinates if i[1] < i[0]**2]

rd_x_above = [i[0] for i in above]
rd_y_above = [i[1] for i in above] 

rd_x_below = [i[0] for i in below]
rd_y_below = [i[1] for i in below] 
        
ax2.scatter(rd_x_above, rd_y_above, c="mediumorchid", s=3, alpha=0.2)
ax2.scatter(rd_x_below, rd_y_below, c="tomato", s=3, alpha=0.2, label="Area solution")
leg2 = plt.legend(loc="upper right")
for lh in leg2.legendHandles: 
    lh.set_alpha(1)

solution = 1*(1-0)*len(below)/len(coordinates)

print(solution)


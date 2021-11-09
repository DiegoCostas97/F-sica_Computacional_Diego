#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 19:45:09 2021

@author: USC\diego.costas.rodrigu
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import scipy.optimize as sco
import itertools as it
import math


def LCG(a, c, m, seed, size): 
    x = seed
    output = []
    
    for i in range(size):
        x = (a*x + c)%m
        output.append(x)
    
    normalized_output = [i/float(m) for i in output]
    
    return [output, normalized_output]

#GEN6
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        
rn, nrn = LCG(16807, 0, 21474, 10, 2700) # m lower than usual in order to be able to see the periodicity

coordinates = list(chunks(nrn, 3))

X = [i[0] for i in coordinates]
Y = [i[1] for i in coordinates]
Z = [i[2] for i in coordinates]

fig = plt.figure()

ax = fig.add_subplot(111, projection="3d")

ax.scatter3D(X, Y, Z, color="lightseagreen", alpha=.7)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Marsaglia Planes")


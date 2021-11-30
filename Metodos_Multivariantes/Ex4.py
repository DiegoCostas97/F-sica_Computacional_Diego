#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 19:01:29 2021

@author: USC\diego.costas.rodrigu
"""

import numpy as np
import matplotlib.pyplot as plt
import random as rd
import pandas as pd

df = pd.read_csv("test_cluster_1000.dat", delim_whitespace=True, header=None)
variables = [df[i] for i in range(2)]
events = [[i, j] for (i, j) in zip(variables[0], variables[1])]

# Build the matrix of distances.
d = [[np.sqrt((i[0] - j[0])**2 + (i[1] - j[1])**2) for j in events] for i in events]
d = np.reshape(d, (1000, 1000))

plt.scatter([i[0] for i in events], [i[1] for i in events])

mins = [np.min([j for j in i if j != 0]) for i in d]

min_events = [list(d[i]).index(mins[i]) for i in range(len(d))] # Closest event to event i (row)
    
mask = [np]
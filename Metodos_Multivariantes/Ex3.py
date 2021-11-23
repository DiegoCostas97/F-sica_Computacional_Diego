#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 19:45:58 2021

@author: USC\diego.costas.rodrigu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rd

df = pd.read_csv("test_cluster_1000.dat", delim_whitespace=True, header=None)

variables = [df[i] for i in range(2)]
coordinates = [[i, j] for (i, j) in zip(variables[0], variables[1])]
r_centers = [rd.choice(coordinates) for i in range(5)]

plt.scatter(variables[0], variables[1], alpha=0.5)
plt.scatter([i[0] for i in r_centers], [i[1] for i in r_centers], c="orange", alpha=1)

for i in coordinates:
    if np.sqrt()
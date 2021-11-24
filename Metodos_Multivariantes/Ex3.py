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

def chunks(lst, n):
    """
        Yield successive n-sized chunks from lst.
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

df = pd.read_csv("test_cluster_1000.dat", delim_whitespace=True, header=None)

variables = [df[i] for i in range(2)]
coordinates = [[i, j] for (i, j) in zip(variables[0], variables[1])]
r_centers = [rd.choice(coordinates) for i in range(5)]

fig1 = plt.figure(figsize=(12,6))
plt.scatter(variables[0], variables[1], alpha=0.5)
plt.scatter([i[0] for i in r_centers], [i[1] for i in r_centers], c="orange", alpha=1)

d_c = [np.sqrt(i[0]**2 + j[0]**2) for j in r_centers for i in coordinates]
d_c = list(chunks(d_c, 1000))  
    
Ds = [[np.sqrt((i[0] - j[0])**2 + (i[1] - j[1])**2) for j in r_centers] for i in coordinates] # Distancias de cada punto
                                                                                              # a cada centro.
C1 = [coordinates[i] for i in range(len(Ds)) if min(Ds[i]) == Ds[i][0]] # Cluster 1
C2 = [coordinates[i] for i in range(len(Ds)) if min(Ds[i]) == Ds[i][1]] # Cluster 2
C3 = [coordinates[i] for i in range(len(Ds)) if min(Ds[i]) == Ds[i][2]] # Cluster 3
C4 = [coordinates[i] for i in range(len(Ds)) if min(Ds[i]) == Ds[i][3]] # Cluster 4
C5 = [coordinates[i] for i in range(len(Ds)) if min(Ds[i]) == Ds[i][4]] # Cluster 5

clusters = C1 + C2 + C3 + C4 + C5

fig2 = plt.figure(figsize=(12,6)) 
plt.scatter([i[0] for i in C1], [i[1] for i in C1], c="lightblue", alpha=0.7, label="Cluster 1")
plt.scatter([i[0] for i in C2], [i[1] for i in C2], c="lightseagreen", alpha=0.7, label="Cluster 2")
plt.scatter([i[0] for i in C3], [i[1] for i in C3], c="khaki", alpha=0.7, label="Cluster 3")
plt.scatter([i[0] for i in C4], [i[1] for i in C4], c="lightcoral", alpha=0.7, label="Cluster 4")
plt.scatter([i[0] for i in C5], [i[1] for i in C5], c="plum", alpha=0.7, label="Cluster 5")
plt.scatter([i[0] for i in r_centers], [i[1] for i in r_centers], c="k", s=3, alpha=1, label="Centers")

plt.legend();

def gravity_center(cluster):
    x = 0
    y = 0
    for i in cluster:
        x += i[0]
        y += i[1]
    
    x = x/len(cluster)
    y = y/len(cluster)
    
    gravity_center = [x, y]
    
    return gravity_center

gravity_centers = [gravity_center(C1), gravity_center(C2), gravity_center(C3), gravity_center(C4), gravity_center(C5)]

# gc1 = rd.choice(C1)
# gc2 = rd.choice(C2)
# gc3 = rd.choice(C3)
# gc4 = rd.choice(C4)
# gc5 = rd.choice(C5)
# gravity_centers = [gc1, gc2, gc3, gc4, gc5]

Ds_2 = [[np.sqrt((i[0] - j[0])**2 + (i[1] - j[1])**2) for j in gravity_centers] for i in clusters]

nC1 = [clusters[i] for i in range(len(Ds_2)) if min(Ds_2[i]) == Ds_2[i][0]]
nC2 = [clusters[i] for i in range(len(Ds_2)) if min(Ds_2[i]) == Ds_2[i][1]]
nC3 = [clusters[i] for i in range(len(Ds_2)) if min(Ds_2[i]) == Ds_2[i][2]]
nC4 = [clusters[i] for i in range(len(Ds_2)) if min(Ds_2[i]) == Ds_2[i][3]]
nC5 = [clusters[i] for i in range(len(Ds_2)) if min(Ds_2[i]) == Ds_2[i][4]]

fig3 = plt.figure(figsize=(12,6)) 
plt.scatter([i[0] for i in nC1], [i[1] for i in nC1], c="lightblue", alpha=0.7, label="Cluster 1")
plt.scatter([i[0] for i in nC2], [i[1] for i in nC2], c="lightseagreen", alpha=0.7, label="Cluster 2")
plt.scatter([i[0] for i in nC3], [i[1] for i in nC3], c="khaki", alpha=0.7, label="Cluster 3")
plt.scatter([i[0] for i in nC4], [i[1] for i in nC4], c="lightcoral", alpha=0.7, label="Cluster 4")
plt.scatter([i[0] for i in nC5], [i[1] for i in nC5], c="plum", alpha=0.7, label="Cluster 5")
plt.scatter([i[0] for i in gravity_centers], [i[1] for i in gravity_centers], c="k", s=3, alpha=1, label="gravity centers")











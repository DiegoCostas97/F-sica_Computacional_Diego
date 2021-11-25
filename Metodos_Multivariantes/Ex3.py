#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 18:45:10 2021

@author: USC\diego.costas.rodrigu
"""
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import pandas as pd

        
def gravity_center(cluster : list):
    """
        Computes the gravity centers as arithmetic mean of the points.
    """
    x = 0
    y = 0
    for i in cluster:
        x += i[0]
        y += i[1]
    
    x = x/len(cluster)
    y = y/len(cluster)
    
    gravity_center = [x, y]
    
    return gravity_center

def cluster(clusters        : list,
            gravity_centers : list):
    """
        Returns the new clusters when a set of older clusters and their gravity centers are given as input.
    """
    Ds_n = [[np.sqrt((clusters[i][k][0] - j[0])**2 + (clusters[i][k][1] - j[1])**2) for j in gravity_centers] for i in range(len(clusters)) for k in range(len(clusters[i]))]
    
    aa = clusters[0] + clusters[1] + clusters[2] + clusters[3] + clusters[4]
    
    C1 = [aa[i] for i in range(len(Ds_n)) if min(Ds_n[i]) == Ds_n[i][0]]
    C2 = [aa[i] for i in range(len(Ds_n)) if min(Ds_n[i]) == Ds_n[i][1]]
    C3 = [aa[i] for i in range(len(Ds_n)) if min(Ds_n[i]) == Ds_n[i][2]]
    C4 = [aa[i] for i in range(len(Ds_n)) if min(Ds_n[i]) == Ds_n[i][3]]
    C5 = [aa[i] for i in range(len(Ds_n)) if min(Ds_n[i]) == Ds_n[i][4]]
    
    return [C1, C2, C3, C4, C5]

df = pd.read_csv("test_cluster_1000.dat", delim_whitespace=True, header=None)

variables = [df[i] for i in range(2)]
coordinates = [[i, j] for (i, j) in zip(variables[0], variables[1])]
r_centers = [rd.choice(coordinates) for i in range(5)]

Ds_0 = [[np.sqrt((i[0] - j[0])**2 + (i[1] - j[1])**2) for j in r_centers] for i in coordinates] 

C1 = [coordinates[i] for i in range(len(Ds_0)) if min(Ds_0[i]) == Ds_0[i][0]] 
C2 = [coordinates[i] for i in range(len(Ds_0)) if min(Ds_0[i]) == Ds_0[i][1]] 
C3 = [coordinates[i] for i in range(len(Ds_0)) if min(Ds_0[i]) == Ds_0[i][2]] 
C4 = [coordinates[i] for i in range(len(Ds_0)) if min(Ds_0[i]) == Ds_0[i][3]] 
C5 = [coordinates[i] for i in range(len(Ds_0)) if min(Ds_0[i]) == Ds_0[i][4]]

clusters = [C1, C2, C3, C4, C5]
gravity_centers = [gravity_center(i) for i in clusters]

count = 0
while gravity_centers != r_centers:
    
    Cs = cluster(clusters, gravity_centers)
    r_centers = gravity_centers
    gravity_centers = [gravity_center(i) for i in Cs]
    count += 1

print("The k-means algorithm needed {} iterations to converge".format(count))
fig = plt.figure(figsize=(12,6)) 
plt.scatter([i[0] for i in Cs[0]], [i[1] for i in Cs[0]], c="lightblue", alpha=0.7, label="Cluster 1")
plt.scatter([i[0] for i in Cs[1]], [i[1] for i in Cs[1]], c="lightseagreen", alpha=0.7, label="Cluster 2")
plt.scatter([i[0] for i in Cs[2]], [i[1] for i in Cs[2]], c="khaki", alpha=0.7, label="Cluster 3")
plt.scatter([i[0] for i in Cs[3]], [i[1] for i in Cs[3]], c="lightcoral", alpha=0.7, label="Cluster 4")
plt.scatter([i[0] for i in Cs[4]], [i[1] for i in Cs[4]], c="plum", alpha=0.7, label="Cluster 5")
# plt.scatter([i[0] for i in gravity_centers], [i[1] for i in gravity_centers], c="k", s=3, alpha=1, label="gravity centers")
plt.legend()
        
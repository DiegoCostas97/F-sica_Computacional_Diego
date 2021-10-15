#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:17:01 2021

@author: RAI\diego.costas
"""
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt

x = st.norm.rvs(loc=0, size=1000)
y = st.norm.rvs(loc=0, size=1000)

plt.scatter(x, y)

# a) COMPUTE THE DISTANCE OF THE POINTS RESPECT TO THE ORIGIN:

def distance(lst1, lst2):
    d = []
    for (i,j) in zip(lst1, lst2):
        d.append(np.sqrt(i**2 + j**2))
        
    return d

dd = [np.sqrt(i**2 + j**2) for i in x for j in y]
d = distance(x, y)

# b) order the points by distance to the origin.
       
ordered_distances = sorted(d, reverse=True) #Lista de valores ordeados de maior a menor distancia á orixe

# c) select those points at a distance greater than 1 respect the origin and that they are in the first quadrant.

def distance_greater_than_one_in_first_quadrat(lst1, lst2):
    d = []
    for (i,j) in zip(lst1, lst2):
        if i > 0 and j > 0:
            d.append(np.sqrt(i**2 + j**2))
    distance_g1 = [i for i in d if i >1 if i > 1]
            
    return distance_g1

gt1ifq = distance_greater_than_one_in_first_quadrat(x, y)

def test_function(function, lst1, lst2):
    assert function(lst1, lst2) == function(lst2, lst1)
    gt1 = [i > 1 for i in function(lst1, lst2)]
    assert all(gt1)
        
    return True

try:
    test_function(distance_greater_than_one_in_first_quadrat, x, y)
    print("test passed")
except:
    print("test failed")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 19:07:27 2021

@author: USC\diego.costas.rodrigu
"""

import numpy as np
import matplotlib.pyplot as plt

# Read the data.
data = np.loadtxt("test1.dat")

# Compute the mean & sigma for every column.
def mean(lst   : list, 
         power : int):
    """
        Calculates the mean of a list of values.
    """
    
    data = [i**power for i in lst]
    sum_ = 0 
    
    for j in data:
        sum_ += j
    
    mean_ = 1/len(data)*sum_
    
    return mean_

def sigma(lst : list):
    """
        Calculates the sigma of a list of values.
    """
    data = lst
    sigma_s = mean(data, 2) - mean(data, 1)**2
    
    return np.sqrt(sigma_s)

means = [mean([i[j] for i in data], 1) for j in range(len(data[0]))]
s_devs = [sigma([i[j] for i in data]) for j in range(len(data[0]))]

# Compute the correlation matrix.
def mean_xx_(lst1 : list,
            lst2 : list):
    
    mean_xx = [mean([i*j for i,j in zip(lst1, lst2)], 1)] 
    
    return mean_xx

variables = [[i[j] for i in data] for j in range(len(data[0]))]

correlations_coefficients = [((mean_xx_(variables[i], variables[j]) - means[i]*means[j])/(s_devs[i]*s_devs[j])) for i in range(len(variables)) for j in range(len(variables))]
correlation_matrix = np.reshape(correlations_coefficients, (5,5))


print("The correlation matrix is: ")
print(" ")
print(correlation_matrix)
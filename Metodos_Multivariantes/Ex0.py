#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 19:19:07 2021

@author: USC\diego.costas.rodrigu
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# # Read the data.
# def read_data(file : str):
#     """
#         Reads a .dat file into a x and y lists to work with
#     """
    
#     data = np.loadtxt(file)
#     x = [i[0] for i in data]
#     y = [i[1] for i in data]
    
#     return x, y

# x, y = read_data("test0.dat")

# # Evaluate mean, sigma and correlation coefficient.
# def mean(lst   : list, 
#          power : int):
#     """
#         Calculates the mean of a list of values.
#     """
    
#     data = [i**power for i in lst]
#     sum_ = 0 
    
#     for j in data:
#         sum_ += j
    
#     mean_ = 1/len(data)*sum_
    
#     return mean_

# def sigma(lst : list):
#     """
#         Calculates the sigma of a list of values.
#     """
#     data = lst
#     sigma_s = mean(data, 2) - mean(data, 1)**2
    
#     return np.sqrt(sigma_s)

# mean_x = mean(x, 1)
# mean_y = mean(y, 1)

# sigma_x = sigma(x)
# sigma_y = sigma(y)

# mean_xy = mean([i*j for i,j in zip(x,y)], 1)

# correlation_coefficient = (mean_xy - mean_x*mean_y)/(sigma_x*sigma_y)

# # Print the results nicely:

# print("--------------------------------------------------")
# print("| The mean of the x value is: {:.2f}                 |".format(mean_x))
# print("| The mean of the y value is: {:.2f}               |".format(mean_y))
# print("|                                                  |")
# print("| The sigma of the x value is: {:.2f}                |".format(sigma_x))
# print("| The mean of the y value is: {:.2f}                 |".format(sigma_y))
# print("|                                                  |")
# print("| The correlation coefficient of the data is {:.2f}  |".format(correlation_coefficient))
# print("--------------------------------------------------")

def abracadabra(file_name : str):
    
    def read_data(file : str):
        """
            Reads a .dat file into a x and y lists to work with
        """
        
        data = np.loadtxt(file)
        x = [i[0] for i in data]
        y = [i[1] for i in data]
        
        return x, y

    x, y = read_data("test0.dat")

    # Evaluate mean, sigma and correlation coefficient.
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

    mean_x = mean(x, 1)
    mean_y = mean(y, 1)

    sigma_x = sigma(x)
    sigma_y = sigma(y)

    mean_xy = mean([i*j for i,j in zip(x,y)], 1)

    correlation_coefficient = (mean_xy - mean_x*mean_y)/(sigma_x*sigma_y)

    # Print the results nicely:

    print("--------------------------------------------------")
    print("| The mean of the x value is: {:.2f}                 |".format(mean_x))
    print("| The mean of the y value is: {:.2f}               |".format(mean_y))
    print("|                                                  |")
    print("| The sigma of the x value is: {:.2f}                |".format(sigma_x))
    print("| The mean of the y value is: {:.2f}                 |".format(sigma_y))
    print("|                                                  |")
    print("| The correlation coefficient of the data is {:.2f}  |".format(correlation_coefficient))
    print("--------------------------------------------------")
    
    y_ML = mean_y + correlation_coefficient*sigma_y/sigma_x*(x - mean_x)
    x_ML = mean_x + correlation_coefficient*sigma_x/sigma_y*(y - mean_y)
    
    plt.scatter(x, y, s=4, alpha=0.5, c="lightblue")
    plt.plot(x, y_ML, linestyle="-.", c="red", linewidth=0.5)
    plt.plot(x_ML, y, linestyle="-.", c="green", linewidth=0.5)
    
    return [y_ML, x_ML]


y_ML, x_ML = abracadabra("test0.dat")





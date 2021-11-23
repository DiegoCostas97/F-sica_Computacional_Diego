#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 19:04:49 2021

@author: USC\diego.costas.rodrigu
"""

import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
import matplotlib.pyplot as plt

def mean(lst   : list, 
          power=1):
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

def chunks(lst, n):
    """
        Yield successive n-sized chunks from lst.
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

df = pd.read_csv("test_temperature.dat", delim_whitespace=True, header=None)
df = df.drop([0, 13, 14, 15, 16, 17], axis=1)

normalized_df = df
for col in normalized_df.columns:
    normalized_df[col].values[:] = (normalized_df[col].values[:] - 
                                    mean(normalized_df[col].values[:]))/sigma(normalized_df[col].values[:])

variables = [df.loc[:,i] for i in df.columns]
normalized_variables = [(i - mean(i))/sigma(i) for i in variables]

events = [rows for index, rows in normalized_df.iterrows()]
events = list(chunks(np.hstack(events), 12))

# events_2 = [((rows - mean(rows))/sigma(rows)) for index, rows in df.iterrows()]
# events_2 = list(chunks(np.hstack(events_2), 12))

# Evaluates the PCA: Evaluates the eigenvalues, sorts them and choose the two largest eigenvalues.
covariance = [mean((i - mean(i))*(j - mean(j))) for i in normalized_variables for j in normalized_variables]
covariance_matrix = np.reshape(covariance, (12, 12))

eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

index_eig = [(i,v) for i,v in enumerate(eigenvalues)]
two_biggest_eigenvalues_with_index = sorted(index_eig, key=lambda x: x[1], reverse=True)[:2]
corresponding_eigenvectors = [eigenvectors.T[i[0]] for i in two_biggest_eigenvalues_with_index[0:][0:]]


#  Projects every event onto the subspace of the two eigenvectors
Us = list(chunks([np.dot(i, events[j]) for i in corresponding_eigenvectors for j in range(len(events))], 35))

# Projects every variable onto the subspace.
variable_projections = [sum(variables[k]*i) for i in Us for k in range(len(variables))]

z_1_m = [Us[0]*i for i in variables]
z_2_m = [Us[1]*i for i in variables]


plt.scatter(Us[0], Us[1])
plt.xlabel("Coordinate 1")
plt.ylabel("Coordinate 2")















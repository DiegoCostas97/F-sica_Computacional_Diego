#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:10:38 2021

@author: USC\diego.costas.rodrigu
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


population_1 = pd.read_csv("train_fisher_A.dat", delim_whitespace=True, header=None).drop(columns=[0])
population_2 = pd.read_csv("train_fisher_B.dat", delim_whitespace=True, header=None).drop(columns=[0])

test_A = pd.read_csv("test_fisher_A.dat", delim_whitespace=True, header=None).drop(columns=[0])
test_B = pd.read_csv("test_fisher_B.dat", delim_whitespace=True, header=None).drop(columns=[0])

def computew(traindataset1, traindataset2):
    """
        Computes the w coefficient for the training dataset and the F points in order to 
        apply it to the test set and decide a doog cut-off respectively.
    """
    
    variables_p1 = [population_1[col].values for col in population_1]
    variables_p2 = [population_2[col].values for col in population_2]
    
    covariance_matrix_p1 = np.cov(variables_p1)
    # covariance_matrix_p2 = np.cov(variables_p2)
    
    V_p1 = np.linalg.inv(covariance_matrix_p1)
    # V_p2 = np.linalg.inv(covariance_matrix_p2)
    
    means_p1 = [np.mean(i) for i in variables_p1]
    means_p2 = [np.mean(i) for i in variables_p2]
    
    # w computation. We are ssuming both covariance matrix are equal.
    w = np.dot(V_p1, [i - j for (i,j) in zip(means_p1, means_p2)])
    # F1 = np.dot(w, means_p1)
    # F2 = np.dot(w, means_p2)
    
    F_p1 = [np.dot(w, list(population_1.loc[i])) for i in range(len(population_1))]
    F_p2 = [np.dot(w, list(population_2.loc[i])) for i in range(len(population_2))] 
    
    return w, F_p1, F_p2

w, F_p1, F_p2 = computew(population_1, population_2)

# Plots the traning datasets ir onrder to select a adecuate cut-off
fig1 = plt.figure()
counts1, bins1, _1 = plt.hist(F_p1, color="khaki", alpha=0.6, bins=int(np.sqrt(len(F_p1))), label="Population 1")
counts2, bins2, _2 = plt.hist(F_p2, color="mediumturquoise", alpha=0.6, bins=int(np.sqrt(len(F_p2))), label="Population 2")
plt.legend()
plt.pause(1)

# Filter the new dataset with the discriminant computated for the training dataset
F_testA = [np.dot(w, list(test_A.loc[i])) for i in range(len(test_A))]
F_testB = [np.dot(w, list(test_B.loc[i])) for i in range(len(test_B))]

fig2 = plt.figure()
countsA, binsA, _A = plt.hist(F_testA, color="khaki", alpha=0.6, bins=int(np.sqrt(len(F_testA))), label="Test A")
countsB, binsB, _B = plt.hist(F_testB, color="mediumturquoise", alpha=0.6, bins=int(np.sqrt(len(F_testB))), label="Test B")

max_A = np.max(countsA)
max_B = np.max(countsB)
maxxx = np.max([max_A, max_B])
cut = float(input("Set the cut-off: ")) # Asks for cut-off
plt.vlines(cut, 0, maxxx, linestyle="--", color="k", alpha=0.6)
plt.legend()

# Build the confusion matrix
real_A = np.sum([i for (i, j) in zip(countsA, binsA) if j > cut]) 
fake_A = np.sum([i for (i, j) in zip(countsA, binsA) if j < cut])
 
real_B = np.sum([i for (i, j) in zip(countsB, binsB) if j < cut])
fake_B = np.sum([i for (i, j) in zip(countsB, binsB) if j > cut])

confussion = ["            ", "r = 1", "r = 2", "Population 1", real_A, fake_A, "Population 2 ", fake_B,  real_B]
confussion_matrix = np.reshape(confussion, (3,3))

# Compute the metrics
accuracy = (real_A + real_A)/(len(test_A) + len(test_B))
specificity = real_A/(real_A + fake_A)
sensitivity = real_B/(real_B + fake_B)
prevalence = (real_B + fake_B)/(len(test_A) + len(test_B))

print("The confusion matrix is: ")
print(confussion_matrix)
print(" ")
print("The metrics that sum up the information we have are: ")
print("Accuracy: ", accuracy)
print("Specificity: ", specificity)
print("Sensitivity: ", sensitivity)
print("Prevalence: ", prevalence)
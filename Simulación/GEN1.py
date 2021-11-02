#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 19:14:49 2021

@author: USC\diego.costas.rodrigu
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import scipy.optimize as sco
import itertools as it


# GEN1
def LCG(a, c, m, seed, size):
    x = seed
    output = []
    
    for i in range(size):
        x = (a*x + c)%m
        output.append(x)
    
    normalized_output = [i/float(m) for i in output]
    
    return [output, normalized_output]


# GEN2
rn, nrn = LCG(16807, 0, 2147483647, 10, 100000)

fig = plt.figure(figsize=(15,10))

ax1 = fig.add_subplot(221)
counts, bins, patches = ax1.hist(nrn, bins=int(np.sqrt(len(rn))), histtype="stepfilled", color="gold", alpha=0.5)
ax1.set_xlabel("Normalized Random Numbers (NRN)")
ax1.set_ylabel("Counts/bin")

homogen = [i - int(np.sqrt(len(rn))) for i in counts] 
ax2 = fig.add_subplot(222)

counts2, bins2, patches2 = ax2.hist(homogen, bins=int(np.sqrt(len(homogen))), histtype="step")
bins_centers = 0.5*(bins2[1:] + bins2[:-1])
ax2.scatter(bins_centers, counts2)

# def poisson(k, lamb):
#     return ss.poisson.pmf(k, lamb)
#
# params, pcov = sco.curve_fit(poisson, bins_centers, counts2)
# ax2.plot(bins_centers, poisson(bins_centers, *params))

ax2.set_xlabel("Poisson Distribution for NRN")
ax2.set_ylabel("Counts/bin")

# GEN3
distances = []

for i in range(len(rn))[::2]:
    distances.append((nrn[i] - nrn[i+1])**2)
 
ax3 = fig.add_subplot(223)
n, x, _ = ax3.hist(distances, bins=80, histtype="stepfilled", color="green", alpha=0.5)
bins_centers = 0.5*(x[1:]+x[:-1])
#ax3.plot(bins_centers, n)
ax3.set_xlabel("distance²")
ax3.set_ylabel("Counts/bin")

#GEN4
def GEN4(numbers): 
    possible_configurations = list(it.permutations([0, 1, 2, 3]))
    counting = np.zeros(24)

    for four_list in numbers:
        for index, configuration in enumerate(possible_configurations):
            if list(configuration) == list(np.argsort(four_list)):
                counting[index] += 1

    return counting

four_listed = []

for i in rn:
    
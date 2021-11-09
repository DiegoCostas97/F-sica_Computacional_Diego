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
import math


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
ax1.hlines(int(np.sqrt(len(rn))), 0, 1, linestyle="-.", color="k")
homogen = [i - np.mean(counts) for i in counts] 

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
ax3.set_xlabel("Distribución de Homoxeneidade")
ax3.set_ylabel("Counts/bin")

#GEN4
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def GEN4(numbers): 
    possible_configurations = list(it.permutations([0, 1, 2, 3]))
    counting = np.zeros(24)

    for four_list in numbers:
        if len(four_list) == 4:
            for index, configuration in enumerate(possible_configurations):
                if list(configuration) == list(np.argsort(four_list)):
                    counting[index] += 1
        else:
            break
    return counting


numbers = list(chunks(nrn, 4))
hist_data = GEN4(numbers)

ax4 = fig.add_subplot(224)

x = np.arange(1, 25, 1)
ax4.bar(x, hist_data)
ax4.hlines(np.mean(hist_data), 0.6, 24.4, color="k", linestyle="-.")
ax4.set_xlabel("Possible Combinations")
ax4.set_ylabel("Counts/combination")
ax4.set_xticks(np.arange(1,25,1))

fig2 = plt.figure(figsize=(10,6))

ax5 = fig2.add_subplot(121)

homogen_2 = [i - np.mean(hist_data) for i in hist_data]
ax5.hist(homogen_2, bins=int(np.sqrt(len(homogen_2))), histtype="step")
ax5.set_xlabel("Distribución de Homoxeneidade")
ax5.set_ylabel("Counts/bin")

#GEN5

hundreds = list(chunks(nrn, 100))
sum_hundreds = [sum(i) for i in hundreds]

ax6 = fig2.add_subplot(122)

counts3, bins3, _3 = ax6.hist(sum_hundreds, histtype="step")
bins_centers3 = 0.5*(bins3[1:] + bins3[:-1])
ax6.scatter(bins_centers3, counts3, c="orange", alpha=0.7)

mu, std = ss.norm.fit(sum_hundreds)

ax6.plot(bins_centers3, ss.norm.pdf(bins_centers3, mu, std))
    
    

    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:07:47 2021

@author: USC\diego.costas.rodrigu
"""

import numpy as np
import matplotlib.pyplot as plt

rn = np.random.uniform(0, 1, 100000)

x = np.linspace(0, 1, 100)
plt.plot(x, x)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        
r_coordinates = list(chunks(rn, 2))

X = [i[0] for i in r_coordinates]
Y = [i[1] for i in r_coordinates]

plt.scatter(X, Y, s=3, alpha=0.3)

def func_1(x):
    return x

y = [func_1(i) for i in X]

func_2 = lambda x: x*x
y_2 = [func_2(i) for i in X]

solution = 1/len(r_coordinates)*(1 - 0)*sum(y_2)
print(solution)
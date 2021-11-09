#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:17:15 2021

@author: USC\diego.costas.rodrigu
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import scipy.optimize as sco
import itertools as it

numbers = ([1, 3, 2, 0], [1, 3, 2, 0], [1, 3, 2, 0], [1, 3, 2, 0])

def GEN4(numbers): 
    possible_configurations = list(it.permutations([0, 1, 2, 3]))
    counting = np.zeros(24)

    for four_list in numbers:
        for index, configuration in enumerate(possible_configurations):
            if list(configuration) == list(np.argsort(four_list)):
                counting[index] += 1

    return counting

    
        

        
        
        
    

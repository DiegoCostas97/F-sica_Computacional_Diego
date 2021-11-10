#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 21:32:55 2021
@author: diegocostasrodriguez
"""

import numpy as np
import matplotlib.pyplot as plt
from math import pi

def IntegracionPorMuestreo(bot_lim   : int,
                           up_lim    : int,
                           y_bot_lim : int,
                           y_up_lim  : int,
                           function):
    """
        Calcula o valor numérico dunha integral definida 
        usando o método de integración por muestreo
    """
    
    fig = plt.figure(figsize=(10,6))
    ax1 = fig.add_subplot(111)

    x = np.linspace(bot_lim, up_lim, 100)
    ax1.plot(x, function(x), linestyle="-.", c="k", label="$f(x) = x$")
    
    def chunks(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
    
    rd_x = np.random.uniform(bot_lim, up_lim, 100000)
    rd_y = np.random.uniform(y_bot_lim, y_up_lim, 100000)
    coordinates = coordinates = list(zip(rd_x, rd_y))
    
    above = [i for i in coordinates if i[1] >= function(i[0])]
    below = [i for i in coordinates if i[1] < function(i[0])]
    
    rd_x_above = [i[0] for i in above]
    rd_y_above = [i[1] for i in above] 
    
    rd_x_below = [i[0] for i in below]
    rd_y_below = [i[1] for i in below] 
            
    ax1.scatter(rd_x_above, rd_y_above, c="mediumseagreen", s=3, alpha=0.2, label="Failure")
    ax1.scatter(rd_x_below, rd_y_below, c="tomato", s=3, alpha=0.2, label="Correct")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    leg = plt.legend(loc="upper right")
    for lh in leg.legendHandles: 
        lh.set_alpha(1)
    
    solution = y_up_lim*(up_lim - bot_lim)*len(below)/len(coordinates)
    print("O resultado da integración entre {:.2f} e {:.2f} da como resultado: {}".format(bot_lim, up_lim, solution))

# Integrais que pide o exercicio:
#
# IntegracionPorMuestreo(0, 1, 0, 1, lambda x: x)
IntegracionPorMuestreo(0, 1, 0, 1, lambda x: x**2)

# Outras integrais que tamén podemos calcular con este método e quedan chulas! Proba a que queiras, seguro que funciona ;)
#
# IntegracionPorMuestreo(0, 2*pi, -1, 1, lambda x: np.sin(x)) 



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:50:00 2021

@author: RAI\diego.costas
"""

import scipy.integrate as si
import numpy as np
import matplotlib.pyplot as plt
def deriv(y, t):
    dy_dt = -y
    return dy_dt

t_inic = 0
t_fin = 10

tiempos = np.linspace(t_inic, t_fin, 100)

y0 = 1

sol = si.odeint(deriv, y0, tiempos)

plt.plot(tiempos, sol, "^", c="r")
plt.grid()




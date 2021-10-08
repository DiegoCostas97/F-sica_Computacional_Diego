#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 18:45:00 2021

@author: RAI\diego.costas
"""

import scipy.integrate as si
import numpy as np
import matplotlib.pyplot as plt

def deriv(x, t):
    dx_dt = -x**3 + np.sin(t)
    return dx_dt

t_inic = 0
t_fin = 10

tiempos = np.linspace(t_inic, t_fin, 100)

x0 = 0

sol = si.odeint(deriv, x0, tiempos)

plt.plot(tiempos, sol, "+", c="purple", label="Solución de: \n $dx/dt=-x³+sen(t)$ para $0 \leq t \leq 10$")
plt.xlabel("t")
plt.ylabel("x")
plt.legend(loc="lower left");
plt.grid()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 19:46:01 2021

@author: RAI\diego.costas
"""

import pandas as pd
import numpy as np
import scipy.optimize as sco
import matplotlib.pyplot as plt

df = pd.read_csv("02_ej5_c.txt", sep="\t", header=None)

x = np.hstack(df[0])
y = np.hstack(df[1])
sy = np.hstack(df[2])

def funcion_de_axuste(x, A, B, C):
    return A/((x - B)**2 + (C/2)**2)

coef, cov = sco.curve_fit(funcion_de_axuste, x, y, p0=(1,1,1), sigma=sy)
y_axuste = funcion_de_axuste(np.linspace(0,200,500), *coef)

fig = plt.figure()

plt.errorbar(x, y, sy, linestyle=" ", marker=".", c="k")
plt.plot(np.linspace(0,200,500), y_axuste, linestyle="-.", c="red")

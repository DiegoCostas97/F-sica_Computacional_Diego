#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:48:44 2021

@author: RAI\diego.costas
"""

import numpy as np
import scipy.linalg as scl
import matplotlib.pyplot as plt

def calcula_todo(x, y, s, N, coeficientes_existentes):
    a = np.zeros((coeficientes_existentes[-1]+1, N))
    for i in range(coeficientes_existentes[-1]+1):
        if i in coeficientes_existentes:
            for j in range(N):
                a[i,j] = x[j]**i/s[j]
        if i not in coeficientes_existentes:
            for j in range(N):
                a[i,j] = 0
    
    b = np.zeros(N)
    for i in range(N):
        b[i] = y[i]/s[i]
     
    B = np.dot(a, b)
    
    A = scl.solve(a,b)
    
    y_axuste = np.zeros(len(x))
    for i in range(len(x)):
        for j in range(len(A)):
            y_axuste[i] += + A[j,0]*x[i]**j
            
    chi_2 = 0
    for i in range(len(y)):
        chi_2 += 1/s[i]**2*(y[i] - y_axuste[i])**2
        
        fig = plt.figure(1, figsize=(7,5))

    plt.errorbar(x, y, yerr=s, ls="None", c="k", marker=".", label="Puntos Experimentais")
    plt.plot(x, y_axuste, marker=" ", linestyle="-.", c="r", label="Axuste por Mínimos Cadrados")
    plt.tick_params(which="major", direction="in",right="on", top="on")

    plt.legend()
    
    return a, np.vstack(b), B, A, y_axuste, chi_2, fig


c_e = list(map(int,(input("Que coeficientes ten o teu polinomio de axuste? ").split(","))))

datos2 = np.loadtxt("ejercicio2c.txt")

x2, y2, s2 = datos2.T

calcula_todo(x2, y2, s2, len(x2), c_e)

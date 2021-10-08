#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 18:47:33 2021

@author: RAI\diego.costas
"""

import numpy as np
import scipy.linalg as scl
import matplotlib.pyplot as plt

##################--FUNCIÓN QUE XENERA TODO--###############

def calcula_todo(x, y, s, N):
    a = np.zeros((coeficientes[-1]+1, N))
    for i in range(coeficientes[-1]+1):
        for j in range(N):
            a[i,j] = x[j]**i/s[j]
            
    b = np.zeros(N)
    for i in range(N):
        b[i] = y[i]/s[i]
    
    b = np.vstack(b)
    
    C = np.dot(a, a.T)
    
    B = np.dot(a, b)
    
    A = scl.solve(C,B)
    for i in range(len(A)):
        if i in coeficientes:
            pass
        elif i not in coeficientes:
            A[i,0] = 0
            
    y_axuste = np.zeros(len(x))
    for i in range(len(x)):
        for j in range(len(A)):
            y_axuste[i] += + A[j,0]*x[i]**j
            
    chi_2 = 0
    for i in range(len(y)):
        chi_2 += 1/s[i]**2*(y[i] - y_axuste[i])**2
    
    return C, B, A, y_axuste, chi_2

##################--EXERCICIO_2--###########################
datos3 = np.loadtxt("ejercicio3c.txt")
x3, y3, s3 = datos3.T

coeficientes = list(map(int, input("Que coeficientes ten o teu polinomio de axuste? ").split(",")))

C3, B3, A3, y3_axuste, chi_2 = calcula_todo(x3, y3, s3, len(x3))


fig = plt.figure(1, figsize=(7,5))

plt.errorbar(x3, y3, yerr=s3, ls="None", c="k", marker=".", label="Puntos Experimentais")
plt.plot(x3, y3_axuste, marker=" ", linestyle="-.", c="r", label="Axuste por Mínimos Cadrados $\chi² = {:.3f}$".format(chi_2))
plt.tick_params(which="major", direction="in",right="on", top="on")

plt.legend()
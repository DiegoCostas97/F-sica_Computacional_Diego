#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 20:04:52 2021

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
    
    print("A matriz de coeficientes é: \n C = ")
    print( C)
    
    y_axuste = np.zeros(len(x))
    for i in range(len(x)):
        for j in range(len(A)):
            y_axuste[i] += + A[j,0]*x[i]**j
            
    chi_2 = 0
    for i in range(len(y)):
        chi_2 += 1/s[i]**2*(y[i] - y_axuste[i])**2
    
    return C, B, A, y_axuste, chi_2

##################--EXERCICIO_2--###########################
datos2 = np.loadtxt("ejercicio2c.txt")
x2, y2, s2 = datos2.T

coeficientes = list(map(int, input("Que coeficientes ten o teu polinomio de axuste? (Introduce os números separados por comas) ").split(",")))
print(" ")

C2, B2, A2, y2_axuste, chi_2 = calcula_todo(x2, y2, s2, len(x2))


fig = plt.figure(1, figsize=(7,5))

plt.errorbar(x2, y2, yerr=s2, ls="None", c="k", marker=".", label="Puntos Experimentais")
plt.plot(x2, y2_axuste, marker=" ", linestyle="-.", c="r", label="Axuste por Mínimos Cadrados $\chi² = {:.3f}$".format(chi_2))
plt.tick_params(which="major", direction="in",right="on", top="on")

plt.legend()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 19:11:37 2021

@author: RAI\diego.costas
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def distribucion_potencial(num_of_iterations, nodos, V_top, V_down, h, carga):
    ret = np.zeros((nodos,nodos))
    rho = np.zeros((nodos,nodos))
    F = len(ret) #Número de filas
    C = len(ret[0]) #Número de columnas
    e_0 = 8.85e-12
    #Condicións de contorno:
    ret[0,:] = V_top
    ret[-1] = V_down
    
    #Collo os nodos onde hai carga:
    rho[1,3] = rho[1,4] = rho[2,3] = rho[2,4] = carga
    rho[3,1] = rho[3,2] = rho[4,1] = rho[4,2] = -carga
    
    #Cálculo do potencial en cada nodo. iteramos porque o valor de V en cada nodo depende dos que ten arredor.
    for it in range(num_of_iterations):
        for i in range(1,F-1):
            for j in range(1,C-1):
                ret[i,j] = 1/4*(ret[i+1,j] + ret[i-1,j] + ret[i,j+1] + ret[i,j-1]) 
    
    final_ret = ret + + h**2*rho/(4*e_0)           
              
    fig = plt.figure()

    ax = fig.add_subplot(111, projection="3d")
    x = np.arange(0, F)
    y = np.arange(0, C)

    X, Y = np.meshgrid(x, y)

        
    ax.plot_wireframe(X, Y, final_ret, rstride=3, cstride=2, color="y")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
                
    return final_ret, fig    

distribucion_potencial(100, 11, 0, 0, 2, 1)
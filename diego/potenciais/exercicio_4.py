#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 19:11:37 2021

@author: RAI\diego.costas
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm as cm
from mpl_toolkits.mplot3d import Axes3D



def distribucion_potencial_con_cargas(num_of_iterations, nodos, V_top, V_down, h):
    ret = np.zeros((nodos,nodos))
    rho = np.zeros((nodos,nodos))
    
    F = len(ret) #Número de filas
    C = len(ret[0]) #Número de columnas
    carga = 2**2 * (1e-4)/(4*8.85e-12)
    #Condicións de contorno:
    ret[0,:] = V_top
    ret[-1] = V_down
    
    J1 = []
    for x in range(8, 17):
        J1.append(x)
    
    J2 = []
    for x in range(24, 33):
        J2.append(x)
    
    #Collo os nodos onde hai carga:
    for j in range(F):
        for i in range(C):
            if i in J1 and j in J1:
                rho[i,j] = carga
            elif i in J2 and j in J2:
                rho[i,j] = -carga
    
    #Cálculo do potencial en cada nodo. iteramos porque o valor de V en cada nodo depende dos que ten arredor.
    for it in range(num_of_iterations):
        for i in range(1,F-1):
            for j in range(1,C-1):
                ret[i,j] = 1/4*(ret[i+1,j] + ret[i-1,j] + ret[i,j+1] + ret[i,j-1] + rho[i,j]) 
             
              
    fig = plt.figure(figsize=(10,6))
    fig.tight_layout(pad=5.)
    
    ax = fig.add_subplot(121, projection="3d")
    x = np.arange(0, F)
    y = np.arange(0, C)
    
    X, Y = np.meshgrid(x, y)
    
        
    ax.plot_surface(X, Y, ret, cmap=cm.plasma)
    
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")  
    
    ax2 = fig.add_subplot(122)
    ax2.imshow(ret, cmap=cm.coolwarm)

distribucion_potencial_con_cargas(100, 40, 0, 0, 2)
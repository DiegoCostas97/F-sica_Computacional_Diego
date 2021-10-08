#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 18:47:07 2021

@author: RAI\diego.costas
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm as cm
from mpl_toolkits.mplot3d import Axes3D

def heat_flux(iterations, nodos, T_top, T_down, T_left, T_right):
    ret = np.zeros((nodos,nodos))
    qx = np.zeros((nodos,nodos))
    qy = np.zeros((nodos,nodos))
    
    F = len(ret) #Número de filas
    C = len(ret[0]) #Número de columnas
    k = 0.49
    h = 2
    
    #Condicións de contorno:
    ret[0,:] = T_top
    ret[-1] = T_down
    ret[:,0] = T_left
    ret[:,-1] = T_right
    
    #Cálculo do potencial en cada nodo. iteramos porque o valor de V en cada nodo depende dos que ten arredor.
    for it in range(iterations):
        for i in range(1,F-1):
            for j in range(1,C-1):
                ret[i,j] = 1/4*(ret[i+1,j] + ret[i-1,j] + ret[i,j+1] + ret[i,j-1])
                
    #Cálculo do fluxo
    for i in range(1,F-1):
        for j in range(1,C-1):
            #flux[i,j] = -k*((ret[i+1,j] - ret[i-1,j])/(2*h) + (ret[i,j+1] - ret[i,j-1])/(2*h))
            qx[i,j] = (-k*(ret[i+1,j] - ret[i-1,j])/(2*h))
            qy[i,j] = (-k*(ret[i,j+1] - ret[i,j-1])/(2*h))
    
    
    x = np.arange(0,nodos, 1)
    y = np.arange(0,nodos, 1)
    
    X, Y = np.meshgrid(x,y)
    
    fig = plt.figure()
    
    ax1 = plt.plot()
    plt.streamplot(X, Y, qy, qx, density=1.5, color=(-Y), cmap = cm.coolwarm)
    plt.xlabel("{}ºC".format(T_down))
    plt.ylabel("{}ºC".format(T_left))
    plt.tick_params(axis='x', which='both', bottom=False, left=False, labelbottom=False)
    
    ax2 = plt.twinx()
    plt.ylabel("{}ºC".format(T_right))
    plt.title("{}ºC".format(T_top))
    
    plt.tick_params()
    return fig

heat_flux(100, 40, 100, 0, 75, 50)
    
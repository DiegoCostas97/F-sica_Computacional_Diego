#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 20:16:23 2021

@author: RAI\diego.costas
"""

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

data = np.random.rand(3, 100)
x, y, z = data  # for show
c = np.arange(len(x)) / len(x)  # create some colours

p = ax.scatter(x, y, z, c=0.5*c, cmap=plt.cm.magma)
ax.set_xlabel('$\psi_1$')
ax.set_ylabel('$\Phi$')
ax.set_zlabel('$\psi_2$')

ax.set_box_aspect([np.ptp(i) for i in data])  # equal aspect ratio

fig.colorbar(p, ax=ax)
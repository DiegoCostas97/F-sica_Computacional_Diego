# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
from scipy import linalg as scl

arr2 = np.array([1.,2,3,4,5,6,7,8,9]).reshape(3,3)

#print(arr2)

#print(scl.det(arr2))
#inv1 = scl.inv(arr2)

p, l, u = scl.lu(arr2)

a = np.array([[1., -2.],
             [3., 2.]])
b = np.array([[1.], [11]])

x = scl.solve(a,b)
#Aprint(x)

A = np.array([0.3, 0.52, 1, 0.5, 1, 1.9, 0.1, 0.3, 0.5]).reshape(3,3)
B = np.array([-0.01, 0.67, -0.44]).reshape(3,1)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 19:43:13 2021

@author: RAI\diego.costas
"""

"""
    2. Implement class *Vector* and *Matrix* using python lists. First define the attributes and methods, 
    then define a set of test-functions to verify the code, implement the methods and finally ensure that 
    they pass your tests.
"""

import numpy as np
from math import pi

class Vector:
    """ Vector of arbitrary elements using Python lists
    """
    
    def __init__(self, body, angle=0):
        if type(body) == list:
            self.body = body
        else:
            raise TypeError('body must be a list')
        self.angle = angle
        return
    def __iter__(self):
        return VectorIterator(self)

    def module(self):
        squares = [i**2 for i in self]
        module = np.sqrt(sum(squares))
        return module
    
    def __str__(self):
        """ convert to a string
        """
        s = str(self.body)
        return s
        
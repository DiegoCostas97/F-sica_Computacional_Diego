#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 19:26:43 2021

@author: RAI\diego.costas
"""

import numpy as np
import math

class Complex:
    """ Complex number with module and phase as attributes
    """
        
    def __init__(self, mod, phase):
        """ To construct a complex number from the module and the phase
        """
        if (mod < 0): 
            raise TypeError('module must be zero or positive')
        self.mod   = mod
        self.phase = phase
        return
    
    def real(self):
        """ return the real part
        """
        real = self.mod * math.cos(self.phase) 
        return real
 
    def img(self):
        """ return the imaginary part
        """
        img = self.mod * math.sin(self.phase)
        return img
    
    def __abs__(self):
        """ return the module
        """
        return self.mod
    
    def __add__(self, y):
        """ add to complex numbers <=> x+y
        """
        
        if type(y) == int:
            real = self.real() + y
            img  = self.img()  + 0
            mod  = math.sqrt(real*real + img*img)
            phase = 0.
            if (mod > 0): 
                phase = math.acos(real / mod)
            add = Complex(mod, phase)
        
        else:
            real = self.real() + y.real()
            img  = self.img()  + y.img()
            mod  = math.sqrt(real*real + img*img)
            phase = 0.
            if (mod > 0): 
                phase = math.acos(real / mod)
            add = Complex(mod, phase)
        
        return add
        
        
    def __mul__(self, y):
        """ the product of two complex numbers: x*y
        """ 
        mod   = self.mod   * y.mod
        phase = self.phase + y.phase
        return Complex(mod, phase)
        
    def conjugate(self):
        """ complex conjugate
        """
        return Complex(self.mod, -1. * self.phase)
    
    def __str__(self):
        """ convert to a string
        """
        if self.mod == 0:
            s = str(0)
        
        elif self.phase == 0:
            s = str(self.mod)
        
        else:
            s = str(self.mod) + 'e^' + str(self.phase)
        return s
    
    def __truediv__(self, y):
        """ the division of the complex numbers: x/y
        """
        mod = self.mod / y.mod
        phase = self.phase - y.phase
        return Complex(mod, phase)
        
    
    






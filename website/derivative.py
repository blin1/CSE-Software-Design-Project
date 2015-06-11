# -*- coding: utf-8 -*-
'''
Jarrett Liang
CSE
Derivative at a Point
This application will provide the derivative of a function at a point.
'''

from sympy import *
import numpy as np

#This function will return the derivative of a function at a point

def diffpt(expression,a,b): #The expression as a string, then x and y coordinates
    a=float(a)
    b=float(b)
    x = Symbol('x')
    y = expression
    yprime = diff(y,x)
    f = lambdify(x, yprime, 'numpy') 
    slope=f(a) #Plugs in x-coordinate to the derivative
    return slope

def diffgeneral(expression):
    x = Symbol('x')
    y = expression
    yprime = diff(y,x)
    return yprime
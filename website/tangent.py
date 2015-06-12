# -*- coding: utf-8 -*-
'''
Jarrett Liang
CSE
Tangent Line
This application will provide the tangent line of an expression at a certain coordinate. 
'''

from sympy import *
import numpy as np

x = Symbol('x')

def tangentLine(expression,a): # Parameters are expression, x-coordinate, y-coordinate
    exp = sympify(expression)
    a = float(a)
    b = exp.subs(x,a)
    y = expression
    yprime = diff(y,x) #Derivative of expression
    f = lambdify(x, yprime, 'numpy')
    slope=f(a) #Substitutes x-coord for x in derivative for slope
    intercept= round(b-slope*a,6) #Calculates y-intercept of the line
    if slope==0: #Returns the tangent line as an expression in a string
        if intercept==0: 
            return str(slope)+"0"
        else:
            return str(intercept)
    if intercept==0:
        answer= str(slope)+"*x"        
    elif intercept>0:
        answer= str(slope)+"*x+"+str(intercept)
    else:
        answer= str(slope)+"*x"+str(intercept)
    return answer
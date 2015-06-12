'''
Blain Liang
CSE
Midterm Integrals
This application will provide the indefinite or definite of the inputted function.
'''

import sympy as sym

x = sym.Symbol('x') # define 'x' string as x for use in functions

def definite(f,start,end):
    start = float(start)
    end = float(end)
    return round(sym.integrate(f,(x,start,end)),6)
    

def indefinite(f):
   return str(sym.integrate(f))+' + C' # Add constant of integration   
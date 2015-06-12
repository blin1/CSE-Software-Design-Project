'''
Billy Lin and Blain Liang 
CSE
Midterm Solver
This application will provide the solution to an equation set to 0.
'''

import sympy as sym

def solve(exp1,exp2):
    x = sym.Symbol('x') # define 'x' string as x for use in functions
    exp1=str(exp1)
    exp2=str(exp2)
    exp1=sym.sympify(exp1)
    exp2=sym.sympify(exp2)
    formula=exp1-exp2
    answer=sym.solve(formula,x) # Solve with respect to x
    return answer
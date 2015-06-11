'''
Blain Liang
CSE
Software Function Intersection
This application will provide the points of intersection of two functions.
'''

from sympy import *
import matplotlib.pyplot as plt
import numpy

x = Symbol('x') # define 'x' string as x for use in functions

def intersection(exp1,exp2):
    
    exp1=sympify(exp1) # convert expressions to usable form
    exp2=sympify(exp2)
    
    exp=exp1-exp2 
    solution=solve(exp) # solve for points of intersection
    
    #minval=min(solution) # determine highest and lowest x value to scale graph
    #maxval=max(solution)
    
    '''if minval==maxval: # if only 1 solution, use default graph size of [-25,25]
        diff=25
    else: # if multiple solutions, space solutions appropriately
        diff=maxval-minval'''
        
    points=[] # initialize points list
    
    for value in solution: #find corresponding y value for each x value and add point to list
        yvalue=exp1.subs(x,value)
        value=str(value)
        yvalue=str(yvalue)
        points.append(sympify('('+value+','+yvalue+")"))
    
    if points == []:
        return "No intersection"
    else:    
        return points # return all solutions 

    '''a = numpy.linspace(minval-diff,maxval+diff,100) # 100 linearly spaced numbers
    b=[]
    
    for item in a: #compute values for expression 1
       b.append(exp1.subs(x,item))  
       
    c = numpy.linspace(minval-diff,maxval+diff,100) # 100 linearly spaced numbers
    d=[]
    
    for item in a: # compute values for expression 2
       d.append(exp2.subs(x,item))  
       
    plt.plot(a,b) #graph both data sets
    plt.plot(c,d)
    
    for point in points: #highlight intersection points with enlarged cyan dots
        plt.plot(point[0],point[1],'co') '''
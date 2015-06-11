from sympy import *
import matplotlib.pyplot as plt

import numpy
import math

#from matplotlib.pyplot import figure, show
import numpy as npy
from numpy.random import rand

x = Symbol('x')



def max_min(formula,start,end):
    start=float(start)
    end=float(end)
    formula_sym=sympify(formula)
    derivative = diff(formula_sym,x) #find derivative expression
    critical_nums = solve(derivative,x) #set derivative = 0 and solve
    graph_max_min(formula_sym, derivative)
    if critical_nums == []:
        if start<end:
            return "max: x="+str(end)+ "       min: x="+str(start)
        else:
            return "max: x="+str(start)+ "       min: x="+str(end)
            
    
    else:
        critical_nums.append(start)
        critical_nums.append(end)
        for item in critical_nums: #delete all critical nums out of the given bounds
            if item<start or item>end:
                del (item)
        min_critical = min(critical_nums)
        max_critical = max(critical_nums)
        if "sin" in str(formula) or "cos" in str(formula) or "tan" in str(formula): #finds other values of trig function that are equal to 0
            while min_critical>start: #make sure not out of bounds
                min_critical = min_critical-pi
                if min_critical>start:
                    critical_nums.append(min_critical)
            while max_critical<end: #make sure not out of bounds
                max_critical = max_critical+pi
                if max_critical<end:
                    critical_nums.append(max_critical)
        critical_nums.append(start) #appends start index to test points
        critical_nums.append(end) #appends end index to test points
        critical_nums.sort() #sorts test points in increasing oder
        #print critical_nums #test
        decreasing_increasing = [] #array showing if increasing or decreasing over the different intervals
        for i in range(0,len(critical_nums)-1): #testing if inc. or dec.
            average = (critical_nums[i]+critical_nums[i+1])/2 #find value between two test pts
            if derivative.subs(x,average) < 0: #append 0 if dec. on interval
                decreasing_increasing.append(0)
            else:
                decreasing_increasing.append(1) #append 1 if inc. on interval
        #print decreasing_increasing #test
        for i in range(0,len(decreasing_increasing)-1):
            if decreasing_increasing[i] == 0 and decreasing_increasing[i+1] == 1: #if going from dec. to inc., it is a min
                if start<end:
                    return "min: ("+str(float(critical_nums[i+1]))+','+str(float(formula_sym.subs(x,float(critical_nums[i+1]))))+')'+"      max: ("+str(float(end))+','+str(float(formula_sym.subs(x,float(end))))+')'
                else:
                    return "min: x="+str(float(critical_nums[i+1]))+','+str(float(formula_sym.subs(x,float(critical_nums[i+1]))))+')'+"      max: ("+str(float(start))+','+str(float(formula_sym.subs(x,float(start))))+')'

            if decreasing_increasing[i] == 1 and decreasing_increasing[i+1] == 0: #if going from inc. to dec., it is a max
                if start<end:
                    return "max: x="+str(float(critical_nums[i+1]))+','+str(float(formula_sym.subs(x,float(critical_nums[i+1]))))+')'+"      min: ("+str(float(start))+','+str(float(formula_sym.subs(x,float(start))))+')'
                else:
                    return "max: x="+str(float(critical_nums[i+1]))+','+str(float(formula_sym.subs(x,float(critical_nums[i+1]))))+')'+"      min: ("+str(float(end))+','+str(float(formula_sym.subs(x,float(end))))+')'

def graph_max_min(formula_sym,derivative):
    plt.clf()
    z = numpy.linspace(-5,5,100) # 100 linearly spaced numbers
    y=[]
    for item in z:
        y.append(derivative.subs(x,item)) #y values (derivative)
    
    a = numpy.linspace(-5,5,100) # 100 linearly spaced numbers
    b=[]
    for item in a:
       b.append(formula_sym.subs(x,item)) #y values (function

        
    fig = plt.figure()
    ax1 = fig.add_subplot(211) #1st subplot for function
    ax2 = fig.add_subplot(212) #2nd subplot for derivative
    col = ax2.scatter(z,y,picker=True) #plot graph for derivative going through pts
    col2 = ax2.plot(z, y, label = 'Derivative') #plot points on graph for derivative
    #col3 = ax2.scatter(a,b)
    col4 = ax1.plot(a,b) #plot graph for function
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    
    plt.savefig('maxmin.jpg')
 


'''
Blain Liang
CSE
Midterm Riemann Sum
This application will provide the left, middle, or right riemann sums of the inputted function.
'''

import sympy as sym
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def riemann():
    x = sym.Symbol('x') # define 'x' string as x for use in functions
    
    # Ask for function and convert to usable form
    while True:
        formula=raw_input('What is your function in terms of x?')
        try:
            formula_sym=sym.sympify(formula)
            break
        except:
            print('Please enter a function in terms of x.')
    
    # Get valid start value
    while True:
        start=raw_input('Start:')
        try:
            start=float(start)
            break
        except:
            print('Please enter a number.')
    
    # Get a valid end value
    while True:
        end=raw_input('End:')
        try:
            end=float(end)
            break
        except:
            print('Please enter a number.')
            
    # Get a valid number of rectangles        
    while True:
        num=raw_input('Number of Rectangles:')
        try:
            num=int(num)
            if num>0 and int(num)==num:
                break
            else:
                print ('Please enter an integer greater than 0.')
        except:
            print('Please enter a number.')
            
    width=((float(end)-float(start))/num) # Solve for width of rectangle
    area=0 # initialize area accumulator
    
    # Get a valid riemann sum type
    while True:
        rtype=raw_input('L M or R:')
        if rtype=='L'or rtype=='M' or rtype =='R':
             break
        else:
            print 'Please enter L, M, or R'
            
            
    # Find area of each rectangle and add to accumulator
    if rtype=='L':
        for i in range (num):
            xval=start+i*width
            height=formula_sym.subs(x,xval)
            rect=height*width
            area+=rect
    elif rtype=='R':
        for i in range (num):
            xval=start+width+i*width
            height=formula_sym.subs(x,xval)
            rect=height*width
            area+=rect
    elif rtype=='M':
        for i in range (num):
            xval=start+i*width+width/2
            height=formula_sym.subs(x,xval)
            rect=height*width
            area+=rect    
            
    # Return total area in riemann sum
    f = lambda x: eval(formula)
    xx=0.0
    numRange = np.arange(start, end, .02)
    d = {"L": 0, "R": 1, "M": 0.5}
    offset = d[rtype]
    for i in range(num):
        xx += f(start + (i+offset)*width)
        plt.gca().add_patch(matplotlib.patches.Rectangle((i*width + start,0),width,f(start + (i+offset)*width)))
    plt.plot(numRange,f(numRange),color=(1.0, 0.00, 0.00), zorder=5)
    
    return area
    
def riemann(a, b, n, l, f):
    plt.clf()
    a=float(a)
    b=float(b)
    n=int(n)
    numRange = np.arange(a, b, .02)
    y = f(numRange)
    w = float(b - a)/n
    x = 0.0
    d = {"l": 0, "r": 1, "m": 0.5}
    offset = d[l[0]]
    for i in range(n):
        x += f(a + (i+offset)*w)
        plt.gca().add_patch(matplotlib.patches.Rectangle((i*w + a,0),w,f(a + (i+offset)*w)))
        plt.plot(numRange, y, color=(1.0, 0.00, 0.00), zorder=5)
    plt.savefig('riemann.jpg')
    s = w * x
    return s

def trapezoid(a, b, n, f):
    a=float(a)
    b=float(b)
    n=int(n)
    numRange = np.arange(a, b, .02)
    y = f(numRange)
    print y
    w = float(b - a)/n
    x=0.0
    area=0
    for i in range(n):
        area+=((f(x)+f(x+w))/2)*w
        x+=x+w
    return area
        
    


def main():
    print #empty line
    functionString = raw_input("Enter a function: ")
    a = input("Enter the start point: ")
    b = input("Enter the end point: ")
    n = input("Enter the number of rectangles: ")
    l = raw_input("Type right, left, middle, or trapezoid: ")
    if l != 'trapezoid':
        summation = riemann(a, b, n, l, lambda x: eval(functionString))
    else:
        summation = trapezoid(a,b,n,lambda x: eval(functionString))
    plt.show()
    return summation


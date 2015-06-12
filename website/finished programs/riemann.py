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
from sympy import *
import sympy as sy
import matplotlib.pyplot as plt

import math
from matplotlib.pyplot import figure, show
import numpy as npy
from graph_general import *

def arclen(expression,lower,upper):
    plt.clf()
    x = Symbol('x')
    lower = float(lower)
    upper = float(upper)
    derivative = sy.diff(expression,x)
    result = integrate(math.sqrt(1+(derivative**2)), (x,lower,upper))
    graph_general(expression, lower-5,upper+5, "red", "arclen.jpg")
    graph_general(expression,lower,upper, "blue", "arclen.jpg")
    return result
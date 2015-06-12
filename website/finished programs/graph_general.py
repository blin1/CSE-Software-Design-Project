from sympy import *
import matplotlib.pyplot as plt
import numpy
from mayavi.mlab import *
import solver as solv
from pylab import *
from matplotlib.patches import Polygon

def graph_general(expression, lower, upper, color_in = 'blue', name = 'figure.jpg'): #Graphs functions and holes in a range
    x = Symbol('x')
    y = expression
    f = lambdify(x, y, 'numpy') #Converts string into usable equation
    points=int((upper-lower)*20+1) #The number of points to be used,spaced .05 apart.
    domain_list= numpy.linspace(lower,upper,points) #Generates the list of x-values
    range_list= []
    holes = find_hole(expression, lower, upper) #Find any holes
    for b in holes: #Plots all holes
        plt.plot(b[0], b[1], 'wo')
    for a in range(0,points): #This calculates and appends the y for each x
        range_list.append(f(domain_list[a])) 
    plt.plot(domain_list, range_list, color = color_in) #Plots function in given range
    plt.grid(which='major', axis='both') #Add gridlines
    plt.savefig(name) #Saves the graph

def clear_fig(name = 'figure.jpg'):
    plt.clf() #Clears the canvas
    plt.savefig(name) #Saves blank image
    
def graph_3d(expression, range_x, range_y): #Graphs 3D surfaces
    x = Symbol('x')
    y = Symbol('y')
    z = expression
    f = lambdify((x,y), z, 'numpy') #Turns expression into usable equation in terms of x and y
    points_x = (range_x[1]-range_x[0])*20+1 #Calculates amount of points in the domain
    points_y = (range_y[1]-range_y[0])*20+1
    list_x = numpy.linspace(range_x[0],range_x[1],points_x) #Generates domain
    list_y = numpy.linspace(range_y[0],range_y[1],points_y)
    array_x = []
    array_y = []
    array_z = [] 
    for a in range(0,points_x): #x-values and y-values are arranged in 2D arrays
        add_x = []
        for b in range(0,points_y):
            add_x.append(list_x[a])
        array_x.append(add_x)
    for c in range(0,points_x):
        array_y.append(list_y)
    for d in range(0,points_x): # Uses domain lists to calculate and append z-values in a 2D array
        list_z=[]
        for e in range(0,points_y):
            list_z.append(f(list_x[d],list_y[e]))
        array_z.append(list_z)
    mesh(array_x, array_y, array_z, colormap="bone") #Creates surface using x, y, and z arrays
    axes(nb_labels = 5) #Adds axes
    savefig('mesh.jpg') #Saves image

def clear_mesh():
    clf() #Clears canvas
    savefig('mesh.jpg') #Saves blank image
    
def find_hole(expression,lower,upper): #Finds the holes of a function in a range
    x = Symbol("x")
    y = sympify(expression)
    forward_open = ['[','('] #List of 'open' separators
    forward_close = [']',')'] #List of 'closed' separators
    separators = ['+','-'] # Neutral separators
    exists = 0 
    found = []
    term_list = []
    holes = []
    while exists != -1: #Finds all division signs in the expression
        exists = expression.find('/',exists)
        if exists != -1:
            found.append(exists)
            exists=exists+1
    for a in found: #For each division sign, find denominator
        counter = 0
        term_indexes = [a+1]#List of indexes of denominator and numerator
        index = a+1 #Starting index of denominator
        while len(term_indexes) < 2: #This loop finds the end of the denomninator
            if index >= len(expression): #If end of expression is reached, append index for end of expression
                term_indexes.append(len(expression))
            elif expression[index] in forward_open: #If open separator found, add to counter
                counter += 1
            elif expression[index] in forward_close: #If closed separator found, subtract from counter
                counter -= 1
                if counter <= 0:# If end of term reached, append current index
                    term_indexes.append(index)
            elif expression[index] in separators and counter == 0: #If neutral separator found, and separators are paired, append current index
                term_indexes.append(index)
            index += 1 #Move forward one index
        index = a-1 #Ending index of numerator
        counter = 0
        while len(term_indexes) < 3: #This loop finds the beginning of the numerator
            if index < 0: #If beginning of expression reached, append index for beginning
                term_indexes.append(0)
            elif expression[index] in forward_close: #If closed separator found, add to counter
                counter += 1
            elif expression[index] in forward_open: #if open separator found, subtract form counter.
                counter -= 1
                if counter <= 0: #If end of term reached, append current index
                    term_indexes.append(index+1)
            elif expression[index] in separators and counter == 0: #If neutral separator found and separators are paired, append current index
                term_indexes.append(index)
            index -= 1 #Move back one index
        term_indexes.append(a) #Append endpoint of numerator
        term_list.append(term_indexes) 
    for b in term_list: #Solves numerator and denominator to find holes
        denominator = expression[b[0]:b[1]] #Slice denominator
        numerator = expression[b[2]:b[3]] #Slice numerator
        d_solution = solv.solve(denominator,0) #Solve denominator
        n_solution = solv.solve(numerator,0) #Solve numerator
        for c in d_solution: #Find matching solutions in given range
            if c in n_solution and c >= lower and c<= upper:
                holes.append([c,limit(y,x,c)])
    return holes

def find_holes(exp, lower, upper):
    lower = float(lower)
    upper = float(upper)
    graph_general(exp, lower, upper, name='holes.png')
    holes = find_hole(exp, lower, upper)
    return holes

def integration_plot(expression, lower, upper, name = 'integration,jpg'): #Graphs a function and area under the curve in a range
    plt.clf() #Clears the canvas
    intercepts = solv.solve(expression,0) #Finds x-intercepts
    endpoints = [lower] #Appends lower bound
    for a in intercepts: #Appends all intercepts within the range
        if a > lower and a < upper:
            endpoints.append(a)
    endpoints.append(upper) #Appends upper bound
    for b in range(0,len(endpoints) - 1): #For each adjacent pair of endpoints, add a shape under the curve
        add_poly(expression, endpoints[b], endpoints[b+1])
    graph_general(expression, lower, upper) #Graph function
        
def add_poly(expression, lower, upper):
    ax = subplot(111)
    x = Symbol('x')
    f = lambdify(x,expression)
    ix = arange(lower, upper+.05, 0.05) #List of x coordinates along the function
    iy = []
    for a in ix:
        iy.append(f(a)) #Solve for y coordinates for each x
    verts = [(lower,0)] + list(zip(ix,iy)) + [(upper,0)] #Add intercepts to list of vertices
    poly = Polygon(verts, facecolor='0.8', edgecolor='k')
    ax.add_patch(poly) #Add the shape

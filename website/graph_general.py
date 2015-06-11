from sympy import *
import matplotlib.pyplot as plt
import numpy
from mayavi.mlab import *
import solver as solv

def graph_general(expression, lower, upper, color_in = 'blue', name = 'figure.jpg'):
    x = Symbol('x')
    y = expression
    f = lambdify(x, y, 'numpy') #Converts string into usable equation
    points=int((upper-lower)*20+1) #The number of points to be used,spaced .05 apart.
    domain_list= numpy.linspace(lower,upper,points) #Generates the list of x-values
    range_list= []
    holes = find_holes(expression, lower, upper)
    for b in holes:
        plt.plot(b[0], b[1], color = 'white', markersize = 2.00)#Creating the graph
    for a in range(0,points):#This calculates and appends the y of each x
        range_list.append(f(domain_list[a])) 
    plt.plot(domain_list, range_list, color = color_in)
    plt.grid(which='major', axis='both') #Graph options
    plt.savefig(name) #Show the graph
    #plt.show()
def clear_fig():
    plt.clf()
    plt.savefig('figure.jpg')
    
def graph_3d(expression, range_x, range_y):
    x = Symbol('x')
    y = Symbol('y')
    z = expression
    f = lambdify((x,y), z, 'numpy') #Turns expression into usable equation in terms of x and y
    points_x = (range_x[1]-range_x[0])*20+1 #Calculates amount of points in the domain
    points_y = (range_y[1]-range_y[0])*20+1
    list_x = []
    list_y = []
    for s in range(0,points_x): #Generates x-values
        list_x.append(range_x[1]+s*.05)
    for t in range(0,points_y): #Generates y-values
        list_y.append(range_y[1]+t*.05)  
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
    axes(nb_labels = 5)
    savefig('mesh.jpg')

def clear_mesh():
    clf()
    savefig('mesh.jpg')
    
def find_holes(expression,lower,upper):
    x = Symbol("x")
    lower = float(lower)
    upper = float(upper)
    y = sympify(expression)
    forward_open = ['[','(']
    forward_close = [']',')']
    separators = ['+','-']
    exists = 0
    found = []
    term_list = []
    holes = []
    while exists != -1:
        exists = expression.find('/',exists)
        if exists != -1:
            found.append(exists)
            exists=exists+1
    for a in found:
        counter = 0
        term_indexes = [a+1]
        index = a+1
        while len(term_indexes) < 2:
            if index >= len(expression):
                term_indexes.append(len(expression))
            elif expression[index] in forward_open:
                counter += 1
            elif expression[index] in forward_close:
                counter -= 1
                if counter <= 0:
                    term_indexes.append(index)
            elif expression[index] in separators and counter == 0:
                term_indexes.append(index)
            index += 1
        index = a-1
        while len(term_indexes) < 3:
            if index <= 0:
                term_indexes.append(1)
            elif expression[index] in forward_close:
                counter += 1
            elif expression[index] in forward_open:
                counter -= 1
                if counter <= 0:
                    term_indexes.append(index+1)
            elif expression[index] in separators and counter == 0:
                term_indexes.append(index)
            index -= 1
        term_indexes.append(a)
        term_list.append(term_indexes)
    print term_list
    for b in term_list:
        denominator = expression[b[0]:b[1]]
        numerator = expression[b[2]:b[3]]
        d_solution = solv.solve(denominator,0)
        print b
        print numerator,'hi'
        n_solution = solv.solve(numerator,0)
        for c in d_solution:
            if c in n_solution and c >= lower and c<= upper:
                holes.append([c,limit(y,x,c)])
    return holes


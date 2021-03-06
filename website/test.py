from bottle import *

import sympy as sym
import numpy as np

import factor2 as fact
import solver as solv
import riemann as riem
import integral as inte
import derivative as diff
import tangent as tan
import maxmin as mm
import intersection as inter
import arclen as arc
import graph_general as graph

@route('/')
def main():
    return template('homePage.tpl')

@route('/factor/')
def factor():
    title = 'Factor'
    answer = '0'
    number = request.query.number
    expression = request.query.expression
    mode = request.query.mode
    number = number.encode("utf8")
    expression = expression.encode("utf8")
    mode = mode.encode("utf8")

    if number == "":
        number = '0'
    if expression == "":
        expression = '0'
        
    if mode == "number":
        if '.' in number:
            number = float(number)
        else:
            number = int(number)
        answer = fact.factorx(number)
    else:
        answer = fact.factorx(expression)
    return template('factorPage.tpl', title = title, answer = answer)

@route('/solve/')
def solve():
    title = 'Solve'
    answer = '0'
    exp1 = request.query.exp1
    exp2 = request.query.exp2
    exp1 = exp1.encode('utf8')
    exp2 = exp2.encode('utf8')
    if exp1 == '':
        exp1 = 'x'
    if exp2 == '':
        exp2 = '0'
    answer = solv.solve(exp1,exp2)
    return template('solvePage.tpl', title = title, answer = answer)

@route('/simplify/')
def simplify():
    x = sym.Symbol('x')
    y = sym.Symbol('y')
    z = sym.Symbol('z')
    title = 'Simplify'
    answer = '0'
    exp = request.query.expression
    exp = exp.encode('utf8')
    if exp == '':
        exp = '0'
    answer = sym.simplify(exp)
    return template('simplifyPage.tpl', title = title, answer = answer)

@route('/arclen/')
def arclen():
    title = 'Arc Length'
    answer = '0'
    function = request.query.function
    start = request.query.start
    end = request.query.end

    function = function.encode('utf8')
    start = start.encode('utf8')
    end = end.encode('utf8')

    if function and start and end != '':
        answer = arc.arclen(function, start, end)    
    else:
        answer = 'Please fill in all fields.'

    return template('arclenPage.tpl', title=title, answer=answer)

@route('/derivative/')
def derivative():
    title = 'Derivative'
    answer = '0'
    function = request.query.function
    mode = request.query.mode
    xcoor = request.query.xcoor
    
    function = function.encode('utf8')
    mode = mode.encode('utf8')
    xcoor = xcoor.encode('utf8')

    if function and mode != '':
        if mode == 'general':
            answer = diff.diffgeneral(function)
        if mode == 'point' and xcoor != '':
            answer = diff.diffpt(function,xcoor)
    else:
        answer = 'Please fill in all fields.'

    return template('derivativePage.tpl', title = title, answer = answer)

@route('/integral/')
def integral():
    title = 'Integration'
    answer = '0'
    function = request.query.function
    mode = request.query.mode
    start = request.query.start
    end = request.query.end
    
    function = function.encode('utf8')
    mode = mode.encode('utf8')
    start = start.encode('utf8')
    end = end.encode('utf8')
    
    if function and mode != '':
        if mode == 'indefinite':
            answer = inte.indefinite(function)
        if mode == 'definite' and start and end != '':
            answer = inte.definite(function,start,end)
    else:
        answer = 'Please fill in all fields.'

    return template('integralPage.tpl', title=title, answer=answer)

@route('/maxmin/')
def maxmin():
    title = 'Maximum/Minimum'
    answer = '0'
    function = request.query.function
    start = request.query.start
    end = request.query.end
    
    function = function.encode('utf8')
    start = start.encode('utf8')
    end = end.encode('utf8')

    if function and start and end != '':
        answer = mm.max_min(function, start, end)    
    else:
        answer = 'Please fill in all fields.'

    return template('maxminPage.tpl', title=title, answer=answer)

@route('/riemann/')
def riemann():
    title = 'Riemann Sums'
    answer = '0'
    function = request.query.function
    start = request.query.start
    end = request.query.end
    rekt = request.query.rekt
    mode = request.query.mode
    function = function.encode('utf8')
    start = start.encode('utf8')
    end = end.encode('utf8')
    rekt = rekt.encode('utf8')
    mode = mode.encode('utf8')
    f = lambda x: eval(function)

    if function and start and end and rekt and mode != '':
        if mode == 'trapezoid':
            answer = riem.trapezoid(start, end, rekt, f)
        else:
            answer = riem.riemann(start, end, rekt, mode, f)
    else:
        answer = 'Please fill in all fields.'

    return template('riemannPage.tpl', title = title, answer = answer)

@route('/tangent/')
def tangent():
    title = 'Tangent Line'
    answer = '0'
    function = request.query.function
    xcoor = request.query.xcoor
    
    function = function.encode('utf8')
    xcoor = xcoor.encode('utf8')

    if function and xcoor != '':
        answer = tan.tangentLine(function, xcoor)    
    else:
        answer = 'Please fill in all fields.'

    return template('tangentPage.tpl', title = title, answer = answer)

@route('/2d/')
def twod():
    title = '2D Graphing'
    mode = request.query.mode
    function = request.query.function

    mode = mode.encode('utf8')
    function = function.encode('utf8')

    if mode == 'graph':
        if function != '':
            answer = 'Graphed'
            graph.graph_general(function, -50, 50, name = '2d.png')
        else:
            answer = 'Please fill in all fields.'    
    else:
        answer = 'Cleared'
        graph.clear_fig(name = '2d.png')
        
    return template('2dPage.tpl', title = title, answer = answer)

@route('/3d/')
def threed():
    title = '3D Graphing'
    mode = request.query.mode
    function = request.query.function

    mode = mode.encode('utf8')
    function = function.encode('utf8')

    if mode == 'graph':
        if function != '':
            answer = 'Graphed'
            graph.graph_3d(function, [-10,10],[-10,10])
        else:
            answer = 'Please fill in all fields.'    
    else:
        answer = 'Cleared'
        graph.clear_mesh()
        
    return template('3dPage.tpl', title = title, answer = answer)

@route('/holes/')
def holes():
    title = 'Discontinuities'
    answer = '0'
    expression = request.query.expression
    start = request.query.start
    end = request.query.end

    expression = expression.encode('utf8')
    start = start.encode('utf8')
    end = end.encode('utf8')

    if expression and start and end != '':
        answer = graph.find_holes(expression, start, end)    
    else:
        answer = 'Please fill in all fields.'

    return template('holesPage.tpl', title=title, answer=answer)

@route('/intersection/')
def intersection():
    title = 'Intersection'
    answer = '0'
    function1 = request.query.function1
    function2 = request.query.function2
    
    function1 = function1.encode('utf8')
    function2 = function2.encode('utf8')

    if function1 and function2 != '':
        answer = inter.intersection(function1, function2)    
    else:
        answer = 'Please fill in all fields.'

    return template('intersectionPage.tpl', title=title, answer=answer)
    
@route('feedback')
def feedback():
    title='Feedback'
    return template(feedback.tpl)

'''@route('/data/')
def data():
    title = 'Data Analysis'
    answer = 'Please fill in data set(s).'
    data1 = request.query.data1
    data2 = request.query.data2
    mode = request.query.mode
    tails = request.query.tails

    data1= data1.encode('utf8')
    data2 = data2.encode('utf8')
    mode = mode.encode('utf8')
    tails = tails.encode('utf8')

    if data1 != '':
        answer = data.data_a(data1,data2,mode,tails)
        return template('ttestPage.tpl', title=title, answer=answer)
    else:
        answer = 'Please fill in at least one data set.'
'''    
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root = 'C:/Users/Blain/Documents/CSE-Software-Design-Project-master/website')

run(host='localhost', port=8080, debug=True, reloader=True)
#browser url http://localhost:8080/

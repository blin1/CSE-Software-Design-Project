'''
Billy Lin
CSE
Factor
This application will provide the factored form of an expression.
'''
#Import Python libraries. 
from __future__ import division
import sympy 

#Define the strings 'x,' 'y,' and 'z' as x, y, and z. 
x, y, z = sympy.symbols('x y z')

#Set up pretty printing.
sympy.init_printing(use_unicode=True)

#Finds if a number is prime.
def isPrime(num):
    if num < 2:
        return False
    else:
        if num == 2:
            return True
        else:  #If a number is greater than 2, loop through number to check for factors.
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
    

#Factors expression.        
def factorx(exp):
    if "x" in str(exp): #Checks if the expression includes variable(s).
        factoredExp = sympy.factor(exp) # Factor the expression.
        if str(factoredExp) == str(exp): 
            return 'Prime'
        else:
            return str(factoredExp)
    elif type(exp) != int:
        return "Not Factorable"
    elif isPrime(exp) == True:
        return "Prime"
    else:
        factoredExp = sympy. factorint(exp) #Factor the number.
        factoredList = "" 
        for base, power in factoredExp.iteritems(): #Iterate through the items in list.
            exponent = str(base)
            #If the power is greater than 1, set exponent to base.
            if power > 1:
                exponent = str(base) + '^' + str(power)
            factoredList = factoredList + exponent + "*"
        return factoredList[: -1] #Return factorization.

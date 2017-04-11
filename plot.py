"""
Console driven tester to graph y = a + bx + cx^2 + dx^3 in range (-1,1)

"""

import numpy as np  
import matplotlib.pyplot as plt  

a = float(raw_input('a= '))
b = float(raw_input('b= '))
c = float(raw_input('c= '))
d = float(raw_input('d= '))

def graph(formula, x_range):  
    x = np.array(x_range)  
    y = formula(x)  # <- note now we're calling the function 'formula' with x
    plt.plot(x, y)
    plt.show()  
	
def my_formula(x):
    return a+b*x+c*x**2+d*x**3

print 'Graphing equation:',a,'+',b,'x+',c,'x^2+',d,'x^3'

#Graphing equation
graph(my_formula, range(-1, 2))

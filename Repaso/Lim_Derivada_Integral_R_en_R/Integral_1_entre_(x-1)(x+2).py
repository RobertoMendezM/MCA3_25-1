# -*- coding: utf-8 -*-
"""

Tema:  Integral con Python 

        f(x) = 1/((x -1)*(x+2))

Curso:  Matemáticas para las Ciencias Aplicadas

DAte:    Aug 7 2024

@author: Roberto Méndez Méndez
"""

from sympy import symbols, integrate

x  = symbols('x')
intsen = integrate(1/((x -1)*(x+2)))
print("El resultado es: ", intsen.evalf())



from IPython.display import display, Latex
from sympy import symbols, latex, Integral, init_printing
init_printing(use_latex='mathjax')

x  = symbols('x')
inte_x = Integral(1/((x -1)*(x+2)), x)

print("La derivada es: ")
result = "$${} ={} = {}$$".format(latex(inte_x),latex(inte_x.doit()),
                                  latex(inte_x.doit().simplify()))

display(Latex(result))
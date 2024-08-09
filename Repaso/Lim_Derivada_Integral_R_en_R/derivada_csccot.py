# -*- coding: utf-8 -*-
"""

Tema:   Derivadas con Python 

        f(x) = csc(x)cot(x)  

Curso:  Matemáticas para las Ciencias Aplicadas

Date:    Aug 7 2024

@author: Roberto Méndez
"""

from sympy import symbols, diff, csc, cot

x  = symbols('x')
fx = csc(x)*cot(x)
dx = diff(fx, x)
print("La derivada es: \n {0}  \n= {1} ".format(dx, dx.simplify()))

from IPython.display import display, Latex
from sympy import symbols, latex, Derivative, init_printing
init_printing(use_latex='mathjax')

x  = symbols('x')
derv_x = Derivative(csc(x)*cot(x), x)

print("La derivada es: ")
result = "$${} ={} = {}$$".format(latex(derv_x),latex(derv_x.doit()),
                                  latex(derv_x.doit().simplify()))

display(Latex(result))
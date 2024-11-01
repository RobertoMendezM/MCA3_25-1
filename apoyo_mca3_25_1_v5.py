# -*- coding: utf-8 -*-
"""Apoyo_MCA3_25-1_v5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SoEDp_PaRABGnvsrjIGdTovaGWndAiCv

# **MCA 3**

## Material de apoyo para las clases

Aquí aparecera el código que se utiliza en clase y que no es en si mismo un programa independiente


Referencias:
* [sympy.plotting.plot.plot_parametric](https://docs.sympy.org/latest/modules/plotting.html#sympy.plotting.plot.plot_parametric)
---
Editor: Roberto Méndez

Creado: 13 Sep 24 <br>
Editado: 29 Oct 24

# Cornu's Spiral

Fresnel Fuctions

Clase: 13 Sep 23 <br>
Tema:  
* Longitud de Arco - Repaso
* Tamaño de paso  / Partición.
  * Cambia *t* de -8pi a 8pi ¿Qué notas en la gráfica?
  * Usa el atributo, n=10000 ¿Qué cambio se ve?
"""

from sympy import symbols, cos, sin,  pi, integrate
from sympy import plot_parametric
t, x = symbols('t x')
def f(t):
  return integrate(cos(pi*x**2/2), (x, 0, t ))
def g(t):
  return integrate(sin(pi*x**2/2), (x, 0, t ))

plot_parametric(f(t), g(t), (t, -4*pi, 4*pi),
                line_color='orange');

"""# **Astroid**

Clase: 18 Sep 23 <br>
Tema:  
* Longitud de Arco - Repaso
* Volumen de Revolución
* Área de la Superficie de revolución
"""

from sympy import symbols, cos, sin,  pi
from sympy import plot_parametric
t = symbols('t')
a = 2
def x(t):
  return a*cos(t)**3
def y(t):
  return  a*sin(t)**3

plot_parametric(x(t), y(t), (t, 0, 2*pi),
                line_color='green', size = (5,5));

"""# **Lemniscata Paramétrica**

Examen: 10 Oct 24 <br>
Tema:  
* Longitud de Arco

Referencia:
[https://proofwiki.org/wiki/Definition:Lemniscate_of_Bernoulli](https://proofwiki.org/wiki/Definition:Lemniscate_of_Bernoulli)
"""

from sympy import symbols, cos, sin, sqrt,  pi
from sympy import plot_parametric
t = symbols('t')
a = 2
def x(t):
  return a*sqrt(2)*cos(t)/(sin(t)**2 + 1)
def y(t):
  return a*sqrt(2)*cos(t)*sin(t)/(sin(t)**2 + 1)

plot_parametric(x(t), y(t), (t, 0, 2*pi),
                line_color='green', size = (4,1.5));

"""# **Cardioide Paramétrica**


Tema:
    Área

Referencia:
* [https://openstax.org/books/c%C3%A1lculo-volumen-2/pages/7-4-area-y-longitud-de-arco-en-coordenadas-polares](https://openstax.org/books/c%C3%A1lculo-volumen-2/pages/7-4-area-y-longitud-de-arco-en-coordenadas-polares)
* https://elepa.me/wp-content/uploads/2013/11/fifty-famous-curves.pdf

---
Edición: 10 Oct 24 <br/>
"""

from sympy import symbols, cos, sin, sqrt,  pi
from sympy import plot_parametric
t = symbols('t')
a = 1
# Con b= 2 da la cardioide
# b = 3, 4, 5, 6 figras interesantes
b = 2
def x(t):
  return a*(b*cos(t) - cos(b*t))
def y(t):
  return a*(b*sin(t) - sin(b*t))

plot_parametric(x(t), y(t), (t, 0, 2*pi),
                line_color='green', size = (5,5));

"""# **Cardioide Polar**

Tema:  Área

Referencia:
* [https://krajit.github.io/sympy/polarCurves/polarCurves.html](https://krajit.github.io/sympy/polarCurves/polarCurves.html)

---

Edición: 10 Oct 24
"""

from sympy import symbols, cos, sin, sqrt,  pi
from sympy import plot_parametric
t = symbols('t')
a = 1

r = 2*a*(1 + cos(t))

plot_parametric(r*cos(t), r*sin(t), (t, 0, 2*pi),
                line_color='green', size = (5,5));

"""
Adaptación de la forma polar para que se vea idéntica a la forma paramétrica
"""
from sympy import symbols, cos, sin, sqrt,  pi
from sympy import plot_parametric
t = symbols('t')
a = 1

r = -2*a*(1 + cos(t))

plot_parametric(r*cos(t) + 1, r*sin(t), (t, 0, 2*pi),
                line_color='green', size = (5,5));

"""Editado: 29 Oct 24"""

"""
Adaptación de la forma paramétrica para que se vea idéntica a la forma polar
(del documento original)
"""
from sympy import symbols, cos, sin, sqrt,  pi
from sympy import plot_parametric
t = symbols('t')
a = 1
b = 2
def x(t):
  return -(a*(b*cos(t) - cos(b*t)) - 1)
def y(t):
  return a*(b*sin(t) - sin(b*t))

plot_parametric(x(t), y(t), (t, 0, 2*pi),
                line_color='green', size = (5,5));

"""# **Plano que pasa por tres puntos**

Tarea MCA3: 16 Oct 24  / Entrega 18 de Oct 24

Referencia: <br>
* [https://docs.sympy.org/latest/modules/geometry/plane.html](https://docs.sympy.org/latest/modules/geometry/plane.html)
* [http://blog.espol.edu.ec/ccpg1001/graficas-3d-en-python-sistema-de-ecuaciones-y-planos/](http://blog.espol.edu.ec/ccpg1001/graficas-3d-en-python-sistema-de-ecuaciones-y-planos/)

---

Fecha: 29 Sep 24
"""

import numpy as np
from sympy import symbols, solve, Point3D, Plane

p0 = np.array([1,0,0])
p1 = np.array([2,-2,1])
p2 = np.array([1,-3,-1])

n = np.cross(p1-p0, p2-p0)
print("El producto vectorial (cruz) de P1-P0 x P2 - P0 es: ", n)

p = Plane(Point3D(1,0,0), Point3D(2,-2,1), Point3D(1,-3,-1))

print("Ecuación del plano: ", p.equation())
print("Vector normal al plano: ", p.normal_vector)
print(u"Ecuación implícita: %s = 0"%(p.equation()))

"""## Plano que pasa por tres puntos forma cartesiana con gráfica

Referencia: <br>
https://numython.github.io/posts/2016/03/sympy-es-una-de-esas-librerias-que-lo/

---

Edición: 29 Sep 24
"""

from sympy import Matrix, solve, det, latex
from sympy.abc import x,y,z
from sympy.plotting import plot3d

P1 = (1,0,0)
P2 = (2,-2,1)
P3 = (1,-3,-1)

M = Matrix([[x-P1[0]     , y-P1[1]     , z-P1[2]]    ,
            [P2[0]-P1[0] , P2[1]-P1[1] , P2[2]-P1[2]],
            [P3[0]-P1[0] , P3[1]-P1[1] , P3[2]-P1[2]]])

sol = solve(det(M), z)
print(u"Ecuación implícita: %s = 0"%det(M))
print(u"Ecuación explícita: z=%s"%(sol[0]))

plot3d(sol[0], (x,0,3), (y,0,3), title="$z = %s$"%(latex(sol[0])))
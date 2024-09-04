# -*- coding: utf-8 -*-
"""

Ejemplifica el uso de meshgrid

y grafica parcialmente la lamina del ejemplo en clase MCA3


Created on Tue Sep  3 01:21:58 2024

@Editor: Roberto Méndez Méndez


Referencia:
Advanced Guide to Python 3 Programming pag 64

Problema Simulado: 
    Calculus Stewart 3th edition pag 519 exercise 33
  o Stewart y Kokoska (2023). Calculus Concepts and Contexts 5th edition
     pag 547 ejer 40
  
  40. A manufacturer of corrugated metal roofing wants to
     produce panels that are 28 inches wide and 2 inches high by
     processing flat sheets of metal, as shown in the figure ...
  
     The profile of the roofing takes the shape of a sine wave

"""

import matplotlib.pyplot as pyplot
# Import matplotlib colour map
from matplotlib import cm as colourmap
# Provide access to numpy functions
import numpy as np

# Make the data to be displayed
x_values = np.arange(0, 28, 0.1)
y_values = np.arange(0, 15, 0.1)
# Generate coordinate matrices from coordinate vectors
x_values2, y_values2 = np.meshgrid(x_values, y_values)
# Generate Z values as sin of x plus y values
## z_values = np.sin(x_values2 + y_values2)
z_values = np.sin(np.pi*x_values2/7 )

# Obtain the figure object
figure = pyplot.figure()
# Get the axes object for the 3D graph
# axes = figure.gca(projection='3d')    DEPRECATED
axes = figure.add_subplot(projection='3d')
#axes = figure.gca()
# Plot the surface.
surf = axes.plot_surface(x_values2, y_values2, z_values,
                         cmap=colourmap.coolwarm)
# Add a color bar which maps values to colors.
## figure.colorbar(surf)
# Add labels to the graph
pyplot.title("3D Graph")
axes.set_ylabel('y values', fontsize=8)
axes.set_xlabel('x values', fontsize=8)
axes.set_zlabel('z values', fontsize=8)
# Display the graph
pyplot.show()
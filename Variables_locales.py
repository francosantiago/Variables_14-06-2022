# Ecuaciones de segundo grado usando funciones

import math


"LAS VARIABLES A, B Y C NO SON LAS MISMAS QUE EN LA FUNCIÓN HALLAR_DISCRIMINANTE, DONDE CORRESPONDEN A a1, b1, c1"
def hallar_discriminantes(a1, b1, c1):
    d = math.sqrt(b1*b1 - 4*a*c)
    return d

# Programa principal
a = float(input("Coeficiente de x²: "))
b = float(input("Coeficiente de x¹: "))
c = float(input("Termino independiente: "))

# Calculo del dsicriminante

d1 = hallar_discriminantes(a, b, c)

# Se calculan las raices

x1 = (-b + d1)/ 2*a
x2 = (-b - d1)/ 2*a

# Resultados

print("Primera raiz: ", x1)
print("Segunda raiz: ", x2)


